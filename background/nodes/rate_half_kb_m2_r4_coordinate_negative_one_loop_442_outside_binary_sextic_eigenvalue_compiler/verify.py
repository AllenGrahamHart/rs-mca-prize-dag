#!/usr/bin/env python3
"""Verify the binary-sextic eigenvalue and coefficient compiler."""

import json
import math
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_eigenvalue_compiler"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41EV-2" in statement and "rank three" in statement, "claim")
    require("does not evaluate" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_binary_sextic_invariance_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_explicit_involution_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    x, z = sp.symbols("X Z")
    alpha, beta, gamma = sp.symbols("Alpha Beta Gamma")
    coefficients = sp.symbols("h0:7")
    delta = alpha**2+beta*gamma
    form = sum(coefficients[j]*x**(6-j)*z**j for j in range(7))
    transformed = sp.Poly(sp.expand(form.subs(
        {x: alpha*x+beta*z, z: gamma*x-alpha*z}, simultaneous=True
    )), x, z)

    compiled = []
    for ell in range(7):
        value = 0
        for j in range(7):
            lower = max(0, ell-j)
            upper = min(ell, 6-j)
            for p in range(lower, upper+1):
                value += (
                    coefficients[j]
                    * math.comb(6-j, p)*math.comb(j, ell-p)
                    * alpha**(6-j-p)*beta**p
                    * gamma**(j-ell+p)*(-alpha)**(ell-p)
                )
        compiled.append(sp.expand(value))
        require(sp.expand(value-transformed.coeff_monomial(
            x**(6-ell)*z**ell
        )) == 0, f"coefficient {ell}")

    action = sp.zeros(7)
    for row, expression in enumerate(compiled):
        for column, coefficient in enumerate(coefficients):
            action[row, column] = sp.expand(expression.coeff(coefficient))
    square_error = action*action-delta**6*sp.eye(7)
    require(all(sp.expand(entry) == 0 for entry in square_error),
            "action square")

    specialized = action.subs({alpha: 1, beta: 1, gamma: 1})
    require((specialized-8*sp.eye(7)).rank() == 3, "plus rank")
    require((specialized+8*sp.eye(7)).rank() == 4, "minus rank")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_EIGEN_PASS "
        "eigenvalue=Delta^3 coefficient_equations=7 rank=3 cells=80"
    )


if __name__ == "__main__":
    main()
