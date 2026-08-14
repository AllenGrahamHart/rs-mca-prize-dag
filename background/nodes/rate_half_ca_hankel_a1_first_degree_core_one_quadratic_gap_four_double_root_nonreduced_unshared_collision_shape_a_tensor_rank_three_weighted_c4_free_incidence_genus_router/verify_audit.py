#!/usr/bin/env python3
"""Independent audit of the weighted incidence/genus constants."""

from __future__ import annotations


e = (2**39 + 1) // 3
m = e - 2
n = (3 * e - 7) // 2
T = 3 * e
R = 3 * n + 7
W = 2 * e - 7

parameter_square_cap = T + (m - 1) * (m - 2)
domain_square_cap = R + (n - 1) * (n - 2)

if not T * T > 9 * parameter_square_cap:
    raise SystemExit("parameter ten-vertex floor failed")
if not R * R > 9 * domain_square_cap:
    raise SystemExit("domain ten-vertex floor failed")
if T - W != e + 7 or T - W <= m - 1:
    raise SystemExit("zero-deficit mass failed")
if W != 366503875919:
    raise SystemExit("official deficit failed")

print(
    "RATE_HALF_SHAPE_A_RANK3_WEIGHTED_C4_GENUS_AUDIT_PASS",
    f"parameter_gap={T * T - 9 * parameter_square_cap}",
    f"domain_gap={R * R - 9 * domain_square_cap}",
    f"zero_mass={T - W}",
)
