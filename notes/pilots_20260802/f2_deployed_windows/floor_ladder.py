#!/usr/bin/env python3
"""The 1/p ceiling ladder: worst central-band -log2 rho_b vs m, EXACT integers.

Deployed (K1) rung-1 windows at official-shaped primes.  The point is that the
cancellation exponent SATURATES at log2 p and does not grow with m, so the
budget's linear term m/43 can never be earned.
"""
from __future__ import annotations
import json, math, os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deployed as DP, tower as TW           # noqa: E402
from slicecore import Fp2, pair_reps, residues, sigma_of, Delta_of  # noqa: E402
from verify import DP_V                      # noqa: E402

rows = []
for e in (4, 5, 6, 7, 8):
    p = TW.official_shaped_prime(e)
    n1 = 1 << (e + 1)
    F = Fp2.make(p)
    reps = pair_reps(F, F.subgroup(n1))
    m = len(reps)
    if m > 140:
        continue
    for c in ((1, 1), (2, 3)):
        loc = [residues(F, c, y) for y in reps]
        D = Delta_of(p, loc)
        base = sum(s[1] for s in sigma_of(p, loc)) % (2 * p)
        V = DP_V(p, D, base)
        lo, hi = math.ceil(0.25 * m), math.floor(0.75 * m)
        vals = [(math.log2(math.comb(m, b)) - math.log2(abs(V[b])), b)
                for b in range(lo, hi + 1) if V[b] != 0]
        worst = min(vals)
        med = sorted(v for v, _ in vals)[len(vals) // 2]
        rows.append({"p": p, "e": e, "m": m, "c": list(c),
                     "worst_band_neglog2_rho": worst[0], "worst_b": worst[1],
                     "median_band_neglog2_rho": med,
                     "log2_p": math.log2(p),
                     "gap_to_log2p": math.log2(p) - worst[0],
                     "eta": worst[0] / m,
                     "budget_43_bits": m / 43.0})
        print(f"p={p:5d} m={m:4d} c={c}  worst-band -log2 rho = {worst[0]:8.4f} "
              f"(b={worst[1]})  median = {med:8.4f}  log2 p = {math.log2(p):7.4f}  "
              f"gap = {math.log2(p)-worst[0]:+.4f}  eta = {worst[0]/m:.5f}  "
              f"1/43 budget = {m/43.0:.3f} bits")
DP.dump("E8_floor_ladder.json", {"rows": rows})
