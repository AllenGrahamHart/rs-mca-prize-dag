#!/usr/bin/env python3
"""Replay the exact arithmetic of the core-one quadratic gap-four theorem."""

from itertools import product


E = 183_251_937_963
RHO = 3 * E - 1
DELTA = E - 2

assert E % 3 == 0
assert E % 2 == 1

# Gap identity and minimum.
for u in range(0, 8):
    v = E + 2 - u
    admissible = 0 <= u <= DELTA and 0 <= v <= DELTA
    assert admissible == (u >= 4)

u = 4
v = E + 2 - u
omission = DELTA - v
i_h = DELTA - u
assert (omission, i_h) == (0, E - 6)
assert DELTA - i_h == 4

# Double-root vertical/contact and Picard degrees.
d_star = E - 6
vertical = d_star + 3 * 2
contact = d_star + 2 * 2
assert vertical == E
assert contact == DELTA
double_picard_degree = (RHO + 2) * E - (E + 1) * (RHO - 1)
assert double_picard_degree == 2

# Split-root correction pairs.
pairs = []
for q1, q2 in product(range(0, 16, 3), repeat=2):
    if q1 + q2 != 12:
        continue
    if (E + q1) % 2 or (E + q2) % 2:
        continue
    pairs.append((q1, q2))
assert pairs == [(3, 9), (9, 3)]

q1, q2 = pairs[0]
c1, c2 = (E + q1) // 2, (E + q2) // 2
d1, d2 = E - c1, E - c2
assert c1 + c2 == E + 6
assert d1 + d2 == E - 6
assert 2 * d1 + q1 == E
assert 2 * d2 + q2 == E
assert d1 + d2 + q1 // 3 + q2 // 3 == DELTA
split_picard_degree = (RHO + 3) * E - (E + 1) * (RHO - 1)
assert split_picard_degree == E + 2

print(
    "CORE_ONE_QUADRATIC_GAP_FOUR_NORMAL_FORMS_PASS",
    f"e={E}",
    f"patterns=2",
    f"split_pairs={len(pairs)}",
)
