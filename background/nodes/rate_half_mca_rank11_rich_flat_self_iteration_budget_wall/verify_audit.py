#!/usr/bin/env python3
"""Independent reverse-order replay of the rich-flat recursion wall."""

N, K, M = 2_097_152, 1_048_576, 1_116_048
A, C0 = 1_114_501, 131_850
LOW = 206_105_684_094_104_220
OUTSIDE = N - A


def product(values) -> int:
    out = 1
    for value in values:
        out *= value
    return out


def choose(n: int, r: int) -> int:
    return product(range(n - r + 1, n + 1)) // product(range(1, r + 1))


def cap(q: int) -> int:
    if q == 1:
        return 8_147_918
    ordinary = choose(N - K + q, q) // choose(A - K + q, q)
    return OUTSIDE * ordinary


def census(q: int, delta: int) -> int:
    p = 10 - q
    numerator = product(range(M - p + 1, M + 1))
    return numerator // product([delta] * p)


def cost(q: int, delta: int) -> int:
    return census(q, delta) * cap(q)


best_shared = None
best_one = None
best_two = None
for d in range(C0, 0, -1):
    shared = cost(1, d) + cost(2, d)
    if shared <= LOW:
        item = (C0 - d, d, shared)
        best_shared = item if best_shared is None or item > best_shared else best_shared

    e = C0 + 1 - d
    item_one = (cost(1, d) + cost(2, e), d, e)
    item_two = (cost(2, d) + cost(3, e), d, e)
    best_one = item_one if best_one is None or item_one < best_one else best_one
    best_two = item_two if best_two is None or item_two < best_two else best_two

assert best_shared == (42_452, 89_398, 206_103_676_871_467_496)
assert best_one == (2_539_543_014_780_268_202, 64_305, 67_546)
assert best_two == (3_232_479_920_013_973_566, 66_671, 65_180)
assert best_one[0] > 12 * LOW
assert best_two[0] > 15 * LOW
print("RANK11_RICH_FLAT_SELF_ITERATION_WALL_AUDIT_OK", best_shared[0])
