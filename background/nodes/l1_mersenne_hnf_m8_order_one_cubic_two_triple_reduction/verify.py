#!/usr/bin/env python3
"""Check the h=7 cubic two-triple reduction."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_two_triple_reduction"
DEPENDENCIES = {
    "l1_mersenne_next_to_maximal_hypergeometric_normal_form",
    "l1_mersenne_hnf_order_one_color_degree_barrier",
    "l1_mersenne_hnf_m8_order_one_conic_reduction",
}
CONSUMER = "l1_mixed_petal_amplification"

Poly = list[Fraction]
BiPoly = list[Poly]


def trim(poly: Poly) -> Poly:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return trim(out)


def scale(poly: Poly, scalar: Fraction) -> Poly:
    return trim([scalar * value for value in poly])


def sub(left: Poly, right: Poly) -> Poly:
    return add(left, scale(right, Fraction(-1)))


def mul(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def add_bi(left: BiPoly, right: BiPoly) -> BiPoly:
    out = [[Fraction(0)] for _ in range(max(len(left), len(right)))]
    for index, value in enumerate(left):
        out[index] = add(out[index], value)
    for index, value in enumerate(right):
        out[index] = add(out[index], value)
    while len(out) > 1 and out[-1] == [0]:
        out.pop()
    return out


def scale_bi(poly: BiPoly, scalar: Fraction) -> BiPoly:
    return [scale(coefficient, scalar) for coefficient in poly]


def mul_bi(left: BiPoly, right: BiPoly) -> BiPoly:
    out = [[Fraction(0)] for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = add(out[i + j], mul(a, b))
    return out


def q(index: int) -> Poly:
    return [Fraction(0)] + [
        Fraction(comb(index - 1, degree), index)
        for degree in range(1, index)
    ]


def main() -> None:
    d = [0, 1]
    q2, q3, q4, q5, q6 = (q(index) for index in range(2, 7))
    s1 = add(add(add(add(q2, q3), q4), q5), q6)
    s2 = add(scale(mul(add(q2, q3), add(q2, q3)), Fraction(1, 2)), mul(q2, q4))
    g_at_one = [[1], s1, s2, scale(mul(mul(d, d), d), Fraction(1, 48))]

    first_factor = [[12], d]
    second_factor = [[12], mul(d, [7, 2])]
    correction = mul_bi([[-1], [1]], mul_bi(first_factor, second_factor))
    cleared = add_bi(scale_bi(g_at_one, 720), scale_bi(correction, 5))
    assert cleared[0] == [0]

    q0 = [720, 2076, 2724, 1956, 744, 120]
    q1 = [0, 480, 845, 540, 130]
    q2_coefficient = [0, 0, 35, 25]
    assert cleared[1:] == [q0, q1, q2_coefficient]

    a1 = [0, 0, 35]
    b1 = [0, 378, 378, 154]
    c1 = [360, 720, 840, 480, 120]
    first_minor = sub(mul(a1, q0), mul(c1, q2_coefficient))
    second_minor = sub(mul(a1, q1), mul(b1, q2_coefficient))
    third_minor = sub(mul(b1, q0), mul(c1, q1))
    resultant = sub(mul(first_minor, first_minor), mul(second_minor, third_minor))
    assert len(resultant) - 1 == 14
    assert resultant[-1] == -576000

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
    for anchor in ("(CTR3)", "(CTR4)", "(CTR5)"):
        assert anchor in statement
    for anchor in ("3+3", "-576000", "r(q_2r^2+q_1r+q_0)"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_TWO_TRIPLE_REDUCTION_PASS degree=14 packets=32")


if __name__ == "__main__":
    main()
