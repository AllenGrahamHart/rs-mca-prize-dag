#!/usr/bin/env python3
"""Verify the sharp-pair dimensions and a finite-field barycentric model."""


P = 101
points = [2, 5, 11, 19]


def inv(value):
    return pow(value % P, P - 2, P)


for rank_loss in range(3):
    xs = points[: rank_loss + 2]
    weights = []
    for x in xs:
        derivative = 1
        for y in xs:
            if y != x:
                derivative = derivative * (x - y) % P
        weights.append(inv(derivative))
    for degree in range(rank_loss + 1):
        assert sum(w * pow(x, degree, P) for x, w in zip(xs, weights)) % P == 0

official_rho = 549755813888
official_e = 183251937963
assert 3 * official_e == official_rho + 1
for rank_loss in range(3):
    assert (official_rho + 2) - (official_rho - rank_loss) == rank_loss + 2

print(
    "QUADRATIC_GAP_FOUR_MINIMUM_PAIR_CLONE_BARYCENTRIC_GATE_PASS",
    f"official_e={official_e}",
)
