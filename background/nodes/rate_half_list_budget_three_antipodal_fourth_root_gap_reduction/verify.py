#!/usr/bin/env python3
"""Verify the fourth-root truncation and coefficient-gap reduction."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_fourth_root_gap_reduction"
DEPENDENCY = "rate_half_list_budget_three_antipodal_reverse_residual_stratification"
CONSUMER = "rate_half_list_adjacent_crossing"


def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else Fraction(0))
        + (right[index] if index < len(right) else Fraction(0))
        for index in range(size)
    ])


def scale(poly: list[Fraction], scalar: int) -> list[Fraction]:
    return trim([scalar * coefficient for coefficient in poly])


def multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    answer = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return trim(answer)


def derivative(poly: list[Fraction]) -> list[Fraction]:
    return trim([index * poly[index] for index in range(1, len(poly))] or [Fraction(0)])


def fourth_root_inverse_series(e_poly: list[int], limit: int) -> list[Fraction]:
    answer = [Fraction(1)]
    for m in range(1, limit + 1):
        numerator = sum(
            (4 * m - 3 * j) * e_poly[j] * answer[m - j]
            for j in range(1, min(4, m) + 1)
        )
        answer.append(-numerator / (4 * m))
    return answer


def residual(d_poly: list[Fraction], u_poly: list[Fraction]) -> list[Fraction]:
    r = len(u_poly) - 1
    d = 4 * r + 4
    product = multiply(d_poly, u_poly)
    bracket = add(
        multiply(derivative(d_poly), u_poly),
        scale(multiply(d_poly, derivative(u_poly)), 4),
    )
    return add(scale(product, d), scale([Fraction(0)] + bracket, -1))


def first_nonzero(poly: list[Fraction], start: int = 0) -> int:
    return next(index for index in range(start, len(poly)) if poly[index] != 0)


def algebra_check() -> None:
    fixtures = (
        ([1, 1, 2, -1, 3], 5),
        ([1, -2, 0, 3, 1], 7),
        ([1, 0, 0, 0, 1], 5),
        ([1, 0, 0, 0, 1], 2),
    )
    for e_integer, r in fixtures:
        e_poly = [Fraction(value) for value in e_integer]
        coefficients = fourth_root_inverse_series(e_integer, 4 * r + 4)
        b_poly = coefficients[:r + 1]
        u_poly = list(reversed(b_poly))
        d_poly = list(reversed(e_poly))
        t_poly = residual(d_poly, u_poly)
        assert len(t_poly) - 1 <= 3

        for s in range(r):
            mutation = u_poly.copy()
            mutation[s] += 1
            assert len(residual(d_poly, mutation)) - 1 == s + 4

        b_fourth = multiply(multiply(b_poly, b_poly), multiply(b_poly, b_poly))
        contact_poly = add(multiply(e_poly, b_fourth), [Fraction(-1)])
        contact = first_nonzero(contact_poly, 1)
        omitted = next(
            index
            for index in range(r + 1, len(coefficients))
            if coefficients[index] != 0
        )
        assert contact == omitted

    generic = fourth_root_inverse_series([1, 0, 0, 0, 1], 8)
    assert generic[6] == generic[7] == 0
    assert generic[8] != 0
    intermediate = fourth_root_inverse_series([1, 0, 0, 0, 1], 4)
    assert intermediate[3] == 0
    assert intermediate[4] != 0


def official_arithmetic_check() -> None:
    r = (1 << 37) - 1
    generic_v = (1 << 36) - 2
    intermediate_v = ((1 << 38) - 4) // 3
    assert 2 * (r - generic_v) == r + 3
    assert 3 * (r - intermediate_v) == r + 2


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
        "B(z)=sum_(m=0)^r a_m z^m",
        "4m a_m=-sum_(j=1)^4",
        "a_(r+1)=a_(r+2)=0",
        "a_(r+1)=0",
        "neither proves",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    official_arithmetic_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_FOURTH_ROOT_GAP_PASS "
        "generic_gap=2 intermediate_gap=1 recurrence_width=4"
    )


if __name__ == "__main__":
    main()
