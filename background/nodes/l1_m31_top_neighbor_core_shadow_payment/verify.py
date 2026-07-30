#!/usr/bin/env python3
"""Exact arithmetic replay for the M31 core-shadow payment."""

from math import comb

N = 1_053_557
k = 4_981
t = 4_980
w = 67_447
d = 215_793


def flat_cap(r: int) -> int:
    s = r + 1
    return comb(N - k + s, s) // comb(w + s, s)


assert flat_cap(0) == 15
assert flat_cap(1) == 241
assert flat_cap(1) - 1 == 240

core_floor = (d * t + 240 - 1) // 240
assert core_floor == 4_477_705

print(
    "L1_M31_TOP_NEIGHBOR_CORE_SHADOW_PASS "
    f"line_neighbors={flat_cap(0)-1} plane_neighbors={flat_cap(1)-1} "
    f"core_floor={core_floor}"
)
