#!/usr/bin/env python3
"""Verify the 442 outside-product involution compiler."""

import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_outside_product_involution_compiler"
DEPLOYED_PRIME = 2130706433


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("(KB44O-4)" in statement and "8464" in statement, "claim")
    require("every `4 x 4`" in proof and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_exceptional_product_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_q_orientation_lift",
        "rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate",
        "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_edge_skeleton_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    l, b, c = sp.symbols("l b c")
    cases = {
        ("H6", -1): ((l, -l**2, 1, -l, l**2), l**2-l+1,
                      4*b**2+b+4, 3*c+2*b-2, -1, 49),
        ("H6", 1): ((l, -l**2, 1, -l, l**2), l**2-l+1,
                     4*b**2+7*b+4, c-2*b-2, -1, 1),
        ("H8L", -1): ((l, -l**2, 1, -1, l**2), l**4+1,
                       b**2-b*l**3+b*l-b+1,
                       c-(b-2)*(l**3-l+1), -l, 784),
        ("H8L", 1): ((l, -l**2, 1, -1, l**2), l**4+1,
                      b**2-2*b*l**3+2*b*l-b+1,
                      c+b*l**3-b*l-b-2, -l, 8464),
        ("H8M", -1): ((-l**2, l, 1, l**2, -1), l**4+1,
                       b**2-b*l**3+b*l-b+1,
                       c-(2*b-1)*(l**3-l+1), -l, 784),
        ("H8M", 1): ((-l**2, l, 1, l**2, -1), l**4+1,
                      b**2-2*b*l**3+2*b*l-b+1,
                      c-2*b+l**3-l-1, -l, 8464),
    }

    for (name, tau), (labels, relation, b_gate, c_gate, xi, norm) in cases.items():
        products = (-1, -b**2, b, c, tau*b*c)
        if name == "H6":
            pairs = ((-1, c), (-b**2, tau*b*c))
            singleton = b
            numerator = b*(b*l**2+b-l**2+2*l-1)
            denominator = b*l**2-2*b*l+b-l**2-1
        elif name == "H8L":
            pairs = ((b, c), (-b**2, tau*b*c))
            singleton = -1
            numerator = b*(2*b*l**2+2*b-l**2+2*l-1)
            denominator = b*l**2-2*b*l+b-2*l**2-2
        else:
            pairs = ((b, tau*b*c), (c, -1))
            singleton = -b**2
            numerator = b*(b*l**2-2*b*l+b-2*l**2-2)
            denominator = 2*b*l**2+2*b-l**2+2*l-1

        pair_rows = [sp.Matrix([y*z, -(y+z), -1]) for y, z in pairs]
        gamma, alpha, beta = pair_rows[0].cross(pair_rows[1])
        require(all(sp.expand(row.dot(sp.Matrix([gamma, alpha, beta]))) == 0
                    for row in pair_rows), f"{name}/{tau} cross product")
        require(sp.expand(alpha**2+gamma*beta) != 0, f"{name}/{tau} symbolic determinant")

        common_rows = [sp.Matrix([[-p, -p*k, 1, k]]) for k, p in zip(labels, products)]
        candidate = sp.Matrix([[-numerator, -numerator*xi,
                                denominator, denominator*xi]])
        ideal = sp.groebner((relation, b_gate, c_gate), c, b, l, order="lex")
        for indices in itertools.combinations(range(5), 3):
            matrix = sp.Matrix.vstack(*(common_rows[index] for index in indices), candidate)
            require(ideal.reduce(sp.expand(matrix.det()))[1] == 0,
                    f"{name}/{tau} candidate minor {indices}")

        involution_row = sp.expand(
            gamma*singleton*numerator
            - alpha*(singleton*denominator+numerator)
            - beta*denominator
        )
        require(ideal.reduce(involution_row)[1] == 0, f"{name}/{tau} singleton pair")

        for factor in (sp.cancel(numerator/b), denominator):
            inner = sp.resultant(b_gate, factor, b)
            outer = sp.resultant(relation, inner, l)
            require(outer == norm, f"{name}/{tau} protected norm")

    require(all(DEPLOYED_PRIME % prime for prime in (2, 7, 23)), "deployed characteristic")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_OUTSIDE_PASS "
        "rows=6 candidate_minors=60 protected_norms=12 residual_pairs=3 "
        "excluded_characteristics=2,7,23"
    )


if __name__ == "__main__":
    main()
