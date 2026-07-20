#!/usr/bin/env python3
"""Verify the quotient-orbit three-resultant candidate screen."""

from __future__ import annotations

import json
from math import factorial, gcd
from pathlib import Path

from sympy import Poly, diff, resultant, symbols


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_quotient_orbit_three_resultant_candidate_screen"
DEPENDENCIES = {
    "f3_h3_quotient_orbit_canonical_resultant_manifest",
    "f3_h3_quotient_algebra_fitting_support_compiler",
}
CONSUMERS = {
    "f3_h3_dsp8_correlation_bound",
    "f3_h3_official_order_template_survivor",
}
T = symbols("T")


def hasse(polynomial: Poly, order: int) -> Poly:
    return Poly(diff(polynomial.as_expr(), T, order) / factorial(order), T)


def resultant_triple(block: Poly, product: Poly) -> tuple[int, int, int]:
    return tuple(
        int(resultant(block.as_expr(), hasse(product, order).as_expr(), T))
        for order in range(3)
    )


def gcd_triple(values: tuple[int, int, int]) -> int:
    result = 0
    for value in values:
        result = gcd(result, abs(value))
    while result and result % 2 == 0:
        result //= 2
    return result


def algebra_check() -> None:
    block = Poly(T**2 + 1, T)

    double_block = Poly(block.as_expr() ** 2 * (T - 2), T)
    double_resultants = resultant_triple(block, double_block)
    assert double_resultants == (0, 0, 80)
    assert gcd_triple(double_resultants) == 5

    characteristic_five_survivor = Poly(block.as_expr() ** 3 + 5, T)
    survivor_resultants = resultant_triple(block, characteristic_five_survivor)
    assert survivor_resultants == (25, 0, 0)
    assert gcd_triple(survivor_resultants) == 25
    block_mod_five = Poly(block, T, modulus=5)
    survivor_derivatives = [
        Poly(hasse(characteristic_five_survivor, order), T, modulus=5)
        for order in range(3)
    ]
    common = block_mod_five
    for derivative in survivor_derivatives:
        common = common.gcd(derivative)
    assert common.degree() == 2

    false_positive = Poly(3 + 3 * T + 3 * T**2 + 3 * T**4 + 3 * T**5, T)
    false_resultants = resultant_triple(block, false_positive)
    assert false_resultants == (45, 360, 1125)
    assert gcd_triple(false_resultants) == 45
    common = block_mod_five
    for order in range(3):
        common = common.gcd(Poly(hasse(false_positive, order), T, modulus=5))
    assert common.degree() == 0


def official_count_check() -> None:
    blocks = 24_534
    assert 3 * blocks == 73_602


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for consumer in CONSUMERS:
        assert (NODE, consumer, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join(
        (base / name).read_text() for name in required if name.endswith(".md")
    )
    for marker in (
        "s_O,35 divides g_O",
        "73,602",
        "not all zero",
        "converse",
        "different roots",
        "Complete factorization",
    ):
        assert marker in text


def main() -> None:
    algebra_check()
    official_count_check()
    packet_check()
    print(
        "F3_H3_QUOTIENT_ORBIT_THREE_RESULTANT_CANDIDATE_SCREEN_PASS "
        "resultants_per_block=3 n8192_tasks=73602 false_positive_control=1"
    )


if __name__ == "__main__":
    main()
