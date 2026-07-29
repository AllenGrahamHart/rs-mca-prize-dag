#!/usr/bin/env python3
"""Audit denominator clearing for the coefficient bivariate compiler."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_coefficient_bivariate_compiler"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_coefficient_router"
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    for b, q in ((F(2), F(5)), (F(-1), F(9)), (F(5, 2), F(11))):
        a = b - 6
        kappa = 12 * q - 44 * b - 294
        p = 40 * b * (b**2 - 6 * b + 27) + 42 * q * (11 * b + 15)
        d_star = (
            3 * q * (40 * b**2 - 253 * b + 1155)
            - 20 * b * (11 * b**2 + 81 * b + 414)
        )
        q_star = (
            720 * b * (360 + 1098 * q + 191 * q**2 - 10 * q**3)
            + kappa * q * p
        )
        k_star = 240 * b * q * a - p
        ell = (b**2 + 6 * b + 105 + 8 * q) / 16
        d_core = d_star / (3600 * b)
        q0 = q_star / (72 * d_star)
        e_g = k_star - 720 * b * q**2
        f_g = 6 * d_core * (k_star - 2160 * b * q0)
        j_g = 2160 * b * (q0 - d_core) - p
        l_g = 2160 * b * ell - 6 * p
        theta_g = e_g * d_core * l_g - j_g * f_g

        l_star = 135 * b * (b**2 + 6 * b + 105 + 8 * q) - 6 * p
        f_star = d_star * k_star - 30 * b * q_star
        j_star = 150 * b * q_star - 3 * d_star**2 - 5 * p * d_star
        x_star = q_star - 24 * d_star * q**2
        theta_star = 5 * e_g * d_star**2 * l_star - 6 * j_star * f_star

        assert l_g == l_star
        assert f_g == f_star / (600 * b)
        assert j_g == j_star / (5 * d_star)
        assert theta_g == theta_star / (18000 * b * d_star)
        assert q_star - 24 * d_star * q**2 == x_star

        assert e_g != 0
        g_generic = -f_star / (600 * b * e_g)
        assert e_g * g_generic + f_g == 0

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
    for anchor in ("(FBC1)", "(FBC2)", "(FBC5)", "(FBC6)"):
        assert anchor in statement
    for anchor in ("F_*/(600b)", "J_*/(5D_*)", "Theta_*/(18000bD_*)"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_GENERIC_FULLY_PROPORTIONAL_COEFFICIENT_BIVARIATE_COMPILER_PASS")


if __name__ == "__main__":
    main()
