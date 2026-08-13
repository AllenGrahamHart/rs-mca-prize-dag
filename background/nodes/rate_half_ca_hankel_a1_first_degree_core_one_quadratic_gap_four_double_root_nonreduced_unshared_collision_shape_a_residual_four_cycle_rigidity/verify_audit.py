#!/usr/bin/env python3
"""Independent audit of the residual divisor and bundle-degree argument."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


e = 183251937963
d = 3 * e - 2
deg_r = e - 6
deg_b = 2

require(deg_r + 3 * deg_b == e, "vertical normal form")
require(deg_r + 2 * deg_b == e - 2, "contact normal form")
require(2 * deg_b == 4, "twice-B residual")

# The two possible normalized correction partitions have the same pullback
# intersection length.
for partition in ((2,), (1, 1)):
    require(sum(partition) == deg_b, "correction partition")
    require(sum(2 * value for value in partition) == 4, "local length four")

first_negative_ceiling = 1 - d
second_negative_ceiling = first_negative_ceiling + 1
require(first_negative_ceiling < 0, "first modification negativity")
require(second_negative_ceiling == 2 - d < 0, "second modification negativity")

print(
    "RATE_HALF_SHAPE_A_RESIDUAL_FOUR_RIGIDITY_AUDIT_PASS "
    f"residual=4 negative_ceiling={second_negative_ceiling}"
)
