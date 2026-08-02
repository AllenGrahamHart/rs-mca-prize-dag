#!/usr/bin/env python3
"""Verify the complete cell-5/8 root-sign orbit exclusion."""

import json
import subprocess
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell58_complete_root_sign_orbit_exclusion"
CHECKER = ROOT / (
    "experiments/prize_resolution/"
    "check_rate_half_kb_positive_433_1a_cell58_source_reciprocal_transport.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("{5,8} x {-1,+1} x {-1,+1}" in statement, "eight-row claim")
    require("does not treat another role-cell orbit" in statement, "scope")
    require("nonclaim" in contract, "contract nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_r4_coordinate_coefficient_normal_form",
        "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell58_epsilon2_minus_transport_exclusion",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    completed = subprocess.run(
        [sys.executable, str(CHECKER)], cwd=ROOT, check=True,
        capture_output=True, text=True,
    )
    require("SOURCE_RECIPROCAL_TRANSPORT_PASS" in completed.stdout,
            "checker output")
    print("positive 433-1a cell-5/8 complete sign orbit verified")


if __name__ == "__main__":
    main()
