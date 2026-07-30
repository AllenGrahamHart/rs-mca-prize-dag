#!/usr/bin/env python3
"""Exact arithmetic replay for the M31 two-block incidence router."""

g = 354_972
external = 698_585
N = 1_053_557
k = 4_981
t = k - 1
m = 72_428
M0 = 2_157_929
d = 67_448

assert g + external == N
assert N * t - m * m == 898_676

low_num = external * (d - t)
low_den = d * d - external * t
high_num = g * (d - t)
high_den = d * d - g * t

assert (low_num, low_den, low_num // low_den) == (
    43_637_207_780,
    1_070_279_404,
    40,
)
assert (high_num, high_den, high_num // high_den) == (
    22_174_390_896,
    2_781_472_144,
    7,
)

center_num = m * g
assert 24_402 * N < center_num < 24_403 * N

delta = N * t - m * m
width_num = g * external * (N * (m - t) + M0 * delta)
width_den = M0 * N * N
assert width_num < 457 * 457 * width_den
assert M0 - 40 - 7 == 2_157_882

print(
    "L1_M31_TWO_BLOCK_INCIDENCE_PASS "
    "low=40 high=7 middle=2157882 mean=(23945,24860)"
)
