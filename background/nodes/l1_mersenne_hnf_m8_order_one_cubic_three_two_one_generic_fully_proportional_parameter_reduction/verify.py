#!/usr/bin/env python3
"""Audit identities for the fully-proportional parameter reduction."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_parameter_reduction"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_doubly_singular_quadratic_quotient_router"
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    for ad, q, r0 in ((F(2), F(5), F(7)), (F(-1), F(9), F(2)), (F(5, 2), F(11), F(-4))):
        b = ad + 6
        p = 40 * b * (b**2 - 6 * b + 27) + 42 * q * (11 * b + 15)
        q_poly = 480 * b**2 + 12960 + 5544 * q
        tc = 3240 + 3402 * q + 315 * q**2
        n1 = q**2 * (
            40 * ad**3 + 480 * ad**2 + (2520 + 462 * q) * ad + 6480 + 3402 * q
        ) + 2880 * q * r0 * (ad + 6)
        n0 = (
            q * r0 * (480 * ad**2 + 5760 * ad + 30240 + 5544 * q)
            + 17280 * r0**2
            + q**2 * (3240 + 3402 * q + 315 * q**2)
        )
        assert n1 == q * (q * p + 2880 * b * r0)
        assert n0 == q * r0 * q_poly + 17280 * r0**2 + q**2 * tc

    for c2, c1, c0, role_r, q, ad, r0 in (
        (F(1), F(2), F(3), F(5), F(7), F(4), F(11)),
        (F(2), F(-1), F(5), F(-3), F(11), F(-2), F(7)),
    ):
        delta_phi = c1**2 - 4 * c2 * c0
        role_s0 = -c1 * role_r / (2 * c0) - q * ad / 18
        u1 = 9 * q * (c1 * role_r + 2 * c0 * role_s0) + c0 * q**2 * ad
        u0 = 27 * (c2 * role_r**2 + c1 * role_r * role_s0 + c0 * role_s0**2) + 12 * c0 * q * r0
        weld = c0**2 * (q**2 * ad**2 + 144 * q * r0) - 81 * delta_phi * role_r**2
        assert u1 == 0
        assert 12 * c0 * u0 == weld

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
    for anchor in ("(FPR1)", "(FPR2)", "(FPR4)", "(FPR5)"):
        assert anchor in statement
    for anchor in ("N_1=q(qP+2880bR_0)", "Complete the square", "discriminant"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_GENERIC_FULLY_PROPORTIONAL_PARAMETER_REDUCTION_PASS")


if __name__ == "__main__":
    main()
