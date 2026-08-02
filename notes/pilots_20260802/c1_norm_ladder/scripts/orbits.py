#!/usr/bin/env python3
"""Exact orbit counts n_w of ternary weight-w vectors under U and under G.

U = {+- x^i}  (order 2N)  -- the prior pilot's orbit notion (weight profile / 2N).
G = <U, Galois x -> x^u>  (order 2N * phi(2N)) -- the full norm-preserving group.
Counts by Burnside; the U-counts are cross-checked against the free-action formula
C(N,w) 2^w / (2N).
"""

from __future__ import annotations

import argparse
import json
from math import comb

from norm_core import burnside_orbit_counts, group_G, group_U


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--Ns", default="4,8,16,32")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = {}
    for N in [int(x) for x in args.Ns.split(",")]:
        U = group_U(N)
        G = group_G(N)
        nU = burnside_orbit_counts(U, N)
        nG = burnside_orbit_counts(G, N)
        rows = []
        for w in range(1, N + 1):
            tot = comb(N, w) * (1 << w)
            assert tot % (2 * N) == 0
            assert nU[w] == tot // (2 * N), (N, w, nU[w], tot // (2 * N))
            rows.append({"w": w, "n_ternary_f": tot,
                         "n_orbits_U": nU[w], "n_orbits_G": nG[w]})
        out[str(2 * N)] = {"twoN": 2 * N, "N": N, "|U|": len(U), "|G|": len(G),
                           "rows": rows,
                           "total_orbits_U": sum(r["n_orbits_U"] for r in rows),
                           "total_orbits_G": sum(r["n_orbits_G"] for r in rows)}
        print("2N=%d |U|=%d |G|=%d" % (2 * N, len(U), len(G)))
        for r in rows:
            print("   w=%2d  #f=%-12d n_w^U=%-10d n_w^G=%d"
                  % (r["w"], r["n_ternary_f"], r["n_orbits_U"], r["n_orbits_G"]))
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)


if __name__ == "__main__":
    main()
