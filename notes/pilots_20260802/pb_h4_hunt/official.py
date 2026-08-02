#!/usr/bin/env python3
"""Official-row arithmetic for the (H4) hunt: design ceilings, the
spread-block feasibility margin, and the split-fibre selection parameter.

Row constants are the banked ones replayed by the pb_gamma_exposure pilot.
Run:  tools/ramguard tiny -- python3 official.py
"""
from __future__ import annotations

import json
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))

ROWS = [
    dict(row="RowC 1/4", n=2 ** 10, K=2 ** 8, A=261, h=5),
    dict(row="RowC 1/8", n=2 ** 10, K=2 ** 7, A=133, h=5),
    dict(row="RowC 1/16", n=2 ** 10, K=2 ** 6, A=67, h=3),
    dict(row="prize 1/4", n=2 ** 41, K=2 ** 39, A=558345748481, h=2 ** 33 + 1),
    dict(row="prize 1/8", n=2 ** 41, K=2 ** 38, A=283467841537, h=2 ** 33 + 1),
    dict(row="prize 1/16", n=2 ** 41, K=2 ** 37, A=141733920769, h=2 ** 32 + 1),
]


def lg_binom(n, k):
    if k <= 0 or k >= n:
        return 0.0
    return (math.lgamma(n + 1) - math.lgamma(k + 1)
            - math.lgamma(n - k + 1)) / math.log(2)


def main():
    out = []
    for R in ROWS:
        n, K, A, h = R["n"], R["K"], R["A"], R["h"]
        r = n - K
        c_fix = (2 * r - 1) // h
        c_free = (2 * r - 1) // (h - 1)
        budget = 8 * n ** 3
        lgC = lg_binom(n, A)
        # q floors: L1 soundness q^h >= C*2^128 ; envelope pin
        lgq_L1 = (lgC + 128) / h
        lgq_pin = 250.0 if n == 2 ** 10 else 255.9
        # spread-block feasibility: blocks of size m >= h+1, need b ~ n/m
        # disjoint blocks with collinear moment vectors.  Expected number of
        # m-subsets on a fixed line = C(n,m)/q^{h-1}; need >= b.
        blk = []
        for m in sorted({h + 1, 2 * (h + 1), max(h + 1, A // 4),
                         max(h + 1, A // 2), A // 1 if A > h else h + 1}):
            if m < h + 1 or m > A:
                continue
            b = n // m
            a = A // m
            if b < a + 1 or a < 2:
                fam = 0
            else:
                fam = lg_binom(b, a)
            for tag, lgq in (("L1", lgq_L1), ("pin", lgq_pin)):
                margin = lg_binom(n, m) - (h - 1) * lgq - math.log2(max(b, 2))
                blk.append(dict(m=m, b=b, a=a, lg_family=fam, q=tag,
                                lg_feasibility_margin=margin,
                                feasible=margin >= 0))
        # split-fibre selection parameter nu at the widest split shape
        # (F,a,g) = (n/m, (A-g)/m, 1) with m the row's unique fibre width
        m_sf = None
        mm = 1
        while mm <= n:                       # n is a power of two on all rows
            if mm <= h < 2 * mm and (A - 1) % mm == 0:
                m_sf = mm
            mm *= 2
        nu = None
        if m_sf:
            F = n // m_sf
            a_sf = (A - 1) // m_sf
            lgCsf = lg_binom(F - 1, a_sf)
            nu = dict(m=m_sf, F=F, a=a_sf, lg_family=lgCsf,
                      lg_nu_at_L1=math.log2(a_sf * (F - 1 - a_sf))
                      + lgq_L1 - lgCsf,
                      lg_nu_at_pin=math.log2(a_sf * (F - 1 - a_sf))
                      + lgq_pin - lgCsf)
        out.append(dict(row=R["row"], n=n, K=K, A=A, h=h, r=r,
                        design_ceiling_slopes_fixed=c_fix,
                        design_ceiling_slopes_free=c_free,
                        budget_8n3=budget,
                        lg_budget=math.log2(budget),
                        lg_ceiling=math.log2(c_free),
                        ceiling_below_budget_bits=math.log2(budget)
                        - math.log2(c_free),
                        lg_C_nA=lgC, lg_q_L1=lgq_L1, lg_q_pin=lgq_pin,
                        spread_blocks=blk, split_fibre=nu))
        print(f"{R['row']:<11s} r={r:<14d} ceiling(slopes free)="
              f"{c_free:<5d} 8n^3=2^{math.log2(budget):.1f} "
              f"ceiling is 2^{math.log2(budget)-math.log2(c_free):.1f} below budget")
        for bl in blk[:4]:
            print(f"    spread-block m={bl['m']:<12d} b={bl['b']:<10d} "
                  f"a={bl['a']:<8d} lg|family|={bl['lg_family']:9.1f} "
                  f"q={bl['q']:<4s} feasibility margin "
                  f"{bl['lg_feasibility_margin']:+12.1f} bits "
                  f"{'FEASIBLE' if bl['feasible'] else 'infeasible'}")
        if nu:
            print(f"    split-fibre m={nu['m']} F={nu['F']} a={nu['a']} "
                  f"lg|family|={nu['lg_family']:.1f}; lg nu (selected "
                  f"neighbours per member) = {nu['lg_nu_at_L1']:+.2f} at the "
                  f"L1 floor, {nu['lg_nu_at_pin']:+.2f} at the envelope pin")
    p = os.path.join(HERE, "OFFICIAL.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(f"-> {p}")


if __name__ == "__main__":
    main()
