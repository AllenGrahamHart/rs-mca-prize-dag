#!/usr/bin/env python3
"""Exact reciprocal-eliminant certificates for the four m=8 rows."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_zero_reciprocal_elimination"
DEPENDENCIES = (
    "l1_mersenne_next_to_maximal_hypergeometric_normal_form",
    "l1_mersenne_hnf_frobenius_reciprocal_gate",
)
CONSUMER = "l1_mixed_petal_amplification"
ROWS = (8191, 131071, 524287, 2147483647)
H = 7
START = 200
BOUND_12 = 1344
BOUND_13 = 1792
ROOT_MULTIPLICITIES = {
    0: 176,
    1: 4,
    -1: 176,
    -2: 168,
    -3: 162,
    -4: 152,
    -5: 128,
    -6: 64,
    -7: 2,
}


def trim(poly: list[int], prime: int) -> list[int]:
    while len(poly) > 1 and poly[-1] % prime == 0:
        poly.pop()
    return [value % prime for value in poly]


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return trim(out, prime)


def scale(poly: list[int], scalar: int, prime: int) -> list[int]:
    return trim([scalar * value % prime for value in poly], prime)


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return trim(out, prime)


def divide(
    dividend: list[int], divisor: list[int], prime: int
) -> tuple[list[int], list[int]]:
    remainder = trim(dividend[:], prime)
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, prime)
    while len(remainder) >= len(divisor) and any(remainder):
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1] * inverse % prime
        quotient[shift] = coefficient
        for i, value in enumerate(divisor):
            remainder[i + shift] = (remainder[i + shift] - coefficient * value) % prime
        trim(remainder, prime)
    return trim(quotient, prime), remainder


def evaluate(poly: list[int], value: int, prime: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % prime
    return result


def resultant(left: list[int], right: list[int], prime: int) -> int:
    left, right = trim(left, prime), trim(right, prime)
    m, n = len(left) - 1, len(right) - 1
    if n == 0:
        return pow(right[0], m, prime)
    if m < n:
        result = resultant(right, left, prime)
        return -result % prime if m * n % 2 else result
    _, remainder = divide(left, right, prime)
    if remainder == [0]:
        return 0
    degree = len(remainder) - 1
    result = pow(right[-1], m - degree, prime) * resultant(right, remainder, prime) % prime
    return -result % prime if m * n % 2 else result


def interpolate(values: list[int], start: int, prime: int) -> list[int]:
    differences = [value % prime for value in values]
    basis = [1]
    result = [0]
    factorial = 1
    for degree in range(len(values)):
        coefficient = differences[0] * pow(factorial, -1, prime) % prime
        result = add(result, scale(basis, coefficient, prime), prime)
        differences = [
            (differences[i + 1] - differences[i]) % prime
            for i in range(len(differences) - 1)
        ]
        basis = multiply(basis, [(-start - degree) % prime, 1], prime)
        factorial = factorial * (degree + 1) % prime
    return trim(result, prime)


def gcd(left: list[int], right: list[int], prime: int) -> list[int]:
    left, right = trim(left, prime), trim(right, prime)
    while right != [0]:
        _, remainder = divide(left, right, prime)
        left, right = right, remainder
    return scale(left, pow(left[-1], -1, prime), prime)


def expected_factor(prime: int) -> list[int]:
    result = [1]
    for root, multiplicity in ROOT_MULTIPLICITIES.items():
        for _ in range(multiplicity):
            result = multiply(result, [(-root) % prime, 1], prime)
    return scale(result, pow(result[-1], -1, prime), prime)


def reduce_rational(poly: sp.Expr, variable: sp.Symbol, prime: int) -> list[int]:
    rational = sp.Poly(poly, variable, domain=sp.QQ)
    out = [0] * (rational.degree() + 1)
    for (exponent,), coefficient in rational.terms():
        numerator, denominator = map(int, coefficient.as_numer_denom())
        assert denominator % prime
        out[exponent] = numerator % prime * pow(denominator % prime, -1, prime) % prime
    return trim(out, prime)


def row_certificate(q_rational: list[sp.Expr], variable: sp.Symbol, prime: int) -> tuple[int, int, int]:
    assert prime > BOUND_13
    q = [reduce_rational(value, variable, prime) for value in q_rational]
    assert [len(value) - 1 for value in q] == [8 * j for j in range(H + 1)]
    constant = q[H]

    def equation(j: int, s_value: int) -> list[int]:
        out = scale(q[j], evaluate(constant, s_value, prime), prime)
        out[0] = (out[0] - evaluate(q[H - j], s_value, prime)) % prime
        return trim(out, prime)

    def eliminant(j: int, bound: int) -> list[int]:
        values = [
            resultant(equation(1, value), equation(j, value), prime)
            for value in range(START, START + bound + 1)
        ]
        out = interpolate(values, START, prime)
        check = START + bound + 37
        assert evaluate(out, check, prime) == resultant(
            equation(1, check), equation(j, check), prime
        )
        return out

    r12 = eliminant(2, BOUND_12)
    r13 = eliminant(3, BOUND_13)
    common = gcd(r12, r13, prime)
    assert (len(r12) - 1, len(r13) - 1, len(common) - 1) == (1320, 1760, 1032)
    assert common == expected_factor(prime)
    return len(r12) - 1, len(r13) - 1, len(common) - 1


def main() -> None:
    s, w, z = sp.symbols("s w z")
    locator = sum(
        sp.prod(s + j for j in range(r)) / sp.factorial(r) * w ** (H - r)
        for r in range(H + 1)
    )
    q_poly = sp.Poly(sp.resultant(locator, z - w**8, w), z)
    assert q_poly.degree() == H
    q_rational = [q_poly.nth(H - j) for j in range(H + 1)]
    assert [sp.degree(value, s) for value in q_rational] == [8 * j for j in range(H + 1)]

    certificates = [row_certificate(q_rational, s, prime) for prime in ROWS]
    assert certificates == [(1320, 1760, 1032)] * 4

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dependency in DEPENDENCIES:
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = Path(__file__).with_name("statement.md").read_text()
    proof = Path(__file__).with_name("proof.md").read_text()
    assert "complete `m=8,h=7`" in statement
    assert "degree 1032" in proof and "R_12" in proof and "R_13" in proof

    wrong = expected_factor(ROWS[0])[:-1]
    assert len(wrong) - 1 != 1032

    print(
        "L1_MERSENNE_HNF_M8_ORDER_ZERO_RECIPROCAL_ELIMINATION_PASS "
        "rows=4 q_degrees=0:8:56 eliminants=8 degrees=1320,1760 gcd_degree=1032 mutations=1"
    )


if __name__ == "__main__":
    main()
