#!/usr/bin/env python3
"""Verify the cell-9 75-to-24 active label quotient."""

import json
from pathlib import Path
import subprocess


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = ROOT / "experiments/prize_resolution/rate_half_kb_positive_433_1b_universal_generic_label_orbit_router.py"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_universal_generic_outside_label_orbit_quotient",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_endpoint_roles_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_regularized_base_locus_complete_exclusion",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    process = subprocess.run(["python3", str(SCRIPT)], capture_output=True,
                             text=True, timeout=10)
    require(process.returncode == 0 and "active_labels=75 active_orbits=24 "
            "active_sizes=1:1,2:9,4:14" in process.stdout
            and not process.stderr, "router replay")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED"
            and all(nodes[parent]["status"] == "PROVED" for parent in PARENTS)
            and all((parent, NODE.name, "req") in edges for parent in PARENTS)
            and (NODE.name, "rate_half_band_closure", "ev") in edges,
            "DAG composition")
    print("cell=9 paid_labels=30 active_labels=75 active_orbits=24")


if __name__ == "__main__":
    main()
