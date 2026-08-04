#!/usr/bin/env python3
"""Exact maximal-fiber inversion, Bonferroni, and negative controls."""

from itertools import product
from math import comb


checks = 0


def raw_moment(k, depth, maximal):
    """Raw subset count induced by a finite maximal-depth spectrum."""
    return sum(
        count * comb(k + exact_depth, k + depth)
        for exact_depth, count in maximal.items()
        if exact_depth >= depth
    )


def truncated_sieve(k, depth, length, raw):
    return sum(
        (-1) ** j * comb(k + depth + j, k + depth) * raw[depth + j]
        for j in range(length + 1)
    )

# Exhaustive toy census already independently replayed in ld_core_count:
# k=6, d=1, maximal spectrum {depth 1: 4, depth 5: 1}.
k, d = 6, 1
maximal = {1: 4, 5: 1}
raw = sum(count * comb(k + e, k + d) for e, count in maximal.items())
assert raw == 334
assert raw == 4 + comb(11, 7)
assert raw > 17 * 20 * 20 // 25  # 334 > 272
checks += 3

# Exhaust all small nonnegative spectra. This simultaneously checks the
# predicate-filtered theorem: a fiber-constant predicate merely replaces the
# full spectrum by an arbitrary coordinatewise sub-spectrum.
for k in range(1, 5):
    for base_depth in range(0, 4):
        top_depth = base_depth + 4
        depths = range(base_depth, top_depth + 1)
        for counts in product(range(3), repeat=len(depths)):
            maximal = dict(zip(depths, counts))
            raw = {
                depth: raw_moment(k, depth, maximal)
                for depth in depths
            }

            exact = truncated_sieve(
                k, base_depth, top_depth - base_depth, raw
            )
            assert exact == maximal[base_depth]
            checks += 1

            for length in range(top_depth - base_depth + 1):
                sieve = truncated_sieve(k, base_depth, length, raw)
                if length % 2 == 0:
                    assert maximal[base_depth] <= sieve
                else:
                    assert sieve <= maximal[base_depth]
                checks += 1

# Check the closed coefficient of every omitted exact-depth stratum.
for k in range(1, 8):
    for depth in range(0, 6):
        for gap in range(1, 9):
            for length in range(gap):
                direct = sum(
                    (-1) ** j
                    * comb(k + depth + j, k + depth)
                    * comb(k + depth + gap, k + depth + j)
                    for j in range(length + 1)
                )
                closed = (
                    comb(k + depth + gap, k + depth)
                    * (-1) ** length
                    * comb(gap - 1, length)
                )
                assert direct == closed
                checks += 1

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
