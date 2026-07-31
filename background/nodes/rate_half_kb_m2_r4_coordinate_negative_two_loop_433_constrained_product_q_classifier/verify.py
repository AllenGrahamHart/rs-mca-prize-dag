#!/usr/bin/env python3
"""Verify the constrained 433 product-q classifier."""

import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_constrained_product_q_classifier"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def minors(labels, products):
    rows = [[-p, -p*k, 1, k] for k, p in zip(labels, products)]
    return [sp.expand(sp.det(sp.Matrix([rows[i] for i in indices])))
            for indices in itertools.combinations(range(5), 4)]


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("P_8(M)" in statement and "at most 24" in statement, "claim")
    require("Res_c" in proof and "nonclaim" in contract, "certificate")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_product_q_weld",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_product_minor_cell_cut",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    m, ell, c = sp.symbols("m ell c")
    b = -c**3
    p8 = m**4 + 8*m**3 - 2*m**2 + 8*m + 1
    products = (-1, -c**2, b, -b, b*c)

    for name, labels, sign in (
        ("X2", (-m**2,m,1,m**2,-m), -1),
        ("N1", (-1,m,1,m**2,-m), 1),
    ):
        f = (c**2+1)*(m+1)**2 + sign*c*(m-1)**2
        values = minors(labels, products)
        ideal = sp.groebner((p8, f), c, m, order="lex")
        require(all(ideal.reduce(value)[1] == 0 for value in values), f"minor converse {name}")
        L, Z = labels[0], labels[4]
        q = sp.cancel((Z*(1-L)**2*(c**2+b)**2-c**2*(1+b)**2*(Z-L)**2)/(c**2*(c-1)**2))
        require(ideal.reduce(sp.expand(q))[1] == 0, f"q converse {name}")
        resultant = sp.factor(sp.resultant(f, sp.expand(q), c))
        expected = (m**2*(m**2+1)**4*p8**2 if name == "X2" else 16*m**2*p8**2)
        require(sp.expand(resultant-expected) == 0, f"resultant {name}")

    # L1 converse after stripping only protected factors.
    l1_labels = (ell,m,1,-1,-m)
    l1_minors = [sp.rem(value, m**2+1, m) for value in minors(l1_labels, products)]
    pc = 2*c**4 + 3*c**2 + 2
    locator = 3*ell - 4*c**3 - 2*c + m
    l1_ideal = sp.groebner((m**2+1, pc, locator), ell, c, m, order="lex")
    require(all(l1_ideal.reduce(value)[1] == 0 for value in l1_minors), "L1 minors")
    q_l1 = sp.rem(sp.expand((-m)*(1-ell)**2*(c**2+b)**2-c**2*(1+b)**2*(-m-ell)**2), m**2+1, m)
    require(l1_ideal.reduce(q_l1)[1] == 0, "L1 q")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_CONSTRAINED_PASS "
        "cells=X2,N1,L1 degrees=8,8,8 cap=24 resultants=exact"
    )


if __name__ == "__main__":
    main()
