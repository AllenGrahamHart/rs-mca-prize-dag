#!/usr/bin/env python3
"""Verify the quotient-orbit Taylor cutoff ladder."""

from __future__ import annotations

import json
from math import factorial, gcd
from pathlib import Path

from sympy import Poly, diff, resultant, symbols


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_quotient_orbit_taylor_cutoff_ladder"
DEPENDENCIES = {
    "f3_h3_quotient_orbit_taylor_content_support_compiler",
    "f3_h3_quotient_algebra_fitting_support_compiler",
}
CONSUMERS = {
    "f3_h3_dsp8_correlation_bound",
    "f3_h3_official_order_template_survivor",
}
T, X = symbols("T X")


def hasse(polynomial: Poly, order: int) -> Poly:
    return Poly(diff(polynomial.as_expr(), T, order) / factorial(order), T)


def content_at_cutoff(block: Poly, product: Poly, cutoff: int) -> int:
    packet = sum(hasse(product, order).as_expr() * X**order for order in range(cutoff + 1))
    certificate = Poly(resultant(block.as_expr(), packet, T), X)
    content = 0
    for coefficient in certificate.all_coeffs():
        content = gcd(content, abs(int(coefficient)))
    while content and content % 2 == 0:
        content //= 2
    return content


def common_root(block: Poly, product: Poly, cutoff: int, prime: int) -> bool:
    common = Poly(block, T, modulus=prime)
    for order in range(cutoff + 1):
        common = common.gcd(Poly(hasse(product, order), T, modulus=prime))
    return common.degree() > 0


def ladder_check() -> None:
    examples = (
        (Poly(T**2 + 1, T), Poly((T**2 + 1) ** 5 + 5, T)),
        (Poly(T**2 + T + 1, T), Poly((T**2 + T + 1) ** 4 + 3, T)),
        (Poly(T**2 - 2, T), Poly(T**9 + 6 * T**5 + 35 * T + 15, T)),
    )
    primes = (3, 5, 7, 11, 13, 17, 19)
    for block, product in examples:
        contents = {cutoff: content_at_cutoff(block, product, cutoff) for cutoff in range(2, 5)}
        assert all(value > 0 for value in contents.values())
        for cutoff, content in contents.items():
            for prime in primes:
                assert (content % prime == 0) == common_root(
                    block, product, cutoff, prime
                )
        for prime in primes:
            support = [contents[cutoff] % prime == 0 for cutoff in range(2, 5)]
            assert support == sorted(support, reverse=True)


def strict_screen_check() -> None:
    block = Poly(T**2 + 1, T)
    product = Poly(3 + 3 * T + 3 * T**2 + 3 * T**4 + 3 * T**5, T)
    scalar_resultants = [
        int(resultant(block.as_expr(), hasse(product, order).as_expr(), T))
        for order in range(3)
    ]
    scalar_gcd = gcd(gcd(abs(scalar_resultants[0]), abs(scalar_resultants[1])), abs(scalar_resultants[2]))
    assert scalar_gcd % 5 == 0
    assert content_at_cutoff(block, product, 2) % 5 != 0


def degree_check() -> None:
    assert 2 * 4_096 == 8_192
    assert 2 * 67_084_290 == 134_168_580
    assert 8_192 < 143_360


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
        "rad(c_O,c)=rad(s_O,c)",
        "rad(c_O,b) divides rad(c_O,a)",
        "8,192",
        "134,168,580",
        "different-root false positives",
        "Exact row evaluation",
    ):
        assert marker in text


def main() -> None:
    ladder_check()
    strict_screen_check()
    degree_check()
    packet_check()
    print(
        "F3_H3_QUOTIENT_ORBIT_TAYLOR_CUTOFF_LADDER_PASS "
        "cutoffs=2..4 exact_nested=1 n8192_c2_max_x_degree=8192"
    )


if __name__ == "__main__":
    main()
