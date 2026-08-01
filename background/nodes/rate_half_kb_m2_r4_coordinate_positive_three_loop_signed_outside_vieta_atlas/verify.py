#!/usr/bin/env python3
"""Verify the signed positive three-loop outside-Vieta atlas."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_three_loop_signed_outside_vieta_atlas"
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_three_loop_signed_outside_vieta_atlas.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("outside_vieta", SCRIPT)
    outside_vieta = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(outside_vieta)
    orbits, lanes = outside_vieta.verify()
    require(len(orbits) == 2, "sign orbits")
    require(len(lanes) == 8, "lane count")
    require(all(len(records) == 7 for records in lanes.values()), "edge count")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_r4_coordinate_positive_three_loop_common_placement_atlas",
        "rate_half_kb_m2_r4_coordinate_positive_three_loop_complete_edge_skeleton_classifier",
        "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    statement = (NODE / "statement.md").read_text()
    require("exactly eight signed Vieta lanes" in statement, "claim")
    require("resultant alone does not enforce" in statement, "resultant fence")
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_SIGNED_OUTSIDE_VERIFY_PASS "
        "sign_orbits=2 placements=4 lanes=8 edge_records=56"
    )


if __name__ == "__main__":
    main()
