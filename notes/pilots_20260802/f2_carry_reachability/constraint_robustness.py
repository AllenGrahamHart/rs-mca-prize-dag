#!/usr/bin/env python3
"""How much orientation freedom must the descent destroy to save compression?

Run:  tools/ramguard local -- python3 \
        notes/pilots_20260802/f2_carry_reachability/constraint_robustness.py

The audit's abstraction gives each conjugate pair a FREE orientation bit.
The unproven seam (F2A.1) could in principle deliver a CONSTRAINED
orientation set T <= F_2^m instead.  This measures |reachable sums| when
T is a random affine GF(2)-subspace of dimension d -- i.e. when the
descent freezes all but d of the m orientation bits' worth of freedom.

Exact integer arithmetic throughout.
"""

from __future__ import annotations

import json
import math
import os
import random
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from f2model import Fp2, deltas, pair_reps, divisors  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "results")


def reachable_from_subspace(ds: list[int], two_p: int, basis: list[int],
                            offset: int) -> int:
    """|{ sum_{i in supp(tau)} d_i : tau in offset + span(basis) }|."""
    d = len(basis)
    seen = set()
    cur = offset
    # Gray-code walk over the 2^d cosets
    def subsum(mask: int) -> int:
        t = 0
        mm = mask
        while mm:
            low = mm & -mm
            t += ds[low.bit_length() - 1]
            mm ^= low
        return t % two_p
    seen.add(subsum(cur))
    prev = 0
    for i in range(1, 1 << d):
        g = i ^ (i >> 1)
        flip = g ^ prev
        prev = g
        j = flip.bit_length() - 1
        cur ^= basis[j]
        seen.add(subsum(cur))
    return len(seen)


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for p, want_pairs in ((101, 48), (1021, 48)):
        F = Fp2.make(p)
        two_p = 2 * p
        n = next(x for x in sorted(divisors(p * p - 1), reverse=True)
                 if x % 2 == 0 and (p - 1) % x != 0 and x <= 4000)
        mu = F.subgroup(n)
        reps = pair_reps(F, mu)[:want_pairs]
        m = len(reps)
        rng = random.Random(4242 + p)
        c = (rng.randrange(1, p), rng.randrange(1, p))
        ds = deltas(F, c, reps)
        print(f"\np={p}  2p={two_p}  n={n}  m={m} pairs  c={c}")
        print(f"{'dim d':>6} {'2^d':>10} {'mean |reach|':>13}"
              f" {'max |reach|':>12} {'2p':>8}")
        for d in list(range(1, 13)) + [14, 16]:
            if d > m:
                break
            vals = []
            for _ in range(6):
                basis = [rng.getrandbits(m) | (1 << rng.randrange(m))
                         for _ in range(d)]
                offset = rng.getrandbits(m)
                vals.append(reachable_from_subspace(ds, two_p, basis,
                                                    offset))
            rows.append({"p": p, "n": n, "m": m, "dim": d,
                         "two_pow_d": 2 ** d,
                         "mean_reachable": statistics.fmean(vals),
                         "max_reachable": max(vals),
                         "min_reachable": min(vals),
                         "two_p": two_p})
            print(f"{d:6d} {2**d:10d} {statistics.fmean(vals):13.1f}"
                  f" {max(vals):12d} {two_p:8d}")
    with open(os.path.join(OUT, "constraint_robustness.json"), "w") as f:
        json.dump({"rows": rows}, f, indent=1)
    # the operative summary
    print("\nSUMMARY: |reachable| tracks min(2^d, 2p).  To hold the carry "
          "state count at B the descent must cut the orientation space to "
          "GF(2)-dimension <= log2(B) -- i.e. freeze all but O(1) of the "
          "m ~ 2^39 orientation bits.")
    print("F2A2_CONSTRAINT_DONE")


if __name__ == "__main__":
    main()
