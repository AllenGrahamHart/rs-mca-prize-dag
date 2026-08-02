#!/usr/bin/env python3
"""Calibrate the Aff(N) support-orbit reduction against known exhaustive tables.

1. brute force over ALL 3^N ternary f at N = 4, 8 -> per-weight maxima;
2. reduced scan at N = 4, 8, 16 -> must agree, weight by weight, with (1) and
   with the prior pilot's published tables (results/ladder.json).
"""

from __future__ import annotations

import json
import os
import sys
from itertools import product as iproduct

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, "/home/u2470931/smooth-read-solomin/prize/notes/"
                   "pilots_20260802/c1_norm_ladder/scripts")

from norm_core import norm_batch_int64, norm_bareiss  # noqa: E402
from scan import scan                                  # noqa: E402

PUBLISHED = {
    4: [None, 1, 4, 9, 8],
    8: [None, 1, 16, 81, 196, 529, 1154, 2401, 2176],
    16: [None, 1, 256, 6561, 38416, 279841, 1331716, 5764801, 14760962,
         38950081, 84580802, 184497889, 342386306, 777684769, 1040410946,
         1612931233, 2311094272],
    32: {1: 1, 2: 65536, 3: 43046721, 4: 1475789056, 5: 78310985281,
         6: 1773467504656, 7: 33232930569601},
}


def brute(N: int) -> dict[int, int]:
    rows = np.array(list(iproduct((-1, 0, 1), repeat=N)), dtype=np.int8)
    wts = (rows != 0).sum(axis=1)
    vals = norm_batch_int64(rows)
    out = {}
    for w in range(1, N + 1):
        m = wts == w
        out[w] = int(vals[m].max())
    return out


def main() -> None:
    outdir = os.path.join(os.path.dirname(HERE), "results", "calib")
    os.makedirs(outdir, exist_ok=True)
    rep = {"brute_force": {}, "reduced": {}, "agreement": {}}
    for N in (4, 8):
        rep["brute_force"][str(N)] = {str(w): str(v) for w, v in brute(N).items()}
    for N in (4, 8, 16):
        row = {}
        for w in range(1, N + 1):
            r = scan(N, w, 0, 1, outdir)
            row[str(w)] = {"max": r["max_norm"],
                           "orbits": r["n_support_orbits_total"],
                           "scanned": r["n_polynomials_scanned"],
                           "argmax": r["argmax_f"]}
        rep["reduced"][str(N)] = row
    ok = True
    for N in (4, 8, 16):
        for w in range(1, N + 1):
            got = int(rep["reduced"][str(N)][str(w)]["max"])
            want = PUBLISHED[N][w]
            same_pub = got == want
            same_bf = True
            if N in (4, 8):
                same_bf = got == int(rep["brute_force"][str(N)][str(w)])
            rep["agreement"]["N%d_w%d" % (N, w)] = {
                "reduced": str(got), "published": str(want),
                "matches_published": same_pub, "matches_bruteforce": same_bf}
            ok = ok and same_pub and same_bf
    rep["ALL_AGREE"] = ok
    # reduction factor table
    rep["reduction_factor"] = {}
    from math import comb
    for N in (16, 32, 64):
        for w in range(2, 13):
            if w > N:
                continue
            naive = comb(N, w) * 2 ** w
            try:
                orbits = int(np.load(os.path.join(outdir, "reps_N%02d_w%02d.npy" % (N, w))).size)
            except Exception:
                continue
            rep["reduction_factor"]["N%d_w%d" % (N, w)] = {
                "naive": naive, "reduced": orbits * 2 ** (w - 1),
                "factor": round(naive / (orbits * 2 ** (w - 1)), 2)}
    with open(os.path.join(os.path.dirname(HERE), "results", "calib.json"), "w") as fh:
        json.dump(rep, fh, indent=1)
    print(json.dumps({"ALL_AGREE": ok,
                      "agreement": rep["agreement"]}, indent=1)[:4000])


if __name__ == "__main__":
    main()
