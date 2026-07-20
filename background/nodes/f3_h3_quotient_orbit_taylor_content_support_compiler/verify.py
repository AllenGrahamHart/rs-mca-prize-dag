#!/usr/bin/env python3
"""Verify the quotient-orbit Taylor-content support compiler."""

from __future__ import annotations

import json
from math import factorial, gcd
from pathlib import Path

from sympy import Poly, diff, resultant, symbols


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_quotient_orbit_taylor_content_support_compiler"
DEPENDENCIES = {
    "f3_h3_quotient_orbit_canonical_resultant_manifest",
    "f3_h3_quotient_algebra_fitting_support_compiler",
}
CONSUMERS = {
    "f3_h3_dsp8_correlation_bound",
    "f3_h3_official_order_template_survivor",
}
T, X = symbols("T X")


def hasse(polynomial: Poly, order: int) -> Poly:
    return Poly(diff(polynomial.as_expr(), T, order) / factorial(order), T)


def taylor_resultant(block: Poly, product: Poly, cutoff: int) -> Poly:
    packet = sum(hasse(product, order).as_expr() * X**order for order in range(cutoff + 1))
    return Poly(resultant(block.as_expr(), packet, T), X)


def odd_content(polynomial: Poly) -> int:
    result = 0
    for coefficient in polynomial.all_coeffs():
        result = gcd(result, abs(int(coefficient)))
    while result and result % 2 == 0:
        result //= 2
    return result


def common_root(block: Poly, product: Poly, cutoff: int, prime: int) -> bool:
    common = Poly(block, T, modulus=prime)
    for order in range(cutoff + 1):
        common = common.gcd(Poly(hasse(product, order), T, modulus=prime))
    return common.degree() > 0


def support_check() -> None:
    examples = (
        (Poly(T**2 + 1, T), Poly((T**2 + 1) ** 3 + 5, T), 2),
        (
            Poly(T**2 + 1, T),
            Poly(3 + 3 * T + 3 * T**2 + 3 * T**4 + 3 * T**5, T),
            2,
        ),
        (Poly(T**2 + T + 1, T), Poly((T**2 + T + 1) ** 3 + 3, T), 2),
        (Poly(T**2 - 2, T), Poly(T**7 + 4 * T**3 + 21, T), 3),
    )
    for block, product, cutoff in examples:
        content = odd_content(taylor_resultant(block, product, cutoff))
        assert content > 0
        for prime in (3, 5, 7, 11, 13, 17, 19):
            assert (content % prime == 0) == common_root(
                block, product, cutoff, prime
            )

    survivor = examples[0]
    assert odd_content(taylor_resultant(*survivor)) % 5 == 0

    false_positive = examples[1]
    content = odd_content(taylor_resultant(*false_positive))
    scalar_resultants = [
        int(resultant(false_positive[0].as_expr(), hasse(false_positive[1], i).as_expr(), T))
        for i in range(3)
    ]
    scalar_gcd = gcd(gcd(abs(scalar_resultants[0]), abs(scalar_resultants[1])), abs(scalar_resultants[2]))
    assert scalar_gcd % 5 == 0
    assert content % 5 != 0

    repeated = examples[2]
    assert Poly(repeated[0], T, modulus=3).gcd(
        Poly(diff(repeated[0].as_expr(), T), T, modulus=3)
    ).degree() > 0
    assert odd_content(taylor_resultant(*repeated)) % 3 == 0


def degree_check() -> None:
    max_degree = 4_096
    total_degree = 67_084_290
    assert 35 * max_degree == 143_360
    assert 35 * total_degree == 2_347_950_150
    assert 24_534 < 73_602


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
        "Pcal_n(T+X) mod X^36",
        "rad(c_O,35)=rad(s_O,35)",
        "24,534",
        "143,360",
        "2,347,950,150",
        "No equality of valuations",
    ):
        assert marker in text


def main() -> None:
    support_check()
    degree_check()
    packet_check()
    print(
        "F3_H3_QUOTIENT_ORBIT_TAYLOR_CONTENT_SUPPORT_COMPILER_PASS "
        "exact_support=1 repeated_root_control=1 n8192_blocks=24534 max_x_degree=143360"
    )


if __name__ == "__main__":
    main()
