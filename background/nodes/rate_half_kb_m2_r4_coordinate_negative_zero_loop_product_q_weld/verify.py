#!/usr/bin/env python3
"""Verify the negative zero-loop product-to-q weld."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_zero_loop_product_q_weld"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("necessary" in statement and "sufficient" in statement and
            "two `4 x 4`" in statement,
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

    s = sp.symbols("s0:5")
    c0, c1, c2 = sp.symbols("c0 c1 c2")
    rows = [sp.Matrix([[1, value, value**2,
                        -(c0+c1*value+c2*value**2)]]) for value in s]
    for fourth in (3, 4):
        matrix = sp.Matrix.vstack(rows[0], rows[1], rows[2], rows[fourth])
        require(sp.expand(matrix.det()) == 0, f"quadratic determinant {fourth}")

    # The first three Vandermonde rows have rank three for distinct labels.
    vandermonde = sp.Matrix([[1, s[index], s[index]**2] for index in range(3)])
    expected_vandermonde = -(s[0]-s[1])*(s[0]-s[2])*(s[1]-s[2])
    require(sp.expand(vandermonde.det()-expected_vandermonde) == 0,
            "Vandermonde anchors")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ZERO_LOOP_PRODUCT_Q_WELD_PASS "
        "labels=5 rank_cap=3 scalar_welds=2"
    )


if __name__ == "__main__":
    main()
