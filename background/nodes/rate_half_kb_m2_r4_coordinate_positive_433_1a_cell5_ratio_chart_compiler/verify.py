#!/usr/bin/env python3
"""Verify the deployed-field positive 433-1a cell-5 ratio compiler."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_cell5_ratio_compiler.py"
)
RESULT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_cell5_ratio_result.json"
)
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "common_vieta_pivot_chart_reduction",
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "product_base_rank_global_certificate",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("ratio", SCRIPT)
    ratio = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(ratio)
    observed = json.loads(RESULT.read_text())
    require(ratio.payload_hash(observed) == observed["payload_sha256"],
            "result seal")
    require(ratio.compile_result() == observed, "exact compiler replay")
    require(observed["degrees_in_b"] == [1, 2, 2], "ratio degrees")
    require([item["terms"] for item in observed["generic_eliminants"]]
            == [244, 340], "eliminant terms")
    require(observed["conclusion"] == {
        "deployed_cell5_chart_reduced_exactly": True,
        "generic_source_variables": ["x", "r", "t"],
        "denominator_branch_closed": False,
        "outside_equations_imposed": False,
        "route_deleted": False,
    }, "scope conclusion")

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
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_RATIO_VERIFY_PASS "
        "degrees=1,2,2 eliminants=244,340 exceptional=open route=open"
    )


if __name__ == "__main__":
    main()
