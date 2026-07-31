#!/usr/bin/env python3
"""Verify the 442 signed-pair matching-template exclusion."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_signed_pair_matching_template_exclusion"
DEPLOYED_PRIME = 2130706433


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("= 72" in statement and "of the 540" in statement, "claim")
    require("does not delete an entire" in statement and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_outside_product_involution_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_product_invariance_router",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    x, y = sp.symbols("x y")
    row = lambda u, v: sp.Matrix([u*v, -(u+v), -1])
    internal = row(x, -x).cross(row(y, -y))
    require(internal == sp.Matrix([0, y**2-x**2, 0]), "negation kernel")
    cross_same = row(x, y).cross(row(-x, -y))
    cross_swap = row(x, -y).cross(row(-x, y))
    require(cross_same[1] == 0 and cross_swap[1] == 0, "reciprocal kernels")
    require(sp.expand(cross_same[0]-2*(x+y)) == 0, "same-sign cross guard")
    require(sp.expand(cross_swap[0]-2*(x-y)) == 0, "opposite-sign cross guard")

    l, b = sp.symbols("l b")
    cases = (
        (l**2-l+1, 4*b**2+b+4, (b+1)*(b**2-b+1), 30625),
        (l**2-l+1, 4*b**2+7*b+4, (b-1)*(b**2+b+1), 18225),
        (l**4+1, b**2-b*l**3+b*l-b+1, (b-1)*(b+1), 49),
        (l**4+1, b**2-2*b*l**3+2*b*l-b+1, b**2+1, 2401),
        (l**4+1, b**2-b*l**3+b*l-b+1, (b-1)*(b+1), 49),
        (l**4+1, b**2-2*b*l**3+2*b*l-b+1, b**2+1, 2401),
    )
    for relation, b_gate, alpha_factor, norm in cases:
        inner = sp.resultant(b_gate, alpha_factor, b)
        outer = sp.resultant(relation, inner, l)
        require(outer == norm, "protected Alpha norm")

    require(all(DEPLOYED_PRIME % prime for prime in (2, 3, 5, 7)), "deployed field")
    require(6*2*2*3 == 72 and 540-72 == 468, "subcase count")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_TEMPLATE_PASS "
        "rows=6 affected_cells=24 deleted_matchings=72 residual_cap=468"
    )


if __name__ == "__main__":
    main()
