#!/usr/bin/env python3
"""Replay value and derivative Lagrange rows at an exact double zero."""

from math import comb

PRIME = 101


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def inv(value):
    return pow(value % PRIME, PRIME - 2, PRIME)


def poly_mul(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % PRIME
    return out


def hasse(poly, point, order):
    return sum(
        comb(power, order) * coefficient * pow(point, power - order, PRIME)
        for power, coefficient in enumerate(poly)
        if power >= order
    ) % PRIME


def evaluate(poly, point):
    return hasse(poly, point, 0)


rows = [1, 2, 3, 4, 5]
x_star = 17
tau = 11
other_root = 29

locator = [1]
for x in rows:
    locator = poly_mul(locator, [(-x) % PRIME, 1])

locator_value = evaluate(locator, x_star)
locator_derivative = hasse(locator, x_star, 1)
barycentric = []
derivative = []
for x in rows:
    derivative_at_x = 1
    for y in rows:
        if y != x:
            derivative_at_x = derivative_at_x * (x - y) % PRIME
    b_x = locator_value * inv(x_star - x) * inv(derivative_at_x) % PRIME
    d_x = b_x * (
        locator_derivative * inv(locator_value) - inv(x_star - x)
    ) % PRIME
    barycentric.append(b_x)
    derivative.append(d_x)

base = poly_mul([(-tau) % PRIME, 1], [(-tau) % PRIME, 1])
base = poly_mul(base, [(-other_root) % PRIME, 1])
jet_rows = (
    [1],
    [(-tau) % PRIME, 1],
    poly_mul([(-tau) % PRIME, 1], [(-tau) % PRIME, 1]),
)

checks = 0
for expected_profile, h_poly in zip(((4,), (1, 3), (2, 2)), jet_rows):
    row_polys = []
    for x in rows:
        size = max(len(base), len(h_poly))
        row = [0] * size
        for i, value in enumerate(base):
            row[i] = (row[i] + value) % PRIME
        for i, value in enumerate(h_poly):
            row[i] = (row[i] + (x - x_star) * value) % PRIME
        row_polys.append(row)

    reconstructed_value = [
        sum(
            barycentric[index]
            * (row_polys[index][power] if power < len(row_polys[index]) else 0)
            for index in range(len(rows))
        ) % PRIME
        for power in range(max(map(len, row_polys)))
    ]
    reconstructed_derivative = [
        sum(
            derivative[index]
            * (row_polys[index][power] if power < len(row_polys[index]) else 0)
            for index in range(len(rows))
        ) % PRIME
        for power in range(max(map(len, row_polys)))
    ]

    for power in range(len(reconstructed_value)):
        require(
            reconstructed_value[power]
            == (base[power] if power < len(base) else 0),
            "outside value interpolation",
        )
        require(
            reconstructed_derivative[power]
            == (h_poly[power] if power < len(h_poly) else 0),
            "outside derivative interpolation",
        )
        checks += 2

    r_jets = [hasse(reconstructed_value, tau, order) for order in range(3)]
    j_jets = [hasse(reconstructed_derivative, tau, order) for order in range(2)]
    require(r_jets[0] == r_jets[1] == 0 and r_jets[2] != 0, "value-row order")
    profile = (4,)
    if j_jets[0] == 0:
        profile = (1, 3) if j_jets[1] else (2, 2)
    require(profile == expected_profile, "derivative-row profile")
    checks += 2

print(f"RATE_HALF_COLLISION_BARYCENTRIC_SPLIT_JET_PASS checks={checks}")
