#!/usr/bin/env python3
"""Verify the parity-forced canonical factorization and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization"
PARITY = "rate_half_list_budget_three_antipodal_generic_deleted_pair_parity_reduction"
SPAN = "rate_half_list_budget_three_antipodal_generic_canonical_span_criterion"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 97


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, value in enumerate(left):
        for j, other in enumerate(right):
            answer[i + j] = (answer[i + j] + value * other) % PRIME
    return answer


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return [
        ((left[index] if index < len(left) else 0)
         + (right[index] if index < len(right) else 0))
        % PRIME
        for index in range(size)
    ]


def shift(poly: list[int], amount: int, scale: int = 1) -> list[int]:
    return [0] * amount + [scale * value % PRIME for value in poly]


def power_sums(poly: list[int], limit: int) -> list[int]:
    answer = [0] * (limit + 1)
    for degree in range(1, limit + 1):
        convolution = sum(
            poly[index] * answer[degree - index]
            for index in range(1, degree)
        )
        answer[degree] = (-degree * poly[degree] - convolution) % PRIME
    return answer


def algebra_check() -> None:
    m_value = 2
    h = 2 * m_value + 1
    b_zero = [1, 2, 3, 4]
    c_zero = [1, 5]
    lam, mu = 3, 7
    b2 = multiply(b_zero, b_zero)
    c2 = multiply(c_zero, c_zero)
    first = add(b2, shift(c2, h, lam))
    second = add(b2, shift(c2, h, mu))
    product = multiply(first, second)

    b4 = multiply(b2, b2)
    middle = shift(multiply(b2, c2), h, lam + mu)
    final = shift(multiply(c2, c2), 2 * h, lam * mu)
    assert product == add(add(b4, middle), final)
    assert len(first) - 1 == len(second) - 1 == 4 * m_value - 1
    assert first[0] == second[0] == 1
    assert first[:h] == second[:h]
    first_moments = power_sums(first, h)
    second_moments = power_sums(second, h)
    assert first_moments[1:h] == second_moments[1:h]
    assert (
        first_moments[h] - second_moments[h]
    ) % PRIME == (-h * (lam - mu)) % PRIME

    b_z = [0] * (2 * len(b_zero) - 1)
    c_z = [0] * (2 * len(c_zero) - 1)
    b_z[::2] = b_zero
    c_z[::2] = c_zero
    odd_term = shift(multiply(b_z, multiply(c_z, multiply(c_z, c_z))), 3 * h)
    assert any(odd_term[index] for index in range(1, len(odd_term), 2))
    assert all(odd_term[index] == 0 for index in range(0, len(odd_term), 2))


def wiring_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARITY]["status"] == nodes[SPAN]["status"] == "PROVED"
    assert (PARITY, NODE, "req") in edges
    assert (SPAN, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "beta=0",
        "exact degree `4M-1`",
        "roots partition",
        "1<=j<=2M",
        "-h(lambda-mu)",
        "does not",
    ):
        assert marker in statement


def main() -> None:
    algebra_check()
    wiring_check()
    print(
        "RATE_HALF_ANTIPODAL_GENERIC_DELETED_PAIR_FACTORIZATION_PASS "
        "odd_coefficient=0 factors=2 flat_moments=2M first_difference=h"
    )


if __name__ == "__main__":
    main()
