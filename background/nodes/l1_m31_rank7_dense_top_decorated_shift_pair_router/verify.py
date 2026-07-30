#!/usr/bin/env python3
"""Exact threshold replay for the dense top decorated shift-pair router."""

N = 1_053_557
k = 4_981
t = k - 1
m = 72_428
w = m - k
M0 = 2_157_929
delta = N * t - m * m

assert delta == 898_676
assert w + 1 == 67_448

# The deficit upper bound is strictly below 9/10 of all pairs.
assert 10 * (M0 * delta + N * (m - t)) < 9 * N * (M0 - 1)

# Hence average top-edge degree exceeds (M0-1)/10.
assert (M0 - 1) // 10 == 215_792
forced_degree = (M0 - 1) // 10 + 1
assert forced_degree == 215_793
line_members = (N - t) // (m - t)
assert line_members == 15
neighbors_per_direction = line_members - 1
forced_directions = (forced_degree + neighbors_per_direction - 1) // neighbors_per_direction
assert forced_directions == 15_414

print(
    "L1_M31_DENSE_TOP_SHIFT_PAIR_PASS "
    f"delta={delta} degree={forced_degree} directions={forced_directions} "
    f"e={w + 1}"
)
