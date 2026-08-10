#!/usr/bin/env python3
"""D3 -- DOES THE C8 FIRING MECHANISM REACH THE REAL 408 RESIDUAL ROWS?

The C8 hit is explained EXACTLY by an arithmetic sufficient condition,
not by a small-numbers artefact:

  (FALS-1)  every guarded root set is a d-subset of the core C, so
            |U| <= N = k-1.  Hence  N + kappa < 2d  ==>  sigma < 2a,
            i.e. the COMPLEMENT orientation of (PC3') beats the direct
            one at the whole cell.  In particular 2d > N with kappa = 0
            suffices.

This script asks whether `2d > N` (and the sharper `N + kappa < 2d`) is
reachable inside the node's OWN admissible d-windows at the real
k = 2^40 rows, using the SAME row generator and the SAME window
arithmetic as the round-25 audit (`fpc5_exact.p7_large_source_sieve`,
`d4_cj3_audit`), so the comparison is apples to apples.

Windows, verbatim from d4_cj3_audit.audit:
  residual window   [dres_lo, dcap]                    (the 408 rows)
  CJ window         lo = max(dres_lo, (t-1)ell, ceil(h/2))
                    hi = min(dcap, (t-1)ell + b)       (H-u == H-lt)

Stdlib only.  Run via tools/ramguard local -- python3 from repo root.
"""
from __future__ import annotations

import json
import sys
from math import comb

ROOT = "/home/u2470931/smooth-read-solomin/prize"
sys.path.insert(0, ROOT + "/notes/pilots_20260807/fpc5_diag")
sys.path.insert(0, ROOT + "/notes/pilots_20260808/t_petal_lemma")
from fpc5_exact import p7_large_source_sieve            # noqa: E402
from tpetal_cj3_probe import neg_interval               # noqa: E402


def analyse(k=2 ** 40):
    N = k - 1
    rows = p7_large_source_sieve()
    res = {"rows_total": len(rows), "k": k, "N": N}
    hit_resid, hit_cj, hit_cj_live = [], [], []
    tM = {}
    for r in rows:
        t, ell, M, b = r["t"], r["ell"], r["M"], r["b"]
        rate = int(r["rate"].split("/")[1])
        h = t * ell
        dlo, dhi = r["residual_d_window"]
        tM[(r["rate"], M, t)] = tM.get((r["rate"], M, t), 0) + 1
        # --- (a) inside the RESIDUAL window only
        if 2 * dhi > N:
            hit_resid.append({"rate": r["rate"], "M": M, "t": t,
                              "tag": r["tag"], "ell": ell, "b": b,
                              "d_max": dhi, "two_d_minus_N": 2 * dhi - N})
        # --- (b) inside the CJ-admissible window
        lo = max(dlo, (t - 1) * ell, (h + 1) // 2)
        hi = min(dhi, (t - 1) * ell + b)
        if lo > hi:
            continue
        if 2 * hi > N:
            u = hi - (t - 1) * ell
            rJ = 2 * hi - h
            Jp = hi * hi - N * (2 * hi - h)          # d^2 - N(e-1)
            A, B = b + N, -2 * N * ((t - 1) * ell + b)
            Cc = N * ((t - 1) ** 2 * ell ** 2 + b * t * ell)
            Jcj = A * hi * hi + B * hi + Cc
            rec = {"rate": r["rate"], "M": M, "t": t, "tag": r["tag"],
                   "ell": ell, "b": b, "u": u, "d": hi, "r_J": rJ,
                   "CJ_window": [lo, hi], "two_d_minus_N": 2 * hi - N,
                   "d_over_N": hi / N, "J_plain": Jp, "LIVE": Jp <= 0,
                   "J_CJ": Jcj, "CJ3_fires": Jcj > 0}
            hit_cj.append(rec)
            if Jp <= 0:
                hit_cj_live.append(rec)
    res["rows_with_2d_gt_N_in_residual_window"] = len(hit_resid)
    res["rows_with_2d_gt_N_in_CJ_window"] = len(hit_cj)
    res["rows_with_2d_gt_N_in_CJ_window_and_LIVE"] = len(hit_cj_live)
    res["sample_resid"] = hit_resid[:6]
    res["sample_cj"] = hit_cj[:6]
    res["(rate,M,t) combos present"] = {str(k2): v
                                        for k2, v in sorted(tM.items())}
    # --- structural explanation: 2d > N needs t > M/2 while H-u needs
    #     t <= M-2 (since (t-1)ell <= ell(M-2)-1).  Report the feasible
    #     (M,t) band and whether the sieve ever produces it.
    band = []
    for M in range(5, 25):
        ts = [t for t in range(2, M - 1) if 2 * t > M]
        if ts:
            band.append({"M": M, "t_band_for_2d_gt_N": ts,
                         "sieve_t_present": sorted(
                             {t for (rt, MM, t) in tM if MM == M})})
    res["feasible_(M,t)_band"] = band
    return res


def anticode(sigma, a, delta):
    e = a - delta + 1
    if a <= 0 or e <= 0 or e > sigma:
        return None
    return comb(sigma, e) // comb(a, e)


def c8_pricing():
    """Both (PC3') orientations at the C8 cell, and the trivial C(N,d)."""
    N, d = 9, 5
    out = []
    for ovl in (2, 3, 4):
        delta = d - ovl
        for kappa in (0, 1):
            sig, a = N - kappa, d - kappa
            out.append({"kappa": kappa, "OVL_MAX": ovl, "delta": delta,
                        "ANN_SIGMA": sig, "ANN_A": a, "ANN_ACO": sig - a,
                        "FIRE_SIGMA": sig < 2 * a,
                        "AC_DIRECT": anticode(sig, a, delta),
                        "AC_COMP": anticode(sig, sig - a, delta),
                        "trivial_binom_N_d": comb(N, d)})
    return out


def main():
    print(json.dumps({"REAL_ROWS": analyse(), "C8_PRICING": c8_pricing()},
                     indent=1))


if __name__ == "__main__":
    main()
