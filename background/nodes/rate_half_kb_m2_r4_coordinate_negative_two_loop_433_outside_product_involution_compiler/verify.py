#!/usr/bin/env python3
"""Verify the 433 outside-product involution compiler."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_outside_product_involution_compiler"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("2^32" in statement and "xi=-M" in statement, "claim")
    require("cross product" in proof and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_m2_m3_product_q_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate",
        "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    m, b, c = sp.symbols("m b c")
    p6 = m**6 + 2*m**5 + 7*m**4 - 4*m**3 + 7*m**2 + 2*m + 1
    a_poly = 2*m**5 + 3*m**4 + 12*m**3 - 14*m**2 + 18*m + 3
    d_poly = 2*m**5 + 5*m**4 + 16*m**3 - 2*m**2 + 6*m + 5
    e_poly = a_poly - 8

    for epsilon in (-1, 1):
        cell = "M2" if epsilon == -1 else "M3"
        pairs = ((b, -1), (-b, b*c)) if epsilon == -1 else ((b, b*c), (-b, -1))
        pair_rows = [sp.Matrix([y*z, -(y+z), -1]) for y, z in pairs]
        cross = pair_rows[0].cross(pair_rows[1])
        gamma = 2*b + epsilon*(b*c+1)
        alpha = b*(b*c-1)
        beta = epsilon*b**2*(b*c+2*epsilon*c+1)
        expected = sp.Matrix([gamma, alpha, beta])
        require(all(sp.expand(x-y) == 0 for x, y in zip(cross, expected)),
                f"{cell} cross product")
        determinant = sp.factor(alpha**2+gamma*beta)
        expected_det = 2*b**2*(b+epsilon)*(c+epsilon)*(b*c+1)
        require(sp.expand(determinant-expected_det) == 0, f"{cell} determinant")
        require(all(sp.expand(row.dot(expected)) == 0 for row in pair_rows),
                f"{cell} known pairs")

        if epsilon == -1:
            vector = (
                3*b*m**2+b-m**2+1,
                -b*m**2-3*b-m**2+1,
                b*(b*m**2-b-3*m**2-1),
                b*(b*m**2-b+m**2+3),
            )
        else:
            vector = (
                m**2*(b*m**2+3*b-m**2+1),
                -3*b*m**2-b-m**2+1,
                b*m**2*(b*m**2-b-m**2-3),
                b*(b*m**2-b+3*m**2+1),
            )
        d0, d1, n0, n1 = vector
        f_num = sp.expand(n0-m*n1)
        f_den = sp.expand(d0-m*d1)
        numerator = epsilon*b*(b*(m-1)**2-epsilon*(m+1)**2)
        denominator = b*(m+1)**2-epsilon*(m-1)**2
        require(sp.expand(f_num*denominator-numerator*f_den) == 0,
                f"{cell} forced mate")

        b_poly = 4*b**2 + epsilon*a_poly*b + 4
        for protected in (denominator, numerator/(epsilon*b)):
            inner = sp.resultant(b_poly, sp.expand(protected), b)
            outer = sp.resultant(p6, inner, m)
            require(outer == 2**32, f"{cell} resultant")

        c_poly = 8*c + b*d_poly + epsilon*e_poly
        classifier = sp.groebner((p6, b_poly, c_poly), c, b, m, order="lex")
        y = -c**2
        involution_mate = sp.expand(
            gamma*y*numerator-alpha*(y*denominator+numerator)-beta*denominator
        )
        require(classifier.reduce(involution_mate)[1] == 0,
                f"{cell} singleton involution")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_OUTSIDE_PASS "
        "cells=M2,M3 mate=xi=-M resultants=2^32 residual_pairs=3"
    )


if __name__ == "__main__":
    main()
