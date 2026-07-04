#!/usr/bin/env python3
"""Prune audit: nodes with NO path (req or ev, any direction chain toward
the grands) reaching the prize are candidates for archiving. Conservative:
a node survives if any directed path (mixed kinds) reaches a grand."""
import json, os
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "..", "dag.json")))
fwd = defaultdict(list)
for e in d["edges"]:
    fwd[e["from"]].append(e["to"])
reach = {}
def reaches(v, seen=None):
    if v in ("mca_grand", "list_grand"): return True
    if v in reach: return reach[v]
    seen = seen or set()
    if v in seen: return False
    seen.add(v)
    r = any(reaches(w, seen) for w in fwd[v])
    reach[v] = r
    return r
prunable = [n["id"] for n in d["nodes"] if not reaches(n["id"])]
print(f"prune candidates (no path of any kind to the prize): {len(prunable)}")
for x in sorted(prunable)[:20]:
    print(" -", x, f"[{next(n['status'] for n in d['nodes'] if n['id']==x)}]")
