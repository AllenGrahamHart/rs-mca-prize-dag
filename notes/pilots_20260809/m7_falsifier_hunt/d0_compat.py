#!/usr/bin/env python3
"""ESCAPE TEST 2b (PREREG P10, second half): my generalised M>=5 chart
code, specialised to (M=4, t=2, u=b=ell-3, arm-A pool and arm-A sampling
order), must reproduce round-25 d2_arm_a.py CONFIG BY CONFIG.

Compares NSPLIT (full contributor filters) and the full pairwise overlap
histogram against the banked/replayed d2_arm_a record list.

Stdlib only.  Run via tools/ramguard local -- python3 from repo root.
"""
from __future__ import annotations

import json
import random
import sys

ROOT = "/home/u2470931/smooth-read-solomin/prize"
sys.path.insert(0, ROOT + "/notes/pilots_20260807/fpc5_diag")
sys.path.insert(0, ROOT + "/notes/pilots_20260807/mf_wall_adversary")
sys.path.insert(0, ROOT + "/notes/pilots_20260809/m7_falsifier_hunt")
from rh_m4t2_census import (pgcd, pdegree, pmul, prem, peval)   # noqa: E402
from rh_bucket import rref_kernel, monic_chart, enumerate_split  # noqa: E402
from d2_hunt import build_flat_general, hist                     # noqa: E402


def main():
    ell, q, nconfig, seed = 4, 97, 32, 20260809
    ref = json.load(open(ROOT + "/notes/pilots_20260809/m7_falsifier_hunt/"
                         "replay_ell4_q97_full.json"))["recs"]
    d = 2 * ell - 3
    b = ell - 3
    rng = random.Random(seed)
    mine = []
    for ci in range(nconfig):
        pts = rng.sample(range(1, q), b + 4 * ell)
        bg = pts[:b]
        petals = [pts[b + i * ell:b + (i + 1) * ell] for i in range(4)]
        allowed = sorted(set(range(1, q)) - set(pts))
        labels = rng.sample(range(1, q), 4)
        T, P, G, rows = build_flat_general(bg, petals, labels, (0, 1), q, d)
        if rows != ell - 1:
            continue
        basis = rref_kernel(T, d + 1, q)
        if len(basis) != ell - 1:
            continue
        v0, dirs = monic_chart(basis, d, q)
        if v0 is None:
            continue
        g = v0[:]
        for dv in dirs:
            g = pgcd(g, dv, q)
        if max(pdegree(g), 0) > 0:
            continue
        found, swept = enumerate_split(v0, dirs, allowed, d, q)
        keep = []
        for rs, coefs in found.items():
            F = v0[:]
            for i, c in enumerate(coefs):
                if c:
                    F = [(x + c * y) % q for x, y in zip(F, dirs[i])]
            W = prem(pmul(F, G, q), P, q)
            if any(peval(W, x, q) == 0 for x in rs):
                continue
            bad = False
            for iu in (2, 3):
                cu = labels[iu]
                for x in petals[iu]:
                    if (peval(W, x, q) - cu * peval(F, x, q)) % q == 0:
                        bad = True
                        break
                if bad:
                    break
            if bad:
                continue
            keep.append(set(rs))
        if len(keep) < 2:
            continue
        ov = [len(keep[i] & keep[j]) for i in range(len(keep))
              for j in range(i + 1, len(keep))]
        mine.append({"NSPLIT": len(keep), "swept": swept,
                     "OVL_HIST_ALL": {str(k): v
                                      for k, v in sorted(hist(ov).items())}})
    ok_n = all(a["NSPLIT"] == b2["NSPLIT"] for a, b2 in zip(mine, ref))
    ok_h = all(a["OVL_HIST_ALL"] == b2["OVL_HIST_ALL"]
               for a, b2 in zip(mine, ref))
    ok_s = all(a["swept"] == b2["chart_points_swept"]
               for a, b2 in zip(mine, ref))
    print(json.dumps({
        "configs_mine": len(mine), "configs_ref": len(ref),
        "NSPLIT_match_all": ok_n and len(mine) == len(ref),
        "OVL_HIST_match_all": ok_h and len(mine) == len(ref),
        "chart_points_swept_match_all": ok_s and len(mine) == len(ref),
        "first_mismatch": next(
            ({"i": i, "mine": a, "ref": {"NSPLIT": b2["NSPLIT"],
                                         "OVL": b2["OVL_HIST_ALL"]}}
             for i, (a, b2) in enumerate(zip(mine, ref))
             if a["NSPLIT"] != b2["NSPLIT"]
             or a["OVL_HIST_ALL"] != b2["OVL_HIST_ALL"]), None),
        "NSPLIT_mine_first8": [r["NSPLIT"] for r in mine[:8]],
        "NSPLIT_ref_first8": [r["NSPLIT"] for r in ref[:8]],
    }, indent=1))


if __name__ == "__main__":
    main()
