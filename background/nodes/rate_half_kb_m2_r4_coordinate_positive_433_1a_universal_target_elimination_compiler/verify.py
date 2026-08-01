#!/usr/bin/env python3
"""Verify the positive 433-1a universal target elimination compiler."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PARENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "outside_case_symmetry_quotient"
)
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_universal_target_elimination.py"
)
RESULT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_universal_target_elimination_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("target", SCRIPT)
    target = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(target)
    expected = target.compile_result()
    observed = json.loads(RESULT.read_text())
    require(target.payload_hash(observed) == observed["payload_sha256"],
            "result seal")
    require(observed == expected, "result content")
    require(len(expected["universal_product_relations"]) == 4,
            "product relation count")
    require(len(expected["universal_squared_sum_relations"]) == 7,
            "sum relation count")
    require(expected["conclusion"] == {
        "target_variables_d_e_f_eliminated_exactly": True,
        "formal_case_count_compiled": 267,
        "outside_source_systems_proved_empty": False,
        "route_deleted": False,
    }, "conclusion")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_UNIVERSAL_TARGET_ELIMINATION_VERIFY_PASS "
        "products=4 sums=7 cases=267 route=open"
    )


if __name__ == "__main__":
    main()
