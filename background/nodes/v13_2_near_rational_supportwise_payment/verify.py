#!/usr/bin/env python3
"""Verify the smooth F_17 support-wise counterexample to the v13.2 step."""

import json
from itertools import combinations
from pathlib import Path

P = 17
D = (1, 2, 4, 8, 16, 15, 13, 9)
K = 4
M = 5
W = M - K
U = (0, 0, 0, 0, 0, 0, 1, 1)
V = (0, 0, 0, 0, 0, 0, 1, 2)


def line_word(z):
    return tuple((u + z * v) % P for u, v in zip(U, V))


def solve_polynomial(word, support):
    matrix = []
    for index in support[:K]:
        x = D[index]
        matrix.append([pow(x, degree, P) for degree in range(K)] + [word[index]])

    for column in range(K):
        pivot = next(row for row in range(column, K) if matrix[row][column] % P)
        matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
        factor = pow(matrix[column][column], P - 2, P)
        matrix[column] = [(factor * value) % P for value in matrix[column]]
        for row in range(K):
            if row == column:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                (left - factor * right) % P
                for left, right in zip(matrix[row], matrix[column])
            ]

    coefficients = tuple(matrix[row][K] for row in range(K))
    for index in support:
        value = sum(
            coefficient * pow(D[index], degree, P)
            for degree, coefficient in enumerate(coefficients)
        ) % P
        if value != word[index]:
            return None
    return coefficients


def witness_supports(word):
    return [
        support
        for size in range(M, len(D) + 1)
        for support in combinations(range(len(D)), size)
        if solve_polynomial(word, support) is not None
    ]


def extends_jointly(support):
    return solve_polynomial(U, support) is not None and solve_polynomial(V, support) is not None


assert len(D) - 3 * W >= M
assert 2 * W <= len(D) - K

expected = {
    8: ((0, 0, 0, 0, 0, 0, 9, 0), (0, 1, 2, 3, 7), 13),
    16: ((0, 0, 0, 0, 0, 0, 0, 16), (0, 1, 2, 3, 6), 9),
}
for slope, (word, bad_support, error_root) in expected.items():
    assert line_word(slope) == word
    assert witness_supports(word)
    assert bad_support in witness_supports(word)
    assert not extends_jointly(bad_support)

    # (X-error_root, 0) is a nonzero lattice vector of shifted degree one:
    # its first component kills the unique nonzero coordinate of the word.
    for x, value in zip(D, word):
        assert ((x - error_root) * value) % P == 0

# The common zero-codeword support exists, but does not remove bad supports.
common_support = (0, 1, 2, 3, 4, 5)
assert extends_jointly(common_support)

bad_slopes = []
for slope in range(P):
    witnesses = witness_supports(line_word(slope))
    if any(not extends_jointly(support) for support in witnesses):
        bad_slopes.append(slope)
assert 8 in bad_slopes and 16 in bad_slopes

root = Path(__file__).resolve().parents[3]
dag = json.loads((root / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
assert nodes["v13_2_near_rational_pair_proximity"]["status"] == "PROVED"
assert nodes["v13_2_near_rational_supportwise_payment"]["status"] == "REFUTED"

print("V13_2_NEAR_RATIONAL_SUPPORTWISE_PAYMENT_REFUTED", bad_slopes)
