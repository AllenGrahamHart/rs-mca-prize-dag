#!/usr/bin/env python3
"""Verify component zero of the opposite-parity forced-DE exclusion."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_de_opposite_parity_deployed_product_exclusion"
PARENT_PATH = ROOT / (
    "background/nodes/"
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_"
    "s1_forced_de_deployed_product_exclusion/verify.py"
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
    require("KB41DO-1" in statement and "78 cells" in statement, "claim")
    require("does not transport" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_de_deployed_product_exclusion",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    PARENT.factor_audit()
    PARENT.solve_quietly(0, alpha_sign=-1)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S1_DE_OPP_PASS "
        "component=0 alpha=-1 pairs=79 unit=True"
    )


if __name__ == "__main__":
    main()
