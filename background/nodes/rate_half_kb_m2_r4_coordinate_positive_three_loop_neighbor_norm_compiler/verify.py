#!/usr/bin/env python3
"""Verify the positive three-loop target-neighbor norm compiler."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_three_loop_neighbor_norm_compiler"
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_three_loop_neighbor_norm.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("neighbor_norm", SCRIPT)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    result = module.verify()
    require(result == {
        "numerator_u_degree": 2,
        "denominator_u_degree": 2,
        "placements": 4,
        "lanes": 8,
        "target_degree": 4,
        "profile_433_colored_values_determined": True,
        "profile_442_colored_product_determined": True,
    }, "neighbor norm replay")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
        "rate_half_kb_m2_r4_coordinate_positive_three_loop_common_placement_atlas",
        "rate_half_kb_m2_r4_coordinate_positive_three_loop_signed_outside_vieta_atlas",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    statement = (NODE / "statement.md").read_text()
    require("degree at most two" in statement, "degree claim")
    require("do not reconstruct" in statement, "scope fence")
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_NEIGHBOR_NORM_VERIFY_PASS "
        "norm_degree=2/2 placements=4 lanes=8"
    )


if __name__ == "__main__":
    main()
