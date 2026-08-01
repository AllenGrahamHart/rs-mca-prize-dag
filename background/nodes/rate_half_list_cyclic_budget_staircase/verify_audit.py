#!/usr/bin/env python3
"""Audit scope for the rate-half LIST cyclic budget staircase."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_list_cyclic_budget_staircase"
PARENT = "rate_half_cyclic_rotated_prefix_floor"
CONSUMER = "rate_half_list_adjacent_crossing"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    text = "\n".join(
        (NODE / name).read_text()
        for name in ("statement.md", "proof.md", "claim_contract.md", "audit.md")
    )
    for marker in ("first five tiers", "recovers", "exact printed values",
                   "does not prove any safe-side", "does not solve LIST"):
        require(marker in text, f"missing marker {marker}")
    require("superexponential" not in text, "invalid growth claim retained")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "node status")
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer edge")
    print("rate-half LIST cyclic budget staircase audit verified")


if __name__ == "__main__":
    main()
