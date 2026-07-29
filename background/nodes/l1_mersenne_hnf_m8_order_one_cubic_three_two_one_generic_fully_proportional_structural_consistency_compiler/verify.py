#!/usr/bin/env python3
"""Audit structural identities after fully-proportional reconstruction."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_structural_consistency_compiler"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_q_quotient_router"
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    for b, q, g, d_core, q0 in (
        (F(2), F(5), F(7), F(3), F(11)),
        (F(-1), F(9), F(-4), F(5), F(2)),
        (F(5, 2), F(11), F(13, 7), F(-3), F(17)),
    ):
        x = (b + 15) / 4
        a = -(b + 3) / 2
        ell = (b**2 + 6 * b + 105 + 8 * q) / 16
        h = ell - g
        y = (ell - 2 * g) / a - x
        l2 = 15 + q / 2
        g_original = (l2 - x**2 - a * (2 * x + y)) / 2
        assert g_original == g
        assert g + a * (x + y) == h

        v = g + x * y + y**2
        d_residual = d_core - y * v
        q_original = 6 * g + a * x * (x + y) - 20 - 8 * q / 3 - d_core
        q_simplified = a * g + x * ell - 20 - 8 * q / 3 - d_core
        assert q_original == q_simplified
        assert q0 - q_original == q0 - q_simplified

        r_struct = F(19)
        constants = 15 + 23 * q / 4 + q**2 / 8
        w0 = y * (a + x) * v + constants
        original_r_residual = r_struct - (g * h - x * q0 - w0)
        simplified_r_residual = (
            r_struct
            - g * (ell - g)
            + x * q0
            + (a + x) * d_core
            + constants
        )
        assert original_r_residual - simplified_r_residual == -(a + x) * d_residual

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
    for anchor in ("(FSC1)", "(FSC3)", "(FSC5)", "(FSC6)"):
        assert anchor in statement
    for anchor in ("A(x+Y_c)", "W_0=Y_c(A+x)V_c", "degrees 7 and 11"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_GENERIC_FULLY_PROPORTIONAL_STRUCTURAL_CONSISTENCY_COMPILER_PASS")


if __name__ == "__main__":
    main()
