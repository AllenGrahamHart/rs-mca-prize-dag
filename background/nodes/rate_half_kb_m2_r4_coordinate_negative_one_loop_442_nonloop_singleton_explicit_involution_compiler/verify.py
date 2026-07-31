#!/usr/bin/env python3
"""Verify the explicit involution compiler for the finite common orbit."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_explicit_involution_compiler"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("KB41I-4" in statement and "Phi(Y,Z)" in statement, "claim")
    require("does not enumerate" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_degree12_gate",
        "rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_edge_skeleton_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    b, c, y, z = sp.symbols("b c y z")
    row_1 = sp.Matrix([-b**3, b**2-b, -1])
    row_2 = sp.Matrix([b*c, b+c, -1])
    coefficients = row_1.cross(row_2)
    gamma = c+2*b-b**2
    alpha = -b*(c+b**2)
    beta = b**2*(c-b**2-2*b*c)
    require(all(sp.expand(left-right) == 0 for left, right in zip(
        coefficients, (gamma, alpha, beta)
    )), "cross product")

    phi = gamma*y*z-alpha*(y+z)-beta
    require(sp.expand(phi.subs({y: -b**2, z: b})) == 0,
            "first common pair")
    require(sp.expand(phi.subs({y: -b, z: -c})) == 0,
            "second common pair")
    determinant = sp.factor(alpha**2+gamma*beta)
    require(determinant == 2*b**2*(b-1)*(b+c)*(b**2-c),
            "nonsingularity")

    mate = sp.factor((alpha*c+beta)/(gamma*c-alpha))
    expected_mate = (
        -b*(b**3+3*b**2*c-b*c+c**2)
        /(b**3-b**2*c+3*b*c+c**2)
    )
    require(sp.simplify(mate-expected_mate) == 0, "forced mate")
    require(sp.simplify(phi.subs({y: c, z: mate})) == 0,
            "mate involution equation")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_INVOLUTION_PASS "
        "common_pairs=2 forced_mate=1 outside_pairs=3"
    )


if __name__ == "__main__":
    main()
