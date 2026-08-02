#!/usr/bin/env python3
"""Recon: what does a DEPLOYED window actually look like?  Exact.

Stage 1 -- the full-group instance the prior pilots used (n_ord = p^2-1):
confirm m = p(p-1)/2, the multiplicity law, and the exact defect D.
Stage 2 -- every OTHER admissible order n_ord | p^2-1: same quantities.
"""
from __future__ import annotations
import collections, os, sys
from fractions import Fraction
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deployed as DP  # noqa: E402

print("=== stage 1: the FULL group (what the banked pilots instantiated) ===")
for p in (7, 11, 13, 19, 23, 31, 41):
    n_ord = p * p - 1
    for c in ((1, 1), (2, 3)):
        D, base, m, reps, loc = DP.deployed_window(p, n_ord, c)
        ctr = collections.Counter(D)
        mults = sorted(ctr.values())
        law = mults == list(range(1, p))
        cd, xd = DP.parity_classes(p, D)
        nz = sorted(abs(v) for v in cd if v)
        dfc = DP.defect(p, D)
        fb = DP.flat_bound(p, D)
        fl, ka, mx = DP.measured_flat(p, D)
        bm = DP.beta_min(D)
        print(f"p={p:3d} c={c} m={m:5d} (p(p-1)/2={p*(p-1)//2}) "
              f"#vals={len(ctr):3d} multlaw={law} "
              f"|c_d| nonzero={nz if p <= 13 else str(nz[:6])+'...'} "
              f"D={dfc} D/m={float(Fraction(dfc,m)):.6f} "
              f"flat>={float(fb):.6f} flat_meas={fl:.6f}@k={ka} "
              f"beta_min={float(bm):.4f}")

print()
print("=== stage 2: EVERY admissible subgroup order ===")
for p in (11, 13, 19, 23, 31):
    orders = DP.deployed_orders(p)
    print(f"--- p={p}: p^2-1={p*p-1}, {len(orders)} admissible orders: {orders}")
    for n_ord in orders:
        row = []
        for c in ((1, 1), (2, 3)):
            D, base, m, reps, loc = DP.deployed_window(p, n_ord, c)
            if m == 0:
                row.append("m=0")
                continue
            ctr = collections.Counter(D)
            dfc = DP.defect(p, D)
            fb = DP.flat_bound(p, D)
            fl, ka, mx = DP.measured_flat(p, D)
            bm = DP.beta_min(D)
            row.append(f"c={c} m={m:4d} #v={len(ctr):3d} D={dfc:4d} "
                       f"flat>={float(fb):+.4f} meas={fl:.4f}@{ka} bmin={float(bm):.4f}")
        print(f"   n_ord={n_ord:6d} | " + " | ".join(row))
