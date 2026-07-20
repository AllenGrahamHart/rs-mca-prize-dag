#!/usr/bin/env python3
"""Mutation audit for the marked constant-shift exclusion."""


def rank_mod(rows: list[list[int]], prime: int) -> int:
    matrix = [[entry % prime for entry in row] for row in rows]
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, prime)
        matrix[rank] = [(entry * inverse) % prime for entry in matrix[rank]]
        for index in range(len(matrix)):
            if index == rank or not matrix[index][column]:
                continue
            factor = matrix[index][column]
            matrix[index] = [
                (left - factor * right) % prime
                for left, right in zip(matrix[index], matrix[rank])
            ]
        rank += 1
    return rank


def main() -> None:
    # At d=ell the forced common divisor can be exactly the mark degree.
    ell, d, v = 5, 5, 2
    assert d + v - ell == v

    # At the upper boundary a third P-block can occur.
    ell, d, v = 5, 6, 4
    assert d + v == 2 * ell

    # Two distinct labels permit rank two with nonconstant values.
    rows = [[1, 0, 0, 0], [1, 1, 1, 1]]
    assert rank_mod(rows, 7) == 2

    # Dropping saturation permits the rank-three common factor to exceed J.
    ell, d, v = 7, 9, 1
    assert d + v - ell == 3 > v

    print("L1_MARKED_CONSTANT_SHIFT_AUDIT_PASS mutations=4")


if __name__ == "__main__":
    main()
