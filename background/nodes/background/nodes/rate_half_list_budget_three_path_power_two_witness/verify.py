#!/usr/bin/env python3
"""Verify the exact order-sixteen path witness and its DAG edge."""

from __future__ import annotations

import json
from pathlib import Path


P = 17
K = 8
ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_path_power_two_witness"
CONSUMER = "rate_half_list_adjacent_crossing"
DOMAIN = tuple(range(1, 17))
POLYS = (
    (0,),
    (8, 5, 13, 2, 15, 3, 1, 8),
    (12, 16, 8, 3, 7, 12, 10, 4),
    (5, 13, 0, 14, 16, 2, 4, 1),
)
RECEIVED = (4, 14, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 2)
SUPPORTS = (
    (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15),
    (1, 2, 3, 6, 7, 8, 10, 11, 13, 15, 16),
    (1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 16),
    (1, 2, 3, 4, 5, 7, 8, 12, 13, 14, 15),
)
BLOCKS = (
    frozenset((1, 2, 3)),
    frozenset((4, 5, 12)),
    frozenset((7, 8, 13, 15)),
    frozenset((6, 10, 11)),
)


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return tuple(
        ((left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)) % P
        for i in range(size)
    )


def scale(poly: tuple[int, ...], scalar: int) -> tuple[int, ...]:
    return tuple(scalar * value % P for value in poly)


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % P
    return tuple(answer)


def trim(poly: tuple[int, ...]) -> tuple[int, ...]:
    answer = list(poly)
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return tuple(answer)


def locator(roots: frozenset[int]) -> tuple[int, ...]:
    answer = (1,)
    for root in sorted(roots):
        answer = multiply(answer, (-root % P, 1))
    return answer


def evaluate(poly: tuple[int, ...], x: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % P
    return value


def rank(matrix: list[list[int]]) -> int:
    rows = [row[:] for row in matrix]
    pivot_row = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column], -1, P)
        rows[pivot_row] = [inverse * value % P for value in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row and rows[i][column]:
                factor = rows[i][column]
                rows[i] = [
                    (value - factor * pivot_value) % P
                    for value, pivot_value in zip(rows[i], rows[pivot_row], strict=True)
                ]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def intersection_matrix() -> list[list[int]]:
    rows: list[list[int]] = []
    support_sets = tuple(set(support) for support in SUPPORTS)
    for x in DOMAIN:
        members = tuple(i for i, support in enumerate(support_sets) if x in support)
        if len(members) <= 1:
            continue
        base = 0 if 0 in members else members[0]
        powers = tuple(pow(x, degree, P) for degree in range(K))
        for member in members:
            if member == base:
                continue
            row = [0] * (3 * K)
            if member:
                start = (member - 1) * K
                row[start : start + K] = powers
            if base:
                start = (base - 1) * K
                row[start : start + K] = [(-value) % P for value in powers]
            rows.append(row)
    return rows


def main() -> None:
    words = tuple(tuple(evaluate(poly, x) for x in DOMAIN) for poly in POLYS)
    actual = tuple(
        tuple(x for x, left, right in zip(DOMAIN, word, RECEIVED, strict=True) if left == right)
        for word in words
    )
    assert actual == SUPPORTS
    assert all(len(poly) <= K for poly in POLYS)
    assert len(set(words)) == 4
    assert tuple(len(support) for support in actual) == (11, 11, 11, 11)

    membership = {x: tuple(i for i, support in enumerate(actual) if x in support) for x in DOMAIN}
    for omitted, block in enumerate(BLOCKS):
        assert all(membership[x] == tuple(i for i in range(4) if i != omitted) for x in block)
    assert membership[9] == (0, 2)
    assert membership[16] == (1, 2)
    assert membership[14] == (3,)
    assert max(len(set(actual[i]) & set(actual[j])) for i in range(4) for j in range(i + 1, 4)) == 7

    a0, a1, a2, a3 = tuple(locator(block) for block in BLOCKS)
    assert (a0, a1, a2, a3) == (
        (11, 11, 11, 1),
        (15, 9, 13, 1),
        (6, 12, 8, 8, 1),
        (3, 15, 7, 1),
    )
    first_left = add(scale(a2, 8), scale(multiply((1, 1), a0), 13))
    first_right = scale(multiply((8, 1), a1), 4)
    assert trim(first_left) == trim(first_right)
    assert trim(add(scale(a3, 8), scale(a0, 10))) == a1

    p0 = multiply((1, 1), a0)
    p1 = multiply((8, 1), a1)
    p2 = a2
    p3 = multiply((3, 1), a3)
    assert trim(add(scale(p2, 8), scale(p0, 13))) == scale(p1, 4)
    difference = add(p1, scale(p0, -1))
    p3_difference = add(p3, scale(p0, -1))
    pivot = next(i for i, value in enumerate(difference) if value)
    ratio = p3_difference[pivot] * pow(difference[pivot], -1, P) % P
    assert any(p3_difference[i] != ratio * difference[i] % P for i in range(len(difference)))
    assert multiply(multiply(p0, p1), multiply(p2, p3)) == (16,) + (0,) * 15 + (1,)

    matrix = intersection_matrix()
    vector = [coefficient for poly in POLYS[1:] for coefficient in poly]
    assert len(matrix) == 28 and len(matrix[0]) == len(vector) == 24
    assert all(sum(a * b for a, b in zip(row, vector, strict=True)) % P == 0 for row in matrix)
    assert rank(matrix) == 23

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (NODE, CONSUMER, "ev") in edges
    print(
        "RATE_HALF_LIST_BUDGET_THREE_PATH_POWER_TWO_WITNESS_PASS "
        "domain=16 agreement=11x4 type=path rank=23/24 first_pencil_members=3 dag=1/1"
    )


if __name__ == "__main__":
    main()
