#!/usr/bin/env python3
"""Verify the first cubic component of the deployed S1 cell exclusion."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_de_deployed_product_exclusion"
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


def factor_audit():
    b = sp.symbols("b")
    sextic = b**6-2*b**5+7*b**4-8*b**3+7*b**2-2*b+1
    factors = tuple(
        b**3+modulus[2]*b**2+modulus[1]*b+modulus[0]
        for modulus in SOLVER.CUBICS
    )
    require(sp.Poly(sextic-factors[0]*factors[1], b,
                    modulus=SOLVER.P).is_zero, "cubic product")
    require(all(sp.Poly(factor, b, modulus=SOLVER.P).is_irreducible
                for factor in factors), "cubic irreducibility")


def solve_quietly(component):
    transcript = io.StringIO()
    with contextlib.redirect_stdout(transcript):
        equations, basis = SOLVER.solve_component(component)
    require(tuple(len(equation) for equation in equations) == (25, 25, 25),
            "sparse profiles")
    require(basis == [{(0, 0): SOLVER.ONE}], "unit ideal")
    require("BUCHBERGER_UNIT pairs=79" in transcript.getvalue(), "pair count")


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41DX-2" in statement and "79 S-pairs" in statement, "claim")
    require("does not delete another" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_quotient_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_mate_coordinate_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_uniform_row_selector",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    factor_audit()
    solve_quietly(0)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S1_DE_PASS "
        "component=0 terms=25,25,25 pairs=79 unit=True"
    )


if __name__ == "__main__":
    main()
