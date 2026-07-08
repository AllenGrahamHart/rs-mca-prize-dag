#!/usr/bin/env python3
"""Complete Modal census of the A=[0,1,2] h=3 shape slice at n=96."""

from __future__ import annotations

import modal


app = modal.App("rs-mca-h3-consecutive-core-census")
image = modal.Image.debian_slim().pip_install("sympy")

N = 96
N_SHARDS = 64
A = (0, 1, 2)


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def scan_shard(shard: int) -> dict:
    import itertools
    import math
    import sympy as sp

    x = sp.Symbol("x")
    phi = sp.Poly(sp.cyclotomic_poly(N, x), x, domain=sp.ZZ)

    def terms_e1(b):
        return [(1, t) for t in A] + [(-1, t) for t in b]

    def terms_e2(b):
        out = []
        for u, v in itertools.combinations(A, 2):
            out.append((1, u + v))
        for u, v in itertools.combinations(b, 2):
            out.append((-1, u + v))
        return out

    def poly_from_terms(terms):
        poly = sp.Poly(0, x, domain=sp.ZZ)
        for coeff, exp in terms:
            poly += sp.Poly(coeff * x ** (exp % N), x, domain=sp.ZZ)
        return poly.rem(phi)

    def norm_from_terms(terms):
        poly = poly_from_terms(terms)
        if poly.is_zero:
            return 0
        return abs(int(sp.resultant(phi.as_expr(), poly.as_expr(), x)))

    def primitive_roots_mod(p):
        for cand in range(2, p):
            z = pow(cand, (p - 1) // N, p)
            if z == 1:
                continue
            y, order = z, 1
            while y != 1 and order <= N:
                y = y * z % p
                order += 1
            if order == N:
                return sorted({pow(z, k, p) for k in range(1, N + 1) if math.gcd(k, N) == 1})
        return []

    def eval_terms_mod(terms, z, p):
        return sum(coeff * pow(z, exp, p) for coeff, exp in terms) % p

    def actual_activation(b, p):
        e1 = terms_e1(b)
        e2 = terms_e2(b)
        return any(
            eval_terms_mod(e1, z, p) == 0 and eval_terms_mod(e2, z, p) == 0
            for z in primitive_roots_mod(p)
        )

    total = 0
    norm_exceptions = []
    activation_exceptions = []
    for idx, b in enumerate(itertools.combinations(range(3, N), 3)):
        if idx % N_SHARDS != shard:
            continue
        total += 1
        n1 = norm_from_terms(terms_e1(b))
        n2 = norm_from_terms(terms_e2(b))
        if n1 == 0 or n2 == 0:
            continue
        factors = sp.factorint(math.gcd(n1, n2))
        threshold = [int(p) for p in factors if int(p) % N == 1 and int(p) >= N * N]
        if threshold:
            rec = {"shape": [0, 1, 2, *b], "threshold_norm_primes": threshold}
            norm_exceptions.append(rec)
            active = [p for p in threshold if actual_activation(b, p)]
            if active:
                activation_exceptions.append({"shape": [0, 1, 2, *b], "activation_primes": active})
    return {
        "shard": shard,
        "total": total,
        "norm_exceptions": norm_exceptions,
        "activation_exceptions": activation_exceptions,
    }


@app.local_entrypoint()
def main():
    results = []
    for item in scan_shard.map(range(N_SHARDS), return_exceptions=True):
        if isinstance(item, Exception):
            print(f"SHARD_ERROR {item!r}")
            continue
        results.append(item)
        print(
            f"shard={item['shard']} total={item['total']} "
            f"norm_exceptions={len(item['norm_exceptions'])} "
            f"activation_exceptions={len(item['activation_exceptions'])}"
        )
        for rec in item["activation_exceptions"][:3]:
            print(f"  ACTIVATION_EXCEPTION {rec}")

    total = sum(r["total"] for r in results)
    norm_total = sum(len(r["norm_exceptions"]) for r in results)
    active = []
    for r in results:
        active.extend(r["activation_exceptions"])
    print(
        f"TOTAL shapes={total} norm_exceptions={norm_total} "
        f"activation_exceptions={len(active)}"
    )
    for rec in sorted(active, key=lambda r: r["shape"]):
        print(f"ACTIVATION {rec}")
    print("H3_CONSECUTIVE_CORE_CENSUS_DONE")


if __name__ == "__main__":
    main()
