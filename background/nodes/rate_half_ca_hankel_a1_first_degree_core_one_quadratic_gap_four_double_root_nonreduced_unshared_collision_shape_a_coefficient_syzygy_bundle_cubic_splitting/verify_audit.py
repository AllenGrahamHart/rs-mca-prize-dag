#!/usr/bin/env python3
"""Independent audit of the minimum syzygy profiles."""

from __future__ import annotations


e = (2**39 + 1) // 3
m = e - 2
r = -(-(e + 1) // 3)
k2 = 3 * r - (e + 1)
profiles = ((1, 0, r - 2), (0, 2, r - 3))

if k2 != 2:
    raise SystemExit("minimum kernel failed")
for c1, c2, c3 in profiles:
    if c1 + c2 + c3 != r - 1:
        raise SystemExit("profile rank failed")
    if c1 + 2 * c2 + 3 * c3 != m:
        raise SystemExit("profile degree failed")
    if 2 * c1 + c2 != k2:
        raise SystemExit("profile sections failed")

print(
    "RATE_HALF_SHAPE_A_COEFFICIENT_SYZYGY_BUNDLE_CUBIC_SPLITTING_AUDIT_PASS",
    f"rank={r}",
    f"profiles={profiles}",
)
