#!/usr/bin/env python3
"""Verify the intermediate Hensel cubic and linear-remainder gates."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_intermediate_hensel_cubic_gate"
DEPENDENCY = "rate_half_list_budget_three_antipodal_intermediate_hensel_quadratic_gate"
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


def gates(c_star: list[Fraction], b_poly: list[Fraction], h_value: int) -> tuple[Fraction, ...]:
    limit = len(c_star)
    inv_b = inverse(b_poly, limit)
    cstar2_over_b = multiply(power(c_star, 2, limit), inv_b, limit)
    cstar3_over_b2 = multiply(power(c_star, 3, limit), power(inv_b, 2, limit), limit)
    delta_1 = cstar2_over_b[h_value]
    kappa_1 = c_star[2 * h_value]
    delta_2 = cstar2_over_b[2 * h_value]
    gamma_1 = cstar3_over_b2[h_value]
    kappa_2 = c_star[3 * h_value]
    coefficient_a = (
        -27 * delta_2
        + 27 * gamma_1 * delta_1
        - 35 * delta_1**2
        + 105 * kappa_1
    )
    coefficient_b = (
        81 * kappa_2
        - 81 * gamma_1 * kappa_1
        + 105 * delta_1 * kappa_1
    )
    return delta_1, kappa_1, delta_2, gamma_1, kappa_2, coefficient_a, coefficient_b


def universal_check() -> None:
    limit = 5
    v_series = [
        Fraction(1),
        Fraction(-1, 3),
        Fraction(1, 3),
        Fraction(-35, 81),
    ]
    left = multiply(
        power(v_series, 3, limit),
        add([1], shift(v_series, 1, limit), limit),
        limit,
    )
    assert left[:4] == [1, 0, 0, 0]
    assert left[4] != 0


def fixture_check() -> None:
    for h_value in (3, 4, 6):
        limit = 4 * h_value + 1
        b_poly = [Fraction(1), Fraction(2), Fraction(-1)]
        c_poly = [Fraction(1)] + [
            Fraction((5 * index + h_value) % 13 - 6)
            for index in range(1, 2 * h_value - 1)
        ]
        u_value = Fraction(3 * h_value + 1, h_value + 4)
        inv_b = inverse(b_poly, limit)
        h_series = add(
            power(c_poly, 3, limit),
            scale(
                shift(multiply(power(c_poly, 4, limit), inv_b, limit), h_value, limit),
                u_value,
                limit,
            ),
            limit,
        )
        c_star = cube_root_one(h_series, limit)
        delta_1, kappa_1, delta_2, gamma_1, kappa_2, coefficient_a, coefficient_b = gates(
            c_star, b_poly, h_value
        )
        quadratic = u_value**2 - delta_1 * u_value + 3 * kappa_1
        cubic = (
            81 * kappa_2
            - 27 * delta_2 * u_value
            + 27 * gamma_1 * u_value**2
            - 35 * u_value**3
        )
        assert quadratic == cubic == 0
        assert coefficient_a * u_value + coefficient_b == 0


def degenerate_selector_check() -> None:
    for h_value in (3, 5, 8):
        limit = 4 * h_value + 1
        u_value = Fraction(7, 3)
        h_series = [Fraction(1)] + [Fraction(0)] * (limit - 1)
        h_series[h_value] = u_value
        c_star = cube_root_one(h_series, limit)
        delta_1, kappa_1, _, _, _, coefficient_a, coefficient_b = gates(
            c_star, [Fraction(1)], h_value
        )
        other_root = -u_value / 3
        assert u_value**2 - delta_1 * u_value + 3 * kappa_1 == 0
        assert other_root**2 - delta_1 * other_root + 3 * kappa_1 == 0
        assert coefficient_a != 0
        assert -coefficient_b / coefficient_a == u_value
        assert coefficient_a * other_root + coefficient_b != 0


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
        "-(35/81)q^3",
        "81kappa_2-27uDelta_2+27u^2Gamma_1-35u^3=0",
        "A u+B=0",
        "test only u=-B/A",
        "A=0, B=0",
        "does not prove",
    ):
        assert marker in statement


def main() -> None:
    universal_check()
    fixture_check()
    degenerate_selector_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_INTERMEDIATE_HENSEL_CUBIC_PASS "
        "universal_terms=4 reduced_degree=1 exceptional_coefficients=2"
    )


if __name__ == "__main__":
    main()
