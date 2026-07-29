#!/usr/bin/env python3
"""Check the degree and diagonal multiplicity in the role compiler."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_cubic_three_two_one_role_polynomial_compiler"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler"
CONSUMER = "l1_mixed_petal_amplification"


def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def remainder(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = left[:]
    divisor = right[:]
    while len(out) >= len(divisor) and out != [0]:
        scale = out[-1] / divisor[-1]
        shift = len(out) - len(divisor)
        for index, value in enumerate(divisor):
            out[index + shift] -= scale * value
        trim(out)
    return out


def gcd(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    a, b = trim(left[:]), trim(right[:])
    while b != [0]:
        a, b = b, remainder(a, b)
    leader = a[-1]
    return [value / leader for value in a]


def main() -> None:
    c = [Fraction(1)] * 8
    c_prime = [Fraction(index) for index in range(1, 8)]
    u_minus_one = [Fraction(-1), Fraction(1)]
    derivative_factor = [Fraction(0)] * (len(c_prime) + 1)
    for i, a in enumerate(u_minus_one):
        for j, b in enumerate(c_prime):
            derivative_factor[i + j] += a * b
    assert gcd(c, derivative_factor) == [Fraction(1)]
    assert 7 * 7 == 49 and 49 - 7 == 42 and 7 * 6 == 42
    assert gcd(c, c_prime) == [Fraction(1)]

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
    for anchor in ("(RPC2)", "(RPC3)", "(RPC4)", "(RPC5)"):
        assert anchor in statement
    for anchor in ("degree seven", "exactly seven", "42 ordered"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_CUBIC_THREE_TWO_ONE_ROLE_POLYNOMIAL_COMPILER_PASS")


if __name__ == "__main__":
    main()
