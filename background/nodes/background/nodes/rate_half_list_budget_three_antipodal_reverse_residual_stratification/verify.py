#!/usr/bin/env python3
"""Verify the antipodal reverse-residual theorem and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_reverse_residual_stratification"
DEPENDENCY = "rate_half_list_budget_three_antipodal_pencil_degree_floor"
CONSUMER = "rate_half_list_adjacent_crossing"


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * coefficient for coefficient in poly])


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return trim(answer)


def derivative(poly: list[int]) -> list[int]:
    return trim([index * poly[index] for index in range(1, len(poly))] or [0])


def reverse_at_degree(poly: list[int], degree: int) -> list[int]:
    assert len(poly) <= degree + 1
    return list(reversed(poly + [0] * (degree + 1 - len(poly))))


def polynomial_identity_check() -> None:
    fixtures = (
        ([2, -1, 3, 4, 1], [1, 2, -1, 1]),
        ([-3, 5, 0, -2, 1], [4, 0, 3, -2, 1]),
        ([7, -4, 2, 1, 1], [-2, 5, 0, 1]),
    )
    for deleted, u_poly in fixtures:
        r = len(u_poly) - 1
        d = 4 * r + 4
        du = multiply(deleted, u_poly)
        bracket = add(
            multiply(derivative(deleted), u_poly),
            scale(multiply(deleted, derivative(u_poly)), 4),
        )
        residual = add(scale(du, d), scale([0] + bracket, -1))
        assert len(residual) - 1 <= r + 3

        e_reverse = list(reversed(deleted))
        b_reverse = list(reversed(u_poly))
        k_poly = add(
            multiply(derivative(e_reverse), b_reverse),
            scale(multiply(e_reverse, derivative(b_reverse)), 4),
        )
        assert reverse_at_degree(residual, r + 3) == k_poly


def arithmetic_check() -> None:
    for r in range(1, 257):
        for q in (2, 3, 4):
            minimum_v = max(0, ((q - 1) * r - 4 + q - 1) // q)
            for v in range(minimum_v, r):
                residual_degree = r + 4 - q * (r - v)
                assert residual_degree >= 0
                assert residual_degree == (
                    r + 4 - q * (r - minimum_v)
                    + q * (v - minimum_v)
                )
            if minimum_v > 0:
                assert r + 4 - q * (r - minimum_v + 1) < 0

    r = (1 << 37) - 1
    generic_v = (1 << 36) - 2
    intermediate_v = ((1 << 38) - 4) // 3
    assert r + 4 - 2 * (r - generic_v) == 1
    assert r + 4 - 3 * (r - intermediate_v) == 2
    assert r + 4 - 2 * (r - generic_v + 1) == -1
    assert r + 4 - 3 * (r - intermediate_v + 1) == -1


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
        "deg T=r+4-qh",
        "exceptional-root count is at most one",
        "exceptional-root count is at most two",
        "does not exclude",
    ):
        assert marker in statement


def main() -> None:
    polynomial_identity_check()
    arithmetic_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_REVERSE_RESIDUAL_PASS "
        "generic_boundary_degree=1 intermediate_boundary_degree=2"
    )


if __name__ == "__main__":
    main()
