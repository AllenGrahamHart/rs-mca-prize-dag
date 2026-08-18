#!/usr/bin/env python3
"""Independent direct-product audit of full-span forcing."""

from math import prod


P = 2_130_706_433
Q = P**6
N = 2_097_152
K = 1_048_576
M = 1_116_048
W = 67_472
BUDGET = 274_980_728_111_395_087
RESOURCE = 106_618_568_137_036_225_644


def choose(top: int, count: int) -> int:
    numerator = prod(range(top - count + 1, top + 1))
    denominator = prod(range(1, count + 1))
    quotient, remainder = divmod(numerator, denominator)
    assert remainder == 0
    return quotient


def cap(tau: int, dimension: int) -> int:
    A = M - tau
    return choose(N - K + dimension, dimension) // choose(A - K + dimension, dimension)


def total(tau: int, h: int, dimension: int) -> tuple[int, dict[str, int]]:
    A = M - tau
    c = 2 * A - N
    multiplicity = N - A
    m2 = cap(tau, 2)
    n1 = prod(M - index for index in range(9)) // (c - h) ** 9
    n2 = prod(M - index for index in range(8)) // (c - h) ** 8
    transverse = (
        134_944
        + RESOURCE // (tau + 1)
        + multiplicity
        + n1 * 8_147_918
        + n2 * multiplicity * m2
    )
    paid = multiplicity * cap(tau, dimension)
    return transverse + paid, {
        "transverse": transverse,
        "paid": paid,
        "residual": BUDGET + 1 - transverse,
        "m2": m2,
        "m3": cap(tau, 3),
        "md": cap(tau, dimension),
        "multiplicity": multiplicity,
    }


def max_h(tau: int) -> int:
    c = 2 * (M - tau) - N
    if c <= 0 or total(tau, 0, 9)[0] > BUDGET:
        return -1
    low, high = 0, c - 1
    while low <= high:
        middle = (low + high) // 2
        if total(tau, middle, 9)[0] <= BUDGET:
            low = middle + 1
        else:
            high = middle - 1
    return high


selected_total, data = total(1679, 38384, 9)
adjacent_total, _ = total(1679, 38385, 9)
assert selected_total == 274_969_785_307_868_288
assert BUDGET - selected_total == 10_942_803_526_799
assert adjacent_total - BUDGET == 2_062_328_934_603
assert data["transverse"] == 209_812_758_437_679_617
assert data["paid"] == 65_157_026_870_188_671
assert data["residual"] == 65_167_969_673_715_471
assert data["md"] == 66_298_487_937
assert data["md"] ** 2 < Q
assert -(-data["residual"] // (data["multiplicity"] * data["m2"])) == 262_093_370
assert -(-data["residual"] // (data["multiplicity"] * data["m3"])) == 16_384_884

paying = []
for tau in range(1, W):
    h = max_h(tau)
    if h >= 0:
        paying.append((tau, h))
global_h = max(h for _, h in paying)
assert global_h == 38_384
assert [(tau, h) for tau, h in paying if h == global_h] == [
    (1676, 38384),
    (1677, 38384),
    (1678, 38384),
    (1679, 38384),
]

walls = []
for tau in range(1, W):
    if 2 * (M - tau) - N > 0:
        value, _ = total(tau, 0, 10)
        walls.append((value - BUDGET, tau, value))
assert min(walls) == (773_076_621_594_690_156, 872, 1_048_057_349_706_085_243)

print(
    "RANK11_FULL_SPAN_AUDIT_PASS "
    f"global_h={global_h} containers=16384884 dim10_excess={min(walls)[0]}"
)
