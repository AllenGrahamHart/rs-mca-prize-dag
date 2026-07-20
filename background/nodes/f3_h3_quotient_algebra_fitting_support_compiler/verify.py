#!/usr/bin/env python3
"""Verify the quotient-algebra Fitting support compiler."""

from __future__ import annotations

import json
from math import comb, factorial
from pathlib import Path

from sympy import Poly, expand, gcd, resultant, symbols


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_quotient_algebra_fitting_support_compiler"
DEPENDENCIES = (
    "f3_h3_global_resultant_compression",
    "f3_h3_cutoff_layered_gcd_compiler",
    "f3_h3_shifted_product_sidon",
)
CONSUMER = "f3_h3_mobius_excess_half"
X, T = symbols("X T")


def shifted_polynomial(order: int):
    return sum(
        (-1) ** degree * comb(order, degree) * X ** (degree - 1)
        for degree in range(1, order + 1)
    )


def global_polynomials(order: int) -> tuple[Poly, Poly]:
    d = order - 1
    shifted = shifted_polynomial(order)
    product = Poly(
        resultant(shifted, expand(X**d * shifted.subs(X, T / X)), X), T
    )
    quotient_all = Poly(resultant(shifted, shifted.subs(X, T * X), X), T)
    quotient = quotient_all.exquo(Poly(order * (T - 1) ** d, T))
    assert quotient.LC() == order ** (d - 1)
    return product, quotient


def reduce_poly(poly: Poly, prime: int, scale: int = 1) -> Poly:
    expression = 0
    for (degree,), coefficient in poly.terms():
        numerator, denominator = coefficient.as_numer_denom()
        value = int(numerator) * pow(int(denominator), prime - 2, prime) % prime
        expression += scale * value * T**degree
    return Poly(expression, T, modulus=prime)


def hasse(poly: Poly, order: int, prime: int) -> Poly:
    answer = poly
    for _ in range(order):
        answer = answer.diff()
    return answer.mul_ground(pow(factorial(order), prime - 2, prime)) if order else answer


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next((index for index in range(row, len(work)) if work[index][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        inverse = pow(work[row][column], prime - 2, prime)
        work[row] = [value * inverse % prime for value in work[row]]
        for index in range(len(work)):
            if index != row and work[index][column]:
                scale = work[index][column]
                work[index] = [
                    (left - scale * right) % prime
                    for left, right in zip(work[index], work[row])
                ]
        row += 1
        if row == len(work):
            break
    return row


def presentation_dimension(product: Poly, quotient: Poly, cutoff: int, prime: int, double: bool) -> int:
    degree = quotient.degree()
    generators = [hasse(product, index, prime) for index in range(cutoff + 1)]
    if double:
        generators.append(quotient.diff())
    columns: list[list[int]] = []
    for generator in generators:
        for shift in range(degree):
            remainder = (generator * Poly(T**shift, T, modulus=prime)).rem(quotient)
            columns.append([int(remainder.nth(index)) % prime for index in range(degree)])
    matrix = [[columns[column][row] for column in range(len(columns))] for row in range(degree)]
    return degree - rank_mod(matrix, prime)


def direct_depths(order: int, prime: int, cutoff: int) -> tuple[int, int]:
    generator = next(
        value
        for value in range(2, prime)
        if pow(value, order, prime) == 1 and pow(value, order // 2, prime) != 1
    )
    group = {pow(generator, exponent, prime) for exponent in range(order)}
    shifted = {(1 - value) % prime for value in group if value != 1}
    products: dict[int, int] = {}
    quotients: dict[int, int] = {}
    for left in shifted:
        for right in shifted:
            product = left * right % prime
            products[product] = products.get(product, 0) + 1
            quotient = right * pow(left, prime - 2, prime) % prime
            if quotient != 1:
                quotients[quotient] = quotients.get(quotient, 0) + 1
    support = double = 0
    for target, multiplicity in products.items():
        excess = max(multiplicity - cutoff, 0)
        quotient = quotients.get(target, 0)
        support += min(quotient, excess)
        double += min(max(quotient - 1, 0), excess)
    return support, double


def exact_row(order: int, prime: int, cutoff: int, expected: tuple[int, int]) -> None:
    product_z, quotient_z = global_polynomials(order)
    product = reduce_poly(product_z, prime)
    inverse_lead = pow(int(quotient_z.LC()), prime - 2, prime)
    quotient = reduce_poly(quotient_z, prime, inverse_lead)

    common = quotient
    for index in range(cutoff + 1):
        common = gcd(common, hasse(product, index, prime))
    common_double = gcd(common, quotient.diff())
    gcd_depths = (common.degree(), common_double.degree())
    presentation = (
        presentation_dimension(product, quotient, cutoff, prime, False),
        presentation_dimension(product, quotient, cutoff, prime, True),
    )
    assert direct_depths(order, prime, cutoff) == expected
    assert gcd_depths == expected
    assert presentation == expected


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
        "r_(n,c)^X=#M_c^X",
        "p divides r_(n,c)^X iff X_c>0",
        "p divides r_(n,c)^Y iff Y_c>0",
        "p divides s_(n,c)^X iff X_c>0",
        "s_(n,c)^Y divides s_(n,c)^X",
        "scalar-elimination ideals",
        "min((R(t)-1)_+,q_c(t))",
        "does not retain the full weights",
    ):
        assert marker in text


def main() -> None:
    exact_row(8, 17, 2, (16, 14))
    exact_row(8, 73, 2, (0, 0))
    packet_check()
    print("F3_H3_QUOTIENT_ALGEBRA_FITTING_SUPPORT_PASS rows=2 ranks=X,Y")


if __name__ == "__main__":
    main()
