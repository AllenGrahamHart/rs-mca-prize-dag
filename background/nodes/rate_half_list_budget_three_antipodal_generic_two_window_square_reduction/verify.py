#!/usr/bin/env python3
"""Verify the generic two-window square reduction and DAG wiring."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_two_window_square_reduction"
DEPENDENCY = "rate_half_list_budget_three_antipodal_generic_secondary_gap_reduction"
CONSUMER = "rate_half_list_adjacent_crossing"


def add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    return [
        (left[index] if index < len(left) else Fraction(0))
        + (right[index] if index < len(right) else Fraction(0))
        for index in range(size)
    ]


def multiply(
    left: list[Fraction], right: list[Fraction], limit: int | None = None
) -> list[Fraction]:
    size = len(left) + len(right) - 1
    if limit is not None:
        size = min(size, limit)
    answer = [Fraction(0)] * size
    for i, value in enumerate(left):
        for j, other in enumerate(right):
            if i + j >= size:
                break
            answer[i + j] += value * other
    return answer


def derivative(poly: list[Fraction]) -> list[Fraction]:
    return [index * poly[index] for index in range(1, len(poly))]


def inverse(poly: list[Fraction], limit: int) -> list[Fraction]:
    answer = [1 / poly[0]]
    for degree in range(1, limit):
        answer.append(
            -answer[0]
            * sum(
                poly[index] * answer[degree - index]
                for index in range(1, min(degree, len(poly) - 1) + 1)
            )
        )
    return answer


def square_root_one(poly: list[Fraction], limit: int) -> list[Fraction]:
    answer = [Fraction(1)]
    for degree in range(1, limit):
        cross = sum(answer[index] * answer[degree - index] for index in range(1, degree))
        answer.append((poly[degree] - cross) / 2)
    return answer


def fourth_root_inverse(e_poly: list[int], limit: int) -> list[Fraction]:
    answer = [Fraction(1)]
    for degree in range(1, limit):
        numerator = sum(
            (4 * degree - 3 * index) * e_poly[index] * answer[degree - index]
            for index in range(1, min(4, degree) + 1)
        )
        answer.append(-numerator / (4 * degree))
    return answer


def algebra_check() -> None:
    # E=1+z^4 divides 1-z^24 and supplies exact primary and secondary gaps.
    h = 4
    d = 8 * h - 8
    r = 2 * h - 3
    e_poly = [1, 0, 0, 0, 1]
    coefficients = fourth_root_inverse(e_poly, 48)
    assert coefficients[2 * h - 2] == coefficients[2 * h - 1] == 0
    c = coefficients[2 * h]
    assert c == Fraction(5, 32)

    b_poly = coefficients[: r + 1]
    low = coefficients[:h]
    tail = coefficients[2 * h : 3 * h]
    direct_square = [value / c for value in multiply(low, tail, h)]

    quotient = [Fraction(0)] * (d - 3)
    for index in range(d // 4):
        quotient[4 * index] = Fraction((-1) ** index)
    b2 = multiply(b_poly, b_poly)
    b4 = multiply(b2, b2)
    residual = add(quotient, [-value for value in b4])
    rbar = residual[2 * h :]
    alpha = rbar[0]
    original_square = multiply(rbar, inverse(b2, h), h)
    original_square = [value / alpha for value in original_square]
    assert original_square == direct_square

    root = square_root_one(direct_square, h)
    assert root == [Fraction(1), 0, 0, 0]
    assert root[h - 2] == root[h - 1] == 0

    mutation = direct_square.copy()
    mutation[h - 2] += 2
    mutated_root = square_root_one(mutation, h)
    assert mutated_root[h - 2] == 1

    # Check the differential tail identity beyond the claimed window.
    e_fraction = list(map(Fraction, e_poly))
    k_poly = add(
        multiply(derivative(e_fraction), b_poly),
        [4 * value for value in multiply(e_fraction, derivative(b_poly))],
    )
    full_tail = coefficients[2 * h :]
    first_factor = add(
        [Fraction(0)] + derivative(e_fraction),
        [8 * h * value for value in e_fraction],
    )
    bracket = add(
        multiply(first_factor, full_tail),
        [Fraction(0)] + [4 * value for value in multiply(e_fraction, derivative(full_tail))],
    )
    assert all(value == 0 for value in bracket[2:24])
    expected_k = [Fraction(0)] * (2 * h - 1) + [-bracket[0], -bracket[1]]
    assert add(k_poly, [-value for value in expected_k])[: 2 * h + 1] == [
        Fraction(0)
    ] * (2 * h + 1)


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
        "P^2 = L T/c mod z^h",
        "L T=c C^2 mod z^h",
        "linear differential forcing",
        "does not exclude",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_GENERIC_TWO_WINDOW_SQUARE_PASS "
        "windows=2 modulus=h differential_forcing_degree=1 mutation=1"
    )


if __name__ == "__main__":
    main()
