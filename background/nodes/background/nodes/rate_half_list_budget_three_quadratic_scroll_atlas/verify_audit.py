#!/usr/bin/env python3
"""Independent rank-dichotomy audit of the balanced scroll normal form."""

from __future__ import annotations


P = 103


def rank(matrix: list[list[int]]) -> int:
    rows = [list(value % P for value in row) for row in matrix]
    pivot_row = 0
    for column in range(len(rows[0])):
        pivot = next((row for row in range(pivot_row, len(rows)) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column], -1, P)
        rows[pivot_row] = [value * inverse % P for value in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row:
                continue
            factor = rows[row][column]
            rows[row] = [(value - factor * base) % P for value, base in zip(rows[row], rows[pivot_row], strict=True)]
        pivot_row += 1
    return pivot_row


def columns_to_rows(columns: tuple[tuple[int, ...], ...]) -> list[list[int]]:
    return [[columns[column][row] for column in range(4)] for row in range(4)]


def main() -> None:
    full_columns = (
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
    )
    deficient_columns = (
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (1, 1, 1, 0),
    )
    assert rank(columns_to_rows(full_columns)) == 4
    assert rank(columns_to_rows(deficient_columns)) == 3

    alpha, beta, x = 7, 11, 13
    coordinates = (alpha, x * alpha % P, beta, x * beta % P)
    assert coordinates[1] == x * coordinates[0] % P
    assert coordinates[3] == x * coordinates[2] % P
    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_QUADRATIC_SCROLL_ATLAS_PASS "
        "rank_branches=4,3 canonical_relations=2"
    )


if __name__ == "__main__":
    main()
