#!/usr/bin/env python3
"""Verify the cell-12 105-to-36 generic label quotient."""

import hashlib
import json
from pathlib import Path
import subprocess


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
SCRIPT = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cell12_generic_label_orbit_router.py"
)
SCRIPT_SHA256 = "d9d68dac01842f6a0caacc1e1f9db80f6c57908ee6f52ad08aa49d1789eca4b7"
EXPECTED = (
    "RATE_HALF_KB_POSITIVE_433_1B_CELL12_LABEL_ORBIT_ROUTER_PASS "
    "labels=105 orbits=36 sizes=1:3,2:15,4:18 "
    "sha256=b5ec5e8418af3385dc83aeeb9aca9c8b851eae9e23794e6637f1b42a37576cb6"
)
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell12_elliptic_four_basis_common_locus",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell12_rational_boundary_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_universal_xi4_xi3_outside_role_transport",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "router digest")
    process = subprocess.run(
        ["python3", str(SCRIPT)], capture_output=True, text=True, timeout=10
    )
    require(process.returncode == 0 and process.stdout.strip() == EXPECTED
            and not process.stderr, "router replay")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"missing parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "DAG consumer")
    print("cell=12 labels=105 generic_orbits=36 sizes=1:3,2:15,4:18")


if __name__ == "__main__":
    main()
