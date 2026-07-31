#!/usr/bin/env python3
"""Verify the forced-colored S2 exclusion in cubic component zero."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s2_forced_colored_deployed_product_exclusion"
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
        equations, basis = SOLVER.solve_component(
            component, cell="s2-forced-colored"
        )
    require(tuple(len(equation) for equation in equations) == (7, 7, 7),
            "sparse profiles")
    require(basis == [{(0, 0): SOLVER.ONE}], "unit ideal")
    require("BUCHBERGER_UNIT pairs=7" in transcript.getvalue(), "pair count")


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41S2C-1" in statement and "40 to 36" in statement, "claim")
    require("does not delete" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_common_sign_product_transport",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_invariance_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    replay(0)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S2_COLORED_PASS "
        "component=0 terms=7,7,7 pairs=7 unit=True frontier=36"
    )


if __name__ == "__main__":
    main()
