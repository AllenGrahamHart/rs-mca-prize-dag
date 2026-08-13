#!/usr/bin/env python3
"""Independent index and layer-cake audit for the recurrence flag."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


e = 183251937963
p = (3 * e - 1) // 2
R = 3 * p - 2
d = 2 * p - 1
n = p - 3

require(R - 1 - (d + 1) == n, "first omitted coefficient index")
require(R - 1 - (d + 1 + n - 1) == 1, "last nonconstant coefficient index")
require(R == 824633720830, "classified row count")
require(d == 549755813887 and n == 274877906941, "official degrees")

degree_drops = (4, 2, 2, 1, 0)
nested_counts = tuple(sum(drop >= level for drop in degree_drops) for level in range(1, 5))
require(nested_counts == (4, 3, 1, 1), "nested common-root counts")
require(sum(degree_drops) == sum(nested_counts) == 9, "layer-cake identity")

print(
    "RATE_HALF_SHAPE_A_OMITTED_RECURRENCE_FLAG_AUDIT_PASS "
    f"R={R} d={d} n={n} layer_cake={sum(nested_counts)}"
)
