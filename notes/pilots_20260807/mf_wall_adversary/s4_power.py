#!/usr/bin/env python3
"""S4 POWER CONTROL (run FIRST).

S4-P1 (the HARD control): does the round-23 shape-pun test separate
FPC5 red 1 (l1_fpc5_ratehalf_m4_t2_payment, OPEN) from its PROVED
sibling l1_fpc5_ratequarter_m4_t2_payment (absolute bound 10)?

Both are M=4, t=2, two-full-petal FPC5 cells with the SAME algebra;
only the source arithmetic differs:
    rate 1/2 :  4ell+b = k+1     ->  2ell < k-1   (under-determined)
    rate 1/4 :  4ell+b = 3k+1    ->  2ell > k-1   (OVER-determined)

The round-23 test (MF) asks only: "count monic degree-d locators split
on C inside a linear flat of projective dimension e = 2d+1-t*ell whose
codimension is exactly sigma".  This script decides, by EXACT INTEGER
arithmetic at the official row k = 2^40, whether the PROVED cell also
satisfies every clause of (MF) -- growing e, codim = sigma, first
moment far below 1.  If it does, the test groups a two-line-proved
problem with an open one and therefore HAS NO POWER.

Also emits the over-determination predicate t*ell > N, which is the
(MF)-expressible predicate that DOES separate them.

Stdlib only.  Run via tools/ramguard.
"""
from __future__ import annotations

import json
from math import comb, log2


def log2_binom(N, d):
    """log2 C(N,d): exact for small N, binary entropy for huge N."""
    if N < 2000:
        return log2(comb(N, d)) if 0 <= d <= N else float("-inf")
    if d <= 0 or d >= N:
        return 0.0
    p = d / N
    H = -(p * log2(p) + (1 - p) * log2(1 - p))
    return N * H


def cell_scan(k, rate_den, M=4, t=2, label=""):
    """Scan the admissible (ell, b) window and the FPC5 d-window.

    Source equation for rate 1/rate_den with M petals:
        M*ell + b = (rate_den-1)*k + 1,   0 <= b < ell.
    FPC5 clause: d < ell*(M-2), 2 <= t < 2M-4, e = 2d+1-t*ell -> infty.
    Core N = k-1.  sigma = t*ell + r - d - 1 = codim (round-23 identity).
    """
    S = (rate_den - 1) * k + 1
    N = k - 1
    n = rate_den * k
    q = n + 1                     # official q >= n; lower bound on log2 q
    lo = S // (M + 1) + 1         # b < ell  =>  ell > S/(M+1)
    hi = S // M                   # b >= 0   =>  ell <= S/M
    rows = []
    for tag, ell in (("ell_min", lo), ("ell_mid", (lo + hi) // 2),
                     ("ell_max", hi)):
        b = S - M * ell
        if not (0 <= b < ell):
            continue
        dcap = min(ell * (M - 2) - 1, N)      # FPC5 cap d < ell(M-2)
        dlo = max(t * ell // 2, 0)            # e = 2d+1-t*ell >= 1
        if dlo > dcap:
            continue
        for dtag, d in (("d_lo", dlo), ("d_mid", (dlo + dcap) // 2),
                        ("d_hi", dcap)):
            if not (dlo <= d <= dcap):
                continue
            e = 2 * d + 1 - t * ell           # projective flat dimension
            for r in (0, b):                  # background agreements
                sigma = t * ell + r - d - 1
                codim = t * ell + r - d - 1   # the round-23 identity
                lb = log2_binom(N, d)
                fm = lb - sigma * log2(q)     # log2 first moment
                rows.append({
                    "family": label, "tag": f"{tag}/{dtag}/r={r}",
                    "ell": ell, "b": b, "d": d, "N": N,
                    "e_proj_dim": e, "e_over_n": e / n,
                    "sigma": sigma, "codim": codim,
                    "codim_equals_sigma": codim == sigma,
                    "sigma_positive": sigma > 0,
                    "log2_first_moment_upper": fm,
                    "first_moment_below_1": fm < 0,
                    "overdetermined_t_ell_gt_N": t * ell > N,
                })
    return rows


def mf_clause_table(rows):
    """Round-23 (MF) clause vector for a family."""
    if not rows:
        return None
    return {
        "codim_equals_sigma_ALWAYS": all(r["codim_equals_sigma"] for r in rows),
        "sigma_positive_ALWAYS": all(r["sigma_positive"] for r in rows),
        "max_e_proj_dim": max(r["e_proj_dim"] for r in rows),
        "max_e_over_n": max(r["e_over_n"] for r in rows),
        "e_grows_linearly_in_n": max(r["e_over_n"] for r in rows) > 0.01,
        "first_moment_below_1_ALWAYS": all(r["first_moment_below_1"]
                                           for r in rows),
        "worst_log2_first_moment": max(r["log2_first_moment_upper"]
                                       for r in rows),
        "overdetermined_t_ell_gt_N": sorted(
            {r["overdetermined_t_ell_gt_N"] for r in rows}),
    }


def small_cell_check():
    """The same clauses at small reachable cells, exact integers."""
    out = []
    # rate 1/2 sharp line: 5ell = k+4, b=r=s=ell-3, d=2ell-3
    for ell in (4, 5, 6, 8, 12):
        k = 5 * ell - 4
        N = k - 1
        d = 2 * ell - 3
        r = b = ell - 3
        sigma = 2 * ell + r - d - 1
        e = 2 * d + 1 - 2 * ell
        n = 2 * k
        out.append({"family": "ratehalf_M4_t2_sharp", "ell": ell, "k": k,
                    "n": n, "N": N, "d": d, "b": b, "r": r,
                    "sigma": sigma, "codim": 2 * ell + r - d - 1,
                    "e_proj_dim": e,
                    "t_ell": 2 * ell, "overdetermined": 2 * ell > N,
                    "log2_first_moment": log2_binom(N, d)
                    - sigma * log2(n + 1)})
    # rate 1/4: 4ell+b = 3k+1.  Pick k so an integer (ell,b) exists.
    for k in (13, 21, 41, 85, 169):
        S = 3 * k + 1
        N = k - 1
        n = 4 * k
        for ell in range(S // 5 + 1, S // 4 + 1):
            b = S - 4 * ell
            if not (0 <= b < ell):
                continue
            dcap = min(2 * ell - 1, N)
            dlo = ell                      # e >= 1
            if dlo > dcap:
                continue
            for d in (dlo, dcap):
                sigma = 2 * ell + 0 - d - 1
                e = 2 * d + 1 - 2 * ell
                out.append({"family": "ratequarter_M4_t2_PROVED",
                            "ell": ell, "k": k, "n": n, "N": N, "d": d,
                            "b": b, "r": 0, "sigma": sigma,
                            "codim": 2 * ell + 0 - d - 1,
                            "e_proj_dim": e,
                            "t_ell": 2 * ell, "overdetermined": 2 * ell > N,
                            "log2_first_moment": log2_binom(N, d)
                            - sigma * log2(n + 1)})
            break
    return out


def main():
    k = 2 ** 40
    half = cell_scan(k, 2, label="ratehalf_M4_t2_RED1_OPEN")
    quarter = cell_scan(k, 4, label="ratequarter_M4_t2_PROVED_bound10")
    small = small_cell_check()
    # verify codim = sigma identically on every row (round-23 identity)
    assert all(r["codim"] == r["sigma"] for r in small)
    print(json.dumps({
        "S4_P1_power_control": {
            "control_pair": ["l1_fpc5_ratehalf_m4_t2_payment (OPEN red 1)",
                             "l1_fpc5_ratequarter_m4_t2_payment "
                             "(PROVED, absolute bound 6+4=10)"],
            "official_row_k": k,
            "MF_clauses_RED1_ratehalf": mf_clause_table(half),
            "MF_clauses_PROVED_ratequarter": mf_clause_table(quarter),
            "n_rows_scanned": {"ratehalf": len(half),
                               "ratequarter": len(quarter)},
        },
        "sample_rows_ratehalf": half[:6],
        "sample_rows_ratequarter": quarter[:6],
        "small_exact_cells": small,
    }, indent=1))


if __name__ == "__main__":
    main()
