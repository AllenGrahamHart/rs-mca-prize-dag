#!/usr/bin/env python3
"""Quick reconnaissance: the Delta multiset distribution over the pair set."""
from __future__ import annotations
import sys, os, collections, math
sys.dont_write_bytecode = True
_HERE = os.path.dirname(os.path.abspath(__file__))
_SLICE = os.path.join(os.path.dirname(_HERE), "f2_slice_coefficients")
sys.path.insert(0, _SLICE)
from slicecore import (Fp2, pair_reps, residues, admissible_orders, Delta_of)

for p in (23, 41, 67, 101, 127, 151):
    F = Fp2.make(p)
    orders = admissible_orders(p)
    mu = orders[-1]
    reps = pair_reps(F, F.subgroup(mu))
    for c in ((1, 1), (2, 3)):
        loc = [residues(F, c, y) for y in reps]
        D = Delta_of(p, loc)
        ctr = collections.Counter(D)
        mult = sorted(ctr.values(), reverse=True)
        nodd = sum(1 for x in D if x % 2)
        # best arc of width w: max count in a window of w consecutive residues
        arcbest = {}
        for w in (1, 2, 3, 5, 9):
            best = 0
            for a in range(2 * p):
                best = max(best, sum(ctr.get((a + t) % (2 * p), 0) for t in range(w)))
            arcbest[w] = best
        print(f"p={p:4d} mu={mu:6d} m={len(reps):5d} c={c} distinct_Delta={len(ctr):4d} "
              f"odd={nodd}/{len(D)} maxmult={mult[0]:4d} top5={mult[:5]} "
              f"arc={arcbest}")
