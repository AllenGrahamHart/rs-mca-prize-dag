#!/usr/bin/env python3
"""Verify the forced-EF S2 guard contradiction in component zero."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s2_forced_ef_guarded_product_exclusion"
SOLVER_PATH = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_442_s1_quotient_buchberger.py"
)
SPEC = importlib.util.spec_from_file_location("solver", SOLVER_PATH)
SOLVER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SOLVER)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def replay(component):
    transcript = io.StringIO()
    with contextlib.redirect_stdout(transcript):
        equations, basis = SOLVER.solve_component(component, cell="s2-forced-ef")
    require(tuple(len(equation) for equation in equations) == (7, 7, 7),
            "sparse profiles")
    require({(0, 2): SOLVER.ONE} in basis, "e-squared guard equation")
    require("BUCHBERGER_DONE basis=8 pairs=28" in transcript.getvalue(),
            "completed pair count")


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41S2E-1" in statement and "frontier falls from 36"
            in statement and "to 32" in statement, "claim")
    require("does not claim a raw unit" in statement
            and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s2_forced_colored_deployed_product_exclusion",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_common_sign_product_transport",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    replay(0)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S2_EF_PASS "
        "component=0 terms=7,7,7 pairs=28 guard=e^2 frontier=32"
    )


if __name__ == "__main__":
    main()
