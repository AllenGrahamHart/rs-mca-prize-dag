#!/usr/bin/env python3
"""Verify the guarded S1 forced-DE product witness over F_41."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_de_f41_product_witness"
SCAN_PATH = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_442_s1_forced_de_scan.py"
)
SPEC = importlib.util.spec_from_file_location("scan", SCAN_PATH)
SCAN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SCAN)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41FW-3" in statement and "unique guarded" in statement,
            "claim")
    require("deployed characteristic" in statement
            and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_cubic_root_gate",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_explicit_involution_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_edge_skeleton_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_eigenvalue_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    accepted = []
    for d in range(1, SCAN.P):
        for s in range(1, SCAN.P):
            coefficients = SCAN.residual_form(d, s)
            if (all(SCAN.equation(coefficients, ell) == 0
                    for ell in range(7)) and SCAN.guarded(d, s)):
                accepted.append((d, s))
    require(accepted == [(15, 34)], "guarded census")
    require(SCAN.residual_form(15, 34)
            == [15, 27, 7, 12, 23, 1, 17], "coefficients")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_F41_PASS "
        "tested=1600 guarded=1 d=15 e=7 f=18"
    )


if __name__ == "__main__":
    main()
