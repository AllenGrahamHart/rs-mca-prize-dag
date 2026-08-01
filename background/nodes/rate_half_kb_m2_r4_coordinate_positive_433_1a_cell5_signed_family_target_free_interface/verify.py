#!/usr/bin/env python3
"""Verify the cell-5 signed-family target-free interface."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "universal_target_elimination_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell5_ratio_exceptional_branch_exclusion",
)
COMPILER = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_signed_family_target_free.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("compiler", COMPILER)
    compiler = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(compiler)
    result = compiler.verify()
    require(result["cut_count"] == 4, "cut count")
    require(result["source_slot_count"] == 3, "source slots")
    require(result["target_variables_eliminated"] == 2, "target variables")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent edge {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_SIGNED_FAMILY_VERIFY_PASS "
        "cuts=4 families=2 route=open"
    )


if __name__ == "__main__":
    main()
