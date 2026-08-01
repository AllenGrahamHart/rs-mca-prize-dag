#!/usr/bin/env python3
"""Audit DAG wiring and scope for the DLI C1 L=1 owner ledger."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PARENTS = {
    "dli_wcl_newton_short_window_exclusion",
    "dli_wcl_weight3_ambient_exclusion",
    "dli_wcl_weight4_ambient_exclusion",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    combined = "\n".join(path.read_text() for path in NODE.glob("*.md"))
    for marker in (
        "kappa_j(0)=1",
        "3+1/q",
        "not a bound",
        "does not prove C1-ZERO",
        "not DAG premises",
    ):
        require(marker in combined, f"missing scope marker: {marker}")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent edge {parent}")
    require((NODE_ID, "dli_c1r3_gated_envelope_bound", "ev") in edges,
            "consumer edge")
    print("DLI C1 L=1 owner-ledger audit verified")


if __name__ == "__main__":
    main()
