#!/usr/bin/env python3
"""CATCH-24A own-repo scan: duplicated (from,to) edges declared from both ends.

Reads only node.json shards (never dag.json), reproduces the exact edge
expansion of tools/dag_manifest.py, and reports ordered pairs carrying more
than one edge -- i.e. an edge declared from both endpoints, possibly with
conflicting kinds.
"""

import json
import os
from collections import defaultdict

ROOT = os.getcwd()
SECTIONS = {
    "requires": ("req", "incoming"),
    "alternatives": ("alt", "incoming"),
    "evidence_for": ("ev", "outgoing"),
    "refutes": ("ref", "outgoing"),
}


def main() -> None:
    pairs = defaultdict(list)
    shards = 0
    for tree in ("critical", "background"):
        base = os.path.join(ROOT, tree, "nodes")
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            path = os.path.join(base, name, "node.json")
            if not os.path.isfile(path):
                continue
            shards += 1
            with open(path) as handle:
                payload = json.load(handle)
            node_id = payload["node"]["id"]
            for section, (kind, direction) in SECTIONS.items():
                key = "from" if direction == "incoming" else "to"
                for row in payload.get(section, []):
                    other = row[key]
                    if direction == "incoming":
                        edge = (other, node_id)
                    else:
                        edge = (node_id, other)
                    pairs[edge].append((kind, node_id, section))

    dupes = {k: v for k, v in pairs.items() if len(v) > 1}
    print("SHARDS", shards)
    print("ORDERED_PAIRS", len(pairs))
    print("DOUBLED_PAIRS", len(dupes))
    for edge in sorted(dupes):
        kinds = sorted({row[0] for row in dupes[edge]})
        flag = "CONFLICTING_KINDS" if len(kinds) > 1 else "SAME_KIND"
        print(f"  {edge[0]} -> {edge[1]} :: {flag} :: " + "; ".join(
            f"{k} declared by {who}.{sec}" for k, who, sec in dupes[edge]
        ))

    # Reverse-direction pairs (A->B and B->A both present) as a second signal.
    rev = sorted(e for e in pairs if (e[1], e[0]) in pairs and e[0] < e[1])
    print("BIDIRECTIONAL_PAIRS", len(rev))
    for edge in rev:
        print("  ", edge, [r[0] for r in pairs[edge]],
              [r[0] for r in pairs[(edge[1], edge[0])]])


if __name__ == "__main__":
    main()
