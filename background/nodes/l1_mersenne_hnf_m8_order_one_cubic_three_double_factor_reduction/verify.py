#!/usr/bin/env python3
"""Check the cubic three-double factor formulas and DAG wiring."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_double_factor_reduction"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_color_remainder_router"
CONSUMER = "l1_mixed_petal_amplification"


def multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def fiber(U: Fraction, V: Fraction, u: Fraction) -> tuple[list[Fraction], Fraction, Fraction]:
    y = u - U
    v = u * u - U * u + V
    factor = [v, u, Fraction(1)]
    cubic = multiply(factor, [-y, Fraction(1)])
    assert cubic[3] == 1
    assert cubic[2] == U
    assert cubic[1] == V
    return factor, y, -cubic[0]


def main() -> None:
    U, V, w = Fraction(5), Fraction(-2), Fraction(7)
    colors: list[Fraction] = []
    factors: list[list[Fraction]] = []
    for u in (Fraction(1), Fraction(3), Fraction(8)):
        factor, _, offset = fiber(U, V, u)
        factors.append(factor)
        colors.append(w + offset)

    product = multiply(multiply(factors[0], factors[1]), factors[2])
    assert len(product) == 7 and product[-1] == 1
    assert len(set(colors)) == 3
    assert (colors[1] - colors[0]) / (colors[2] - colors[0]) == Fraction(-4, 21)

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
    for anchor in ("(TDF2)", "(TDF3)", "(TDF4)"):
        assert anchor in statement
    for anchor in ("u_i-y_i=U", "v_i-u_i y_i=V", "-v_i y_i=w-a_i"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_DOUBLE_FACTOR_REDUCTION_PASS")


if __name__ == "__main__":
    main()
