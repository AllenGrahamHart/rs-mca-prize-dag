#!/usr/bin/env python3
"""Verify the antipodal Möbius weld and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_mobius_weld"
DEPENDENCY = "rate_half_list_budget_three_fiber_four_antipodal_descent"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 1_000_003


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    answer = [0] * size
    for index in range(size):
        answer[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % PRIME
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def scale(polynomial: list[int], scalar: int) -> list[int]:
    return [scalar * value % PRIME for value in polynomial]


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % PRIME
    return answer


def null_vector(matrix: list[list[int]]) -> list[int]:
    rows = [row[:] for row in matrix]
    pivots = []
    rank = 0
    for column in range(len(rows[0])):
        pivot = next(
            (row for row in range(rank, len(rows)) if rows[row][column]), None
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], PRIME - 2, PRIME)
        rows[rank] = [value * inverse % PRIME for value in rows[rank]]
        for row in range(len(rows)):
            if row != rank and rows[row][column]:
                factor = rows[row][column]
                rows[row] = [
                    (left - factor * right) % PRIME
                    for left, right in zip(rows[row], rows[rank], strict=True)
                ]
        pivots.append(column)
        rank += 1
    assert rank == len(rows[0]) - 1
    free = next(column for column in range(len(rows[0])) if column not in pivots)
    answer = [0] * len(rows[0])
    answer[free] = 1
    for row, pivot in reversed(list(enumerate(pivots))):
        answer[pivot] = -rows[row][free] % PRIME
    return answer


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    a_values = (1, 2, 3, 4)
    alpha, beta, gamma, delta = 2, 3, 5, 7
    assert (alpha * delta - beta * gamma) % PRIME != 0
    c_values = tuple(
        (alpha * a + beta) * pow(gamma * a + delta, PRIME - 2, PRIME) % PRIME
        for a in a_values
    )
    assert len(set(c_values)) == 4

    matrix = [
        [1] * 4,
        list(a_values),
        list(c_values),
        [a * c % PRIME for a, c in zip(a_values, c_values, strict=True)],
    ]
    lambdas = null_vector(matrix)
    assert all(lambdas)

    u_polynomial = [1, 2, 0, 1]
    v_polynomial = [6, 4, 1]
    g_values = [
        add(u_polynomial, scale(v_polynomial, c)) for c in c_values
    ]
    first = [0]
    second = [0]
    for a, coefficient, g in zip(a_values, lambdas, g_values, strict=True):
        first = add(first, scale(g, coefficient))
        second = add(second, scale(g, coefficient * a))
    assert first == [0] and second == [0]

    r_polynomial = add(scale(u_polynomial, delta), scale(v_polynomial, beta))
    s_polynomial = add(scale(u_polynomial, gamma), scale(v_polynomial, alpha))
    left_product = [1]
    right_product = [1]
    kappa = 1
    for a, g in zip(a_values, g_values, strict=True):
        left_product = multiply(left_product, add(r_polynomial, scale(s_polynomial, a)))
        right_product = multiply(right_product, g)
        kappa = kappa * (gamma * a + delta) % PRIME
    assert left_product == scale(right_product, kappa)
    packet_check()
    print(
        "RATE_HALF_LIST_B3_ANTIPODAL_MOBIUS_WELD_PASS "
        "paired_points=4 relations=2 norm_factors=4"
    )


if __name__ == "__main__":
    main()
