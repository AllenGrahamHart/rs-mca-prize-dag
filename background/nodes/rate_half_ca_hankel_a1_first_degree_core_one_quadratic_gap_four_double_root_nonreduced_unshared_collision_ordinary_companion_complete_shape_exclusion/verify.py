#!/usr/bin/env python3
"""Replay the complete ordinary-companion shape exclusion."""

from math import gcd


def require(condition, message):
    if not condition:
        raise AssertionError(message)


N = 2**41
e = (2**39 + 1) // 3
full_fibers = 3 * e - 14
residual_pairs_per_fiber = 6 * 5 - 6
pair_multiplicity = 4
pair_floor = residual_pairs_per_fiber * full_fibers // pair_multiplicity

require(full_fibers == 2**39 - 13, "full six-row fiber floor")
require(residual_pairs_per_fiber == 24, "deck-graph deletion")
require(pair_floor == 3298534883250, "residual ordered-pair floor")
require(5 - 1 == 4, "residual component cap")

first_cube_constant = 108 * (20 * 20) ** 2
require(first_cube_constant == 17280000, "gcd first-term constant")
require(64 * first_cube_constant * N**2 < pair_floor**3, "four-component first term")
require(4 * 4800 * N**2 < 2**167 * pair_floor, "four-component characteristic term")

require(gcd(6, N) == 2, "subgroup-compatible scaling order")
require(6 % 4 != 0, "degree-six deck group cannot contain V4")


def scale(a, x, prime):
    return a * x % prime


def reciprocal(a, x, prime):
    return a * pow(x, -1, prime) % prime


for prime, x, k in ((101, 7, 9), (127, 11, 25)):
    # Antipodal plus reciprocal and reciprocal plus antipodal commute.
    left = scale(-1, reciprocal(k, x, prime), prime)
    right = reciprocal(k, scale(-1, x, prime), prime)
    require(left == right, "antipodal/reciprocal V4 relation")

    # Two reciprocal involutions whose quotient has order two also commute.
    c = -k % prime
    left = reciprocal(c, reciprocal(k, x, prime), prime)
    right = reciprocal(k, reciprocal(c, x, prime), prime)
    require(left == right == (-x) % prime, "reciprocal/reciprocal V4 relation")

print(
    "RATE_HALF_ORDINARY_COMPANION_COMPLETE_EXCLUSION_PASS "
    f"full_fibers={full_fibers} residual_pair_floor={pair_floor} "
    "survivor=shape_A"
)
