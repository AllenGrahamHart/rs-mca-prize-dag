#!/usr/bin/env python3
"""Independent product-quotient audit of the two-by-five factor router."""

from math import prod


N = 2_097_152
K = 1_048_576
M = 1_116_048
A = 1_114_369
U = N - A
H = 38_385
BUDGET = 274_980_728_111_395_087
TRANSVERSE = 209_812_758_437_679_617
AVAILABLE = BUDGET - TRANSVERSE


def choose(top: int, count: int) -> int:
    numerator = prod(range(top - count + 1, top + 1))
    denominator = prod(range(1, count + 1))
    quotient, remainder = divmod(numerator, denominator)
    assert remainder == 0
    return quotient


def cap(dimension: int) -> int:
    return choose(N - K + dimension, dimension) // choose(A - K + dimension, dimension)


R4, R5, R6 = (U * cap(dimension) for dimension in (4, 5, 6))
assert (R4, R5, R6) == (63_397_365_764, 1_010_335_321_405, 16_100_859_197_492)


def cost(cutoff: int, h: int) -> tuple[int, tuple[int, ...]]:
    roots = H - cutoff + 1
    gap = roots - h
    factor_classes = M // cutoff
    n2 = M * (M - 1) * (M - 2) // gap**3
    n3 = M * (M - 1) // gap**2
    parts = (factor_classes * R5, n2 * R4, n3 * R6)
    return sum(parts), (roots, gap, factor_classes, n2, n3, *parts)


selected, data = cost(408, 18165)
adjacent, _ = cost(408, 18166)
assert data == (
    37978,
    19813,
    2735,
    178729,
    3172,
    2763267104042675,
    11330947785633956,
    51071925374444624,
)
assert selected == 65_166_140_264_121_255
assert AVAILABLE - selected == 1_829_409_594_215
assert TRANSVERSE + adjacent - BUDGET == 15_983_178_478_905


def max_h(cutoff: int) -> int:
    roots = H - cutoff + 1
    if roots <= 2 or cost(cutoff, 2)[0] > AVAILABLE:
        return -1
    low, high = 2, roots - 1
    while low <= high:
        middle = (low + high) // 2
        if cost(cutoff, middle)[0] <= AVAILABLE:
            low = middle + 1
        else:
            high = middle - 1
    return high


paying = []
for cutoff in range(1, H):
    h = max_h(cutoff)
    if h >= 0:
        paying.append((cutoff, h))
global_h = max(h for _, h in paying)
maxima = [(cutoff, h) for cutoff, h in paying if h == global_h]
assert global_h == 18165
assert maxima == [(408, 18165), (411, 18165)]
assert max(maxima, key=lambda item: AVAILABLE - cost(*item)[0]) == (408, 18165)

print(
    "RANK11_FACTOR_FLAG_2X5_AUDIT_PASS "
    f"T=408 h={global_h} factor_classes={data[2]} residual_classes={data[3]+data[4]}"
)
