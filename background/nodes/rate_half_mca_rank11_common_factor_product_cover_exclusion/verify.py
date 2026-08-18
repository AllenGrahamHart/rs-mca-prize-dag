#!/usr/bin/env python3
"""Controls for the common-factor product-cover exclusion."""

from itertools import product


def rank_mod(rows: list[list[int]], prime: int) -> int:
    matrix = [[value % prime for value in row] for row in rows]
    rank = 0
    columns = len(matrix[0]) if matrix else 0
    for column in range(columns):
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
            if index == rank:
                continue
            factor = matrix[index][column]
            if factor:
                matrix[index] = [
                    (matrix[index][j] - factor * matrix[rank][j]) % prime
                    for j in range(columns)
                ]
        rank += 1
    return rank


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def padded(row: list[int], length: int) -> list[int]:
    return row + [0] * (length - len(row))


fixtures = [
    (
        [(1, 0), (0, 1)],
        [(1, 0, 0), (0, 1, 0), (0, 0, 1)],
    ),
    (
        [(1, 1, 0), (0, 1, 1)],
        [(1, 0, 1), (0, 1, 0), (1, 1, 1)],
    ),
    (
        [(1, 0, 0, 1), (0, 1, 1, 0)],
        [(1, 1), (1, 2), (2, 1)],
    ),
]

for prime in (5, 7, 101):
    for pencil, residual in fixtures:
        products = [multiply(tuple(p), tuple(b)) for p, b in product(pencil, residual)]
        width = max(map(len, products))
        assert rank_mod([padded(row, width) for row in products], prime) <= 6

B = 8_406
H = 42_452
M = 1_116_048
core = -(-(B * H - M) // (B - 1))
assert core == 42_325
assert M + (B - 1) * core >= B * H
assert M + (B - 1) * (core - 1) < B * H

print(
    "RANK11_PRODUCT_COVER_PASS "
    f"fixtures={len(fixtures)*3} span_cap=6 containers={B} core_floor={core}"
)
