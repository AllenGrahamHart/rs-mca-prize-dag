#!/usr/bin/env python3
"""Verify the intermediate Hensel quadratic gate."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_intermediate_hensel_quadratic_gate"
DEPENDENCY = "rate_half_list_budget_three_antipodal_intermediate_hensel_certifier"
CONSUMER = "rate_half_list_adjacent_crossing"


def pad(poly: list[Fraction], limit: int) -> list[Fraction]:
    return (poly + [Fraction(0)] * limit)[:limit]


def add(left: list[Fraction], right: list[Fraction], limit: int) -> list[Fraction]:
    left = pad(left, limit)
    right = pad(right, limit)
    return [left[index] + right[index] for index in range(limit)]


def scale(poly: list[Fraction], scalar: Fraction, limit: int) -> list[Fraction]:
    return [scalar * value for value in pad(poly, limit)]


def multiply(left: list[Fraction], right: list[Fraction], limit: int) -> list[Fraction]:
    answer = [Fraction(0)] * limit
    for i, left_value in enumerate(left[:limit]):
        for j, right_value in enumerate(right[: limit - i]):
            answer[i + j] += left_value * right_value
    return answer


def power(poly: list[Fraction], exponent: int, limit: int) -> list[Fraction]:
    answer = [Fraction(1)]
    for _ in range(exponent):
        answer = multiply(answer, poly, limit)
    return pad(answer, limit)


def shift(poly: list[Fraction], amount: int, limit: int) -> list[Fraction]:
    return pad([Fraction(0)] * amount + poly, limit)


def inverse(poly: list[Fraction], limit: int) -> list[Fraction]:
    assert poly[0] != 0
    answer = [1 / poly[0]]
    for degree in range(1, limit):
        total = sum(
            poly[index] * answer[degree - index]
            for index in range(1, min(degree, len(poly) - 1) + 1)
        )
        answer.append(-total / poly[0])
    return answer


def cube_root_one(poly: list[Fraction], limit: int) -> list[Fraction]:
    assert poly[0] == 1
    answer = [Fraction(1)]
    for degree in range(1, limit):
        trial = pad(answer + [Fraction(0)], degree + 1)
        known = power(trial, 3, degree + 1)[degree]
        answer.append((poly[degree] - known) / 3)
    return answer


def universal_check() -> None:
    limit = 4
    v_series = [Fraction(1), Fraction(-1, 3), Fraction(1, 3)]
    qv = shift(v_series, 1, limit)
    left = multiply(power(v_series, 3, limit), add([1], qv, limit), limit)
    assert left[:3] == [1, 0, 0]
    assert left[3] != 0


def fixture_check() -> None:
    nondegenerate = 0
    for h_value in (3, 4, 6, 9):
        limit = 3 * h_value
        b_poly = [Fraction(1), Fraction(2), Fraction(-1)]
        c_poly = [Fraction(1)] + [
            Fraction((7 * index + h_value) % 11 - 5)
            for index in range(1, 2 * h_value - 1)
        ]
        u_value = Fraction(2 * h_value + 1, h_value + 3)
        inv_b = inverse(b_poly, limit)
        c3 = power(c_poly, 3, limit)
        c4_over_b = multiply(power(c_poly, 4, limit), inv_b, limit)
        h_series = add(c3, scale(shift(c4_over_b, h_value, limit), u_value, limit), limit)
        c_star = cube_root_one(h_series, limit)
        cstar2_over_b = multiply(power(c_star, 2, limit), inv_b, limit)

        delta = cstar2_over_b[h_value - 1]
        kappa = c_star[2 * h_value - 1]
        delta_1 = cstar2_over_b[h_value]
        kappa_1 = c_star[2 * h_value]
        assert 3 * kappa - u_value * delta == 0
        assert u_value**2 - u_value * delta_1 + 3 * kappa_1 == 0
        if delta != 0:
            assert 3 * kappa / delta == u_value
            nondegenerate += 1
    assert nondegenerate >= 2


def sharp_degenerate_check() -> None:
    for h_value in (3, 5, 8):
        limit = 3 * h_value
        u_value = Fraction(7, 3)
        h_series = [Fraction(1)] + [Fraction(0)] * (limit - 1)
        h_series[h_value] = u_value
        c_star = cube_root_one(h_series, limit)
        c_star_squared = power(c_star, 2, limit)
        delta = c_star_squared[h_value - 1]
        kappa = c_star[2 * h_value - 1]
        assert delta == kappa == 0

        delta_1 = c_star_squared[h_value]
        kappa_1 = c_star[2 * h_value]
        polynomial = [3 * kappa_1, -delta_1, Fraction(1)]
        assert sum(polynomial[index] * u_value**index for index in range(3)) == 0
        other_root = -u_value / 3
        assert sum(polynomial[index] * other_root**index for index in range(3)) == 0
        assert u_value != other_root


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
        "V^3(1+qV)=1",
        "V=1-q/3+q^2/3 mod q^3",
        "u^2-uDelta_1+3kappa_1=0",
        "test at most the two roots",
        "never retains a free scalar",
        "does not prove",
    ):
        assert marker in statement


def main() -> None:
    universal_check()
    fixture_check()
    sharp_degenerate_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_INTERMEDIATE_HENSEL_QUADRATIC_PASS "
        "forbidden_coefficients=2 degenerate_candidates=2"
    )


if __name__ == "__main__":
    main()
