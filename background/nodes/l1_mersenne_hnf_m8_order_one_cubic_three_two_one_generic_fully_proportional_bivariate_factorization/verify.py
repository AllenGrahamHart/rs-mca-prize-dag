#!/usr/bin/env python3
"""Audit identities for the fully-proportional bivariate factorization."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_bivariate_factorization"
DEPENDENCY = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_proportional_parameter_reduction"
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    for b, q in ((F(2), F(5)), (F(-1), F(9)), (F(5, 2), F(11))):
        p = 40 * b * (b**2 - 6 * b + 27) + 42 * q * (11 * b + 15)
        q_poly = 480 * b**2 + 12960 + 5544 * q
        tc = 3240 + 3402 * q + 315 * q**2
        fn = 6 * p**2 - b * p * q_poly + 2880 * b**2 * tc
        z = b**2
        fb = (
            63 * (1575 - 247 * z) * q**2
            + 9240 * z * (9 - z) * q
            + 400 * z * (9 - z) * (z + 27)
        )
        discriminant = (
            (9240 * z * (9 - z)) ** 2
            - 4 * 63 * (1575 - 247 * z) * 400 * z * (9 - z) * (z + 27)
        )
        expected_discriminant = 302400 * z * (9 - z) * (
            -200 * z**2 + 4239 * z - 14175
        )
        assert fn == 24 * fb
        assert discriminant == expected_discriminant

    z = F(1575, 247)
    q = -F(10, 231) * (z + 27)
    assert 63 * (1575 - 247 * z) * q**2 == 0
    assert 9240 * z * (9 - z) * q + 400 * z * (9 - z) * (z + 27) == 0

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
    for anchor in ("(FBF1)", "(FBF3)", "(FBF5)", "(FBF6)"):
        assert anchor in statement
    for anchor in ("Collect powers", "z=9", "Disc_q(F_b)"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_GENERIC_FULLY_PROPORTIONAL_BIVARIATE_FACTORIZATION_PASS")


if __name__ == "__main__":
    main()
