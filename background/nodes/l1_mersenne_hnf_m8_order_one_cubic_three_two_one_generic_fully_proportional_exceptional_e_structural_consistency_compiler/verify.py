#!/usr/bin/env python3
"""Audit the exceptional-E structural identities and DAG registration."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_structural_consistency_compiler"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_exceptional_e_quadratic_router"
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    for b, q, d_star, l_star, j_star, d_core, q0 in (
        (F(2), F(5), F(7), F(3), F(11), F(13), F(17)),
        (F(-1), F(9), F(4), F(-5), F(2), F(7), F(-3)),
        (F(5, 2), F(11), F(13), F(17), F(-7), F(-3), F(19)),
    ):
        x = (b + 15) / 4
        a = -(b + 3) / 2
        ell = (b**2 + 6 * b + 105 + 8 * q) / 16
        g = -(d_star**2) * l_star / (720 * b * j_star)
        h = ell - g
        y = (ell - 2 * g) / a - x
        l2 = 15 + q / 2
        assert ell == l2 - x**2 - a * x
        assert (l2 - x**2 - a * (2 * x + y)) / 2 == g
        assert g + a * (x + y) == h

        v = g + x * y + y**2
        d_residual = d_core - y * v
        q_original = 6 * g + a * x * (x + y) - 20 - 8 * q / 3 - d_core
        q_simplified = a * g + x * ell - 20 - 8 * q / 3 - d_core
        assert q_original == q_simplified
        assert q0 - q_original == q0 - q_simplified

        r0 = F(23)
        constants = 15 + 23 * q / 4 + q**2 / 8
        w0 = y * (a + x) * v + constants
        original_residual = r0 - (g * h - x * q0 - w0)
        simplified_residual = (
            r0 - g * (ell - g) + x * q0 + (a + x) * d_core + constants
        )
        assert original_residual - simplified_residual == -(a + x) * d_residual

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
    for anchor in ("(FES1)", "(FES3)", "(FES5)", "(FES6)"):
        assert anchor in statement
    for anchor in ("(9/7)", "degree 24", "degrees 10 and 17"):
        assert anchor in proof

    print(
        "L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_"
        "EXCEPTIONAL_E_STRUCTURAL_CONSISTENCY_COMPILER_PASS"
    )


if __name__ == "__main__":
    main()
