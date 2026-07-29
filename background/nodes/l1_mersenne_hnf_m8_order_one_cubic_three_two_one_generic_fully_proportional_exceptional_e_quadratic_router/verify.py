#!/usr/bin/env python3
"""Audit the exceptional-E quadratic router identities."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_quadratic_router"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_coefficient_bivariate_compiler"
CONSUMER = "l1_mixed_petal_amplification"


def evaluate(poly: list[F], value: F) -> F:
    out = F(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def main() -> None:
    for b in (F(2), F(-1), F(5, 2)):
        a2 = 63 * (1575 - 247 * b**2)
        a1 = 9240 * b**2 * (9 - b**2)
        a0 = 400 * b**2 * (9 - b**2) * (b**2 + 27)
        e2 = -720 * b
        e1 = 240 * b**2 - 1902 * b - 630
        e0 = -40 * b * (b**2 - 6 * b + 27)
        s1 = a2 * e1 - e2 * a1
        s0 = a2 * e0 - e2 * a0
        assert a2 != 0 and s1 != 0

        fb = [a0, a1, a2]
        exceptional = [e0, e1, e2]
        affine = [s0, s1]
        for q in (F(3), F(-2), F(7, 5)):
            assert a2 * evaluate(exceptional, q) - e2 * evaluate(fb, q) == evaluate(
                affine, q
            )

        q_value = -s0 / s1
        v_value = a2 * s0**2 - a1 * s0 * s1 + a0 * s1**2
        assert s1**2 * evaluate(fb, q_value) == v_value
        assert a2 * s1**2 * evaluate(exceptional, q_value) == e2 * v_value

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
    for anchor in ("(FEQ1)", "(FEQ3)", "(FEQ6)", "(FEQ9)"):
        assert anchor in statement
    for anchor in ("K_*=240bq", "S_1q+S_0", "degree at most 16"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_GENERIC_FULLY_PROPORTIONAL_EXCEPTIONAL_E_QUADRATIC_ROUTER_PASS")


if __name__ == "__main__":
    main()
