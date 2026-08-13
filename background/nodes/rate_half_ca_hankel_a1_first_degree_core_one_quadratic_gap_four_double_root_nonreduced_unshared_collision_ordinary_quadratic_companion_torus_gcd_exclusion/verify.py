#!/usr/bin/env python3
"""Exact replay of the ordinary-quadratic torus-gcd exclusion."""

from math import gcd


def require(condition, message):
    if not condition:
        raise AssertionError(message)


N = 2**41
P_FLOOR = 2**167
F = 2**39 - 6
s3_points = 3 * F
c3_points = s3_points // 2

s3_first_cube = 108 * (4 * 4) ** 2 * N**2
c3_first_cube = 108 * (2 * 2) ** 2 * N**2
require(s3_first_cube == 27648 * N**2, "S3 Euler-characteristic constant")
require(c3_first_cube == 1728 * N**2, "C3 Euler-characteristic constant")
require(s3_first_cube < s3_points**3, "S3 gcd first term")
require(c3_first_cube < c3_points**3, "C3 gcd first term")
require(192 * N**2 < P_FLOOR * s3_points, "S3 characteristic term")
require(48 * N**2 < P_FLOOR * c3_points, "C3 characteristic term")

swap_invariant = []
for r in range(-4, 5):
    for s in range(-4, 5):
        if not r or not s or gcd(abs(r), abs(s)) != 1:
            continue
        if (s, r) in ((r, s), (-r, -s)):
            swap_invariant.append((r, s))
require(
    set(swap_invariant) == {(1, 1), (-1, -1), (1, -1), (-1, 1)},
    "S3 translated-subtorus characters",
)

cyclic_characters = []
for q in (1, 2):
    for r in range(-2, 3):
        for s in range(-2, 3):
            if not r or not s or gcd(abs(r), abs(s)) != 1:
                continue
            if q * abs(r) == q * abs(s) == 2:
                cyclic_characters.append((q, r, s))
require(
    set(cyclic_characters)
    == {
        (2, 1, 1),
        (2, 1, -1),
        (2, -1, 1),
        (2, -1, -1),
    },
    "C3 translated-subtorus characters",
)

require(gcd(3, N) == 1, "dyadic subgroup acquired 3-torsion")
require(2 % 3 != 0, "degree-two coordinate factors through cubic quotient")

print(
    "RATE_HALF_QUADRATIC_TORUS_GCD_EXCLUSION_PASS "
    f"s3_points={s3_points} c3_points={c3_points} "
    "shapes_excluded=B,D shapes_remaining=A,C"
)
