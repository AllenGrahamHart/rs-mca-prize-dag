#!/usr/bin/env python3
"""Slice-level cancellation, b-resolved reachability, scaling (F2A.5).

Run:  tools/ramguard local -- python3 \
        notes/pilots_20260802/f2_slice_coefficients/cancellation.py [stage]

stages: count | scale | weight

PROXY.  The exact integer statistic used at scale is the BALANCED-WEIGHT
proxy: keep the carry AND the cosine signs, drop only the magnitude
variation.  Using the modified residue sigma_i = s_i + p u_i (see slicecore)
this is exactly

    V_b = sum_{|tau| = b} h_p( sum_i sigma_i(tau_i) mod 2p )   (an INTEGER)
    rho_b^bal = |V_b| / C(n,b)                                  (exact rational)

Stage "weight" recomputes rho_b = |A_b|/E_b with the TRUE weights
2cos(pi s/p) in exact Z[zeta_p] at small n and cross-checks the proxy.

Reported exponents:
  eta_n = -log2(rho_b)/n           bits per coordinate; targets 1/3 and 1/43
  eta_S = -log2(rho_b)/log2 C(n,b) fraction of the square-root barrier (1/2)
"""

from __future__ import annotations

import json
import math
import os
import sys
from fractions import Fraction

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from slicecore import (  # noqa: E402
    Delta_of, RESULTS, abs_pairs, admissible_orders, carry_sign, elem_sym,
    instance, sigma_of, slice_coeffs_carrydp, slice_reach_dp,
)
from mode_and_coset import V_of, slice_count_sigma  # noqa: E402

TARGET_THIRD = 1.0 / 3.0
TARGET_43 = 1.0 / 43.0


def row_stats(p, loc):
    n = len(loc)
    sig = sigma_of(p, loc)
    N = slice_count_sigma(p, sig)
    V = V_of(p, N, n)
    R = slice_reach_dp(p, sig)
    per = []
    for b in range(n + 1):
        C = math.comb(n, b)
        per.append({"b": b, "V": V[b], "C": C,
                    "reach": bin(R[b]).count("1"),
                    "support": sum(1 for r in range(2 * p) if N[b][r])})
    return per, sum(V)


def neglog2(V, C):
    if V == 0:
        return None
    return math.log2(C) - math.log2(abs(V))


def stage_count():
    rows = []
    for p in (7, 11, 13, 19, 23, 31, 41, 53, 67, 101):
        for c in [(1, 1), (2, 3), (1, 2), (0, 1)]:
            c = (c[0] % p, c[1] % p)
            _, _, full = instance(p, c=c, n=64)
            if len(full) < 16:
                continue
            for n in (16, 24, 32, 48, 64):
                if n > len(full):
                    continue
                per, tot = row_stats(p, full[:n])
                Dl = Delta_of(p, full[:n])
                rows.append({"p": p, "c": list(c), "n": n, "per_b": per,
                             "full": tot, "two_p": 2 * p,
                             "delta_parity": sorted({x % 2 for x in Dl})})
    with open(os.path.join(RESULTS, "slice_cancellation_counts.json"), "w") as f:
        json.dump({"rows": rows}, f)
    print(f"rows={len(rows)}")

    print("\n[T1] balanced-weight slice cancellation, central slice b = n/2")
    print(f"{'p':>4} {'c':>7} {'par':>6} {'n':>4} {'|V_b|':>18} "
          f"{'-log2 rho':>10} {'eta_n':>7} {'eta_S':>7} "
          f"{'>1/3':>5} {'>1/43':>6}")
    for r in rows:
        n, b = r["n"], r["n"] // 2
        e = r["per_b"][b]
        lg = neglog2(e["V"], e["C"])
        if lg is None:
            continue
        etan, etaS = lg / n, lg / math.log2(e["C"])
        print(f"{r['p']:4d} {str(tuple(r['c'])):>7} "
              f"{str(r['delta_parity']):>6} {n:4d} {abs(e['V']):18d} "
              f"{lg:10.3f} {etan:7.4f} {etaS:7.4f} "
              f"{'Y' if etan > TARGET_THIRD else 'n':>5} "
              f"{'Y' if etan > TARGET_43 else 'n':>6}")

    print("\n[T2] b-RESOLVED REACHABILITY |R_b| (Sharp Law A, sliced): "
          "smallest b with |R_b| = 2p, and the coset index")
    print(f"{'p':>4} {'c':>7} {'n':>4} {'2p':>5} {'log2 2p':>8} "
          f"{'b_min_full':>10} {'max|R_b| over b':>15} {'coset index':>11}")
    for r in rows:
        if r["n"] != 48:
            continue
        fulls = [e["b"] for e in r["per_b"] if e["reach"] == r["two_p"]]
        mx = max(e["reach"] for e in r["per_b"])
        idx = r["two_p"] // mx if mx else 0
        print(f"{r['p']:4d} {str(tuple(r['c'])):>7} {r['n']:4d} "
              f"{r['two_p']:5d} {math.log2(r['two_p']):8.2f} "
              f"{(min(fulls) if fulls else -1):10d} {mx:15d} {idx:11d}")


def stage_scale():
    """Worst CENTRAL slice vs n, at fixed p, for mixed and all-odd windows."""
    print("[T3] SCALING: worst slice over n/4 <= b <= 3n/4, vs n "
          "(exact integers)")
    print(f"{'p':>4} {'c':>7} {'win':>4} {'n':>4} {'worst -log2 rho':>16} "
          f"{'eta_n':>8} {'full-window -log2':>18} {'log2 p':>8}")
    rows = []
    for p in (23, 41, 67, 101):
        for c in ((1, 1), (2, 3)):
            _, _, allloc = instance(p, c=c, n=400)
            aD = Delta_of(p, allloc)
            sel_odd = [i for i in range(len(aD)) if aD[i] % 2 == 1]
            for tag, sel in (("mix", list(range(len(allloc)))),
                             ("odd", sel_odd)):
                for n in (16, 24, 32, 48, 64, 80, 96):
                    if n > len(sel):
                        continue
                    loc = [allloc[i] for i in sel[:n]]
                    per, tot = row_stats(p, loc)
                    cand = [neglog2(e["V"], e["C"])
                            for e in per if n // 4 <= e["b"] <= 3 * n // 4]
                    cand = [x for x in cand if x is not None]
                    worst = min(cand) if cand else float("nan")
                    fw = (n - math.log2(abs(tot))) if tot else float("inf")
                    rows.append({"p": p, "c": list(c), "tag": tag, "n": n,
                                 "worst_central_neglog2": worst,
                                 "full_neglog2": fw})
                    print(f"{p:4d} {str(c):>7} {tag:>4} {n:4d} {worst:16.4f} "
                          f"{worst/n:8.4f} {fw:18.4f} {math.log2(p):8.4f}")
    with open(os.path.join(RESULTS, "slice_scaling.json"), "w") as f:
        json.dump({"rows": rows}, f, indent=1)


def stage_weight():
    """TRUE weights, exact Z[zeta_p]; also validates the balanced proxy."""
    rows = []
    print("[T4] TRUE-WEIGHT slice cancellation vs the balanced proxy "
          "(exact algebra; decimal is a 60-digit rendering)")
    print(f"{'p':>4} {'c':>7} {'n':>3} {'b':>3} {'true -log2 rho':>15} "
          f"{'proxy -log2 rho':>16} {'eta_n(true)':>12}")
    for p, nmax in ((7, 12), (11, 12), (13, 12), (19, 10), (23, 10)):
        for c in [(1, 1), (2, 3), (0, 1)]:
            c = (c[0] % p, c[1] % p)
            _, _, full = instance(p, c=c, n=nmax)
            if len(full) < nmax:
                continue
            for n in (8, nmax):
                loc = full[:n]
                A = slice_coeffs_carrydp(p, loc)
                E = elem_sym(abs_pairs(p, loc))
                per_proxy, _ = row_stats(p, loc)
                per = []
                for b in range(n + 1):
                    assert (A[b] - A[b].conj()).is_zero(), "A_b must be real"
                    av = abs(complex(A[b].tocomplex()))
                    ev = abs(complex(E[b].tocomplex()))
                    per.append({"b": b, "neglog2_true":
                                (math.log2(ev / av) if av > 0 else None),
                                "neglog2_proxy":
                                neglog2(per_proxy[b]["V"], per_proxy[b]["C"])})
                tot_A = abs(complex(sum(x.tocomplex() for x in A)))
                tot_E = sum(abs(complex(x.tocomplex())) for x in E)
                rows.append({"p": p, "c": list(c), "n": n, "per_b": per,
                             "full_neglog2": math.log2(tot_E / tot_A)})
                for b in (n // 4, n // 2, 3 * n // 4):
                    e = per[b]
                    if e["neglog2_true"] is None:
                        continue
                    pr = e["neglog2_proxy"]
                    print(f"{p:4d} {str(tuple(c)):>7} {n:3d} {b:3d} "
                          f"{e['neglog2_true']:15.4f} "
                          f"{(pr if pr is not None else float('nan')):16.4f} "
                          f"{e['neglog2_true']/n:12.4f}")
    with open(os.path.join(RESULTS, "slice_cancellation_weighted.json"),
              "w") as f:
        json.dump({"rows": rows,
                   "note": "true ratios are 60-digit renderings of exactly "
                           "computed Z[zeta_p] elements"}, f)


if __name__ == "__main__":
    os.makedirs(RESULTS, exist_ok=True)
    st = sys.argv[1] if len(sys.argv) > 1 else "count"
    {"count": stage_count, "scale": stage_scale, "weight": stage_weight}[st]()
