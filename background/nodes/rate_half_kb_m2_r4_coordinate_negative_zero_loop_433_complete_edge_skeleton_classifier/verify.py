#!/usr/bin/env python3
"""Verify the zero-loop 433 complete-edge skeleton classifier."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
    "complete_edge_skeleton_classifier"
)
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_zero_loop_433_outside_skeleton_census.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("census", SCRIPT)
    census = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(census)
    solutions, orbits = census.verify()
    require(len(solutions) == 21 and len(orbits) == 5, "census")

    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    for name in ("Z0:", "Z1:", "Z2:", "Z3:", "Z4:"):
        require(name in statement, f"skeleton {name}")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
        "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_OUTSIDE_SKELETON_VERIFY_PASS "
        "labeled=21 orbits=5 sizes=6,3,3,3,6"
    )


if __name__ == "__main__":
    main()
