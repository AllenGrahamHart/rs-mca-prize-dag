#!/usr/bin/env python3
"""D6 -- RED-3 MEMBERSHIP: the round-23b repaired method test
(max-to-mean at MATCHED DIMENSION), run on the large-source charts.

The 23b wall, at METHOD level: "a dimension-uniform max-to-mean bound
for split locators in a growing-dimensional flat (the anticode bound's
exponent grows with flat dimension)"
(notes/pilots_20260807/mf_wall_adversary/REPORT.md:141).

Functionals (named, CATCH-19C):
  DIMV        = dim V = d-ell+2 (= e+1-u; the round-24 slice-dimension
                theorem is the u = 0 case)
  MEAN_G      = mean guarded family size over configs
  MAX_G       = max guarded family size over configs
  MAXMEAN_G   = MAX_G / MEAN_G                    (the max-to-mean gap)
  MAXMEAN_R   = the SAME ratio in the matched random-flat arm (same q,
                d, pool, dimension) -- the 23b POWER CONTROL
  LOG2_AC_over_TRUTH = log2(AC_best_orientation) - log2(MAX_G)
                       = how many bits the packing instrument is loose
  The wall signature = LOG2_AC_over_TRUTH grows with DIMV while MAX_G
  stays bounded, in the GUARDED arm, and the random arm behaves the same
  (so the gap is not a guard artefact).

Stdlib only.  Run via tools/ramguard tiny -- python3 from repo root.
"""
from __future__ import annotations

import glob
import json
import math
import os

DIR = ("/home/u2470931/smooth-read-solomin/prize/notes/"
       "pilots_20260809/m7_falsifier_hunt")


def main():
    out = []
    for p in sorted(glob.glob(DIR + "/out_*.json")):
        cid = os.path.basename(p)[4:-5]
        d = json.load(open(p))
        s, recs = d["summary"], d["recs"]
        c = s["cell"]
        dimv = c["d"] - c["ell"] + 2
        ns = [r["NSPLIT_G"] for r in recs]
        rs = [r.get("RAND_NSPLIT", 0) for r in recs]
        mean_g = sum(ns) / len(ns) if ns else 0
        mean_r = sum(rs) / len(rs) if rs else 0
        acs = [min(x for x in (r.get("AC_DIRECT_G"), r.get("AC_COMP_G"))
                   if x is not None)
               for r in recs if r.get("AC_DIRECT_G") is not None
               or r.get("AC_COMP_G") is not None]
        ac_best = max(acs) if acs else None
        mx = max(ns) if ns else 0
        out.append({
            "cell": cid, "t": c["t"], "ell": c["ell"], "d": c["d"],
            "u": c["u"], "b": c["b"], "N": c["N"], "q": s["q"],
            "DIMV": dimv, "configs": s["configs"],
            "MEAN_G": round(mean_g, 4), "MAX_G": mx,
            "MAXMEAN_G": round(mx / mean_g, 3) if mean_g else None,
            "MEAN_R": round(mean_r, 4), "MAX_R": max(rs) if rs else 0,
            "MAXMEAN_R": (round(max(rs) / mean_r, 3) if mean_r else None),
            "AC_best_max_over_configs": ac_best,
            "LOG2_AC_over_TRUTH": (round(math.log2(ac_best) - math.log2(mx), 3)
                                   if ac_best and mx else None),
            "sharp_cap_d_minus_ell": c["d"] - c["ell"],
            "OVL_MAX_G": s["OVL_MAX_G_observed"],
        })
    out.sort(key=lambda r: (r["DIMV"], r["cell"]))
    by_dim = {}
    for r in out:
        by_dim.setdefault(r["DIMV"], []).append(r)
    summ = []
    for k in sorted(by_dim):
        rs2 = [r for r in by_dim[k] if r["MAXMEAN_G"] is not None]
        if not rs2:
            continue
        summ.append({
            "DIMV": k, "cells": len(rs2),
            "MAX_G_range": [min(r["MAX_G"] for r in rs2),
                            max(r["MAX_G"] for r in rs2)],
            "MAXMEAN_G_mean": round(sum(r["MAXMEAN_G"] for r in rs2)
                                    / len(rs2), 3),
            "MAXMEAN_R_mean": round(
                sum(r["MAXMEAN_R"] for r in rs2 if r["MAXMEAN_R"])
                / max(1, sum(1 for r in rs2 if r["MAXMEAN_R"])), 3),
            "LOG2_AC_over_TRUTH_mean": round(
                sum(r["LOG2_AC_over_TRUTH"] for r in rs2
                    if r["LOG2_AC_over_TRUTH"] is not None)
                / max(1, sum(1 for r in rs2
                             if r["LOG2_AC_over_TRUTH"] is not None)), 3),
        })
    print(json.dumps({"per_cell": out, "by_flat_dimension": summ}, indent=1))


if __name__ == "__main__":
    main()
