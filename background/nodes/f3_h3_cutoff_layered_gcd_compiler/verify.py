#!/usr/bin/env python3
"""Verify the H3 cutoff multiplicity-layer gcd compiler."""

from __future__ import annotations

import json
from pathlib import Path

from sympy import Poly, gcd, symbols


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_cutoff_layered_gcd_compiler"
DEPENDENCIES = (
    "f3_h3_global_resultant_compression",
    "f3_h3_cutoff18_double_accident_reduction",
    "f3_h3_uniform_product_fiber_stepanov",
)
CONSUMER = "f3_h3_mobius_excess_half"
T = symbols("T")


def order_generator(order: int, prime: int) -> int:
    for value in range(2, prime):
        if pow(value, order, prime) == 1 and pow(value, order // 2, prime) != 1:
            return value
    raise AssertionError("no subgroup generator")


def hasse(poly: Poly, order: int, prime: int) -> Poly:
    result = poly
    for _ in range(order):
        result = result.diff()
    factorial = 1
    for value in range(2, order + 1):
        factorial = factorial * value % prime
    return result.mul_ground(pow(factorial, prime - 2, prime)) if order else result


def row_polynomials(order: int, prime: int) -> tuple[Poly, Poly, dict[int, int], dict[int, int]]:
    generator = order_generator(order, prime)
    group = {pow(generator, exponent, prime) for exponent in range(order)}
    shifted = {(1 - value) % prime for value in group if value != 1}
    product_count: dict[int, int] = {}
    quotient_count: dict[int, int] = {}
    for left in shifted:
        for right in shifted:
            product = left * right % prime
            product_count[product] = product_count.get(product, 0) + 1
            quotient = right * pow(left, prime - 2, prime) % prime
            if quotient != 1:
                quotient_count[quotient] = quotient_count.get(quotient, 0) + 1

    product_poly = Poly(1, T, modulus=prime)
    quotient_poly = Poly(1, T, modulus=prime)
    for target, multiplicity in product_count.items():
        product_poly *= Poly((T - target) ** multiplicity, T, modulus=prime)
    for target, multiplicity in quotient_count.items():
        quotient_poly *= Poly((T - target) ** multiplicity, T, modulus=prime)
    return product_poly, quotient_poly, product_count, quotient_count


def layered_moments(product_poly: Poly, quotient_poly: Poly, cutoff: int, d: int, prime: int) -> tuple[int, int]:
    rich = product_poly
    for order in range(1, cutoff + 1):
        rich = gcd(rich, hasse(product_poly, order, prime))
    quotient_extra = gcd(quotient_poly, quotient_poly.diff())

    total = extra = 0
    layer = rich
    for index in range(1, d - cutoff + 1):
        if index > 1:
            layer = gcd(layer, hasse(rich, index - 1, prime))
        saturated = layer**d
        total += gcd(quotient_poly, saturated).degree()
        extra += gcd(quotient_extra, saturated).degree()
    return total, extra


def direct_moments(product_count: dict[int, int], quotient_count: dict[int, int], cutoff: int) -> tuple[int, int]:
    total = extra = 0
    for target, product_multiplicity in product_count.items():
        excess = max(product_multiplicity - cutoff, 0)
        quotient_multiplicity = quotient_count.get(target, 0)
        total += excess * quotient_multiplicity
        extra += excess * max(quotient_multiplicity - 1, 0)
    return total, extra


def exact_row(order: int, prime: int, cutoff: int, expected: tuple[int, int]) -> None:
    product_poly, quotient_poly, product_count, quotient_count = row_polynomials(order, prime)
    direct = direct_moments(product_count, quotient_count, cutoff)
    layered = layered_moments(product_poly, quotient_poly, cutoff, order - 1, prime)
    assert direct == expected
    assert layered == direct


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

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
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "G_j=gcd(G^[0],G^[1],...,G^[j-1])",
        "X_c=sum_(j=1)^(d-c) deg gcd(Qcal,G_j^d)",
        "Y_c=sum_(j=1)^(d-c) deg gcd(Qcal_+,G_j^d)",
        "B_n=min(n-19,ceil(33n^(2/3))-19)",
        "Bezout identity",
        "no upper bound on `X_18` or `Y_18`",
    ):
        assert marker in text


def main() -> None:
    exact_row(8, 17, 2, (48, 32))
    exact_row(16, 97, 2, (153, 90))
    packet_check()
    print("F3_H3_CUTOFF_LAYERED_GCD_COMPILER_PASS rows=2 moments=X,Y")


if __name__ == "__main__":
    main()
