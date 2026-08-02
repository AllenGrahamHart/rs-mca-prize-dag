#!/usr/bin/env python3
"""Merge chunked scan JSONs; report exact coverage accounting."""
import glob, json, os, sys
from math import comb
d = sys.argv[1]
out = {}
for p in sorted(glob.glob(os.path.join(d, "N*_w*.json"))):
    r = json.load(open(p))
    key = "N%d_w%d" % (r["N"], r["w"])
    e = out.setdefault(key, {"N": r["N"], "twoN": r["twoN"], "w": r["w"],
                             "nparts": r["nparts"], "parts_done": [],
                             "orbits_total": r["n_support_orbits_total"],
                             "orbits_covered": 0, "polys_scanned": 0,
                             "max": -1, "argmax": None, "above": 0, "files": []})
    e["parts_done"].append(r["part"])
    e["orbits_covered"] += r["n_support_orbits_this_part"]
    e["polys_scanned"] += r["n_polynomials_scanned"]
    v = int(r.get("max_norm", r.get("max_norm_exact")))
    if v > e["max"]:
        e["max"] = v; e["argmax"] = r["argmax_f"]
    e["above"] += r.get("n_above_threshold", r.get("n_strictly_above_target", 0))
    e["files"].append(os.path.basename(p))
for k, e in out.items():
    N, w = e["N"], e["w"]
    e["parts_done"] = sorted(e["parts_done"])
    e["COMPLETE"] = (len(e["parts_done"]) == e["nparts"]
                     and e["orbits_covered"] == e["orbits_total"])
    e["naive_search_space_C(N,w)2^w"] = comb(N, w) * 2 ** w
    e["reduction_factor"] = round(e["naive_search_space_C(N,w)2^w"] / max(1, e["polys_scanned"]), 1)
    e["max"] = str(e["max"])
print(json.dumps(out, indent=1))
