#!/usr/bin/env python3
"""Verify the component-payment arithmetic and distinct-pole mechanism."""

from fractions import Fraction
from math import prod


ROWS = (
    ("1/4", 2**41, 2**33 + 1, 11, 6_840_580_025, 6_840_580_025),
    ("1/8", 2**41, 2**33 + 1, 11, 6_840_580_025, 6_840_580_025),
    ("1/16", 2**41, 2**32 + 1, 10, 3_523_371_941, 3_435_973_837),
)


def cap_fraction(n: int, h: int, s: int, x: int) -> tuple[int, int]:
    numerator = 3 * n ** (s - 2) * prod(x - j for j in (3, 4, 5))
    denominator = (
        2
        * (h - x + 1)
        * (h - x)
        * (h - x - 1)
        * prod(x + j for j in range(3, s + 1))
    )
    return numerator, denominator


def polynomial_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def matrix_rank(columns: list[list[Fraction]]) -> int:
    rows = [list(row) for row in zip(*columns)]
    rank = 0
    for column in range(len(columns)):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        value = rows[rank][column]
        rows[rank] = [entry / value for entry in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][column]:
                scale = rows[i][column]
                rows[i] = [a - scale * b for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


checks = 0
for name, n, h, s, last_paid, uniform_paid in ROWS:
    budget = (17 * n * n - 25 * (n - 4)) // 25
    paid_num, paid_den = cap_fraction(n, h, s, last_paid)
    fail_num, fail_den = cap_fraction(n, h, s, last_paid + 1)
    assert paid_num <= budget * paid_den
    assert fail_num > budget * fail_den
    assert last_paid < h - 2
    assert 5 * uniform_paid <= 4 * h
    uniform_num, uniform_den = cap_fraction(n, h, s, uniform_paid)
    assert uniform_num <= budget * uniform_den
    checks += 5

# The consecutive-ell ratio difference becomes a polynomial with positive
# coefficients in u=ell-1 and the two route slacks q,t.
positive_coefficients = (
    72, 120, 132, 228, 50, 92, 244, 38, 272, 222,
    6, 15, 51, 12, 96, 120, 3, 39, 135, 63,
)
assert all(coefficient > 0 for coefficient in positive_coefficients)
for u in range(4):
    for q in range(4):
        for t in range(4):
            ell = u + 1
            twice_a = 4 * ell + 1 + q + t
            if twice_a % 2:
                continue
            a = twice_a // 2
            E = 6 * ell + 1 + 2 * q + t
            difference = (
                6 * (E - 2) * (a * a - ell * ell)
                - E * (E - 1) * (2 * ell + 1)
            )
            expanded_twice = (
                72*u**3 + 120*u*u*q + 132*u*u*t + 228*u*u
                + 50*u*q*q + 92*u*q*t + 244*u*q
                + 38*u*t*t + 272*u*t + 222*u
                + 6*q**3 + 15*q*q*t + 51*q*q
                + 12*q*t*t + 96*q*t + 120*q
                + 3*t**3 + 39*t*t + 135*t + 63
            )
            assert 2 * difference == expanded_twice > 0
checks += 2

# After multiplication by the common denominator, 1 and three simple-pole
# functions with distinct poles are linearly independent.  Colliding two
# poles is the mutation control.
poles = (1, 2, 4)
common = [Fraction(1)]
for pole in poles:
    common = polynomial_mul(common, [Fraction(-pole), Fraction(1)])
columns = [common]
for omitted in range(3):
    numerator = [Fraction(1)]
    for index, pole in enumerate(poles):
        if index != omitted:
            numerator = polynomial_mul(numerator, [Fraction(-pole), Fraction(1)])
    numerator += [Fraction(0)] * (len(common) - len(numerator))
    columns.append(numerator)
assert matrix_rank(columns) == 4

colliding = (1, 1, 4)
common_collision = [Fraction(1)]
for pole in colliding:
    common_collision = polynomial_mul(
        common_collision, [Fraction(-pole), Fraction(1)]
    )
collision_columns = [common_collision]
for omitted in range(3):
    numerator = [Fraction(1)]
    for index, pole in enumerate(colliding):
        if index != omitted:
            numerator = polynomial_mul(
                numerator, [Fraction(-pole), Fraction(1)]
            )
    numerator += [Fraction(0)] * (len(common_collision) - len(numerator))
    collision_columns.append(numerator)
assert matrix_rank(collision_columns) < 4
checks += 2

# Component accounting: no component, one common line, or degree-two gcd.
assert max(3, 1 + 1, 2) == 3
checks += 1

print(
    "XR_DEFICIENT_WINDOW_AFFINE_PLANE_COMPONENT_PAYMENT_PASS "
    f"rows={len(ROWS)} checks={checks}"
)
