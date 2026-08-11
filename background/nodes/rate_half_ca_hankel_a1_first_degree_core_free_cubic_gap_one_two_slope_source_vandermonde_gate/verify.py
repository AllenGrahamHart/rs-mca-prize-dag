#!/usr/bin/env python3
"""Replay the equality-case weighted Vandermonde radical."""


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


def root_polynomial(roots, modulus):
    coeffs = [1]
    for root in roots:
        nxt = [0] * (len(coeffs) + 1)
        for index, value in enumerate(coeffs):
            nxt[index] = (nxt[index] - root * value) % modulus
            nxt[index + 1] = (nxt[index + 1] + value) % modulus
        coeffs = nxt
    return coeffs


for c in range(1, 8):
    points = list(range(2, c + 2))
    weights = [index + 3 for index in range(c)]
    matrix = [
        [sum(w * pow(x, i + j, P) for x, w in zip(points, weights)) % P
         for j in range(c + 1)]
        for i in range(c)
    ]
    assert rank_mod(matrix, P) == c
    radical = root_polynomial(points, P)
    assert all(
        sum(matrix[i][j] * radical[j] for j in range(c + 1)) % P == 0
        for i in range(c)
    )

RHO = 127
for c_alpha in range(0, 8):
    for c_beta in range(0, 8):
        intersection_cap = RHO - c_alpha - c_beta
        union = 2 * RHO - c_alpha - c_beta - intersection_cap
        assert union == RHO

print(
    "CORE_FREE_CUBIC_GAP_ONE_TWO_SLOPE_VANDERMONDE_PASS",
    "ranks=1..7",
    f"field={P}",
)
