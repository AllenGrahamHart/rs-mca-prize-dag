#!/usr/bin/env python3
"""Replay degree and a small Cauchy--Binet instance for the source frame."""

from itertools import combinations, permutations


def det(matrix, modulus):
    n = len(matrix)
    total = 0
    for perm in permutations(range(n)):
        inversions = sum(
            perm[i] > perm[j] for i in range(n) for j in range(i + 1, n)
        )
        term = 1
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        total += (-1 if inversions % 2 else 1) * term
    return total % modulus


E = 183_251_937_963
RHO = 3 * E - 1
D = RHO - 1
assert D == 3 * E - 2
assert (E - 2) + 2 * (E - 6) + 6 * 2 == D

# Check det(M+tau vv^T)-det(M) against the marked subset sum for size 3.
P = 101
points = [2, 5, 9, 14]
weights = [3, 7, 11, 13]
marked = 9
tau = 17
size = 3
vectors = [[pow(x, i, P) for i in range(size)] for x in points]
M = [[0] * size for _ in range(size)]
for w, v in zip(weights, vectors):
    for i in range(size):
        for j in range(size):
            M[i][j] = (M[i][j] + w * v[i] * v[j]) % P
v_star = vectors[points.index(marked)]
M_marked = [row[:] for row in M]
for i in range(size):
    for j in range(size):
        M_marked[i][j] = (M_marked[i][j] + tau * v_star[i] * v_star[j]) % P

subset_sum = 0
others = [x for x in points if x != marked]
for subset in combinations(others, size - 1):
    cols = [marked, *subset]
    vand = [[pow(x, i, P) for x in cols] for i in range(size)]
    prod = 1
    for x in subset:
        prod = prod * weights[points.index(x)] % P
    subset_sum = (subset_sum + det(vand, P) ** 2 * prod) % P

assert (det(M_marked, P) - det(M, P)) % P == tau * subset_sum % P

print(
    "CORE_ONE_MARKED_SOURCE_FRAME_PASS",
    f"rho={RHO}",
    f"toy_subset_sum={subset_sum}",
)
