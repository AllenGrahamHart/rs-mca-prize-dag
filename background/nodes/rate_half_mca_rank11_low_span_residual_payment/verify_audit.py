#!/usr/bin/env python3
"""Independent product-quotient audit of the low-span payment."""

from math import prod


P = 2_130_706_433
Q = P**6
N = 2_097_152
K = 1_048_576
M = 1_116_048
W = 67_472
NEAR = 134_944
BUDGET = 274_980_728_111_395_087
RESOURCE = 106_618_568_137_036_225_644
RANK1 = 8_147_918


def choose_product(top: int, count: int) -> int:
    if count == 0:
        return 1
    numerator = prod(range(top - count + 1, top + 1))
    denominator = prod(range(1, count + 1))
    quotient, remainder = divmod(numerator, denominator)
    assert remainder == 0
    return quotient


def cell(tau: int, h: int) -> tuple[int, dict[str, int]]:
    A = M - tau
    c = 2 * A - N
    multiplicity = N - A
    caps = [1]
    for dimension in range(1, 7):
        caps.append(
            choose_product(N - K + dimension, dimension)
            // choose_product(A - K + dimension, dimension)
        )
    n1 = prod(M - index for index in range(9)) // (c - h) ** 9
    n2 = prod(M - index for index in range(8)) // (c - h) ** 8
    r2 = multiplicity * caps[2]
    r3 = multiplicity * caps[3]
    r6 = multiplicity * caps[6]
    transverse = (
        NEAR
        + RESOURCE // (tau + 1)
        + multiplicity
        + n1 * RANK1
        + n2 * r2
    )
    residual = BUDGET + 1 - transverse
    return transverse + r6, {
        "transverse": transverse,
        "residual": residual,
        "r2": r2,
        "r3": r3,
        "r6": r6,
        "row_spaces": -(-residual // r2),
        "containers": -(-residual // r3),
        "m6": caps[6],
    }


def max_h(tau: int) -> int:
    c = 2 * (M - tau) - N
    if c <= 0 or cell(tau, 0)[0] > BUDGET:
        return -1
    low, high = 0, c - 1
    while low <= high:
        middle = (low + high) // 2
        if cell(tau, middle)[0] <= BUDGET:
            low = middle + 1
        else:
            high = middle - 1
    return high


selected_total, selected = cell(1549, 42451)
adjacent_total, _ = cell(1549, 42452)
assert selected_total == 274_963_410_460_662_890
assert BUDGET - selected_total == 17_317_650_732_197
assert adjacent_total - BUDGET == 1_804_196_591_101
assert selected == {
    "transverse": 274_947_501_264_373_505,
    "residual": 33_226_847_021_583,
    "r2": 247_628_556,
    "r3": 3_953_213_019,
    "r6": 15_909_196_289_385,
    "row_spaces": 134_181,
    "containers": 8_406,
    "m6": 16_190_045,
}
assert selected["m6"] ** 2 < Q

paying = [(tau, max_h(tau)) for tau in range(1, W) if max_h(tau) >= 0]
global_h = max(h for _, h in paying)
assert paying[0] == (397, 68)
assert paying[-1] == (21131, 1)
assert [(tau, h) for tau, h in paying if h == global_h] == [
    (1547, 42451),
    (1548, 42451),
    (1549, 42451),
]
assert global_h == 42451

print(
    "RANK11_LOW_SPAN_AUDIT_PASS "
    f"global_h={global_h} residual={selected['residual']} "
    f"containers={selected['containers']}"
)
