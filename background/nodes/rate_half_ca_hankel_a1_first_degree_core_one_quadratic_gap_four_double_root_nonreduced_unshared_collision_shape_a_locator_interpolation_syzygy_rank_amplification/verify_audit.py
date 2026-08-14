#!/usr/bin/env python3
"""Independent audit of the interpolation rank floor."""

from __future__ import annotations


e = (2**39 + 1) // 3
n = (3 * e - 7) // 2
d = 3 * e - 2
rows = (9 * e - 7) // 2
r = (e + 1) // 2

if rows - d - 2 != n:
    raise SystemExit("parity range failed")
if not 3 * r - (e + 1) >= r - 1:
    raise SystemExit("kernel capacity failed")
if r != 91625968982:
    raise SystemExit("official rank floor failed")
if 3 * r - (e + 1) != r:
    raise SystemExit("boundary kernel failed")

print(
    "RATE_HALF_SHAPE_A_LOCATOR_INTERPOLATION_RANK_AMPLIFICATION_AUDIT_PASS",
    f"parity_dimension={n + 1}",
    f"rank_floor={r}",
    f"boundary_kernel={r}",
)
