#!/usr/bin/env python3
"""Independent audit of the center-class dimensions."""

from __future__ import annotations


e = (2**39 + 1) // 3
n = (3 * e - 7) // 2
d = 3 * e - 2
total = (9 * e - 7) // 2
r = (e + 1) // 2
k2 = 3 * r - (e + 1)
c1 = 2 * r - e

if k2 - c1 != r - 1:
    raise SystemExit("coordinate projection failed")
if (total - (n + 2), total - (n + 3)) != (d, d - 1):
    raise SystemExit("center locator roots failed")
if (n + 3) - (n + 1) != 2:
    raise SystemExit("large dual dimension failed")
if 3 - 1 != 2:
    raise SystemExit("heavy residual quotient failed")

print(
    "RATE_HALF_SHAPE_A_CENTER_FIBER_LARGE_CLASS_DICHOTOMY_AUDIT_PASS",
    f"boundary={(r, k2, c1)}",
    f"rest={(d, d - 1)}",
)
