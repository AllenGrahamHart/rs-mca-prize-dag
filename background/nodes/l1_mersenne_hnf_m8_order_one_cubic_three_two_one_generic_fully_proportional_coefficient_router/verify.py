#!/usr/bin/env python3
"""Audit identities for the fully-proportional coefficient router."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_coefficient_router"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_bivariate_factorization"
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    for b, q in ((F(2), F(5)), (F(-1), F(9)), (F(5, 2), F(11))):
        a = b - 6
        kappa = 12 * q - 44 * b - 294
        p = 40 * b * (b**2 - 6 * b + 27) + 42 * q * (11 * b + 15)
        r0 = -q * p / (2880 * b)
        d_star = (
            3 * q * (40 * b**2 - 253 * b + 1155)
            - 20 * b * (11 * b**2 + 81 * b + 414)
        )
        assert d_star != 0
        d_core = d_star / (3600 * b)

        b1 = -q * (120 * d_core + 1062 + 86 * q) - 528 * r0
        m1 = 3 * b1 + q * kappa * a
        assert m1 == 0

        q_star = (
            720 * b * (360 + 1098 * q + 191 * q**2 - 10 * q**3)
            + kappa * q * p
        )
        q0 = q_star / (72 * d_star)
        b0 = 360 * d_core * q0 - 360 - 1098 * q - 191 * q**2 + 10 * q**3
        m0 = 3 * b0 + 12 * kappa * r0
        assert m0 == 0

        ell = (b**2 + 6 * b + 105 + 8 * q) / 16
        x = (b + 15) / 4
        aa = -(b + 3) / 2
        y = F(7, 3)
        l2 = 15 + q / 2
        g_struct = (l2 - x**2 - aa * (2 * x + y)) / 2
        h_struct = g_struct + aa * (x + y)
        assert h_struct + g_struct == ell

        k_star = 240 * b * q * a - p
        e_g = k_star - 720 * b * q**2
        f_g = 6 * d_core * (k_star - 2160 * b * q0)
        j_g = 2160 * b * (q0 - d_core) - p
        l_g = 2160 * b * ell - 6 * p

        g = F(13, 7)
        h = ell - g
        t = g + 6 * d_core
        c1 = q * t * a - 9 * d_core * h - 3 * q**2 * g - 9 * t * q0
        c0 = 9 * q * (d_core * h + g * q0) + 12 * t * r0
        assert 240 * b * (c1 + c0 / q) == e_g * g + f_g
        assert 240 * b * c0 / q == j_g * g + d_core * l_g

        assert e_g != 0
        g_generic = -f_g / e_g
        theta = e_g * d_core * l_g - j_g * f_g
        assert e_g * (j_g * g_generic + d_core * l_g) == theta
        assert f_g == 6 * d_core * (e_g + 720 * b * q**2 - 2160 * b * q0)
        assert q_star - 24 * d_star * q**2 == 72 * d_star * (
            q0 - q**2 / 3
        )

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
    for anchor in ("(FCR1)", "(FCR2)", "(FCR5)", "(FCR7)"):
        assert anchor in statement
    for anchor in ("M_1=0", "H+G_2", "C_1+C_0/q"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_GENERIC_FULLY_PROPORTIONAL_COEFFICIENT_ROUTER_PASS")


if __name__ == "__main__":
    main()
