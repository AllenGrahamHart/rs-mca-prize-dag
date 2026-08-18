#!/usr/bin/env python3
"""Independent arithmetic and incidence audit for the product cover."""

from fractions import Fraction


DIM_P = 2
DIM_B = 3
assert DIM_P * DIM_B == 6
assert 6 < 7

containers = 8_406
zeros_per_container = 42_452
universe = 1_116_048
raw = Fraction(containers * zeros_per_container - universe, containers - 1)
floor = (raw.numerator + raw.denominator - 1) // raw.denominator
assert floor == 42_325

# Exact endpoint audit: the printed floor pays all incidences, one less does not.
incidences = containers * zeros_per_container
assert universe + (containers - 1) * floor >= incidences
assert universe + (containers - 1) * (floor - 1) < incidences

# The fixed locus can be only 127 coordinates smaller than every selected core.
assert zeros_per_container - floor == 127

print(
    "RANK11_PRODUCT_COVER_AUDIT_PASS "
    f"span_cap={DIM_P*DIM_B} core_floor={floor} gap={zeros_per_container-floor}"
)
