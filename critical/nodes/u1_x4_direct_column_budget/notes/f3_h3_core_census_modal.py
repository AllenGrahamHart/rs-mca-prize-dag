#!/usr/bin/env python3
"""Parameterized complete Modal census of an h=3 core slice at n=96."""

from __future__ import annotations

import json
from pathlib import Path

import modal


app = modal.App("rs-mca-h3-core-census")
image = modal.Image.debian_slim().pip_install("sympy")

N = 96
N_SHARDS = 64
NOTES_DIR = Path("critical/nodes/u1_x4_direct_column_budget/notes")


def parse_core(core: str) -> tuple[int, int, int]:
    parts = tuple(int(x.strip()) for x in core.split(",") if x.strip())
    if len(parts) != 3:
        raise ValueError(f"expected three comma-separated integers, got {core!r}")
    if len(set(parts)) != 3:
        raise ValueError(f"core entries must be distinct: {parts}")
    if any(x < 0 or x >= N for x in parts):
        raise ValueError(f"core entries must lie in Z/{N}Z: {parts}")
    return tuple(sorted(parts))


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def scan_shard(shard: int, a: tuple[int, int, int]) -> dict:
    import itertools
    import math
    import sympy as sp

    x = sp.Symbol("x")
    phi = sp.Poly(sp.cyclotomic_poly(N, x), x, domain=sp.ZZ)

    def terms_e1(b):
        return [(1, t) for t in a] + [(-1, t) for t in b]

    def terms_e2(b):
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
        for cand in range(2, p):
            z = pow(cand, (p - 1) // N, p)
            if z == 1:
                continue
            y, order = z, 1
            while y != 1 and order <= N:
                y = y * z % p
                order += 1
            if order == N:
                return sorted(
                    {pow(z, k, p) for k in range(1, N + 1) if math.gcd(k, N) == 1}
                )
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
    universe = [t for t in range(N) if t not in a]
    for idx, b in enumerate(itertools.combinations(universe, 3)):
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
            rec = {"shape": [*a, *b], "threshold_norm_primes": threshold}
            norm_exceptions.append(rec)
            active = [p for p in threshold if actual_activation(b, p)]
            if active:
                activation_exceptions.append({"shape": [*a, *b], "activation_primes": active})
    return {
        "shard": shard,
        "total": total,
        "norm_exceptions": norm_exceptions,
        "activation_exceptions": activation_exceptions,
    }


@app.local_entrypoint()
def main(core: str, tag: str = ""):
    a = parse_core(core)
    if not tag:
        tag = "_".join(str(x) for x in a)
    result_path = NOTES_DIR / f"f3_h3_core_{tag}_census_results.json"
    digest = f"H3_CORE_{tag.upper()}_CENSUS_DONE"

    results = []
    cores = [a for _ in range(N_SHARDS)]
    for item in scan_shard.map(range(N_SHARDS), cores, return_exceptions=True):
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

    active = []
    norm_total = 0
    total = 0
    for r in results:
        total += r["total"]
        norm_total += len(r["norm_exceptions"])
        active.extend(r["activation_exceptions"])
    active = sorted(active, key=lambda r: r["shape"])

    payload = {
        "core": list(a),
        "n": N,
        "total_shapes": total,
        "norm_exception_count": norm_total,
        "activation_exception_count": len(active),
        "activation_exceptions": active,
    }
    result_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(
        f"TOTAL shapes={total} norm_exceptions={norm_total} "
        f"activation_exceptions={len(active)}"
    )
    print(f"WROTE {result_path}")
    for rec in active[:80]:
        print(f"ACTIVATION {rec}")
    if len(active) > 80:
        print(f"ACTIVATION_LIST_TRUNCATED printed=80 total={len(active)}")
    print(digest)


if __name__ == "__main__":
    main()
