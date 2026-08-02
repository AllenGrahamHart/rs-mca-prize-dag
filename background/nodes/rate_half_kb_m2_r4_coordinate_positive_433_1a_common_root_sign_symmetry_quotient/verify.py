#!/usr/bin/env python3
"""Verify the ten-orbit positive common root-sign quotient."""

import json
import subprocess
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient"
CHECKER = ROOT / (
    "experiments/prize_resolution/"
    "check_rate_half_kb_positive_433_1a_common_root_sign_symmetry.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("exactly ten" in statement and "exactly nine unclosed" in statement,
            "orbit claim")
    require("not a deletion of the other nine" in statement, "scope")
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
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell58_complete_root_sign_orbit_exclusion",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    completed = subprocess.run(
        [sys.executable, str(CHECKER)], cwd=ROOT, check=True,
        capture_output=True, text=True,
    )
    require("raw_rows=60 exact_orbits=10 closed_orbits=1 open_orbits=9"
            in completed.stdout, "checker output")
    print("positive 433-1a common root-sign symmetry quotient verified")


if __name__ == "__main__":
    main()
