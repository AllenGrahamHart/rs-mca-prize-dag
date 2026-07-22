#!/usr/bin/env python3
"""Exact checks for the weighted self-dual evaluation-code law."""

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
        pivot_value = work[column][column]
        out = out * pivot_value % prime
        inverse = pow(pivot_value, -1, prime)
        for row in range(column + 1, len(work)):
            factor = work[row][column] * inverse % prime
            for index in range(column, len(work)):
                work[row][index] = (
                    work[row][index] - factor * work[column][index]
                ) % prime
    return out % prime


def minor(generator: list[list[int]], columns: tuple[int, ...], prime: int) -> int:
    return determinant([[row[column] for column in columns] for row in generator], prime)


def main() -> None:
    prime = 101
    e = 2
    root_minus_one = 10
    weights = [1, 1, 1, 1]
    generator = [
        [1, 0, root_minus_one, 0],
        [0, 1, 0, root_minus_one],
    ]

    gram = [
        [
            sum(weights[k] * generator[i][k] * generator[j][k] for k in range(2 * e))
            % prime
            for j in range(e)
        ]
        for i in range(e)
    ]
    if any(value for row in gram for value in row):
        raise AssertionError("weighted code is not self-orthogonal")

    universe = tuple(range(2 * e))
    checked = 0
    for subset in combinations(universe, e):
        complement = tuple(index for index in universe if index not in subset)
        delta_i = minor(generator, subset, prime)
        delta_j = minor(generator, complement, prime)
        beta_i = 1
        beta_j = 1
        for index in subset:
            beta_i = beta_i * weights[index] % prime
        for index in complement:
            beta_j = beta_j * weights[index] % prime
        left = delta_j * delta_j * beta_j % prime
        right = pow(-1, e, prime) * delta_i * delta_i * beta_i % prime
        if left != right or bool(delta_i) != bool(delta_j):
            raise AssertionError("complementary minor law failed")
        checked += 1

    print(
        "RATE_HALF_HANKEL_EXCEPTIONAL_SELF_DUAL_CODE_PASS "
        f"prime={prime} e={e} subsets={checked}"
    )


if __name__ == "__main__":
    main()
