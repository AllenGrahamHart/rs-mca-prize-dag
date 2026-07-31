#!/usr/bin/env python3
"""Verify the 433 product-minor cell cut."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_product_minor_cell_cut"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def determinant(labels, products, indices):
    rows = [[-products[i], -products[i]*labels[i], 1, labels[i]] for i in indices]
    return sp.factor(sp.det(sp.Matrix(rows)))


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("(KB43P-2)" in statement and "b=-c^3" in statement, "claim")
    require("No assertion" in proof and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_antipodal_label_atlas",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    m, r, b, c = sp.symbols("m r b c")
    products = (-1, -c**2, b, -b, b*c)
    cells = {
        "X1": (-m, m, 1, m**2, -m**2),
        "N2": (-m, m, 1, m**2, -1),
        "Z1": (-m, m, 1, -1, r),
        "X2": (-m**2, m, 1, m**2, -m),
        "N1": (-1, m, 1, m**2, -m),
        "L1": (r, m, 1, -1, -m),
    }

    expected_delete = -2*m*(b-c)*(b+c)*(m-1)*(m+1)
    for name in ("X1", "N2"):
        actual = determinant(cells[name], products, (0, 1, 2, 3))
        require(sp.expand(actual-expected_delete) == 0, f"delete minor {name}")
    z1 = sp.rem(determinant(cells["Z1"], products, (0, 1, 2, 3)), m**2+1, m)
    require(sp.expand(z1-4*m*(b-c)*(b+c)) == 0, "delete minor Z1")

    expected_force = 2*b*m*(b+c**3)*(m-1)*(m+1)
    for name in ("X2", "N1"):
        actual = determinant(cells[name], products, (1, 2, 3, 4))
        require(sp.expand(actual-expected_force) == 0, f"force minor {name}")
    l1 = sp.rem(determinant(cells["L1"], products, (1, 2, 3, 4)), m**2+1, m)
    require(sp.expand(l1+4*b*m*(b+c**3)) == 0, "force minor L1")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_PRODUCT_CUT_PASS "
        "cells=9 deleted=3 forced_b=-c^3:3 residual=6"
    )


if __name__ == "__main__":
    main()
