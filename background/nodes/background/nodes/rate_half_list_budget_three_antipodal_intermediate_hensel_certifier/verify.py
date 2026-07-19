#!/usr/bin/env python3
"""Verify the intermediate Hensel certifier and DAG wiring."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_intermediate_hensel_certifier"
DEPENDENCY = "rate_half_list_budget_three_antipodal_fourth_root_gap_reduction"
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
    for i, a in enumerate(left[:limit]):
        for j, b in enumerate(right[:limit - i]):
            answer[i + j] += a * b
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
    for m in range(1, limit):
        total = sum(
            poly[j] * answer[m - j]
            for j in range(1, min(m, len(poly) - 1) + 1)
        )
        answer.append(-total / poly[0])
    return answer


def cube_root_one(poly: list[Fraction], limit: int) -> list[Fraction]:
    assert poly[0] == 1
    answer = [Fraction(1)]
    for m in range(1, limit):
        trial = pad(answer + [Fraction(0)], m + 1)
        known = power(trial, 3, m + 1)[m]
        answer.append((poly[m] - known) / 3)
    return answer


def hensel_solution(
    h_series: list[Fraction],
    b_poly: list[Fraction],
    u_value: Fraction,
    h: int,
    limit: int,
) -> list[Fraction]:
    inv_b = inverse(b_poly, limit)
    answer = [Fraction(1)]
    for m in range(1, limit):
        trial = pad(answer + [Fraction(0)], m + 1)
        cubic = power(trial, 3, m + 1)
        quartic_over_b = multiply(power(trial, 4, m + 1), inv_b, m + 1)
        known = cubic[m]
        if m >= h:
            known += u_value * quartic_over_b[m - h]
        answer.append((h_series[m] - known) / 3)
    return answer


def exact_hensel_check() -> None:
    nondegenerate = 0
    for h in (3, 4, 6, 9):
        limit = 3 * h + 3
        b_poly = [Fraction(1), Fraction(2), Fraction(-1), Fraction(3)]
        c_poly = [Fraction(1)] + [
            Fraction((5 * index + h) % 7 - 3)
            for index in range(1, 2 * h - 1)
        ]
        u_value = Fraction(2 * h + 1, h + 2)
        c3 = power(c_poly, 3, limit)
        c4_over_b = multiply(power(c_poly, 4, limit), inverse(b_poly, limit), limit)
        h_series = add(c3, scale(shift(c4_over_b, h, limit), u_value, limit), limit)

        c_star = cube_root_one(h_series, limit)
        quotient = multiply(power(c_star, 2, limit), inverse(b_poly, limit), limit)
        delta = quotient[h - 1]
        kappa = c_star[2 * h - 1]
        assert 3 * kappa - u_value * delta == 0

        solved = hensel_solution(h_series, b_poly, u_value, h, limit)
        assert solved == pad(c_poly, limit)
        predicted = add(
            c_star,
            scale(shift(quotient, h, limit), -u_value / 3, limit),
            2 * h,
        )
        assert predicted == solved[:2 * h]
        if delta != 0:
            assert 3 * kappa / delta == u_value
            nondegenerate += 1
    assert nondegenerate >= 2


def degeneracy_check() -> None:
    for h in (3, 5, 8):
        limit = 2 * h + 2
        b_poly = [Fraction(1)]
        c_poly = [Fraction(1)]
        u_value = Fraction(7, 3)
        h_series = add(
            power(c_poly, 3, limit),
            scale(shift(power(c_poly, 4, limit), h, limit), u_value, limit),
            limit,
        )
        c_star = cube_root_one(h_series, limit)
        quotient = power(c_star, 2, limit)
        assert quotient[h - 1] == 0
        assert c_star[2 * h - 1] == 0
        assert hensel_solution(h_series, b_poly, u_value, h, limit) == pad(c_poly, limit)

        impossible_star = [Fraction(1)] + [Fraction(0)] * (2 * h - 2) + [Fraction(1)]
        impossible_h = power(impossible_star, 3, limit)
        recovered = cube_root_one(impossible_h, limit)
        assert recovered[h - 1] == 0
        assert recovered[2 * h - 1] == 1


def official_arithmetic_check() -> None:
    s = 1 << 37
    h = (s + 1) // 3
    r = s - 1
    v = 2 * h - 2
    assert 3 * h == s + 1
    assert r == 3 * h - 2
    assert v == ((1 << 38) - 4) // 3
    assert h == 45_812_984_491


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
        "3 kappa-u Delta=0",
        "u=3kappa/Delta is unique",
        "terminal gate leaves one scalar",
        "also sufficient to reconstruct",
        "does not prove that every candidate rejects",
    ):
        assert marker in statement


def main() -> None:
    exact_hensel_check()
    degeneracy_check()
    official_arithmetic_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_INTERMEDIATE_HENSEL_PASS "
        "terminal_gate_linear=1 branches=unique,empty,one_parameter"
    )


if __name__ == "__main__":
    main()
