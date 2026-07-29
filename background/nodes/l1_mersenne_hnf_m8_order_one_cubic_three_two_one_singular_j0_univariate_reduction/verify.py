#!/usr/bin/env python3
"""Check the singular-J0 univariate substitution identities."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_singular_j0_univariate_reduction"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_coefficient_matrix_router"
CONSUMER = "l1_mixed_petal_amplification"


def a_poly(q: F) -> F:
    return q**2 + 132 * q + 2916


def b_poly(q: F) -> F:
    return q**3 + 126 * q**2 + 5364 * q + 87480


def p_w(q: F) -> F:
    a = a_poly(q)
    return a**2 * b_poly(q) + 72576 * q**2 * a - 1492992 * q**3


def p_c(q: F) -> F:
    a = a_poly(q)
    t = -144 * q
    return (
        35 * q**2 * a**4
        + 14 * q * (11 * t**2 * a**2 + 27 * t * a**3 + 27 * a**4)
        + 120 * (t**4 + 4 * t**3 * a + 7 * t**2 * a**2 + 6 * t * a**3 + 3 * a**4)
    )


def main() -> None:
    for q in (F(1), F(5), F(-7), F(11, 3)):
        a = a_poly(q)
        assert a != 0
        t = -144 * q
        d = t / a
        fw = b_poly(q) - 504 * d * q - 72 * d**2 * q
        conic = (
            35 * q**2
            + 14 * q * (11 * d**2 + 27 * d + 27)
            + 120 * (d**4 + 4 * d**3 + 7 * d**2 + 6 * d + 3)
        )
        assert d * a + 144 * q == 0
        assert p_w(q) == a**2 * fw
        assert p_c(q) == a**4 * conic

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(JUR1)", "(JUR2)", "(JUR3)", "(JUR4)", "(JUR7)"):
        assert anchor in statement
    for anchor in ("A^2F_W", "A^4 C(q,T/A)", "degree-seven", "degree-ten"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_SINGULAR_J0_UNIVARIATE_REDUCTION_PASS")


if __name__ == "__main__":
    main()
