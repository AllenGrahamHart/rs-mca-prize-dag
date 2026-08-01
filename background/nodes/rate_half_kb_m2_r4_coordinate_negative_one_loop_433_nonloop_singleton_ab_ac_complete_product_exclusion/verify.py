#!/usr/bin/env python3
"""Verify the one-loop 433 cells 3/6 complete-product exclusion."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_433_"
    "nonloop_singleton_ab_ac_complete_product_exclusion"
)
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_433_cell36_complete_product_exclusion.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("certificate", SCRIPT)
    certificate = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(certificate)
    counts = certificate.verify()
    require(sum(counts.values()) == 11760, "cell count")

    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("cells `[3,6]` are empty" in statement, "claim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_433_"
        "nonloop_singleton_ab_ac_finite_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_433_"
        "complete_edge_skeleton_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print(
        "RATE_HALF_KB_ONE_LOOP_433_CELL36_PRODUCT_VERIFY_PASS "
        "S0=3360 S1=6720 S2=1680 total=11760"
    )


if __name__ == "__main__":
    main()
