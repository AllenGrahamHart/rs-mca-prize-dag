#!/usr/bin/env python3
"""Structure of the Delta value set (which residues occur, with what mult)."""
from __future__ import annotations
import sys, os, collections
sys.dont_write_bytecode = True
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "f2_slice_coefficients"))
from slicecore import (Fp2, pair_reps, residues, admissible_orders, Delta_of,
                       sigma_of)

for p in (11, 13, 23):
    F = Fp2.make(p)
    mu = admissible_orders(p)[-1]
    reps = pair_reps(F, F.subgroup(mu))
    for c in ((1, 1), (2, 3)):
        loc = [residues(F, c, y) for y in reps]
        D = Delta_of(p, loc)
        ctr = collections.Counter(D)
        print(f"p={p} c={c} 2p={2*p} values(mult): "
              + " ".join(f"{v}:{ctr[v]}" for v in sorted(ctr)))
        sig = sigma_of(p, loc)
        bases = collections.Counter(s[1] for s in sig)
        print(f"   sigma^- values: {sorted(bases)}")
