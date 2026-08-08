#!/usr/bin/env python3
"""Verify the cell-4 xi4 pairings 1-2 transport corollary."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
SCRIPT = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_xi4_xi3_"
    "universal_outside_role_transport.py"
)
SCRIPT_SHA256 = "b875ebcf7cfb3540b1987c54f7b2c057c21290ef883be76861617009a3ce8316"
DIRECT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_xi3_pairings1_2_reciprocal_linear_exclusion"
)
TRANSPORT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "universal_xi4_xi3_outside_role_transport"
)
DEPENDENCIES = {DIRECT, TRANSPORT}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_certificate():
    specification = importlib.util.spec_from_file_location(
        "universal_transport", SCRIPT
    )
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "proved DAG node")
    for dependency in DEPENDENCIES:
        require(nodes[dependency]["status"] == "PROVED", f"proved {dependency}")
        require((dependency, NODE_ID, "req") in edges, f"required {dependency}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "band evidence")


def main():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "transport certificate custody")
    census = load_certificate().verify_transport()
    require(census == {
        "role_cells": 15,
        "source_signs": 4,
        "target_lanes": 4,
        "matchings": 15,
        "system_bijections": 3600,
    }, "universal transport census")
    verify_dag()
    direct_statement = (
        ROOT / "background/nodes" / DIRECT / "statement.md"
    ).read_text()
    transport_statement = (
        ROOT / "background/nodes" / TRANSPORT / "statement.md"
    ).read_text()
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    require("role-cell-4" in direct_statement
            and "matching index in" in direct_statement
            and "`{1,2}`" in direct_statement,
            "direct-parent scope")
    require("every guarded positive deployed" in transport_statement.lower()
            and "and canonical matching" in transport_statement,
            "universal-parent scope")
    require("4 source signs * 4 target lanes * 2 matchings = 32" in statement,
            "statement payment")
    require("matching 1 maps to matching 1" in proof
            and "matching 2 maps to matching" in proof,
            "matching-index preservation")
    print("cell=4 xi=4 pairings=1,2 transport=exact raw_cases=32")


if __name__ == "__main__":
    main()
