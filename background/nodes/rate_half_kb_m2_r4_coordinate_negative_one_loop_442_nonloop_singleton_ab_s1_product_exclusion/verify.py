#!/usr/bin/env python3
"""Verify all S1 product cells in deployed b row zero."""

import contextlib
import importlib.util
import io
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_"
    "nonloop_singleton_ab_s1_product_exclusion"
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


def run_cell(row, cell, terms, pairs, **signs):
    equations = SOLVER.equations(row, cell, **signs)
    require(tuple(map(len, equations)) == (terms, terms, terms),
            f"sparse profile {cell},{signs}")
    transcript = io.StringIO()
    with contextlib.redirect_stdout(transcript):
        basis, processed = SOLVER.buchberger(equations)
    require(processed == pairs, f"pair count {cell},{signs}")
    return basis, transcript.getvalue()


def replay(row):
    b_value, _, mate = SOLVER.ROWS[row]
    theta = SOLVER.LOOP_ROOTS[row]
    require((theta*theta+mate) % SOLVER.P == 0, "loop square root")
    require((2*b_value*b_value+3*b_value+2) % SOLVER.P == 0, "b row")

    for sign in (1, -1):
        basis, transcript = run_cell(
            row, "forced-de", 25, 79, alpha_sign=sign
        )
        require(basis == [SOLVER.constant(1)]
                and "BUCHBERGER_UNIT pairs=79" in transcript,
                f"forced internal {sign}")

        basis, transcript = run_cell(
            row, "forced-ce", 23, 56, delta_sign=sign
        )
        require(basis == [SOLVER.constant(1)]
                and "BUCHBERGER_UNIT pairs=56" in transcript,
                f"forced colored {sign}")

    for delta_sign, ef_sign in itertools.product((1, -1), repeat=2):
        terms = 17 if delta_sign == 1 else 19
        basis, transcript = run_cell(
            row, "forced-ef", terms, 435,
            delta_sign=delta_sign, ef_sign=ef_sign,
        )
        require({(0, 1): 1} in basis,
                f"forced EF guard {delta_sign},{ef_sign}")
        require("BUCHBERGER_DONE basis=30 pairs=435" in transcript,
                f"forced EF transcript {delta_sign},{ef_sign}")

    for delta_sign, pairs in ((1, 55), (-1, 57)):
        basis, transcript = run_cell(
            row, "s1-forced-loop", 17, pairs, delta_sign=delta_sign
        )
        require(basis == [SOLVER.constant(1)]
                and f"BUCHBERGER_UNIT pairs={pairs}" in transcript,
                f"forced loop {delta_sign}")


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41BS1-2" in statement and "6+10+4=20" in statement, "claim")
    require("does not classify" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_s0_product_exclusion",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_product_involution_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    replay(0)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_AB_S1_PASS "
        "row=0 cells=10 raw_units=6 guarded=4 product_frontier=0"
    )


if __name__ == "__main__":
    main()
