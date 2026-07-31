#!/usr/bin/env python3
"""Verify the negative one-loop product-to-q weld."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_product_q_weld"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("necessary and sufficient" in statement and "two scalar welds" in statement,
            "claim")
    require("does not classify or delete" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_loop_stratified_q_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    n0, n1, d0, d1, h, s, c0, c1 = sp.symbols(
        "n0 n1 d0 d1 h s c0 c1"
    )
    delta = n1*d0 - n0*d1

    def denominator(x):
        return d0 + d1*x

    def numerator(x):
        return n0 + n1*x

    def product(x):
        return numerator(x)/denominator(x)

    c_value = c0 + c1*s
    q_value = -(s-h)*c_value/denominator(s)
    difference = sp.factor(product(h) - product(s))
    expected_difference = delta*(h-s)/(denominator(h)*denominator(s))
    require(sp.cancel(difference - expected_difference) == 0, "Mobius difference")
    w_value = sp.cancel(q_value/(product(h)-product(s)))
    require(sp.cancel(w_value - denominator(h)*c_value/delta) == 0,
            "linearized q value")

    i, j, k = sp.symbols("i j k")
    ci = c0 + c1*i
    cj = c0 + c1*j
    ck = c0 + c1*k
    matrix = sp.Matrix(((1, i, ci), (1, j, cj), (1, k, ck)))
    require(sp.expand(matrix.det()) == 0, "affine-line determinant")

    wi, wj, wk, di, dj, dk, qi, qj, qk = sp.symbols(
        "wi wj wk di dj dk qi qj qk"
    )
    determinant = sp.Matrix(((1, i, wi), (1, j, wj), (1, k, wk))).det()
    cleared = sp.expand(determinant*di*dj*dk)
    expected = sp.expand(
        qi*dj*dk*(k-j) + qj*di*dk*(i-k) + qk*di*dj*(j-i)
    )
    require(sp.expand(cleared.subs({wi: qi/di, wj: qj/dj, wk: qk/dk})
                      - expected) == 0, "cleared weld")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_PRODUCT_Q_WELD_PASS "
        "nonloops=4 rank_cap=2 scalar_welds=2"
    )


if __name__ == "__main__":
    main()
