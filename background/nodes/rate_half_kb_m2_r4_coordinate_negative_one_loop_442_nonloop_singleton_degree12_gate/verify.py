#!/usr/bin/env python3
"""Verify the one-loop 442 nonloop-singleton degree-12 gate."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_degree12_gate"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("G(B)=" in statement and "3*12*2=72" in statement, "claim")
    require("does not assert" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    parent = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_cubic_root_gate"
    require((parent, NODE_ID, "req") in edges, "dependency")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    b, c, r, t = sp.symbols("b c r t")
    i = sp.I
    x = r**2
    a_poly = x**2-6*x+1
    b_poly = (x+1)**2
    c_value = b*(b*a_poly+b_poly)/(b*b_poly+a_poly)
    labels = (1, -1, x, t**2, -x)
    products = (-b**2, b, -b, c, -c)
    rows = [sp.Matrix([[-p, -p*s, 1, s]])
            for p, s in zip(products, labels)]
    product = sp.Matrix.vstack(rows[0], rows[1], rows[2], rows[3]).det()
    product_numerator = sp.together(
        product.subs(c, c_value)
    ).as_numer_denom()[0]
    differences = tuple(products[0]-value for value in products)

    gate = (
        (b**3-b**2-b-1)*(b**3+b**2+b-1)
        *(b**6-2*b**5+7*b**4-8*b**3+7*b**2-2*b+1)
    )
    guarded_factor = -2**56*b**24*(b-1)**12*(b+1)**12

    for epsilon_1 in (1, -1):
        for epsilon_2 in (1, -1):
            roots = (1, epsilon_1*i, r, t, epsilon_2*i*r)
            q_values = tuple(root*edge_sum for root, edge_sum in zip(
                roots, (0, 1+b, 1-b, 1+c, 1-c)
            ))
            left, right, third = 1, 2, 3
            weld = (
                q_values[left]*differences[right]*differences[third]
                *(labels[third]-labels[right])
                + q_values[right]*differences[left]*differences[third]
                *(labels[left]-labels[third])
                + q_values[third]*differences[left]*differences[right]
                *(labels[right]-labels[left])
            )
            weld_numerator = sp.together(
                weld.subs(c, c_value)
            ).as_numer_denom()[0]
            singleton_resultant = sp.resultant(
                product_numerator, weld_numerator, t
            )
            cubic = (
                r**3+(2*epsilon_1*epsilon_2+epsilon_1*i)*r**2
                +(-1-2*epsilon_2*i)*r-epsilon_1*i
            )
            double_resultant = sp.resultant(cubic, singleton_resultant, r)
            require(sp.expand(double_resultant-guarded_factor*gate) == 0,
                    f"double resultant {epsilon_1},{epsilon_2}")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_DEGREE12_PASS "
        "sign_rows=4 b_degree=12 raw_common_bound=72"
    )


if __name__ == "__main__":
    main()
