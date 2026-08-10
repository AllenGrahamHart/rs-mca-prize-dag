#!/usr/bin/env python3
"""D3b -- IS THE FIRING LOAD-BEARING?  Price BOTH (PC3') orientations at
the real k = 2^40 residual rows (PREREG R8 / P15).

At a cell with core C (|C| = N), defect degree d, exact petal support
h = t*ell and the (JB3)/(CJ2) cap r_J = 2d-h, the instrument sees root
sets of size d in an N-set, pairwise meeting in <= r_J, so
delta = d-r_J = h-d and (with kappa = 0, sigma = N)

  AC_DIRECT = C(N, e) / C(d, e),          e = r_J+1 = 2d+1-h
  AC_COMP   = C(N, N-h+1) / C(N-d, N-h+1)

AC_COMP < AC_DIRECT  <=>  N-d < d  <=>  2d > N   (the round-25 threshold).

Reported in bits (lgamma), against log2(n^3) = the polynomial target the
node needs, and log2 C(N,d) = the trivial ceiling.

Stdlib only.  Run via tools/ramguard local -- python3 from repo root.
"""
from __future__ import annotations

import json
import sys
from math import lgamma, log, log2

ROOT = "/home/u2470931/smooth-read-solomin/prize"
sys.path.insert(0, ROOT + "/notes/pilots_20260807/fpc5_diag")
from fpc5_exact import p7_large_source_sieve            # noqa: E402

LN2 = log(2.0)


def lb(n, k):
    """log2 binom(n,k) via lgamma; None if out of range."""
    if k < 0 or k > n:
        return None
    return (lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)) / LN2


def main(k=2 ** 40):
    N = k - 1
    rows = p7_large_source_sieve()
    fired, notfired = [], []
    for r in rows:
        t, ell, M, b = r["t"], r["ell"], r["M"], r["b"]
        rate = int(r["rate"].split("/")[1])
        n = rate * k
        h = t * ell
        dlo, dhi = r["residual_d_window"]
        lo = max(dlo, (t - 1) * ell, (h + 1) // 2)
        hi = min(dhi, (t - 1) * ell + b)
        if lo > hi:
            continue
        d = hi                       # top of the CJ-admissible window
        e = 2 * d + 1 - h
        acd = None if e > N else (lb(N, e) - (lb(d, e) or 0)
                                  if lb(d, e) is not None else None)
        c2 = N - h + 1
        acc = (None if (c2 < 0 or c2 > N - d)
               else lb(N, c2) - lb(N - d, c2))
        rec = {"rate": r["rate"], "M": M, "t": t, "tag": r["tag"],
               "ell": ell, "b": b, "d": d, "h": h, "r_J": 2 * d - h,
               "two_d_minus_N": 2 * d - N, "d_over_N": d / N,
               "log2_AC_DIRECT": acd, "log2_AC_COMP": acc,
               "log2_gain_COMP_over_DIRECT": (acd - acc
                                              if acd is not None
                                              and acc is not None else None),
               "log2_trivial_binom_N_d": lb(N, d),
               "log2_n_cubed": 3 * log2(n),
               "COMP_is_polynomial": (acc is not None
                                      and acc <= 3 * log2(n))}
        (fired if 2 * d > N else notfired).append(rec)

    def agg(rs, key):
        vs = [x[key] for x in rs if x.get(key) is not None]
        if not vs:
            return None
        return {"min": min(vs), "max": max(vs),
                "mean": sum(vs) / len(vs), "n": len(vs)}

    print(json.dumps({
        "k": k, "N": N,
        "rows_CJ_admissible": len(fired) + len(notfired),
        "rows_FIRING_2d_gt_N": len(fired),
        "rows_NOT_firing": len(notfired),
        "FIRING_log2_AC_DIRECT": agg(fired, "log2_AC_DIRECT"),
        "FIRING_log2_AC_COMP": agg(fired, "log2_AC_COMP"),
        "FIRING_log2_gain": agg(fired, "log2_gain_COMP_over_DIRECT"),
        "FIRING_log2_trivial": agg(fired, "log2_trivial_binom_N_d"),
        "FIRING_any_COMP_polynomial": any(x["COMP_is_polynomial"]
                                          for x in fired),
        "log2_n_cubed_range": [min(x["log2_n_cubed"] for x in fired),
                               max(x["log2_n_cubed"] for x in fired)],
        "NOTFIRING_log2_AC_DIRECT": agg(notfired, "log2_AC_DIRECT"),
        "NOTFIRING_log2_AC_COMP": agg(notfired, "log2_AC_COMP"),
        "FIRING_best_row_by_AC_COMP": min(
            (x for x in fired if x["log2_AC_COMP"] is not None),
            key=lambda x: x["log2_AC_COMP"], default=None),
        "FIRING_biggest_margin_row": max(
            fired, key=lambda x: x["two_d_minus_N"], default=None),
        "FIRING_samples": fired[:4],
    }, indent=1))


if __name__ == "__main__":
    main()
