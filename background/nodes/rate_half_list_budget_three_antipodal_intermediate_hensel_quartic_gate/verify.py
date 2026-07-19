#!/usr/bin/env python3
"""Verify the intermediate Hensel quartic and linear-remainder gates."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_intermediate_hensel_quartic_gate"
DEPENDENCY = "rate_half_list_budget_three_antipodal_intermediate_hensel_cubic_gate"
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
    c2_b = multiply(power(c_star, 2, limit), inv_b, limit)
    c3_b2 = multiply(power(c_star, 3, limit), power(inv_b, 2, limit), limit)
    c4_b3 = multiply(power(c_star, 4, limit), power(inv_b, 3, limit), limit)
    d = c2_b[h_value]
    k = c_star[2 * h_value]
    delta_2 = c2_b[2 * h_value]
    gamma_1 = c3_b2[h_value]
    kappa_2 = c_star[3 * h_value]
    coefficient_a = -27 * delta_2 + 27 * gamma_1 * d - 35 * d**2 + 105 * k
    coefficient_b = 81 * kappa_2 - 81 * gamma_1 * k + 105 * d * k
    delta_3 = c2_b[3 * h_value]
    gamma_2 = c3_b2[2 * h_value]
    xi_1 = c4_b3[h_value]
    kappa_3 = c_star[4 * h_value]
    coefficient_c = (
        -81 * delta_3
        + 81 * gamma_2 * d
        - 105 * xi_1 * d**2
        + 315 * xi_1 * k
        + 154 * d**3
        - 924 * d * k
    )
    coefficient_d = (
        243 * kappa_3
        - 243 * gamma_2 * k
        + 315 * xi_1 * d * k
        - 462 * k * d**2
        + 1386 * k**2
    )
    return (
        d, k, delta_2, gamma_1, kappa_2, coefficient_a, coefficient_b,
        delta_3, gamma_2, xi_1, kappa_3, coefficient_c, coefficient_d,
    )


def universal_check() -> None:
    limit = 6
    v_series = [
        Fraction(1), Fraction(-1, 3), Fraction(1, 3),
        Fraction(-35, 81), Fraction(154, 243),
    ]
    left = add(power(v_series, 3, limit), shift(power(v_series, 4, limit), 1, limit), limit)
    assert left[:5] == [1, 0, 0, 0, 0]
    assert left[5] != 0


def fixture_check() -> None:
    for h_value in (3, 4, 6):
        limit = 5 * h_value + 1
        b_poly = [Fraction(1), Fraction(2), Fraction(-1)]
        c_poly = [Fraction(1)] + [
            Fraction((5 * index + h_value) % 13 - 6)
            for index in range(1, 2 * h_value - 1)
        ]
        u_value = Fraction(3 * h_value + 1, h_value + 4)
        inv_b = inverse(b_poly, limit)
        h_series = add(
            power(c_poly, 3, limit),
            scale(shift(multiply(power(c_poly, 4, limit), inv_b, limit), h_value, limit), u_value, limit),
            limit,
        )
        c_star = cube_root_one(h_series, limit)
        values = gates(c_star, b_poly, h_value)
        d, k = values[:2]
        delta_3, gamma_2, xi_1, kappa_3, coefficient_c, coefficient_d = values[7:]
        quartic = (
            243 * kappa_3 - 81 * u_value * delta_3
            + 81 * u_value**2 * gamma_2 - 105 * u_value**3 * xi_1
            + 154 * u_value**4
        )
        assert u_value**2 - d * u_value + 3 * k == 0
        assert quartic == 0
        assert coefficient_c * u_value + coefficient_d == 0


def exceptional_fence_check() -> None:
    p = 59
    c1, c2, c3, c4 = 1, 51, 47, 0
    d, k = 2 * c1 % p, c2
    delta_3 = (2 * c3 + 2 * c1 * c2) % p
    gamma_2 = (3 * c2 + 3 * c1**2) % p
    xi_1, kappa_3 = 4 * c1 % p, c4
    coefficient_a = (51 * c2 - 5 * c1**2) % p
    coefficient_b = (81 * c3 - 33 * c1 * c2) % p
    coefficient_c = (
        -81 * delta_3 + 81 * gamma_2 * d - 105 * xi_1 * d**2
        + 315 * xi_1 * k + 154 * d**3 - 924 * d * k
    ) % p
    coefficient_d = (
        243 * kappa_3 - 243 * gamma_2 * k + 315 * xi_1 * d * k
        - 462 * k * d**2 + 1386 * k**2
    ) % p
    roots = [u for u in range(p) if (u**2 - d * u + 3 * k) % p == 0]
    assert (coefficient_a, coefficient_b) == (0, 0)
    assert roots == [6, 55]
    assert [(coefficient_c * u + coefficient_d) % p for u in roots] == [44, 50]


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
        "(154/243)q^4", "243kappa_3-81uDelta_3", "C u+D=0",
        "test only u=-D/C", "A=B=C=D=0", "This theorem does",
    ):
        assert marker in statement


def main() -> None:
    universal_check()
    fixture_check()
    exceptional_fence_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_INTERMEDIATE_HENSEL_QUARTIC_PASS "
        "universal_terms=5 reduced_degree=1 exceptional_coefficients=4"
    )


if __name__ == "__main__":
    main()
