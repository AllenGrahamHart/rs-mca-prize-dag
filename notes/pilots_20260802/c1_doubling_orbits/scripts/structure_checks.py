#!/usr/bin/env python3
"""Structural checks and the K4 owner metric for the order-2N C1 sweep.

Checks
  (S1) X is independent of the choice of primitive 2N-th root omega (exact).
  (S2) every kernel weight count N_w is divisible by 2N -- the negacyclic
       symmetry d_i -> d_{i-1} (with wraparound sign flip) acts freely, so the
       kernel is a union of size-2N orbits and the relation mass quantises:
           relmass = sum_w (N_w / 2N) * 2N * 2^-w = sum over ORBITS of 2N*2^-w.
       At 2N=32 one weight-w orbit contributes exactly 2^(5-w).
  (S3) X >= (q-1)/(q 2^N) with equality iff A == 1 (AM-GM on each doubling
       cycle: prod_{C in cycle} A(C) = 1 so the mean is >= 1).
  (K4) "unowned excess at cut W" = sum_{w>W} e_w -- how much of the excess is
       carried by relations of weight > W (i.e. has no bounded short owner).
"""

from __future__ import annotations

import argparse
import glob
import json
import math
from fractions import Fraction

import numpy as np

import orbit_spectrum as osp


def omega_independence(qs: list[int], twoN: int) -> list[dict]:
    out = []
    for q in qs:
        N = twoN // 2
        base = osp.root_of_order(q, twoN)
        vals = set()
        profs = set()
        for k in range(1, twoN, 2):
            if math.gcd(k, twoN) != 1:
                continue
            w = pow(base, k, q)
            coeffs = [pow(w, i, q) for i in range(N)]
            vals.add(osp.subset_sum_SS(coeffs, q))
            profs.add(tuple(int(x) for x in osp.kernel_weight_profile(coeffs, q)))
        out.append({"q": q, "n_roots_tested": len(list(range(1, twoN, 2))),
                    "distinct_SS": len(vals), "distinct_profiles": len(profs),
                    "invariant": len(vals) == 1 and len(profs) == 1})
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--glob", nargs="+", required=True)
    ap.add_argument("--twoN", type=int, default=32)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    twoN = args.twoN
    N = twoN // 2
    C = [math.comb(N, w) for w in range(N + 1)]

    rows = []
    for pat in args.glob:
        for f in sorted(glob.glob(pat)):
            rows += json.load(open(f))["rows"]
    rows.sort(key=lambda r: r["q"])

    # (S2) divisibility of N_w by 2N
    bad = [(r["q"], w, r["weight_profile"][w]) for r in rows
           for w in range(1, N + 1) if r["weight_profile"][w] % twoN]
    # (S3) AM-GM floor
    floor_ok = all(Fraction(r["X_num"], r["X_den"]) >=
                   Fraction(r["X_flat_num"], r["X_flat_den"]) for r in rows)
    eq = [r["q"] for r in rows if r["is_exactly_flat"]]

    # (K4) unowned excess -- computed on all rows and on the hard regime q > 2^N
    hard = [r for r in rows if r["hard_regime"]]

    def k4_block(pop):
        k4 = {}
        for W in (4, 5, 6, 7, 8, 9, 10):
            vals = []
            for r in pop:
                e = sum((Fraction(r["weight_profile"][w], 1 << w) - Fraction(C[w], r["q"]))
                        for w in range(W + 1, N + 1))
                vals.append((float(e), r["q"]))
            vals.sort()
            k4[f"W={W}"] = {
                "max_unowned_excess": vals[-1][0], "argmax_q": vals[-1][1],
                "mean_unowned_excess": sum(v for v, _ in vals) / len(vals),
                "p999": vals[int(0.999 * (len(vals) - 1))][0],
                "n_rows_unowned_gt_1": sum(1 for v, _ in vals if v > 1.0),
                "n_rows_unowned_gt_0.5": sum(1 for v, _ in vals if v > 0.5),
            }
        return k4

    k4 = {"all_rows": k4_block(rows), "hard_regime": k4_block(hard)}

    def orbit_block(pop):
        max_orbits = {}
        for w in range(1, N + 1):
            best = max(pop, key=lambda r: r["weight_profile"][w])
            max_orbits[w] = {"max_orbits": best["weight_profile"][w] // twoN,
                             "argmax_q": best["q"],
                             "mean_orbits": sum(r["weight_profile"][w] // twoN
                                                for r in pop) / len(pop)}
        return max_orbits

    orbit_hist = {"all_rows": orbit_block(rows), "hard_regime": orbit_block(hard)}
    max_orbits = orbit_hist

    # what would it take to break X <= 4 : needed orbit mass
    xs = sorted(rows, key=lambda r: -(r["X_num"] / r["X_den"]))
    out = {
        "twoN": twoN, "n_rows": len(rows),
        "S2_all_N_w_divisible_by_2N": len(bad) == 0,
        "S2_violations": bad[:20],
        "S3_X_ge_AMGM_floor_all": floor_ok,
        "S3_equality_rows": eq,
        "S1_omega_independence": omega_independence(
            [rows[0]["q"], rows[len(rows) // 4]["q"], rows[len(rows) // 2]["q"],
             max(rows, key=lambda r: r["X_num"] / r["X_den"])["q"], rows[-1]["q"]],
            twoN),
        "K4_unowned_excess": k4,
        "orbit_counts_by_weight": orbit_hist,
        "max_orbits_by_weight_dup": None,
        "top_rows_orbit_decomposition": [
            {"q": r["q"], "X": float(Fraction(r["X_num"], r["X_den"])),
             "minw": r["min_relation_weight"], "r": r["r"], "n_cycles": r["n_cycles"],
             "orbits": {w: r["weight_profile"][w] // twoN
                        for w in range(1, N + 1) if r["weight_profile"][w]},
             "orbit_mass": float(sum(Fraction(r["weight_profile"][w], 1 << w)
                                     for w in range(1, N + 1))),
             "haar_mass": (2 ** N - 1) / r["q"]}
            for r in xs[:15]],
    }
    with open(args.out, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ("orbit_counts_by_weight","max_orbits_by_weight_dup")}, indent=1)[:9000])


if __name__ == "__main__":
    main()
