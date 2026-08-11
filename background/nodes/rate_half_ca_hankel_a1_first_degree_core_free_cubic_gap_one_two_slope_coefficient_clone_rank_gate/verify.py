#!/usr/bin/env python3
"""Replay the Vandermonde codimension behind the clone-rank bound."""


P = 1_000_003


def rank_mod(matrix, modulus):
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if work[r][col] % modulus), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inv = pow(work[rank][col], -1, modulus)
        work[rank] = [(value * inv) % modulus for value in work[rank]]
        for row in range(rows):
            if row == rank:
                continue
            factor = work[row][col] % modulus
            if factor:
                work[row] = [
                    (a - factor * b) % modulus
                    for a, b in zip(work[row], work[rank])
                ]
        rank += 1
        if rank == rows:
            break
    return rank


for c in range(1, 9):
    for union_excess in range(1, 6):
        points = list(range(2, 2 + c + union_excess))
        vandermonde = [
            [pow(x, degree, P) for x in points]
            for degree in range(c)
        ]
        assert rank_mod(vandermonde, P) == c
        assert len(points) - c == union_excess

print(
    "CORE_FREE_CUBIC_GAP_ONE_COEFFICIENT_CLONE_RANK_PASS",
    "losses=1..8",
    "union_excess=1..5",
)
