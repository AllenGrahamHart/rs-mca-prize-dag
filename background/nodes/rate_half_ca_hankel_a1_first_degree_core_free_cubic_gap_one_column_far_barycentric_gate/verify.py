#!/usr/bin/env python3
"""Replay strict support arithmetic and barycentric null vectors."""


P = 1_000_003
RHO = 127


def derivative_at_root(points, root, modulus):
    value = 1
    for point in points:
        if point != root:
            value = value * (root - point) % modulus
    return value


for c_alpha in range(1, 9):
    c_beta = (2 * c_alpha + 1) % 9
    size_alpha = RHO - c_alpha
    size_beta = RHO - c_beta
    union = RHO + 1
    intersection = size_alpha + size_beta - union
    assert size_beta - intersection == c_alpha + 1
    assert size_alpha - intersection == c_beta + 1

    points = list(range(2, c_alpha + 3))
    barycentric = [pow(derivative_at_root(points, x, P), -1, P) for x in points]
    for degree in range(c_alpha):
        assert sum(
            weight * pow(x, degree, P)
            for x, weight in zip(points, barycentric)
        ) % P == 0
    assert all(weight % P for weight in barycentric)

print(
    "CORE_FREE_CUBIC_GAP_ONE_COLUMN_FAR_BARYCENTRIC_PASS",
    "strict_plus_one=1",
    "degrees=1..8",
)
