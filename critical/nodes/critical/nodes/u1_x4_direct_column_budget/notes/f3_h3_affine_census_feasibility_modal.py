#!/usr/bin/env python3
"""Deterministic affine-representative feasibility shard for Terminal C."""

from __future__ import annotations

import modal


app = modal.App("rs-mca-h3-affine-census-feasibility")
image = modal.Image.debian_slim().pip_install("sympy")

N = 96
N_SHARDS = 8
TARGET_REPS_PER_SHARD = 500
RAW_LIMIT_PER_SHARD = 50000


def stable_bucket(flat: tuple[int, ...]) -> int:
    h = 1469598103934665603
    for x in flat:
        h ^= x + 1
        h *= 1099511628211
        h &= (1 << 64) - 1
    return h % N_SHARDS


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def census_shard(shard: int) -> dict:
    import itertools
    import math
    import sympy as sp

    x = sp.Symbol("x")
    phi = sp.Poly(sp.cyclotomic_poly(N, x), x, domain=sp.ZZ)
    units = [u for u in range(N) if math.gcd(u, N) == 1]

    def canonical_affine(a, b):
        best = None
        for u in units:
            au = tuple((u * t) % N for t in a)
            bu = tuple((u * t) % N for t in b)
            for shift in au:
                left = tuple(sorted((t - shift) % N for t in au))
                right = tuple(sorted((t - shift) % N for t in bu))
                cand = left + right
                if best is None or cand < best:
                    best = cand
            for shift in bu:
                left = tuple(sorted((t - shift) % N for t in bu))
                right = tuple(sorted((t - shift) % N for t in au))
                cand = left + right
                if best is None or cand < best:
                    best = cand
        return best

    def terms_e1(flat):
        a, b = flat[:3], flat[3:]
        return [(1, t) for t in a] + [(-1, t) for t in b]

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

    def actual_activation(flat, p):
        e1 = terms_e1(flat)
        e2 = terms_e2(flat)
        return any(
            eval_terms_mod(e1, z, p) == 0 and eval_terms_mod(e2, z, p) == 0
            for z in primitive_roots_mod(p)
        )

    seen = set()
    norm_exceptions = []
    activation_exceptions = []
    raw_seen = 0

    for a_tail in itertools.combinations(range(1, N), 2):
        a = (0,) + a_tail
        remaining = [t for t in range(1, N) if t not in a_tail]
        for b in itertools.combinations(remaining, 3):
            raw_seen += 1
            flat = canonical_affine(a, b)
            if flat in seen or stable_bucket(flat) != shard:
                if raw_seen >= RAW_LIMIT_PER_SHARD:
                    break
                continue
            seen.add(flat)

            n1 = norm_from_terms(terms_e1(flat))
            n2 = norm_from_terms(terms_e2(flat))
            if n1 != 0 and n2 != 0:
                factors = sp.factorint(math.gcd(n1, n2))
                threshold = [int(p) for p in factors if int(p) % N == 1 and int(p) >= N * N]
                if threshold:
                    rec = {"shape": list(flat), "threshold_norm_primes": threshold}
                    norm_exceptions.append(rec)
                    active = [p for p in threshold if actual_activation(flat, p)]
                    if active:
                        activation_exceptions.append({"shape": list(flat), "activation_primes": active})
            if len(seen) >= TARGET_REPS_PER_SHARD or raw_seen >= RAW_LIMIT_PER_SHARD:
                break
        if len(seen) >= TARGET_REPS_PER_SHARD or raw_seen >= RAW_LIMIT_PER_SHARD:
            break

    return {
        "shard": shard,
        "raw_seen": raw_seen,
        "unique_reps": len(seen),
        "norm_exceptions": norm_exceptions,
        "activation_exceptions": activation_exceptions,
    }


@app.local_entrypoint()
def main():
    results = []
    for item in census_shard.map(range(N_SHARDS), return_exceptions=True):
        if isinstance(item, Exception):
            print(f"SHARD_ERROR {item!r}")
            continue
        results.append(item)
        print(
            f"shard={item['shard']} raw_seen={item['raw_seen']} "
            f"unique_reps={item['unique_reps']} "
            f"norm_exceptions={len(item['norm_exceptions'])} "
            f"activation_exceptions={len(item['activation_exceptions'])}"
        )
        for rec in item["activation_exceptions"][:5]:
            print(f"  ACTIVATION_EXCEPTION {rec}")

    total_reps = sum(r["unique_reps"] for r in results)
    norm_total = sum(len(r["norm_exceptions"]) for r in results)
    active_total = sum(len(r["activation_exceptions"]) for r in results)
    print(
        f"TOTAL unique_reps={total_reps} norm_exceptions={norm_total} "
        f"activation_exceptions={active_total}"
    )
    print("H3_AFFINE_CENSUS_FEASIBILITY_DONE")


if __name__ == "__main__":
    main()
