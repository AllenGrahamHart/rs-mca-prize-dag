#!/usr/bin/env python3
"""Verify tau-minus forced-EF guard emptiness in cubic component zero."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_ef_tau_minus_guarded_product_exclusion"
PARENT_PATH = ROOT / (
    "background/nodes/"
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_"
    "s1_forced_ef_tau_plus_guarded_product_exclusion/verify.py"
)
SPEC = importlib.util.spec_from_file_location("parent", PARENT_PATH)
PARENT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PARENT)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41EM-1" in statement and "72" in statement, "claim")
    require("does not delete those loop" in statement
            and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_ef_tau_plus_guarded_product_exclusion",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    PARENT.PARENT.factor_audit()
    PARENT.replay(0, delta_sign=1, expected_terms=(17, 17, 17))
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S1_EF_MINUS_PASS "
        "component=0 ef_signs=2 terms=17 guard=e pairs=435"
    )


if __name__ == "__main__":
    main()
