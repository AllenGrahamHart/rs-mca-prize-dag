#!/usr/bin/env python3
"""Verify the cell-4 xi3/xi4 pairing-11/14 transport corollary."""

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
    "cell4_xi3_pairing11_quadratic_resultant_signfree_exclusion"
)
XI_TRANSPORT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "universal_xi4_xi3_outside_role_transport"
)
MATCHING_TRANSPORT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_parallel_de_matching_orbit_quotient"
)
MATCHING_SCRIPT = ROOT / "background/nodes" / MATCHING_TRANSPORT / "verify.py"
DEPENDENCIES = {DIRECT, XI_TRANSPORT, MATCHING_TRANSPORT}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_certificate(path, name):
    specification = importlib.util.spec_from_file_location(
        name, path
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
    census = load_certificate(SCRIPT, "universal_transport").verify_transport()
    require(census == {
        "role_cells": 15,
        "source_signs": 4,
        "target_lanes": 4,
        "matchings": 15,
        "system_bijections": 3600,
    }, "universal transport census")
    load_certificate(MATCHING_SCRIPT, "matching_transport").verify_action()
    verify_dag()
    direct_statement = (
        ROOT / "background/nodes" / DIRECT / "statement.md"
    ).read_text()
    xi_transport_statement = (
        ROOT / "background/nodes" / XI_TRANSPORT / "statement.md"
    ).read_text()
    matching_statement = (
        ROOT / "background/nodes" / MATCHING_TRANSPORT / "statement.md"
    ).read_text()
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    require("role-cell-4" in direct_statement
            and "matching index 11" in direct_statement,
            "direct-parent scope")
    require("every guarded positive deployed" in xi_transport_statement.lower()
            and "and canonical matching" in xi_transport_statement,
            "universal-parent scope")
    require("{11,14}" in matching_statement
            and "xi in {2,3,4,5,6}" in matching_statement,
            "matching-parent scope")
    require("4 source signs * 4 target lanes * 4 labels = 64" in statement,
            "statement payment")
    require("transports `(3,11)` to `(3,14)`" in proof
            and "gives `(4,11)`" in proof
            and "gives `(4,14)`" in proof,
            "four-label composition")
    print("cell=4 xi=3,4 pairings=11,14 transport=exact raw_cases=64")


if __name__ == "__main__":
    main()
