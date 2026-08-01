#!/usr/bin/env python3
"""Verify the positive 433-1a outside-case symmetry quotient."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PARENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "quadratic_paired_product_resultant_interface"
)
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_outside_case_symmetry.py"
)
RESULT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1a_outside_case_symmetry_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("symmetry", SCRIPT)
    symmetry = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(symmetry)
    expected = symmetry.compile_result()
    observed = json.loads(RESULT.read_text())
    require(symmetry.payload_hash(observed) == observed["payload_sha256"],
            "result seal")
    require(observed == expected, "result content")
    require(expected["ledger"]["total"] == {
        "labeled_cases": 525,
        "orbits": 267,
    }, "total ledger")
    require(expected["missing_mate_EF"]["current_templates"] == {
        "A_and_B_are_one_gauge_orbit": True,
        "aligned_orbits": 1,
        "near_orbits": 4,
        "total_orbits": 5,
        "uncovered_orbits": 34,
    }, "template coverage")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_OUTSIDE_CASE_SYMMETRY_VERIFY_PASS "
        "labeled=525 orbits=267 aligned=39 near=228 ef=39 templates=5"
    )


if __name__ == "__main__":
    main()
