#!/usr/bin/env python3
from itertools import product


def curve_value(coeffs, gamma, tau, p):
    a, b, c, d = coeffs
    return (a + b * gamma + c * tau + d * gamma * tau) % p


for p in (5, 7, 11):
    clone = (1, 0, 0, 1)  # 1+gamma*tau, irreducible bidegree (1,1).
    clone_points = {
        (gamma, tau)
        for gamma, tau in product(range(p), repeat=2)
        if curve_value(clone, gamma, tau, p) == 0
    }
    assert len(clone_points) == p - 1
    outside_curves = (
        (0, 1, 1, 0),
        (1, 1, 1, 0),
        (2, 1, 0, 1),
        (1, 0, 1, 0),
    )
    for outside in outside_curves:
        intersections = {
            point
            for point in clone_points
            if curve_value(outside, *point, p) == 0
        }
        assert len(intersections) <= 2

for n in range(8, 31):
    for m in range((n + 2) // 2 + 1, n + 1):
        if n > 2 * (m - 1):
            continue
        for c in range(2, m):
            assert 2 * (n - c) <= 2 * c * (m - c)

print("PASS independent clone Bezout fixtures fields=3 and integer_grid_n<=30")
