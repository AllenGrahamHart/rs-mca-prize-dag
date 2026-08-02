#!/usr/bin/env python3
"""Order-64 analogue (2N=64, N=32) of the C1 doubling-orbit sweep.

2^32 Boolean subsets cannot be enumerated, so Z is obtained from an exact
count DP over Z_q (32 rounds of counts <- counts + roll(counts, c)); the
kernel weight profile is obtained by a WEIGHT-CAPPED meet-in-the-middle
(both halves capped at `--wcap`), which is complete for total weight <= wcap
and therefore returns the exact minimum relation weight whenever that
minimum is <= wcap.

All reported X, Z, N_w are exact integers/Fractions.
"""

from __future__ import annotations

import argparse
import json
import time
from fractions import Fraction
from itertools import combinations

import numpy as np

import orbit_spectrum as osp


def capped_ternary(coeffs: list[int], q: int, wcap: int):
    """All ternary vectors over `coeffs` with weight <= wcap: (values, weights)."""
    n = len(coeffs)
    vals = [0]
    wts = [0]
    for w in range(1, wcap + 1):
        for pos in combinations(range(n), w):
            base = [0]
            for p in pos:
                a = coeffs[p]
                base = [(b + a) % q for b in base] + [(b - a) % q for b in base]
            vals.extend(base)
            wts.extend([w] * len(base))
    return np.array(vals, dtype=np.int64), np.array(wts, dtype=np.int64)


def capped_profile(coeffs: list[int], q: int, wcap: int) -> list[int]:
    """Exact N_w for all w <= wcap (entries above wcap are not reported)."""
    n = len(coeffs)
    half = n // 2
    lv, lw = capped_ternary(coeffs[:half], q, wcap)
    rv, rw = capped_ternary(coeffs[half:], q, wcap)
    order = np.argsort(lv, kind="stable")
    lvs, lws = lv[order], lw[order]
    cum = np.zeros((lvs.size + 1, wcap + 1), dtype=np.int64)
    cum[np.arange(1, lvs.size + 1), lws] = 1
    cum = np.cumsum(cum, axis=0)
    targets = (-rv) % q
    lo = np.searchsorted(lvs, targets, side="left")
    hi = np.searchsorted(lvs, targets, side="right")
    hist = cum[hi] - cum[lo]
    idx = rw[:, None] + np.arange(wcap + 1)[None, :]
    N = np.zeros(2 * wcap + 1, dtype=np.int64)
    np.add.at(N, idx.ravel(), hist.ravel())
    return [int(N[w]) for w in range(wcap + 1)]


def subset_sum_SS_dp(coeffs: list[int], q: int) -> int:
    counts = np.zeros(q, dtype=np.int64)
    counts[0] = 1
    for a in coeffs:
        counts = counts + np.roll(counts, a)
    c = counts.astype(object)
    return int(np.sum(c * c))


def process(q: int, twoN: int, wcap: int) -> dict:
    N = twoN // 2
    omega = osp.root_of_order(q, twoN)
    coeffs = [pow(omega, i, q) for i in range(N)]
    fac = osp.factorize(q - 1)
    ord2 = osp.mult_order(2, q, fac)
    import math as _m
    r = ord2 // _m.gcd(ord2, twoN)
    M = (q - 1) // twoN
    SS = subset_sum_SS_dp(coeffs, q)
    num = q * SS - (1 << (2 * N))
    X = Fraction(num, q << N)
    flat = Fraction(q - 1, q << N)
    prof = capped_profile(coeffs, q, wcap)
    nz = [w for w in range(1, wcap + 1) if prof[w] > 0]
    return {
        "q": q, "twoN": twoN, "N": N, "v2_qm1": fac.get(2, 0), "ord2": ord2,
        "r": r, "M": M, "n_cycles": M // r, "max_cycle": r,
        "SS": str(SS), "X_num": X.numerator, "X_den": X.denominator,
        "X_float": float(X), "Z_float": float(Fraction(SS, 1 << N)),
        "X_flat_num": flat.numerator, "X_flat_den": flat.denominator,
        "is_exactly_flat": X == flat, "avgA_float": float(X / flat),
        "sumA_is_integer": num % twoN == 0, "sumA_nonneg": num >= 0,
        "weight_profile_capped": prof, "wcap": wcap,
        "min_relation_weight": (nz[0] if nz else None),
        "min_relation_weight_exact": bool(nz),
        "hard_regime": q > (1 << N),
        "haar_baseline_2N_over_q": (1 << N) / q,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--twoN", type=int, default=64)
    ap.add_argument("--qmin", type=int, default=0)
    ap.add_argument("--qmax", type=int, default=100000)
    ap.add_argument("--wcap", type=int, default=6)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    t0 = time.time()
    ps = osp.primes_up_to(args.qmax)
    qs = [int(p) for p in ps if p % args.twoN == 1 and p > args.qmin]
    rows = [process(q, args.twoN, args.wcap) for q in qs]
    meta = {"twoN": args.twoN, "N": args.twoN // 2,
            "qmin": args.qmin, "qmax": args.qmax,
            "wcap": args.wcap, "n_rows": len(rows),
            "seconds": round(time.time() - t0, 2)}
    with open(args.out, "w") as f:
        json.dump({"meta": meta, "rows": rows}, f)
    print(json.dumps(meta))


if __name__ == "__main__":
    main()
