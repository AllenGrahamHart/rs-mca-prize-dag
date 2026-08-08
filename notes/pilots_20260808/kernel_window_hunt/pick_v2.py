#!/usr/bin/env python3
"""Select the max-v2(p-1) witness across all v2hunt shards, verify it fully,
and write best_witness_v2.json for the standalone repro generator."""
import glob
import json
import sys
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
from hunt import verify_hit

best = None
tot_n = tot_hits = 0
hist = {}
for f in sorted(glob.glob("notes/pilots_20260808/kernel_window_hunt/state/v2hunt_*.json")):
    st = json.load(open(f))
    tot_n += st["n"]
    tot_hits += st["hits"]
    for k, v in st["v2hist"].items():
        hist[int(k)] = hist.get(int(k), 0) + v
    for r in st["best"]:
        if best is None or r["v2"] > best["v2"]:
            best = r
print("TOTAL samples %d, admissible-window hits %d (rate %.4f)"
      % (tot_n, tot_hits, tot_hits / tot_n))
print("v2(p-1) histogram (all shards):", dict(sorted(hist.items())))
print("max v2 =", best["v2"], " pbits =", best["pbits"], " cof =", best["cof"])

rep = verify_hit(best["w"], int(best["p"]), 128)
for k in sorted(rep):
    print("   %-20s %s" % (k, rep[k]))
assert rep["ok"], "max-v2 witness failed verification"
json.dump({"w": best["w"], "p": best["p"]},
          open("notes/pilots_20260808/kernel_window_hunt/state/best_witness_v2.json", "w"))
print("VERIFIED and written")
