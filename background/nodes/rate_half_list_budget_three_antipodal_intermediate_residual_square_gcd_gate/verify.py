#!/usr/bin/env python3
"""Verify the intermediate residual-square gcd gate."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_intermediate_residual_square_gcd_gate"
DEPENDENCY = "rate_half_list_budget_three_antipodal_intermediate_cube_part_router"
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


def gcd(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    left, right = trim(left), trim(right)
    while right != [0]:
        _, remainder = divide(left, right)
        left, right = right, remainder
    return scale(left, 1 / left[-1])


def assert_divides(divisor: list[Fraction], dividend: list[Fraction]) -> None:
    _, remainder = divide(dividend, divisor)
    assert remainder == [0]


def euler_factor_check() -> None:
    y_poly = [Fraction(0), Fraction(1)]
    for d_value in (8, 13, 32):
        d_poly = [Fraction(2), Fraction(-1), Fraction(3)]
        v_poly = [Fraction(1), Fraction(2), Fraction(-1)]
        k_poly = [Fraction(3), Fraction(-2), Fraction(1)]
        s_poly = multiply(multiply(d_poly, power(v_poly, 3)), k_poly)
        routed = add(
            multiply(y_poly, derivative(s_poly)),
            scale(s_poly, -d_value),
        )
        assert_divides(power(v_poly, 2), routed)


def derivative_gcd_check() -> None:
    for d_value in (7, 19):
        u_poly = [Fraction(1), Fraction(-2), Fraction(1)]
        t_poly = [Fraction(3), Fraction(1), Fraction(2)]
        p_poly = add(multiply(t_poly, power(u_poly, 3)), [Fraction(d_value)])
        w_poly = add(
            multiply(derivative(t_poly), u_poly),
            scale(multiply(t_poly, derivative(u_poly)), 3),
        )
        assert derivative(p_poly) == multiply(power(u_poly, 2), w_poly)
        assert gcd(p_poly, u_poly) == [1]
        assert gcd(p_poly, derivative(p_poly)) == gcd(p_poly, w_poly)

    v_poly = [Fraction(1), Fraction(1)]
    u_poly = [Fraction(1)]
    d_value = 7
    t_poly = add(power(v_poly, 2), [Fraction(-d_value)])
    p_poly = add(multiply(t_poly, power(u_poly, 3)), [Fraction(d_value)])
    w_poly = add(
        multiply(derivative(t_poly), u_poly),
        scale(multiply(t_poly, derivative(u_poly)), 3),
    )
    assert p_poly == power(v_poly, 2)
    assert_divides(v_poly, gcd(p_poly, w_poly))


def annihilator_check() -> None:
    y_poly = [Fraction(0), Fraction(1)]
    for d_value in (32, 64):
        d_poly = [Fraction(1), Fraction(-2), Fraction(3), Fraction(1), Fraction(2)]
        u_poly = [Fraction(1), Fraction(3), Fraction(-1), Fraction(2)]
        a0 = add(scale(d_poly, d_value), scale(multiply(y_poly, derivative(d_poly)), -1))
        t_poly = add(
            multiply(a0, u_poly),
            scale(multiply(multiply(y_poly, d_poly), derivative(u_poly)), -4),
        )
        p_poly = add(multiply(t_poly, power(u_poly, 3)), [Fraction(d_value)])
        w_poly = add(
            multiply(derivative(t_poly), u_poly),
            scale(multiply(t_poly, derivative(u_poly)), 3),
        )
        a_poly = add(
            scale(multiply(multiply(y_poly, d_poly), derivative(t_poly)), 4),
            scale(multiply(t_poly, a0), 3),
        )
        left = scale(multiply(multiply(y_poly, d_poly), w_poly), 4)
        right = add(multiply(u_poly, a_poly), scale(power(t_poly, 2), -3))
        assert left == right
        j_poly = add(scale(power(a_poly, 3), d_value), scale(power(t_poly, 7), 27))
        assert_divides(gcd(p_poly, w_poly), j_poly)

    d_value = 1 << 39
    d_poly = [Fraction(1), Fraction(0), Fraction(-1), Fraction(2), Fraction(3)]
    t_poly = [Fraction(2), Fraction(-1), Fraction(5)]
    a0 = add(scale(d_poly, d_value), scale(multiply(y_poly, derivative(d_poly)), -1))
    a_poly = add(
        scale(multiply(multiply(y_poly, d_poly), derivative(t_poly)), 4),
        scale(multiply(t_poly, a0), 3),
    )
    j_poly = add(scale(power(a_poly, 3), d_value), scale(power(t_poly, 7), 27))
    assert len(a_poly) - 1 == 6
    assert len(j_poly) - 1 == 18


def official_degree_check() -> None:
    s_value = 1 << 37
    d_value = 4 * s_value
    r_value = s_value - 1
    h_value = (s_value + 1) // 3
    v_value = 2 * h_value - 2
    assert v_value == ((1 << 38) - 4) // 3
    assert r_value == 3 * h_value - 2
    assert (r_value + 1) - v_value == h_value + 1
    assert d_value > 3 * r_value + 2
    assert v_value > 18


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
        "P=TU^3+d", "W=T'U+3TU'", "V^2 | P", "P'=U^2W",
        "deg gcd(P,W)>=v=(2^38-4)/3", "gcd(P,W) | J",
        "deg J=18", "boundary is empty",
    ):
        assert marker in statement


def main() -> None:
    euler_factor_check()
    derivative_gcd_check()
    annihilator_check()
    official_degree_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_INTERMEDIATE_RESIDUAL_GCD_PASS "
        "square_divisor=exact gcd_cap=18 boundary=excluded"
    )


if __name__ == "__main__":
    main()
