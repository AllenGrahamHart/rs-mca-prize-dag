#!/usr/bin/env python3
"""Verify both forced-loop parities over cubic base component zero."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_loop_deployed_product_exclusion"
SOLVER_PATH = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_442_s1_loop_buchberger.py"
)
SPEC = importlib.util.spec_from_file_location("solver", SOLVER_PATH)
SOLVER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SOLVER)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def replay(component):
    for delta_sign, pair_count in ((-1, 57), (1, 55)):
        transcript = io.StringIO()
        with contextlib.redirect_stdout(transcript):
            equations, basis = SOLVER.solve(component, delta_sign)
        require(tuple(len(equation) for equation in equations)
                == (17, 17, 17), "sparse profiles")
        require(basis == [{(0, 0): SOLVER.EONE}], "unit ideal")
        require(f"LOOP_BUCHBERGER_UNIT pairs={pair_count}"
                in transcript.getvalue(), "pair count")


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41FL-3" in statement and "70" in statement, "claim")
    require("does not transport" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_ef_tau_minus_guarded_product_exclusion",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_mate_coordinate_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    replay(0)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S1_LOOP_PASS "
        "component=0 parities=2 terms=17 pairs=57,55 unit=True"
    )


if __name__ == "__main__":
    main()
