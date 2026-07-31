#!/usr/bin/env python3
"""Verify the one-loop 442 nonloop-singleton cubic-root gate."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_cubic_root_gate"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("P_(e1,e2)" in statement and "KB41C-4" in statement, "claim")
    require("orbit is not deleted" in statement and "nonclaim" in contract,
            "scope")

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
    a_poly = x**2-6*x+1
    b_poly = (x+1)**2
    require(sp.factor(a_poly**2-b_poly**2) == -16*x*(x-1)**2,
            "denominator branch")

    labels = (1, -1, r**2, t**2, -r**2)
    products = (-b**2, b, -b, c, -c)
    rows = [sp.Matrix([[-p, -p*s, 1, s]])
            for p, s in zip(products, labels)]
    product_equation = sp.expand(
        sp.Matrix.vstack(rows[0], rows[1], rows[2], rows[4]).det()
    )
    x_value = r**2
    a_value = a_poly.subs(x, x_value)
    b_value = b_poly.subs(x, x_value)
    expected_product = b*(b**2*a_value+b*b_value-c*(b*b_value+a_value))
    require(sp.expand(product_equation-expected_product) == 0,
            "product equation")
    c_value = b*(b*a_value+b_value)/(b*b_value+a_value)

    expected = {
        (1, 1): (-1-i, (r-1)*(r-i)*(r+i)),
        (1, -1): (-1+i, (r+1)*(r-i)*(r+i)),
        (-1, 1): (-1-i, (r+1)*(r-i)*(r+i)),
        (-1, -1): (-1+i, (r-1)*(r-i)*(r+i)),
    }
    for (epsilon_1, epsilon_2), (scalar, label_factors) in expected.items():
        roots = (1, epsilon_1*i, r, t, epsilon_2*i*r)
        q_values = tuple(root*edge_sum for root, edge_sum in zip(
            roots, (0, 1+b, 1-b, 1+c, 1-c)
        ))
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
        cubic = (
            r**3+(2*epsilon_1*epsilon_2+epsilon_1*i)*r**2
            +(-1-2*epsilon_2*i)*r-epsilon_1*i
        )
        target = scalar*b**2*r*(b-1)**2*(b+1)**2*label_factors*cubic
        require(sp.simplify(sp.expand(numerator-target)) == 0,
                f"q factor {epsilon_1},{epsilon_2}")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_CUBIC_PASS "
        "cells=9,10,12,13 sign_rows=4 degree=3"
    )


if __name__ == "__main__":
    main()
