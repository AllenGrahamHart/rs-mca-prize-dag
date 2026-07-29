#!/usr/bin/env python3
"""Check the cubic 3+2+1 common-quadratic compiler."""

from __future__ import annotations

import json
from fractions import Fraction as FQ
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_factor_reduction"
CONSUMER = "l1_mixed_petal_amplification"


def multiply(left: list[FQ], right: list[FQ]) -> list[FQ]:
    out = [FQ(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def evaluate(poly: list[FQ], value: FQ) -> FQ:
    out = FQ(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def main() -> None:
    u, v, y, z, b = FQ(2), FQ(3), FQ(5), FQ(-1), FQ(7)
    a = y - z
    q_poly = [v, u, FQ(1)]
    g = multiply(q_poly, [-y, FQ(1)])
    f_minus_b = multiply(q_poly, [-z, FQ(1)])
    f = f_minus_b[:]
    f[0] += b
    product = multiply(f, g)
    coeffs = tuple(reversed(product[:-1]))

    g3, g2, g1, _ = g
    l1 = 2 * g1 + a
    l2 = g1**2 + 2 * g2 + a * (u + g1)
    l3 = 2 * g3 + 2 * g1 * g2 + a * (v + u * g1 + g2) + b
    l4 = g2**2 + 2 * g1 * g3 + a * (v * g1 + u * g2 + g3) + b * g1
    l5 = 2 * g2 * g3 + a * (v * g2 + u * g3) + b * g2
    l6 = g3**2 + a * v * g3 + b * g3
    assert coeffs == (l1, l2, l3, l4, l5, l6)

    recovered_a = l1 - 2 * g1
    recovered_g2 = (l2 - g1**2 - recovered_a * (2 * g1 + y)) / 2
    recovered_v = recovered_g2 + g1 * y + y**2
    recovered_g3 = -recovered_v * y
    recovered_b = l3 - 2 * recovered_g3 - 2 * g1 * recovered_g2 - recovered_a * (
        recovered_v + (g1 + y) * g1 + recovered_g2
    )
    assert (recovered_a, recovered_g2, recovered_b) == (a, g2, b)

    lam = FQ(1) + a * evaluate(q_poly, y) / b
    assert evaluate(f, y) == lam * b
    assert a * (3 * y**2 + 2 * g1 * y + g2) == (lam - 1) * b

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
    for anchor in ("(TQC2)", "(TQC5)", "(TQC6)", "(TQC7)"):
        assert anchor in statement
    for anchor in ("common quadratic", "four", "No unit verdict"):
        assert anchor in (statement + proof).lower() or anchor in statement + proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_COMMON_QUADRATIC_COMPILER_PASS")


if __name__ == "__main__":
    main()
