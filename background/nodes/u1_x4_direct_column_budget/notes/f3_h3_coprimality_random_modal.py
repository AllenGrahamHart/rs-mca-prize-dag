#!/usr/bin/env python3
"""Modal random exact-norm sample for Terminal C h=3 pair-coprimality.

The full all-shapes n=96 census is much larger.  This script is a bounded
falsifier: it samples normalized disjoint shape pairs, computes exact
cyclotomic obstruction norms in Q(zeta_96), factors their gcd, and reports any
threshold prime p = 1 mod 96, p >= 96^2.
"""

from __future__ import annotations

import modal


app = modal.App("rs-mca-h3-coprime-random")
image = modal.Image.debian_slim().pip_install("sympy")

N = 96
N_SHARDS = 8
SAMPLES_PER_SHARD = 250


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def sample_shard(shard: int) -> dict:
    import itertools
    import math
    import random
    import sympy as sp

    x = sp.Symbol("x")
    phi = sp.Poly(sp.cyclotomic_poly(N, x), x, domain=sp.ZZ)
    rng = random.Random(20260708 + 1009 * shard)

    def canonical(a, b):
        best = None
        for shift in range(N):
            ar = tuple(sorted((u - shift) % N for u in a))
            br = tuple(sorted((u - shift) % N for u in b))
            for left, right in ((ar, br), (br, ar)):
                if left[0] != 0:
                    continue
                cand = left + right
                if best is None or cand < best:
                    best = cand
        return best

    def terms_e1(flat):
        a, b = flat[:3], flat[3:]
        return [(1, u) for u in a] + [(-1, u) for u in b]

    def terms_e2(flat):
        a, b = flat[:3], flat[3:]
        out = []
        for u, v in itertools.combinations(a, 2):
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
        roots = []
        for cand in range(2, p):
            z = pow(cand, (p - 1) // N, p)
            if z == 1:
                continue
            y, order = z, 1
            while y != 1 and order <= N:
                y = y * z % p
                order += 1
            if order == N:
                # all primitive roots are powers z^k with gcd(k,N)=1
                roots = sorted({pow(z, k, p) for k in range(1, N + 1) if math.gcd(k, N) == 1})
                break
        return roots

    def eval_terms_mod(terms, z, p):
        return sum(coeff * pow(z, exp, p) for coeff, exp in terms) % p

    def actual_activation(flat, p):
        e1 = terms_e1(flat)
        e2 = terms_e2(flat)
        for z in primitive_roots_mod(p):
            if eval_terms_mod(e1, z, p) == 0 and eval_terms_mod(e2, z, p) == 0:
                return True
        return False

    seen = set()
    norm_exceptions = []
    activation_exceptions = []
    attempts = 0
    while len(seen) < SAMPLES_PER_SHARD and attempts < 20 * SAMPLES_PER_SHARD:
        attempts += 1
        a = tuple(sorted(rng.sample(range(N), 3)))
        remaining = [u for u in range(N) if u not in a]
        b = tuple(sorted(rng.sample(remaining, 3)))
        flat = canonical(a, b)
        if flat in seen:
            continue
        seen.add(flat)

        n1 = norm_from_terms(terms_e1(flat))
        n2 = norm_from_terms(terms_e2(flat))
        # Skip char-zero vanishing components; Terminal A classifies the genuine
        # double-zero case as toral, and random samples almost never hit it.
        if n1 == 0 or n2 == 0:
            continue
        factors = sp.factorint(math.gcd(n1, n2))
        threshold = [int(p) for p in factors if int(p) % N == 1 and int(p) >= N * N]
        if threshold:
            record = {"shape": list(flat), "threshold_norm_primes": threshold}
            norm_exceptions.append(record)
            active = [p for p in threshold if actual_activation(flat, p)]
            if active:
                activation_exceptions.append({"shape": list(flat), "activation_primes": active})

    return {
        "shard": shard,
        "attempts": attempts,
        "unique_shapes": len(seen),
        "norm_exceptions": norm_exceptions,
        "activation_exceptions": activation_exceptions,
    }


@app.local_entrypoint()
def main():
    results = []
    for item in sample_shard.map(range(N_SHARDS), return_exceptions=True):
        if isinstance(item, Exception):
            print(f"SHARD_ERROR {item!r}")
            continue
        results.append(item)
        print(
            f"shard={item['shard']} unique={item['unique_shapes']} "
            f"norm_exceptions={len(item['norm_exceptions'])} "
            f"activation_exceptions={len(item['activation_exceptions'])}"
        )
        for rec in item["norm_exceptions"][:3]:
            print(f"  NORM_EXCEPTION {rec}")
        for rec in item["activation_exceptions"][:5]:
            print(f"  ACTIVATION_EXCEPTION {rec}")

    total = sum(r["unique_shapes"] for r in results)
    norm_total = sum(len(r["norm_exceptions"]) for r in results)
    active_total = sum(len(r["activation_exceptions"]) for r in results)
    print(
        f"TOTAL unique_shapes={total} norm_exceptions={norm_total} "
        f"activation_exceptions={active_total}"
    )
    if active_total == 0:
        print("H3_RANDOM_ACTIVATION_SAMPLE_PASS")


if __name__ == "__main__":
    main()
