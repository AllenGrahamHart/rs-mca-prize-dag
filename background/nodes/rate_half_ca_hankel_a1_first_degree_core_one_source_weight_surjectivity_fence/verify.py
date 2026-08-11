#!/usr/bin/env python3
"""Replay official dimensions and a small Vandermonde-surjectivity model."""


def rank_mod(matrix, modulus):
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col] % modulus), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col] % modulus, -1, modulus)
        a[rank] = [(v * inv) % modulus for v in a[rank]]
        for r in range(rows):
            if r == rank:
                continue
            factor = a[r][col] % modulus
            if factor:
                a[r] = [
                    (a[r][c] - factor * a[rank][c]) % modulus
                    for c in range(cols)
                ]
        rank += 1
        if rank == rows:
            break
    return rank


E = 183_251_937_963
RHO = 3 * E - 1
D = RHO - 1
N = 4 * RHO
assert N - 1 == 4 * RHO - 1
assert 2 * D + 1 == 2 * RHO - 1
assert N - 1 >= 2 * D + 1

P = 101
points = [1, 2, 4, 7, 11, 16, 22]
moment_count = 5
vandermonde = [
    [pow(x, k, P) for x in points]
    for k in range(moment_count)
]
assert rank_mod(vandermonde, P) == moment_count

print(
    "CORE_ONE_SOURCE_WEIGHT_SURJECTIVITY_FENCE_PASS",
    f"residual_points={N - 1}",
    f"moments={2 * D + 1}",
)
