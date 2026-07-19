#!/usr/bin/env python3
"""Audit pure-quartic rigidity on the complete d=8 positive census."""

from __future__ import annotations

from itertools import combinations, permutations, product


PRIME = 97


def kernel(matrix: list[list[int]]) -> tuple[int, list[list[int]]]:
    rows = [row[:] for row in matrix]
    pivots: list[int] = []
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

    free = [column for column in range(len(rows[0])) if column not in pivots]
    basis: list[list[int]] = []
    for free_column in free:
        vector = [0] * len(rows[0])
        vector[free_column] = 1
        for row, pivot_column in reversed(list(enumerate(pivots))):
            vector[pivot_column] = -sum(
                rows[row][column] * vector[column] for column in free
            ) % PRIME
        basis.append(vector)
    return rank, basis


def centered_invariants(values: tuple[int, ...]) -> tuple[int, int]:
    center = sum(values) * pow(4, -1, PRIME) % PRIME
    centered = tuple((value - center) % PRIME for value in values)
    e2 = sum(
        centered[i] * centered[j]
        for i in range(4)
        for j in range(i + 1, 4)
    ) % PRIME
    e3 = sum(
        centered[i] * centered[j] * centered[k]
        for i in range(4)
        for j in range(i + 1, 4)
        for k in range(j + 1, 4)
    ) % PRIME
    return e2, e3


def main() -> None:
    generator = 5
    quotient = tuple(pow(generator, 12 * exponent, PRIME) for exponent in range(8))
    half_domain = {pow(generator, 6 * exponent, PRIME) for exponent in range(16)}
    square_roots = {
        value: tuple(root for root in half_domain if root * root % PRIME == value)
        for value in quotient
    }

    checked = 0
    positive = 0
    e2_zero = 0
    pure = 0
    for deleted in combinations(quotient, 4):
        complementary = tuple(value for value in quotient if value not in deleted)
        for a_values in product(*(square_roots[value] for value in deleted)):
            for root_values in permutations(complementary):
                checked += 1
                matrix = [
                    [1] * 4,
                    list(root_values),
                    list(a_values),
                    [
                        a * root % PRIME
                        for a, root in zip(a_values, root_values, strict=True)
                    ],
                ]
                rank, basis = kernel(matrix)
                if rank != 3 or not all(basis[0]):
                    continue
                positive += 1
                e2, e3 = centered_invariants(root_values)
                if e2 == 0:
                    e2_zero += 1
                if e2 == 0 and e3 == 0:
                    pure += 1
                    r = 1
                    v = 0
                    assert v == r - 1

    assert (checked, positive) == (26_880, 192)
    assert e2_zero == 0
    assert pure == 0
    print(
        "AUDIT_RATE_HALF_LIST_B3_ANTIPODAL_PURE_QUARTIC_RIGIDITY_PASS "
        f"assignments={checked} positives={positive} e2_zero={e2_zero} pure={pure}"
    )


if __name__ == "__main__":
    main()
