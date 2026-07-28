#!/usr/bin/env python3
"""Check the coefficient ledger in the quadratic composition identity."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_quadratic_pointwise_composition"
DEPENDENCY = "l1_mersenne_hnf_order_one_frobenius_gate"
CONSUMER = "l1_mixed_petal_amplification"


def mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def add(*polys: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(poly) for poly in polys)
    for poly in polys:
        for index, value in enumerate(poly):
            out[index] += value
    return out


def main() -> None:
    # Independent coefficient expansion at generic rational sample values.
    A, B, C = Fraction(2), Fraction(3), Fraction(5)
    Ap, Bp, Cp = Fraction(7), Fraction(11), Fraction(13)
    E = [C, B, A]
    E2 = mul(E, E)
    E3 = mul(E2, E)
    J = add(
        [Ap * value for value in E3],
        [Fraction(0)] + [Bp * value for value in E2],
        [Fraction(0), Fraction(0)] + [Cp * value for value in E],
        [Fraction(0), Fraction(0), Fraction(-1)],
    )
    T = 3 * B + Bp / Ap
    leader = Ap * A**3
    assert J[6] == leader
    assert J[5] / leader == T / A
    assert J[0] / leader == (C / A) ** 3
    assert (J[1] / leader) / (J[0] / leader) == T / C

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(QPC2)", "(QPC3)", "(QPC4)"):
        assert anchor in statement
    for anchor in ("degree six", "T!=0", "d^(-6)g(1)"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_QUADRATIC_POINTWISE_COMPOSITION_PASS coefficients=4")


if __name__ == "__main__":
    main()
