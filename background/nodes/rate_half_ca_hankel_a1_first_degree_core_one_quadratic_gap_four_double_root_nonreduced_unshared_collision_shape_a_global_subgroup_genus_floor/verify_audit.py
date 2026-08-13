#!/usr/bin/env python3
"""Independent arithmetic audit for the shape-A genus floor."""

from fractions import Fraction
from math import gcd


def require(condition, message):
    if not condition:
        raise AssertionError(message)


N = 2**41
e = (2**39 + 1) // 3
m = e - 2
n = (3 * e - 7) // 2
rows = 3 * 2**38 - 2
points = rows * m

ratio = Fraction(points**3, 54 * N**2 * m * n)
chi = ratio.numerator // ratio.denominator
if ratio.denominator != 1:
    chi += 1

boundary_cap = 2 * (m + n)
genus_ratio = Fraction(chi - boundary_cap + 2, 2)
genus = genus_ratio.numerator // genus_ratio.denominator
if genus_ratio.denominator != 1:
    genus += 1

require(gcd(n, N) == 1, "odd row degree versus dyadic subgroup")
require(Fraction(12 * N**2 * m * n, 2**167) < 1, "second branch below one")
require(chi == 262353693488940318721, "independent chi reconstruction")
require(genus == 131176846286340314460, "independent genus reconstruction")
require(384 * genus < (m - 1) * (n - 1), "factor-384 endpoint")
require((m - 1) * (n - 1) < 385 * genus, "remaining genus factor")

print(
    "RATE_HALF_SHAPE_A_GENUS_FLOOR_AUDIT_PASS "
    f"chi={chi} genus={genus}"
)
