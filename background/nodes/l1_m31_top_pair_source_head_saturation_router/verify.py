#!/usr/bin/env python3
"""Exact arithmetic replay for the M31 source-head saturation router."""

N = 1_053_557
m = 72_428
t = 4_980
M0 = 2_157_929

denominator = m * m - N * (t - 1)
numerator = N * (m - (t - 1))

assert denominator == 154_881
assert numerator == 71_061_366_093
assert divmod(numerator, denominator) == (458_812, 104_721)

fiber_cap = numerator // denominator
assert 4 * fiber_cap < M0 <= 5 * fiber_cap
assert M0 - fiber_cap == 1_699_117

dense_anchor_degree = 215_793
assert dense_anchor_degree * t // 15 == 71_643_276

anchor_degree = 107_897
assert 20 * (anchor_degree - 1) <= M0 - 1 < 20 * anchor_degree
assert (anchor_degree + 13) // 14 == 7_707
assert (anchor_degree * t + 239) // 240 == 2_238_863
assert anchor_degree * t // 15 == 35_821_804

print(
    "L1_M31_TOP_PAIR_SOURCE_HEAD_SATURATION_PASS "
    f"fiber_cap={fiber_cap} full_head_floor={M0-fiber_cap} "
    f"dense_colored_core_floor={dense_anchor_degree*t//15} "
    f"full_head_anchor_degree={anchor_degree}"
)
