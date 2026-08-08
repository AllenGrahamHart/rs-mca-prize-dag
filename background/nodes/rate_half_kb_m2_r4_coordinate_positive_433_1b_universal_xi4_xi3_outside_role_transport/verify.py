#!/usr/bin/env python3
"""Verify the universal xi4-to-xi3 outside-role transport."""

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
DEPENDENCIES = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_certificate():
    specification = importlib.util.spec_from_file_location("universal_transport", SCRIPT)
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
            "certificate custody")
    census = load_certificate().verify_transport()
    require(census == {
        "role_cells": 15,
        "source_signs": 4,
        "target_lanes": 4,
        "matchings": 15,
        "system_bijections": 3600,
    }, "transport census")
    verify_dag()
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    require("every guarded positive deployed" in statement,
            "universal statement scope")
    require("fixes every common role cell" in proof,
            "common-role identity")
    print(
        "role_cells=15 xi4_to_xi3=exact source_signs=4 "
        "lanes=4 matchings=15 system_bijections=3600"
    )


if __name__ == "__main__":
    main()
