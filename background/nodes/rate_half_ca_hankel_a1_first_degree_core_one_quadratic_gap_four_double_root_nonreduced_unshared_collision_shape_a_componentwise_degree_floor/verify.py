#!/usr/bin/env python3
"""Replay the shape-A componentwise subgroup-curve degree floor."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


e = (2**39 + 1) // 3
m = e - 2
n = (3 * e - 7) // 2
N = 2**41
P_char = 2**167

threshold_num = (e + 7) ** 3 * n**3
threshold_den = 108 * N**2 * m**3
D0 = (threshold_num + threshold_den - 1) // threshold_den
point_floor = ((e + 7) * n * D0 + m - 1) // m
second_num = P_char * (e + 7) * n
second_den = 12 * N**2 * m

require(n == 2**38 - 3 and n % 2 == 1, "odd cover degree")
require(D0 == 39768216, "component degree floor")
require((D0 - 1) * threshold_den < threshold_num, "first-term strictness")
require(D0 * threshold_den >= threshold_num, "threshold ceiling")
require(D0 * second_den < second_num, "characteristic-term margin")
require(D0 < P_char, "nonzero differential range")
require(point_floor == 10931403977394458172, "component point floor")
require(m < 4608 * D0, "multiplicity ratio")

print(
    "RATE_HALF_SHAPE_A_COMPONENT_DEGREE_PASS "
    f"D0={D0} point_floor={point_floor} multiplicity_ratio_lt=4608"
)
