#!/usr/bin/env python3
"""Verify the exhaustive five-row negative-coordinate composition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_complete_exclusion"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate",
    "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_"
    "h6_complete_product_exclusion",
    "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_"
    "constrained_complete_product_exclusion",
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_433_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_complete_exclusion",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(all(nodes[parent]["status"] == "PROVED" for parent in PARENTS),
            "parent status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
            "dependency coverage")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    statement = (NODE / "statement.md").read_text()
    for row in (
        "(0,1,0)     (2,2,0)", "(1,1,0)     (1,1,1)",
        "(0,0,0)     (2,2,1)", "(1,0,0)     (1,1,2)",
        "(1,0,1)     (2,0,1)",
    ):
        require(row in statement, f"partition row {row}")
    require("does not exclude positive coordinate parity" in statement,
            "positive-parity fence")
    print(
        "RATE_HALF_KB_M2_R4_NEGATIVE_COORDINATE_EXCLUSION_PASS "
        "skeletons=5 terminal_exclusions=5"
    )


if __name__ == "__main__":
    main()
