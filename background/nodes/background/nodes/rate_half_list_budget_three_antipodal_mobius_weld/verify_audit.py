#!/usr/bin/env python3
"""Audit the Möbius graph on one exact d=8 positive."""

from __future__ import annotations


PRIME = 97


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
        inverse = pow(rows[rank][column], -1, PRIME)
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


def main() -> None:
    a_values = (1, 8, 33, 79)
    root_values = (50, 47, 96, 75)
    relation = (70, 17, 9, 1)
    graph_matrix = [
        [
            a,
            1,
            -root * a % PRIME,
            -root % PRIME,
        ]
        for a, root in zip(a_values, root_values, strict=True)
    ]
    alpha, beta, gamma, delta = null_vector(graph_matrix)
    assert (alpha * delta - beta * gamma) % PRIME != 0
    for a, root in zip(a_values, root_values, strict=True):
        denominator = (gamma * a + delta) % PRIME
        assert denominator
        assert (alpha * a + beta) * pow(denominator, -1, PRIME) % PRIME == root

    rows = (
        (1, 1, 1, 1),
        a_values,
        root_values,
        tuple(a * root % PRIME for a, root in zip(a_values, root_values, strict=True)),
    )
    assert all(
        sum(coefficient * value for coefficient, value in zip(relation, row, strict=True))
        % PRIME
        == 0
        for row in rows
    )
    print(
        "AUDIT_RATE_HALF_LIST_B3_ANTIPODAL_MOBIUS_WELD_PASS "
        "field=97 quotient_order=8 graph_points=4 relation_support=4"
    )


if __name__ == "__main__":
    main()
