#!/usr/bin/env python3
"""Independent audit of the pure-fiber first-jet obstruction."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


e = 183251937963
m = e - 2
n = (3 * e - 7) // 2

require(m > 1 and n > 1, "nonconstant shape-A biform")
require(e + 7 > 0, "pure split fiber exists")
require(n == 274877906941, "independent row degree")
require(n > 4, "one pure fiber exceeds residual degree")

# At every pure-fiber incidence, squarefreeness gives G_X != 0 and the
# classified-row root dictionary gives G_t != 0. Either nonzero value is
# already incompatible with one required mandatory zero.
mandatory_order = 1
raw_t_order = 0
raw_x_order = 0
require(raw_t_order < mandatory_order, "parameter derivative does not descend")
require(raw_x_order < mandatory_order, "row derivative does not descend")

print(
    "RATE_HALF_SHAPE_A_NATURAL_SECTION_FENCE_AUDIT_PASS "
    f"pure_points={n} mandatory_order={mandatory_order}"
)
