#!/usr/bin/env python3
"""Peek at the round-27 banked locator-scan results: find the maximal-slack
(delta = 6) top words by F_SUBSET and by F_LIST, with agreement profiles."""
import json, sys

path = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else None
with open(path) as f:
    rows = json.load(f)
summ = {}
for r in rows:
    key = (r["n"], r["q"], r["t"], r["delta"])
    d = summ.setdefault(str(key), dict(n=r["n"], q=r["q"], t=r["t"], delta=r["delta"],
                                       count=0, maxsub=0, maxlist=0,
                                       argsub=None, arglist=None,
                                       profsub=None, proflist=None))
    d["count"] += 1
    if r["F_SUBSET"] > d["maxsub"]:
        d["maxsub"] = r["F_SUBSET"]; d["argsub"] = r["word"]
        d["profsub"] = r["agreement_profile"]; d["listatsub"] = r["F_LIST"]
    if r["F_LIST"] > d["maxlist"]:
        d["maxlist"] = r["F_LIST"]; d["arglist"] = r["word"]
        d["proflist"] = r["agreement_profile"]; d["subatlist"] = r["F_SUBSET"]
res = dict(path=path, n_rows=len(rows), cells=summ)
print(json.dumps(res, indent=1))
if out:
    with open(out, "w") as f:
        json.dump(res, f, indent=1)
