#!/usr/bin/env python3
"""Verify the one-loop 442 nonloop-singleton opposite-pair exclusion."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_opposite_pair_exclusion"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("entire matching orbit is empty" in statement and "cells"
            in statement, "claim")
    require("does not classify the other three" in statement
            and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    b, c, r, t, x = sp.symbols("b c r t x")
    i = sp.I
    denominator = x**2+2*b*x+1
    constant = b*(b*x**2+b+2*x)
    require(sp.factor(sp.resultant(denominator, constant/b, b))
            == -(x-1)**2*(x+1)**2, "denominator branch")

    labels = (1, r**2, -r**2, t**2, -1)
    products = (-b**2, b, -b, c, -c)
    rows = [sp.Matrix([[-p, -p*s, 1, s]])
            for p, s in zip(products, labels)]
    product_equation = sp.expand(
        sp.Matrix.vstack(rows[0], rows[1], rows[2], rows[4]).det()
    )
    expected_product = sp.expand(
        (r**4+2*b*r**2+1)*c-b*(b*r**4+b+2*r**2)
    )
    require(sp.expand(product_equation-2*b*expected_product) == 0,
            "product equation")
    c_value = b*(b*r**4+b+2*r**2)/(r**4+2*b*r**2+1)

    expected = {
        (1, 1): (2*i, (r-1)*(r-i)*(r**2-i)),
        (1, -1): (2*i, (r+1)*(r-i)*(r**2+i)),
        (-1, 1): (-2*i, (r+1)*(r+i)*(r**2-i)),
        (-1, -1): (-2*i, (r-1)*(r+i)*(r**2+i)),
    }
    for (epsilon_1, epsilon_2), (scalar, residual) in expected.items():
        q_values = (
            0,
            r*(1+b),
            epsilon_2*i*r*(1-b),
            t*(1+c),
            epsilon_1*i*(1-c),
        )
        differences = tuple(products[0]-value for value in products)
        left, right, third = 1, 2, 4
        weld = (
            q_values[left]*differences[right]*differences[third]
            *(labels[third]-labels[right])
            + q_values[right]*differences[left]*differences[third]
            *(labels[left]-labels[third])
            + q_values[third]*differences[left]*differences[right]
            *(labels[right]-labels[left])
        )
        numerator = sp.together(weld.subs(c, c_value)).as_numer_denom()[0]
        target = scalar*b**2*r**2*(b-1)**2*(b+1)**2*residual
        require(sp.simplify(sp.expand(numerator-target)) == 0,
                f"q factor {epsilon_1},{epsilon_2}")

        root_square = epsilon_2*i
        c_on_quadratic = (
            b*(b*root_square**2+b+2*root_square)
            /(root_square**2+2*b*root_square+1)
        )
        require(sp.simplify(c_on_quadratic-1) == 0,
                f"target collision {epsilon_1},{epsilon_2}")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_OPPOSITE_PASS "
        "cells=11,14 sign_classes=4 status=empty"
    )


if __name__ == "__main__":
    main()
