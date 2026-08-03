#!/usr/bin/env python3
"""Exact fiber, raw-overcount, and joint-rank negative controls."""

from math import comb


checks = 0

# Exhaustive toy census already independently replayed in ld_core_count:
# k=6, d=1, maximal spectrum {depth 1: 4, depth 5: 1}.
k, d = 6, 1
maximal = {1: 4, 5: 1}
raw = sum(count * comb(k + e, k + d) for e, count in maximal.items())
assert raw == 334
assert raw == 4 + comb(11, 7)
assert raw > 17 * 20 * 20 // 25  # 334 > 272
checks += 3

# One deeper maximal pair can overwhelm the n^2 target in raw locator
# currency at every prize row; this is not a maximal-occupancy falsifier.
for rate, h in ((4, 2**33 + 1), (8, 2**33 + 1), (16, 2**32 + 1)):
    n = 2**41
    k = n // rate
    d = (h + 1) // 2
    assert comb(k + d + 3, 3) > 17 * n * n // 25
    checks += 1

# Full rank of each word does not force doubled joint rank.
u_rows = {(1, 0, 2), (0, 1, 3)}
v_rows = set(u_rows)
assert len(u_rows) == 2 and len(u_rows | v_rows) == 2
checks += 1

print(f"XR_WINDOW_DIVISOR_MAXIMALITY_FILTER_ALL_PASS checks={checks}")
