#!/usr/bin/env python3
"""Verify the S0 product exclusion in deployed b row zero."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_"
    "nonloop_singleton_ab_s0_product_exclusion"
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
    for sign in (1, -1):
        for cell, terms, pairs, guard in (
            ("s0-forced-colored", 11, 29, None),
            ("s0-forced-ef", 12, 190, {(0, 2): 1}),
            ("s0-forced-internal", 14, 406, {(0, 1): 1}),
        ):
            equations = SOLVER.equations(row, cell, alpha_sign=sign)
            require(tuple(map(len, equations)) == (terms, terms, terms),
                    f"sparse profile {cell},{sign}")
            transcript = io.StringIO()
            with contextlib.redirect_stdout(transcript):
                basis, processed = SOLVER.buchberger(equations)
            require(processed == pairs, f"pair count {cell},{sign}")
            if guard is None:
                require(basis == [SOLVER.constant(1)],
                        f"raw unit {cell},{sign}")
                require(f"BUCHBERGER_UNIT pairs={pairs}" in transcript.getvalue(),
                        f"unit transcript {cell},{sign}")
            else:
                require(guard in basis, f"guard {cell},{sign}")
                require(
                    f"BUCHBERGER_DONE basis={len(basis)} pairs={pairs}"
                    in transcript.getvalue(),
                    f"guard transcript {cell},{sign}",
                )


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41BS0-1" in statement and "only" in statement, "claim")
    require("does not impose" in statement and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_s2_product_exclusion",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_ab_product_involution_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    replay(0)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_AB_S0_PASS "
        "row=0 cells=6 raw_units=2 guarded=4 frontier=0"
    )


if __name__ == "__main__":
    main()
