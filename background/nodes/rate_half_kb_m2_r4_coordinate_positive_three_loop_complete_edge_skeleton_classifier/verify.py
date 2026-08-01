#!/usr/bin/env python3
"""Verify the positive three-loop outside skeleton classifier."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_three_loop_"
    "complete_edge_skeleton_classifier"
)
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_three_loop_outside_skeleton_census.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("census", SCRIPT)
    census = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(census)
    solutions, orbits, costs = census.verify()
    require(len(solutions) == 6 and len(orbits) == 2, "raw census")
    require(costs == (2, 0), "defect router")
    require(orbits[1] == (((0, 1, 1), (2, 2, 1)), 3), "survivor")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_positive_loop_ramification_gate",
        "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    statement = (NODE / "statement.md").read_text()
    require("unique record" in statement, "claim")
    require("does not impose the positive rank-five product map" in statement,
            "nonclaim")
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_EDGE_VERIFY_PASS "
        "raw=6 orbits=2 survivors=1 labeled_survivors=3"
    )


if __name__ == "__main__":
    main()
