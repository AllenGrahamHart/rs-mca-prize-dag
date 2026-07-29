#!/usr/bin/env python3
"""Check the cubic three-double symmetric coefficient compiler."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_double_symmetric_compiler"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_double_factor_reduction"
CONSUMER = "l1_mixed_petal_amplification"


def multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def compiled_coefficients(
    roots: tuple[Fraction, Fraction, Fraction], U: Fraction, V: Fraction
) -> tuple[Fraction, ...]:
    s1 = sum(roots)
    s2 = sum(roots[i] * roots[j] for i in range(3) for j in range(i + 1, 3))
    s3 = roots[0] * roots[1] * roots[2]
    p2 = s1 * s1 - 2 * s2
    p3 = s1**3 - 3 * s1 * s2 + 3 * s3
    p4 = s1**4 - 4 * s1 * s1 * s2 + 2 * s2 * s2 + 4 * s1 * s3
    A0 = p2 - U * s1 + 3 * V
    B0 = p4 - 2 * U * p3 + (U * U + 2 * V) * p2 - 2 * U * V * s1 + 3 * V * V
    l1 = s1
    l2 = s1 * s1 - s2 - U * s1 + 3 * V
    l3 = s1 * s2 - 2 * s3 - 2 * U * s2 + 2 * V * s1
    l4 = (A0 * A0 - B0) / 2 + (s1 - 3 * U) * s3 + V * s2
    l5 = (
        s2 * s3
        - 2 * U * s1 * s3
        + V * (s1 * s2 - 3 * s3)
        + 3 * U * U * s3
        - 2 * U * V * s2
        + V * V * s1
    )
    l6 = (
        s3 * s3
        - U * s2 * s3
        + V * (s2 * s2 - 2 * s1 * s3)
        + U * U * s1 * s3
        - U * V * (s1 * s2 - 3 * s3)
        + V * V * (s1 * s1 - 2 * s2)
        - U**3 * s3
        + U * U * V * s2
        - U * V * V * s1
        + V**3
    )
    return l1, l2, l3, l4, l5, l6


def main() -> None:
    roots = (Fraction(1), Fraction(3), Fraction(8))
    U, V = Fraction(5), Fraction(-2)
    factors = [
        [root * root - U * root + V, root, Fraction(1)]
        for root in roots
    ]
    product = multiply(multiply(factors[0], factors[1]), factors[2])
    direct = tuple(reversed(product[:-1]))
    assert direct == compiled_coefficients(roots, U, V)

    l1, l2, l3, _, _, _ = direct
    s1 = sum(roots)
    s2 = sum(roots[i] * roots[j] for i in range(3) for j in range(i + 1, 3))
    recovered_v = (l2 - s1 * s1 + s2 + U * s1) / 3
    recovered_s3 = (s1 * s2 - 2 * U * s2 + 2 * recovered_v * s1 - l3) / 2
    assert l1 == s1 and recovered_v == V and recovered_s3 == roots[0] * roots[1] * roots[2]

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
    for anchor in ("(TSC2)", "(TSC4)", "(TSC6)", "(TSC7)"):
        assert anchor in statement
    for anchor in ("l_4", "l_5", "l_6", "four"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_DOUBLE_SYMMETRIC_COMPILER_PASS")


if __name__ == "__main__":
    main()
