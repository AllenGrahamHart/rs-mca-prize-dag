#!/usr/bin/env python3
"""Independent finite linear-algebra audit of the six-minor criterion."""

import itertools


PRIME = 29


def rank(rows):
    matrix = [[value % PRIME for value in row] for row in rows]
    pivot = 0
    for column in range(8):
        selected = next((row for row in range(pivot, len(matrix))
                         if matrix[row][column]), None)
        if selected is None:
            continue
        matrix[pivot], matrix[selected] = matrix[selected], matrix[pivot]
        inverse = pow(matrix[pivot][column], -1, PRIME)
        matrix[pivot] = [value * inverse % PRIME for value in matrix[pivot]]
        for row in range(len(matrix)):
            if row != pivot and matrix[row][column]:
                scale = matrix[row][column]
                matrix[row] = [(left - scale * right) % PRIME
                               for left, right in zip(matrix[row], matrix[pivot])]
        pivot += 1
    return pivot


def determinant(rows):
    matrix = [[value % PRIME for value in row] for row in rows]
    value = 1
    for column in range(8):
        selected = next((row for row in range(column, 8)
                         if matrix[row][column]), None)
        if selected is None:
            return 0
        if selected != column:
            matrix[column], matrix[selected] = matrix[selected], matrix[column]
            value = -value
        pivot = matrix[column][column]
        value = value * pivot % PRIME
        inverse = pow(pivot, -1, PRIME)
        for row in range(column + 1, 8):
            scale = matrix[row][column] * inverse % PRIME
            matrix[row] = [(left - scale * right) % PRIME
                           for left, right in zip(matrix[row], matrix[column])]
    return value % PRIME


def main():
    base = [[pow(row + 2, column, PRIME) for column in range(8)]
            for row in range(6)]
    assert rank(base) == 6
    quotient_line = [0, 0, 0, 0, 0, 0, 1, 3]
    rows_rank_seven = [
        [(scale * value) % PRIME for value in quotient_line]
        for scale in (1, 2, 4, 8)
    ]
    assert rank(base + rows_rank_seven) == 7
    assert all(determinant(base + [rows_rank_seven[i], rows_rank_seven[j]]) == 0
               for i, j in itertools.combinations(range(4), 2))
    rows_rank_eight = rows_rank_seven[:]
    rows_rank_eight[-1] = [0, 0, 0, 0, 0, 0, 0, 1]
    assert rank(base + rows_rank_eight) == 8
    assert any(determinant(base + [rows_rank_eight[i], rows_rank_eight[j]]) != 0
               for i, j in itertools.combinations(range(4), 2))
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_COMMON_VIETA_MINOR_AUDIT_PASS "
        "base_rank=6 quotient_dimension=2 pair_minors=6"
    )


if __name__ == "__main__":
    main()
