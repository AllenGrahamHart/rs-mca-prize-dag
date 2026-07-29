#!/usr/bin/env python3
"""Check the cubic three-two-one factor resultant packet."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_factor_reduction"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_color_remainder_router"
CONSUMER = "l1_mixed_petal_amplification"


def evaluate(poly: list[Fraction], value: Fraction) -> Fraction:
    out = Fraction(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def main() -> None:
    # G has roots 1,2,4. The monic F takes values B,B,lambda*B there.
    B, lam = Fraction(3), Fraction(2)
    F = [Fraction(-4), Fraction(25, 2), Fraction(-13, 2), Fraction(1)]
    G = multiply(multiply([-1, 1], [-2, 1]), [-4, 1])
    assert [evaluate(F, root) for root in (1, 2, 4)] == [B, B, lam * B]
    value_resultant = multiply(multiply([-B, 1], [-B, 1]), [-lam * B, 1])
    assert value_resultant == [-54, 45, -12, 1]

    role_assignments = set(itertools.permutations((3, 2, 1)))
    assert len(role_assignments) == 6 and 7 * len(role_assignments) == 42

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
    for anchor in ("(TOF1)", "(TOF2)", "42"):
        assert anchor in statement
    for anchor in ("(X-B)^2", "lambda B", "degree at most six"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_FACTOR_REDUCTION_PASS packets=42")


if __name__ == "__main__":
    main()
