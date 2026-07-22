#!/usr/bin/env python3
"""Exact controls for the exceptional MDS-Schur router."""

from __future__ import annotations

from itertools import combinations


def determinant(matrix: list[list[int]], prime: int) -> int:
    work = [row[:] for row in matrix]
    out = 1
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            out = -out
        value = work[column][column]
        out = out * value % prime
        inverse = pow(value, -1, prime)
        for row in range(column + 1, len(work)):
            factor = work[row][column] * inverse % prime
            work[row] = [
                (a - factor * b) % prime
                for a, b in zip(work[row], work[column])
            ]
    return out % prime


def rank(matrix: list[list[int]], prime: int) -> int:
    work = [row[:] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, prime)
        work[pivot_row] = [value * inverse % prime for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                (a - factor * b) % prime
                for a, b in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
    return pivot_row


def minor(generator: list[list[int]], columns: tuple[int, ...], prime: int) -> int:
    return determinant([[row[column] for column in columns] for row in generator], prime)


def main() -> None:
    prime = 101
    e = 3
    blocks = ((1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12))
    columns = [[a * b % prime, -(a + b) % prime, 1] for a, b in blocks]
    generator = [[column[row] for column in columns] for row in range(e)]

    minors = [
        minor(generator, subset, prime)
        for subset in combinations(range(2 * e), e)
    ]
    if any(value == 0 for value in minors):
        raise AssertionError("positive control is not MDS")
    products = [
        [generator[i][k] * generator[j][k] % prime for k in range(2 * e)]
        for i in range(e)
        for j in range(i, e)
    ]
    if rank(products, prime) != 2 * e - 1:
        raise AssertionError("MDS product span did not have dimension 2e-1")

    non_mds = [[1, 1, 0, 0], [0, 0, 1, 1]]
    subset = (0, 1)
    complement = (2, 3)
    if minor(non_mds, subset, prime) or minor(non_mds, complement, prime):
        raise AssertionError("dependent-complement control failed")

    print(
        "RATE_HALF_HANKEL_FORNEY_MDS_SCHUR_ROUTER_PASS "
        f"prime={prime} e={e} product_dimension={2*e-1}"
    )


if __name__ == "__main__":
    main()
