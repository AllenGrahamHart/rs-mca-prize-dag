#!/usr/bin/env python3
"""Verify tau-plus forced-EF guard emptiness in cubic component zero."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_ef_tau_plus_guarded_product_exclusion"
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


def replay(component, delta_sign=-1, expected_terms=(19, 19, 19)):
    for ef_sign in (-1, 1):
        transcript = io.StringIO()
        with contextlib.redirect_stdout(transcript):
            equations, basis = PARENT.SOLVER.solve_component(
                component, cell="forced-ef",
                delta_sign=delta_sign, ef_sign=ef_sign,
            )
        require(tuple(len(equation) for equation in equations)
                == expected_terms, "sparse profiles")
        require(any(polynomial == {(0, 1): PARENT.SOLVER.ONE}
                    for polynomial in basis), "e guard equation")
        require("BUCHBERGER_DONE basis=30 pairs=435"
                in transcript.getvalue(), "completion count")


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41EP-2" in statement and "74 cells" in statement, "claim")
    require("does not delete the opposite" in statement
            and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_colored_deployed_product_exclusion",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    PARENT.factor_audit()
    replay(0)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S1_EF_PLUS_PASS "
        "component=0 ef_signs=2 terms=19 guard=e pairs=435"
    )


if __name__ == "__main__":
    main()
