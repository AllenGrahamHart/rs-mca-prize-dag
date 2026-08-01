#!/usr/bin/env python3
"""Verify the S2 product exclusion in deployed b row zero."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_"
    "nonloop_singleton_ab_s2_product_exclusion"
)
SOLVER_PATH = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_442_cell36_outside_buchberger.py"
)
SPEC = importlib.util.spec_from_file_location("solver", SOLVER_PATH)
SOLVER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SOLVER)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def replay(row):
    results = {}
    for cell in (
        "s2-forced-colored", "s2-forced-loop",
        "s2-forced-df", "s2-forced-ef",
    ):
        equations = SOLVER.equations(row, cell)
        require(tuple(map(len, equations)) == (7, 7, 7),
                f"sparse profile {cell}")
        transcript = io.StringIO()
        with contextlib.redirect_stdout(transcript):
            basis, pairs = SOLVER.buchberger(equations)
        results[cell] = (basis, pairs, transcript.getvalue())

    for cell in ("s2-forced-colored", "s2-forced-loop"):
        basis, pairs, transcript = results[cell]
        require(basis == [SOLVER.constant(1)] and pairs == 7,
                f"raw unit {cell}")
        require("BUCHBERGER_UNIT pairs=7" in transcript,
                f"unit transcript {cell}")

    basis, pairs, transcript = results["s2-forced-df"]
    require(pairs == 28 and {(2, 0): 1} in basis and {(0, 2): 1} in basis,
            "forced DF guards")
    require("BUCHBERGER_DONE basis=8 pairs=28" in transcript,
            "forced DF transcript")

    basis, pairs, transcript = results["s2-forced-ef"]
    require(pairs == 28 and {(0, 2): 1} in basis,
            "forced EF guard")
    require("BUCHBERGER_DONE basis=8 pairs=28" in transcript,
            "forced EF transcript")


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41BS2-1" in statement and "every" in statement, "claim")
    require("does not classify" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_product_involution_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    replay(0)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_AB_S2_PASS "
        "row=0 cells=4 raw_units=2 guarded=2 frontier=0"
    )


if __name__ == "__main__":
    main()
