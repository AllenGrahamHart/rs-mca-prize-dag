#!/usr/bin/env python3
"""Mutation controls for near-K oriented-difference subset ownership."""

from itertools import combinations
from math import comb


# Sharp c=2 pair: 1-subsets are not unique, while 2-subsets are.
c = 2
left = frozenset((0, 1, 2))
right = frozenset((0, 3, 4))
assert len(left & right) == c - 1
left_one = {frozenset(x) for x in combinations(left, c - 1)}
right_one = {frozenset(x) for x in combinations(right, c - 1)}
left_two = {frozenset(x) for x in combinations(left, c)}
right_two = {frozenset(x) for x in combinations(right, c)}
assert left_one & right_one
assert left_two.isdisjoint(right_two)

# Dropping the low-core cap by one permits a shared owned c-subset.
bad = frozenset((0, 1, 3))
bad_two = {frozenset(x) for x in combinations(bad, c)}
assert len(left & bad) == c
assert left_two & bad_two

# Recheck a paid official endpoint and its first unpaid neighbor.
n = 2**41
K = n // 4
H = n // 256 + 2
paid = comb(n - 2 * K + 12, 6) // comb(H + 5, 6)
unpaid = comb(n - 2 * K + 14, 7) // comb(H + 6, 7)
assert paid == 4_398_046_497_508 <= 8 * n
assert unpaid == 562_949_951_166_976 > 8 * n

print("XR_LOWCORE_NEAR_K_DIFFERENCE_PACKING_AUDIT_PASS", paid, unpaid)
