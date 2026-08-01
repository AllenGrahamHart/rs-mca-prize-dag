#!/usr/bin/env python3
"""Verify both final S0 parity guards in cubic component zero."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s0_forced_internal_guarded_product_exclusion"
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
    for tau_0 in (1, -1):
        transcript = io.StringIO()
        with contextlib.redirect_stdout(transcript):
            equations, basis = SOLVER.solve_component(
                component, alpha_sign=tau_0, cell="s0-forced-internal"
            )
        require(tuple(len(equation) for equation in equations) == (14, 14, 14),
                f"sparse profiles {tau_0}")
        require({(0, 1): SOLVER.ONE} in basis, f"f guard {tau_0}")
        require("BUCHBERGER_DONE basis=29 pairs=406" in transcript.getvalue(),
                f"pair count {tau_0}")


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41S0I-1" in statement and "all eighty" in statement
            and "from 8 to 0" in statement, "claim")
    require("does not classify" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s0_forced_ef_guarded_product_exclusion",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_common_sign_product_transport",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    replay(0)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S0_INTERNAL_PASS "
        "component=0 parities=2 terms=14 pairs=406 guard=f frontier=0"
    )


if __name__ == "__main__":
    main()
