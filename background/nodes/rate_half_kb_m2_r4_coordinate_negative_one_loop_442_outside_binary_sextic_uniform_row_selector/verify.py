#!/usr/bin/env python3
"""Verify the uniform sextic coefficient-row selector."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_uniform_row_selector"
SELECTOR_PATH = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_442_sextic_row_selector.py"
)
SPEC = importlib.util.spec_from_file_location("selector", SELECTOR_PATH)
SELECTOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SELECTOR)
EXPECTED_NORM = 1133299039


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def selected_norm(epsilon_1, epsilon_2):
    action = SELECTOR.build_action(epsilon_1, epsilon_2)
    minor = [[action[row][column] for column in range(3)]
             for row in range(3)]
    return SELECTOR.det_mod(SELECTOR.kdet3(minor))


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41US-1" in statement and "E_0=E_1=E_2" in statement,
            "claim")
    require("does not evaluate" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_eigenvalue_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_quotient_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_mate_coordinate_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    require(selected_norm(1, 1) == EXPECTED_NORM, "representative norm")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_ROW_PASS "
        "signs=1,1 rows=0,1,2 columns=0,1,2 norm=1133299039"
    )


if __name__ == "__main__":
    main()
