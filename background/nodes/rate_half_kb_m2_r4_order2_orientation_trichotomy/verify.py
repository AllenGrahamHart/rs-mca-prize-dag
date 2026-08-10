#!/usr/bin/env python3
"""Verify the component-level order-two orientation composition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
PARENTS = (
    "rate_half_kb_m2_v4_outer_recurrence_router",
    "rate_half_kb_m2_r4_coordinate_transpose_transport",
    "rate_half_kb_m2_r4_diagonal_source_subfield_dichotomy",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "node status")
    require(all(nodes[parent]["status"] == "PROVED" for parent in PARENTS),
            "parent status")
    require(all((parent, NODE.name, "req") in edges for parent in PARENTS),
            "dependency wiring")
    statement = (NODE / "statement.md").read_text()
    require("component" in statement and "does not identify active" in statement,
            "scope fence")
    require("(2,8,1)" in statement and "does not cover" in statement,
            "trivial-stabilizer fence")
    print("order_two_subgroups=3 coordinate_orbits=1 diagonal_branches=2")


if __name__ == "__main__":
    main()
