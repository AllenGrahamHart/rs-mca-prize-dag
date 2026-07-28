#!/usr/bin/env python3
"""Check the h=7 quadratic HNF intersection polynomial."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_quadratic_hnf_intersection"
DEPENDENCIES = {
    "l1_mersenne_hnf_m8_order_one_quadratic_pointwise_composition",
    "l1_mersenne_hnf_m8_order_one_conic_reduction",
}
CONSUMER = "l1_mixed_petal_amplification"


def add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return out


def scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return [scalar * value for value in poly]


def mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def sub(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return add(left, scale(right, Fraction(-1)))


def q(index: int) -> list[Fraction]:
    """Return ((1+d)^(index-1)-1)/index in ascending d-degree."""
    return [Fraction(0)] + [
        Fraction(comb(index - 1, degree), index)
        for degree in range(1, index)
    ]


def main() -> None:
    q2, q3, q4, q5, q6 = (q(index) for index in range(2, 7))
    s1 = add(add(add(add(q2, q3), q4), q5), q6)
    s2 = add(scale(mul(add(q2, q3), add(q2, q3)), Fraction(1, 2)), mul(q2, q4))
    assert s1 == [
        0,
        Fraction(213, 60),
        Fraction(237, 60),
        Fraction(163, 60),
        Fraction(62, 60),
        Fraction(10, 60),
    ]
    assert s2 == [0, 0, Fraction(76, 72), Fraction(55, 72), Fraction(13, 72)]

    # After subtracting (1-r)^3 and dividing by r, the coefficients of
    # r^2, r, 1 are 1+d^3/48, S_2-3, S_1+3.
    a0 = scale(add([1], [0, 0, 0, Fraction(1, 48)]), 720)
    b0 = scale(sub(s2, [3]), 720)
    c0 = scale(add(s1, [3]), 720)
    assert a0 == [720, 0, 0, 15]
    assert b0 == [-2160, 0, 760, 550, 130]
    assert c0 == [2160, 2556, 2844, 1956, 744, 120]

    a1 = [0, 0, 35]
    b1 = [0, 378, 378, 154]
    c1 = [360, 720, 840, 480, 120]
    first_minor = sub(mul(a0, c1), mul(c0, a1))
    second_minor = sub(mul(a0, b1), mul(b0, a1))
    third_minor = sub(mul(b0, c1), mul(c0, b1))
    resultant = sub(mul(first_minor, first_minor), mul(second_minor, third_minor))
    assert len(resultant) - 1 == 14
    assert resultant[-1] == -691200

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    for dependency in DEPENDENCIES:
        assert statuses[dependency] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert statuses[CONSUMER] == "TARGET"
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(QHI3)", "(QHI4)", "(QHI5)"):
        assert anchor in statement
    for anchor in ("S_1", "S_2", "-691200"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_QUADRATIC_HNF_INTERSECTION_PASS degree=14 packets=32")


if __name__ == "__main__":
    main()
