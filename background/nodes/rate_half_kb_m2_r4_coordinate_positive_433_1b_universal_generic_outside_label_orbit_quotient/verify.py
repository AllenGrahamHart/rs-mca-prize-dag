#!/usr/bin/env python3
"""Verify the universal positive 433-1b label quotient."""

import hashlib
import json
from pathlib import Path
import subprocess


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = ROOT / "experiments/prize_resolution/rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
SCRIPT_SHA256 = "82df776b06b375e9bee6fcc77aead1ebca4594028fa2e51df6318422a9d2f9bb"
EXPECTED = (
    "RATE_HALF_KB_POSITIVE_433_1B_UNIVERSAL_LABEL_ORBIT_ROUTER_PASS "
    "labels=105 orbits=36 sizes=1:3,2:15,4:18 "
    "endpoint_labels=30 endpoint_orbits=12 "
    "active_labels=75 active_orbits=24 active_sizes=1:1,2:9,4:14 "
    "full_sha256=b5ec5e8418af3385dc83aeeb9aca9c8b851eae9e23794e6637f1b42a37576cb6 "
    "active_sha256=c5c6f6b2e4af85cf2efd05fe106fa63a09bde9e6fa6ee07ed29a7f292f3b7353"
)
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_universal_xi4_xi3_outside_role_transport",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "router digest")
    process = subprocess.run(["python3", str(SCRIPT)], capture_output=True,
                             text=True, timeout=10)
    require(process.returncode == 0 and process.stdout.strip() == EXPECTED
            and not process.stderr, "router replay")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED"
            and all((parent, NODE.name, "req") in edges for parent in PARENTS)
            and (NODE.name, "rate_half_band_closure", "ev") in edges,
            "DAG wiring")
    print("role_cells=15 labels=105 orbits=36 active_labels=75 active_orbits=24")


if __name__ == "__main__":
    main()
