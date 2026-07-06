#!/usr/bin/env python3
"""Small determinant checks for triangular-minor certificate soundness."""

from __future__ import annotations


def det(matrix: list[list[int]]) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    total = 0
    for col, value in enumerate(matrix[0]):
        sub = [row[:col] + row[col + 1 :] for row in matrix[1:]]
        total += ((-1) ** col) * value * det(sub)
    return total


def diag_product(matrix: list[list[int]]) -> int:
    out = 1
    for i, row in enumerate(matrix):
        out *= row[i]
    return out


def main() -> None:
    upper = [
        [2, 7, -1],
        [0, -3, 5],
        [0, 0, 11],
    ]
    lower = [
        [5, 0, 0, 0],
        [1, -2, 0, 0],
        [9, 3, 7, 0],
        [4, 6, 8, -1],
    ]
    for matrix in (upper, lower):
        assert det(matrix) == diag_product(matrix)
        assert det(matrix) != 0

    zero_diag = [
        [2, 1, 4],
        [0, 0, 3],
        [0, 0, 5],
    ]
    assert det(zero_diag) == 0

    print("PASS: triangular nonzero diagonal gives nonzero determinant")


if __name__ == "__main__":
    main()
