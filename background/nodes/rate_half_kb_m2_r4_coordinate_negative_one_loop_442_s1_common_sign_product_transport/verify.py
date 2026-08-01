#!/usr/bin/env python3
"""Verify product-data transport to common sign row (1,-1)."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_common_sign_product_transport"
EXPERIMENT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_442_common_sign_product_transport.py"
)
SPEC = importlib.util.spec_from_file_location("transport", EXPERIMENT)
TRANSPORT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TRANSPORT)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41T-1" in statement and "frontier falls from 70 to 40"
            in statement, "claim")
    require("does not delete" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_loop_deployed_product_exclusion",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_mate_coordinate_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    records = TRANSPORT.check_row(1, -1)
    require(len(records) == 2, "component count")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S1_TRANSPORT_PASS "
        "row=1,-1 components=2 common_c_m=True frontier=40"
    )


if __name__ == "__main__":
    main()
