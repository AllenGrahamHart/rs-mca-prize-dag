#!/usr/bin/env python3
"""Exact-integer FPC5 arithmetic: P1, P5, P7 and the codimension-reserve
identity.

(1) P1  the sharp rate-half M=4,t=2 cell line n=10*ell-8 vs the 2-power grid.
(2) P5  the minimal Johnson-nonpositive rate-half M=4,t=3 LS6 cell.
(3) IDENT  codim(F-flat) = sigma = t*ell + r - d - 1  (derived, checked).
(4) P7  the large-source (M>=5) Johnson sieve: where J = d^2 - N(e-1) <= 0.
(5) the first-moment margin binom(N,d)/q^sigma at the official rows.
"""
from __future__ import annotations

import json
from math import comb, isqrt, log2


def p1_two_power_line(max_ell=4000):
    """Sharp rate-half m4_t2 cell: b=s=ell-3 forces k=5ell-4, n=2k=10ell-8."""
    hits = []
    for ell in range(4, max_ell + 1):
        n = 10 * ell - 8
        k = 5 * ell - 4
        assert 5 * ell == k + 4
        assert n == 2 * k
        assert (5 * ell - 5) + (ell - 3) + 4 * ell == n      # |C|+b+4ell
        if n & (n - 1) == 0:
            hits.append({"ell": ell, "n": n, "log2n": n.bit_length() - 1,
                         "k": k, "core": 5 * ell - 5, "d": 2 * ell - 3,
                         "binom_core_d": comb(5 * ell - 5, 2 * ell - 3)})
    return hits


def p5_minimal_johnson_nonpositive(max_ell=400):
    """rate-half M=4,t=3: N=4ell+b-2, d=2ell-a, b>=7, b<ell,
    1<=a<=floor((b-3)/4), J = ell(4a-b+2)+a^2+2ab-4a <= 0."""
    best = None
    cells = []
    for ell in range(8, max_ell + 1):
        for b in range(7, ell):
            amax = (b - 3) // 4
            for a in range(1, amax + 1):
                J = ell * (4 * a - b + 2) + a * a + 2 * a * b - 4 * a
                # cross-check against the primitive definition J=d^2-N(e-1)
                N = 4 * ell + b - 2
                d = 2 * ell - a
                e = 2 * d + 1 - 3 * ell
                assert J == d * d - N * (e - 1), (ell, b, a)
                if J <= 0:
                    n = 8 * ell + 2 * b - 2
                    rec = {"ell": ell, "b": b, "a": a, "J": J, "N": N,
                           "j": d, "n": n, "k": 4 * ell + b - 1}
                    cells.append(rec)
                    if best is None or N < best["N"]:
                        best = rec
    cells.sort(key=lambda r: (r["N"], r["j"]))
    for r in cells[:6]:
        r["binom_N_j"] = comb(r["N"], r["j"])
    if best is not None:
        best["binom_N_j"] = comb(best["N"], best["j"])
    return best, cells[:6], len(cells)


def ident_check():
    """codim = t*ell + r - d - 1 = sigma (excess agreement above k)."""
    out = []
    # (A) sharp rate-half m4_t2: t=2, r=b=ell-3, d=2ell-3, N=5ell-5
    for ell in range(4, 40):
        N, b, r, d, t = 5 * ell - 5, ell - 3, ell - 3, 2 * ell - 3, 2
        k = N + 1
        agree = (N - d) + r + t * ell
        sigma = agree - k
        codim = t * ell + r - d - 1
        assert sigma == codim == ell - 1, (ell, sigma, codim)
    out.append({"cell": "ratehalf_m4_t2_sharp",
                "codim=sigma": "ell-1", "checked_ell": "4..39"})
    # (B) rate-half m4_t3 LS6 with R empty: t=3, r=0, d=2ell-a, N=4ell+b-2
    for ell in range(8, 40):
        for b in range(7, ell):
            for a in range(1, max(1, (b - 3) // 4) + 1):
                N, d, t, r = 4 * ell + b - 2, 2 * ell - a, 3, 0
                k = N + 1
                sigma = ((N - d) + r + t * ell) - k
                codim = t * ell + r - d - 1
                assert sigma == codim == ell + a - 1, (ell, b, a)
    out.append({"cell": "ratehalf_m4_t3_LS6 (R empty)",
                "codim=sigma": "ell+a-1", "checked": "ell 8..39"})
    return out


def p7_large_source_sieve(k=2**40, rates=(2, 4, 8, 16)):
    """For each rate 1/r and M >= M_min, decide for which t the Johnson
    denominator J = d^2 - N(e-1) can be <= 0 inside FPC5.

    J <= 0 is possible iff t*ell <= N and d* = N(1-sqrt(1-t*ell/N)) is below
    the FPC5 cap min(ell*(M-2), N).  Exact integer test over the admissible
    ell window (S/(M+1), S/M] sampled at its two ends and the midpoint.
    """
    Mmin = {2: 5, 4: 5, 8: 7, 16: 15}
    N = k - 1
    res = []
    for r in rates:
        S = (r - 1) * k + 1
        for M in range(Mmin[r], Mmin[r] + 12):
            lo = S // (M + 1) + 1
            hi = S // M
            if lo > hi:
                continue
            for tag, ell in (("ell_min", lo), ("ell_max", hi),
                             ("ell_mid", (lo + hi) // 2)):
                b = S - M * ell
                if not (0 <= b < ell):
                    continue
                for t in range(2, min(M, 2 * M - 5) + 1):
                    dcap = min(ell * (M - 2) - 1, N)
                    # smallest d with e>=1: d >= ceil((t*ell)/2)
                    dlo = (t * ell + 1) // 2
                    if dlo > dcap:
                        continue
                    disc = N * N - N * t * ell
                    if disc < 0:
                        jpos = True          # J>0 for every d
                        dstar = None
                    else:
                        dstar = N - isqrt(disc)      # J<=0 iff d >= dstar
                        jpos = dstar > dcap
                    if jpos:
                        continue
                    dres_lo = max(dlo, dstar)
                    e_lo = 2 * dres_lo + 1 - t * ell
                    e_hi = 2 * dcap + 1 - t * ell
                    res.append({
                        "rate": f"1/{r}", "M": M, "t": t, "tag": tag,
                        "ell": ell, "b": b,
                        "d_johnson_paid_below": dstar,
                        "d_cap": dcap,
                        "residual_d_window": [dres_lo, dcap],
                        "residual_width": dcap - dres_lo + 1,
                        "e_range": [e_lo, e_hi],
                        "e_over_n": e_hi / (r * k),
                    })
    return res


def official_first_moment(k=2**40):
    """binom(N,d)/q^sigma at the sharp rate-half m4_t2 official cell."""
    ell = (k + 4) // 5
    out = {"note": "5*ell=k+4 has an integer solution only when k=1 mod 5"}
    out["k_mod_5"] = k % 5
    if (k + 4) % 5 == 0:
        n = 2 * k
        N = k - 1
        d = 2 * ell - 3
        sigma = ell - 1
        q = n + 1
        lg = log2(comb(N, d)) if N < 200 else None
        # log2 binom(N,d) via entropy (N huge)
        p = d / N
        H = -(p * log2(p) + (1 - p) * log2(1 - p))
        out.update({
            "ell": ell, "n": n, "N": N, "d": d, "sigma": sigma,
            "log2_binom_N_d_entropy": N * H,
            "sigma_log2_q_lower": sigma * log2(q),
            "log2_first_moment_upper": N * H - sigma * log2(q),
            "exact_log2_binom_small": lg,
        })
    return out


def main():
    p1 = p1_two_power_line()
    best, top, ncells = p5_minimal_johnson_nonpositive()
    ident = ident_check()
    sieve = p7_large_source_sieve()
    fm = official_first_moment()
    by_M = {}
    for r in sieve:
        key = (r["rate"], r["M"])
        by_M.setdefault(str(key), set()).add(r["t"])
    print(json.dumps({
        "P1_two_power_sharp_cells": p1,
        "P1_verdict": [h["ell"] for h in p1],
        "P5_minimal_johnson_nonpositive_LS6": best,
        "P5_next_smallest": top,
        "P5_total_cells_scanned_le400": ncells,
        "IDENT_codim_equals_sigma": ident,
        "P7_residual_t_by_(rate,M)": {k2: sorted(v)
                                      for k2, v in sorted(by_M.items())},
        "P7_sample_rows": sieve[:14],
        "P7_total_residual_rows": len(sieve),
        "official_first_moment": fm,
    }, indent=1))


if __name__ == "__main__":
    main()
