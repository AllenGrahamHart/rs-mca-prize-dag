#!/usr/bin/env python3
"""Verify the exact xi4-to-xi3 outside-role transport theorem."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
SCRIPT = ROOT / "experiments/prize_resolution/rate_half_kb_positive_433_1b_cell3_xi4_xi3_outside_role_transport.py"
SCRIPT_SHA256 = "a7a00edbc2caf8757862b240eb5390e4d1ca3c34e75c06b03d87ec0f10e0e897"
AGGREGATE = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_complete_exclusion"
)
DEPENDENCIES = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi3_pairing0_reciprocal_square_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi3_pairings1_2_reciprocal_linear_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi3_opposite_de_pairings3_6_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi3_fully_mixed_pairings11_14_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi3_fully_mixed_pairings7_8_10_13_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi3_opposite_de_pairings4_5_9_12_exclusion",
}
MATCHING_BLOCKS = (
    {0}, {1, 2}, {3, 6}, {11, 14}, {7, 8, 10, 13}, {4, 5, 9, 12},
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_compiler():
    specification = importlib.util.spec_from_file_location("xi4_transport", SCRIPT)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "proved DAG node")
    require(nodes[AGGREGATE]["status"] == "PROVED", "proved aggregate")
    for dependency in DEPENDENCIES:
        require(nodes[dependency]["status"] == "PROVED", f"proved {dependency}")
        require((dependency, NODE_ID, "req") in edges, f"required {dependency}")
    require((NODE_ID, AGGREGATE, "req") in edges, "aggregate requirement")


def main():
    require(digest(SCRIPT) == SCRIPT_SHA256, "compiler custody")
    module = load_compiler()
    census = module.verify_transport()
    require(census == {
        "source_signs": 4,
        "target_lanes": 4,
        "matchings": 15,
        "raw_cases": 240,
    }, "transport census")
    require(set().union(*MATCHING_BLOCKS) == set(range(15)),
            "matching partition cover")
    require(sum(len(block) for block in MATCHING_BLOCKS) == 15,
            "matching partition disjointness")
    verify_dag()
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    require("4 source signs * 4 target lanes * 15 matchings = 240" in statement,
            "statement payment")
    require("sends this assignment to cell 6" in proof,
            "rejected shortcut distinguished")
    print("cell=3 xi4_to_xi3=exact matchings=15 raw_cases=240")


if __name__ == "__main__":
    main()
