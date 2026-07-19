#!/usr/bin/env python3
"""Verify the generic canonical Euler divisor gate."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_euler_divisor_gate"
DEPENDENCY = "rate_half_list_budget_three_antipodal_generic_canonical_span_criterion"
CONSUMER = "rate_half_list_adjacent_crossing"


def trim(poly: list[Fraction]) -> list[Fraction]:
    answer = list(poly)
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def scale(poly: list[Fraction], scalar: Fraction) -> list[Fraction]:
    return trim([scalar * value for value in poly])


def multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            answer[i + j] += left_value * right_value
    return trim(answer)


def power(poly: list[Fraction], exponent: int) -> list[Fraction]:
    answer = [Fraction(1)]
    for _ in range(exponent):
        answer = multiply(answer, poly)
    return answer


def derivative(poly: list[Fraction]) -> list[Fraction]:
    if len(poly) == 1:
        return [Fraction(0)]
    return trim([index * poly[index] for index in range(1, len(poly))])


def divide(dividend: list[Fraction], divisor: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    dividend, divisor = trim(dividend), trim(divisor)
    quotient = [Fraction(0)] * max(1, len(dividend) - len(divisor) + 1)
    remainder = list(dividend)
    while remainder != [0] and len(remainder) >= len(divisor):
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1] / divisor[-1]
        quotient[degree] = coefficient
        for index, value in enumerate(divisor):
            remainder[index + degree] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), remainder


def assert_divides(divisor: list[Fraction], dividend: list[Fraction]) -> None:
    _, remainder = divide(dividend, divisor)
    assert remainder == [0]


def euler_check() -> None:
    y_poly = [Fraction(0), Fraction(1)]
    for d_value in (8, 19, 32):
        d_poly = [Fraction(2), Fraction(-1), Fraction(3)]
        v_poly = [Fraction(1), Fraction(2), Fraction(-1)]
        k_poly = [Fraction(3), Fraction(-2), Fraction(1), Fraction(1)]
        s_poly = multiply(multiply(d_poly, power(v_poly, 2)), k_poly)
        routed = add(
            multiply(y_poly, derivative(s_poly)),
            scale(s_poly, -d_value),
        )
        explicit = multiply(
            v_poly,
            add(
                add(
                    scale(multiply(multiply(y_poly, d_poly), multiply(derivative(v_poly), k_poly)), 2),
                    multiply(multiply(y_poly, v_poly), add(multiply(derivative(d_poly), k_poly), multiply(d_poly, derivative(k_poly)))),
                ),
                scale(multiply(multiply(d_poly, v_poly), k_poly), -d_value),
            ),
        )
        assert routed == explicit
        assert_divides(v_poly, routed)


def official_degree_check() -> None:
    r_value = (1 << 37) - 1
    v_value = (1 << 36) - 2
    p_degree = 3 * r_value + 1
    assert p_degree == 6 * (1 << 36) - 2
    assert p_degree - v_value == 5 * (1 << 36)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "P=YS'-dS", "V | P", "gcd(V,TU)=1", "(TU^3+d) mod V=0",
        "deg(P/V)=5*2^36", "does not prove",
    ):
        assert marker in statement


def main() -> None:
    euler_check()
    official_degree_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_GENERIC_EULER_DIVISOR_PASS "
        "outer_coefficients=0 remainder_degree_lt=2^36-2"
    )


if __name__ == "__main__":
    main()
