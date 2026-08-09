#!/usr/bin/env python3
"""D2 ARM B -- THE VERTEX-VS-HULL TEST at OUR M31 route-cut fixture.

Registered at notes/pilots_20260809/m7_complement_repose/PREREG.md R2/R3
(prediction P5, kill criterion E3).

background/nodes/l1_m31_fixed_support_divisor_direction_cap_route_cut
statement.md:19-35 exhibits, inside the SIX-dimensional

    V = span_F {R X, R, 1, X, X^2, X^3}                       (RC1)

the family

    J_a = R (X - a),   a in S \\ R0,      m - t + 1 = 67449     (RC2)/(RC3)

of monic degree-t divisors of L_S.  Those are VERTICES.  The round-25a
calibration compares the complement-coordinate anticode value
`m - (t-1)` against 67449 and calls the instrument EXACT (looseness 2^0).
That comparison is only valid if 67449 is the TRUE number of split
members of V, not merely the number the node exhibits.  The general
monic degree-t member of V is

    F = R (X + beta) + c(X),     deg c <= 3,

a q^5 family; the exhibited ones are exactly c = 0.  This script
enumerates ALL of them that split on S, in a scaled analogue of the same
shape, by last-coordinate bucketing on c_0 (the same trick as
rh_bucket.enumerate_split), and reports

    M31_NSPLIT  = number of distinct root sets of split members
    M31_EXTRA   = M31_NSPLIT - (m - t + 1)

Scale condition preserved: m >= 2t-4, so that a c != 0 member (which
meets R0 in at most deg c <= 3 points) is NOT excluded by counting
alone -- the test has resolution.

Stdlib only.  Run via tools/ramguard local -- python3 ... from repo root.
"""
from __future__ import annotations

import json
import random
import sys
import time
from itertools import product


def main():
    q = int(sys.argv[1])
    m = int(sys.argv[2])
    t = int(sys.argv[3])
    ndraw = int(sys.argv[4])
    seed = int(sys.argv[5])
    outfile = sys.argv[6] if len(sys.argv) > 6 else ""

    assert m >= 2 * t - 4, "scale condition m >= 2t-4 violated"
    assert t >= 5, "need deg R = t-1 >= 4 so that deg c <= 3 is a genuine " \
                   "low-degree perturbation"
    rng = random.Random(seed)
    recs = []
    t0 = time.time()
    for dr in range(ndraw):
        S = rng.sample(range(1, q), m)
        R0 = S[:t - 1]
        rest = sorted(set(S) - set(R0))          # |rest| = m - t + 1
        # R(x) for x in S, evaluated directly from its roots
        Rv = {}
        for x in S:
            v = 1
            for r in R0:
                v = v * (x - r) % q
            Rv[x] = v
        found = {}
        for beta, c1, c2, c3 in product(range(q), repeat=4):
            g = {}
            for x in S:
                val = (Rv[x] * (x + beta) + c3 * x * x % q * x
                       + c2 * x * x + c1 * x) % q
                g.setdefault((-val) % q, []).append(x)
            for c0, xs in g.items():
                if len(xs) == t:
                    found.setdefault(frozenset(xs), (beta, c1, c2, c3, c0))
        S_sets = [set(z) for z in found]
        exhibited = {frozenset(set(R0) | {a}) for a in rest}
        extra = [z for z in found if z not in exhibited]
        missing = [z for z in exhibited if z not in found]
        ovl = []
        for i in range(len(S_sets)):
            for k in range(i + 1, len(S_sets)):
                ovl.append(len(S_sets[i] & S_sets[k]))
        h = {}
        for v in ovl:
            h[v] = h.get(v, 0) + 1
        recs.append({
            "draw": dr, "q": q, "m": m, "t": t,
            "exhibited_m_minus_t_plus_1": m - t + 1,
            "M31_NSPLIT": len(found),
            "M31_EXTRA": len(found) - (m - t + 1),
            "n_extra_members": len(extra),
            "n_exhibited_missing": len(missing),
            "extra_examples": [sorted(z) for z in extra[:3]],
            "extra_coeffs": [found[z] for z in extra[:3]],
            "OVL_HIST": {str(k): v for k, v in sorted(h.items())},
            "all_c_zero": all(found[z][1:] == (0, 0, 0) for z in found),
        })
    summary = {
        "mode": "d2_arm_b_m31_hull", "q": q, "m": m, "t": t,
        "scale_condition_m_ge_2t_minus_4": m >= 2 * t - 4,
        "draws": len(recs), "seed": seed,
        "M31_EXTRA_values": [r["M31_EXTRA"] for r in recs],
        "draws_with_EXTRA_gt_0": sum(1 for r in recs if r["M31_EXTRA"] > 0),
        "draws_with_MISSING_gt_0":
            sum(1 for r in recs if r["n_exhibited_missing"] > 0),
        "OVL_HIST_MERGED": {},
        "elapsed_s": round(time.time() - t0, 1),
    }
    for r in recs:
        for k, v in r["OVL_HIST"].items():
            summary["OVL_HIST_MERGED"][k] = \
                summary["OVL_HIST_MERGED"].get(k, 0) + v
    summary["OVL_HIST_MERGED"] = dict(sorted(
        summary["OVL_HIST_MERGED"].items(), key=lambda x: int(x[0])))
    if outfile:
        with open(outfile, "w") as fh:
            json.dump({"summary": summary, "recs": recs}, fh, indent=1)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
