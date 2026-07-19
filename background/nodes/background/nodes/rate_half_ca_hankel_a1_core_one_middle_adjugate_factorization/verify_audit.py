#!/usr/bin/env python3
"""Audit canonical symmetric minimal-index rank profiles."""

from __future__ import annotations


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(rank, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, prime)
        work[rank] = [(value * inverse) % prime for value in work[rank]]
        for i, row in enumerate(work):
            if i == rank or not row[column]:
                continue
            factor = row[column]
            work[i] = [
                (left - factor * right) % prime
                for left, right in zip(row, work[rank])
            ]
        rank += 1
    return rank


def block(index: int, u: int, v: int, regular: int) -> list[list[int]]:
    size = 2 * index + 2
    matrix = [[0] * size for _ in range(size)]
    for row in range(index):
        matrix[row][index + row] = v
        matrix[index + row][row] = v
        matrix[row][index + row + 1] = -u
        matrix[index + row + 1][row] = -u
    matrix[-1][-1] = regular
    return matrix


def main() -> None:
    checks = 0
    prime = 1009
    for index in range(1, 12):
        d = 2 * index + 1
        for u in range(1, 5):
            for v in range(1, 4):
                regular = (13 * u + 17 * v) % prime
                assert regular
                assert rank_mod(block(index, u, v, regular), prime) == d
                assert rank_mod(block(index, u, v, 0), prime) == d - 1
                checks += 1
    print(
        "AUDIT_RATE_HALF_CA_HANKEL_A1_CORE_ONE_MIDDLE_ADJUGATE_PASS "
        f"rank_profiles={checks} mutation_regular_zero={checks}"
    )


if __name__ == "__main__":
    main()
