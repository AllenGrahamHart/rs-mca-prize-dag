#!/usr/bin/env python3
"""Check the homogeneous substitution that eliminates the role variable."""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_role_weld"
DEPENDENCIES = {
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler",
    "l1_mersenne_hnf_m8_cubic_three_two_one_role_factor_compiler",
}
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    for r, s in ((F(2), F(3)), (F(-5), F(7)), (F(11), F(-4))):
        lam = 1 + r / s
        a = lam**2 - lam + 1
        b = (lam + 1) * (2 * lam - 1) * (lam - 2)
        a0 = s**2 + r * s + r**2
        b0 = (2 * s + r) * (s + 2 * r) * (r - s)
        assert a == a0 / s**2
        assert b == b0 / s**3
        assert s**6 * (b**2 + 50 * a**3) == b0**2 + 50 * a0**3
        assert s**12 * (b**4 - 224 * b**2 * a**3 - 578 * a**6) == (
            b0**4 - 224 * b0**2 * a0**3 - 578 * a0**6
        )

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    for dependency in DEPENDENCIES:
        assert statuses[dependency] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(TRW1)", "(TRW2)", "(TRW3)", "(TRW4)"):
        assert anchor in statement
    for anchor in ("common denominator", "reconstructs", "equivalent"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_TWO_ONE_ROLE_WELD_PASS")


if __name__ == "__main__":
    main()
