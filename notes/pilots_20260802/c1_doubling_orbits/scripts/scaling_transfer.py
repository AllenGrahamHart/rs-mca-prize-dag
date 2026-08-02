#!/usr/bin/env python3
"""N-scaling transfer test for the C1 excess at MATCHED regime q ~ 2^N.

For each 2N, take the first `--nsample` primes q = 1 (mod 2N) with q > 2^N
(so the Haar baseline 2^N/q is just below 1 -- the same normalised regime for
every N, and the regime the official L=1 target X <= 4 lives in), and compute
X exactly.  Comparing the X-distribution across N answers the question the
L=1 lab cannot: does the excess grow with N?

X, Z and the kernel weight profile are exact (integers/Fractions).
"""

from __future__ import annotations

import argparse
import json
import math
import time
from fractions import Fraction

import numpy as np

import orbit_spectrum as osp


def next_primes(start: int, mod: int, count: int) -> list[int]:
    from sympy import isprime
    out = []
    q = start + (mod + 1 - start % mod) % mod
    if q <= start:
        q += mod
    while len(out) < count:
        if isprime(q):
            out.append(q)
        q += mod
    return out


def row(q: int, twoN: int, want_profile: bool) -> dict:
    N = twoN // 2
    omega = osp.root_of_order(q, twoN)
    coeffs = [pow(omega, i, q) for i in range(N)]
    fac = osp.factorize(q - 1)
    ord2 = osp.mult_order(2, q, fac)
    r = ord2 // math.gcd(ord2, twoN)
    M = (q - 1) // twoN
    SS = osp.subset_sum_SS(coeffs, q)
    num = q * SS - (1 << (2 * N))
    X = Fraction(num, q << N)
    d = {"q": q, "twoN": twoN, "N": N, "r": r, "n_cycles": M // r, "M": M,
         "v2_qm1": fac.get(2, 0),
         "X_num": X.numerator, "X_den": X.denominator, "X_float": float(X),
         "relmass_float": float(Fraction(SS, 1 << N) - 1),
         "haar_baseline": (1 << N) / q,
         "sumA_is_integer": num % twoN == 0, "sumA_nonneg": num >= 0,
         "is_exactly_flat": X == Fraction(q - 1, q << N)}
    if want_profile:
        Nw = osp.kernel_weight_profile(coeffs, q)
        assert int(sum(int(Nw[w]) * (1 << (N - w)) for w in range(N + 1))) == SS
        d["weight_profile"] = [int(x) for x in Nw]
        nz = [w for w in range(1, N + 1) if Nw[w] > 0]
        d["min_relation_weight"] = int(nz[0]) if nz else None
        d["orbits_by_weight"] = {w: int(Nw[w]) // twoN
                                 for w in range(1, N + 1) if Nw[w]}
        d["all_Nw_div_2N"] = all(int(Nw[w]) % twoN == 0 for w in range(1, N + 1))
    return d


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--twoNs", default="8,12,16,20,24,28,32")
    ap.add_argument("--nsample", type=int, default=400)
    ap.add_argument("--profile-max-N", type=int, default=24)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    t0 = time.time()
    blocks = []
    for twoN in [int(x) for x in args.twoNs.split(",")]:
        N = twoN // 2
        qs = next_primes(1 << N, twoN, args.nsample)
        rows = [row(q, twoN, N <= args.profile_max_N) for q in qs]
        xs = sorted(r["X_float"] for r in rows)
        n = len(xs)
        blocks.append({
            "twoN": twoN, "N": N, "n": n,
            "q_lo": qs[0], "q_hi": qs[-1], "q_over_2N_hi": qs[-1] / (1 << N),
            "median_X": xs[n // 2], "mean_X": sum(xs) / n,
            "p90_X": xs[int(0.90 * (n - 1))], "p99_X": xs[int(0.99 * (n - 1))],
            "max_X": xs[-1], "min_X": xs[0],
            "argmax_q": max(rows, key=lambda r: r["X_float"])["q"],
            "n_above_4": sum(1 for x in xs if x > 4),
            "n_above_2": sum(1 for x in xs if x > 2),
            "all_sumA_integer": all(r["sumA_is_integer"] for r in rows),
            "all_Nw_div_2N": all(r.get("all_Nw_div_2N", True) for r in rows),
            "flat_rows": [r["q"] for r in rows if r["is_exactly_flat"]],
            "max_row": max(rows, key=lambda r: r["X_float"]),
            "rows": rows,
        })
        print(json.dumps({k: v for k, v in blocks[-1].items()
                          if k not in ("rows", "max_row")}))
    with open(args.out, "w") as f:
        json.dump({"meta": {"seconds": round(time.time() - t0, 2),
                            "nsample": args.nsample,
                            "regime": "first nsample primes q = 1 mod 2N with q > 2^N"},
                   "blocks": blocks}, f)


if __name__ == "__main__":
    main()
