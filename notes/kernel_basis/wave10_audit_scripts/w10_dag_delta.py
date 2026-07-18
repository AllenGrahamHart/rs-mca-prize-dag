#!/usr/bin/env python3
"""wave-10 dag forensics: per-commit node/status/edge deltas for v4 and v5 ranges."""
import json, os, sys, glob

SP = "/tmp/claude-1000/-home-u2470931-smooth-read-solomin/d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad"

def load(path):
    with open(path) as f:
        d = json.load(f)
    # node map + edge set; be schema-agnostic
    nodes = {}
    if isinstance(d, dict) and "nodes" in d:
        nl = d["nodes"]
        if isinstance(nl, dict):
            for k, v in nl.items():
                nodes[k] = v
        else:
            for v in nl:
                nodes[v["id"]] = v
        edges = d.get("edges", [])
    else:
        raise SystemExit("unknown dag schema in " + path)
    eset = set()
    for e in edges:
        if isinstance(e, dict):
            eset.add((e.get("src") or e.get("from"), e.get("dst") or e.get("to"), e.get("kind")))
        else:
            eset.add(tuple(e))
    return nodes, eset

def status(v):
    return v.get("status")

def run(rng):
    files = sorted(glob.glob(os.path.join(SP, "w10_dags", rng, "*.json")))
    assert len(files) >= 2, "need >=2 dumps"
    prev_nodes, prev_edges = load(files[0])
    print(f"=== {rng}: base {os.path.basename(files[0])}: {len(prev_nodes)} nodes, {len(prev_edges)} edges")
    total_new, total_removed, total_flips = [], [], []
    for f in files[1:]:
        tag = os.path.basename(f).replace(".json", "")
        nodes, edges = load(f)
        new = sorted(set(nodes) - set(prev_nodes))
        removed = sorted(set(prev_nodes) - set(nodes))
        flips = [(k, status(prev_nodes[k]), status(nodes[k]))
                 for k in nodes if k in prev_nodes and status(nodes[k]) != status(prev_nodes[k])]
        stmt_changed = [k for k in nodes if k in prev_nodes
                        and nodes[k].get("statement") != prev_nodes[k].get("statement")]
        e_new = edges - prev_edges
        e_rm = prev_edges - edges
        if new or removed or flips or stmt_changed or e_new or e_rm:
            print(f"--- {tag}")
            for k in new:
                print(f"  NEW  {k} [{status(nodes[k])}] layer={nodes[k].get('layer','?')}")
            for k in removed:
                print(f"  REMOVED  {k} [{status(prev_nodes[k])}]")
            for k, a, b in flips:
                print(f"  FLIP {k}: {a} -> {b}")
            for k in stmt_changed:
                print(f"  STMT {k} ({len(str(prev_nodes[k].get('statement')))} -> {len(str(nodes[k].get('statement')))} chars)")
            for e in sorted(e_new, key=str):
                print(f"  +EDGE {e}")
            for e in sorted(e_rm, key=str):
                print(f"  -EDGE {e}")
        total_new += new; total_removed += removed; total_flips += flips
        prev_nodes, prev_edges = nodes, edges
    print(f"=== {rng} NET: {len(total_new)} new, {len(total_removed)} removed, {len(total_flips)} flips; final {len(prev_nodes)} nodes, {len(prev_edges)} edges")
    # net flips (same node flipped multiple times?)
    from collections import Counter
    fc = Counter(k for k, a, b in total_flips)
    for k, c in fc.items():
        if c > 1:
            print(f"    MULTI-FLIP {k}: {c} flips")
    return prev_nodes

if __name__ == "__main__":
    n4 = run("v4")
    print()
    n5 = run("v5")
