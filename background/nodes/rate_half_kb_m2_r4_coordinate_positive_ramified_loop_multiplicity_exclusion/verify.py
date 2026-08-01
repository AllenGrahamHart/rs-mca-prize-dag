#!/usr/bin/env python3
"""Verify the positive ramified-loop multiplicity exclusion."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_ramified_loop_multiplicity_exclusion"
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_ramified_loop_multiplicity_exclusion.py"
)
PARENTS = (
    "rate_half_kb_m2_r4_source_row_interpolation_compiler",
    "rate_half_kb_m2_r4_coordinate_coefficient_normal_form",
    "rate_half_kb_m2_r4_coordinate_positive_loop_ramification_gate",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("multiplicity", SCRIPT)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    require(module.verify() == {
        "local_row_order": 2,
        "required_square_order": 4,
        "branch_charts": 2,
        "loop_placements_deleted": 4,
        "loop_counts_deleted": (2, 3),
        "one_loop_ramified_requires_b1_zero": True,
    }, "multiplicity replay")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    statement = (NODE / "statement.md").read_text()
    require("ell_positive <= 1" in statement, "loop cap")
    require("does not treat positive zero-loop" in statement, "scope fence")
    print(
        "RATE_HALF_KB_POSITIVE_RAMIFIED_LOOP_MULTIPLICITY_VERIFY_PASS "
        "local_order=2 required_order=4 loop_counts=2,3"
    )


if __name__ == "__main__":
    main()
