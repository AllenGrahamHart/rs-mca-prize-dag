#!/usr/bin/env python3
"""Verify the intermediate cube-part and exact cofactor router."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_intermediate_cube_part_router"
DEPENDENCY = "rate_half_list_budget_three_antipodal_intermediate_hensel_certifier"
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


def shift(poly: list[Fraction], amount: int) -> list[Fraction]:
    return [Fraction(0)] * amount + poly


def divide(dividend: list[Fraction], divisor: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    dividend = trim(dividend)
    divisor = trim(divisor)
    if divisor == [0]:
        raise ZeroDivisionError
    if len(dividend) < len(divisor):
        return [Fraction(0)], dividend
    quotient = [Fraction(0)] * (len(dividend) - len(divisor) + 1)
    remainder = list(dividend)
    while remainder != [0] and len(remainder) >= len(divisor):
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1] / divisor[-1]
        quotient[degree] = coefficient
        for index, value in enumerate(divisor):
            remainder[index + degree] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), remainder


def derivative(poly: list[Fraction]) -> list[Fraction]:
    if len(poly) == 1:
        return [Fraction(0)]
    return trim([index * poly[index] for index in range(1, len(poly))])


def gcd(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    left, right = trim(left), trim(right)
    while right != [0]:
        _, remainder = divide(left, right)
        left, right = right, remainder
    return scale(left, 1 / left[-1])


def assert_divides(divisor: list[Fraction], dividend: list[Fraction]) -> None:
    _, remainder = divide(dividend, divisor)
    assert remainder == [0]


def fixture(c_poly: list[Fraction], h_value: int, u_value: Fraction) -> None:
    theta = Fraction(7, 3)
    b_poly = [Fraction(1), Fraction(2), Fraction(0), Fraction(1)]
    assert gcd(b_poly, c_poly) == [1]
    ell = add(b_poly, scale(shift(c_poly, h_value), u_value))
    residual = scale(multiply(power(c_poly, 3), ell), theta)
    assert gcd(c_poly, ell) == [1]
    assert_divides(power(c_poly, 3), residual)
    assert_divides(power(c_poly, 2), gcd(residual, derivative(residual)))
    second_gcd = gcd(gcd(residual, derivative(residual)), derivative(derivative(residual)))
    assert_divides(c_poly, second_gcd)

    quotient, remainder = divide(residual, scale(power(c_poly, 3), theta))
    assert remainder == [0]
    recovered, remainder = divide(add(quotient, scale(b_poly, -1)), shift(c_poly, h_value))
    assert remainder == [0] and recovered == [u_value]


def algebra_check() -> None:
    fixture([Fraction(1), Fraction(-1)], 3, Fraction(5, 2))
    fixture(power([Fraction(1), Fraction(-1)], 2), 5, Fraction(-4, 7))

    c_poly = [Fraction(1), Fraction(1)]
    b_poly = [Fraction(1), Fraction(0), Fraction(1)]
    h_value = 2
    ell = [Fraction(1), Fraction(3), Fraction(1)]
    residual = multiply(power(c_poly, 3), ell)
    assert_divides(power(c_poly, 3), residual)
    quotient, remainder = divide(residual, power(c_poly, 3))
    assert remainder == [0]
    _, remainder = divide(add(quotient, scale(b_poly, -1)), shift(c_poly, h_value))
    assert remainder != [0]


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
        "Rbar=theta C^3 L", "gcd(B,C)=gcd(C,L)=1", "C | Cube(Rbar)",
        "C^2 | gcd(Rbar,Rbar')", "L_C-B=u z^h C", "does not bound",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_INTERMEDIATE_CUBE_PART_PASS "
        "cube_factor=exact derivative_gates=2 cofactor_classifier=exact"
    )


if __name__ == "__main__":
    main()
