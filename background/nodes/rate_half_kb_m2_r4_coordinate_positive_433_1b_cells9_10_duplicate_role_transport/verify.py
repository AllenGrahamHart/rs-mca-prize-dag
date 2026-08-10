#!/usr/bin/env python3
"""Verify the exact duplicate-role transport from cell 9 to cell 10."""

import hashlib
import json
from pathlib import Path
import subprocess


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
SCRIPT = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cells9_10_duplicate_role_transport.py"
)
SCRIPT_SHA256 = "a562de03d52fedad25a9670b492283107b96fab6e4d689f32ff53345e7723f13"
EXPECTED = (
    "RATE_HALF_KB_POSITIVE_433_1B_CELLS9_10_TRANSPORT_PASS "
    "common_rows=20 target_lanes=4 labels=420 systems=1680"
)
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_complete_exclusion",
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_SHA256,
            "transport digest")
    process = subprocess.run(
        ["python3", str(SCRIPT)], capture_output=True, text=True, timeout=10
    )
    require(process.returncode == 0 and process.stdout.strip() == EXPECTED
            and not process.stderr, "transport replay")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"missing parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "DAG consumer")
    print("cells=9,10 principal_systems=1680 transport=bijective")


if __name__ == "__main__":
    main()
