#!/usr/bin/env python3
"""Verify the positive three-loop common-placement atlas."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_three_loop_common_placement_atlas"
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_three_loop_common_placement_atlas.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("atlas", SCRIPT)
    atlas = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(atlas)
    orbit_counts, cases = atlas.verify()
    require(orbit_counts == {"442": 2, "433": 2}, "orbit census")
    require(len(cases) == 4, "case coverage")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_r4_coordinate_positive_three_loop_common_kernel_compiler",
        "rate_half_kb_m2_r4_coordinate_positive_three_loop_complete_edge_skeleton_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    statement = (NODE / "statement.md").read_text()
    require("exactly four common placement orbits" in statement, "claim")
    require("does not assert that a residual solution" in statement, "nonclaim")
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_PLACEMENT_VERIFY_PASS "
        "profiles=2 orbits=4 residual_degrees=6,6,6,6"
    )


if __name__ == "__main__":
    main()
