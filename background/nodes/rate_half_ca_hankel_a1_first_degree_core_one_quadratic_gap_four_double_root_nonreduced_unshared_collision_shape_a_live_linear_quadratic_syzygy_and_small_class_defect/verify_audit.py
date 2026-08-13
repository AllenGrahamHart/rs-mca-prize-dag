#!/usr/bin/env python3
"""Independent audit of the live profile formulas."""

from __future__ import annotations


e = (2**39 + 1) // 3
m = e - 2
n = (3 * e - 7) // 2
r = (e + 1) // 2
c1, c2, c3 = 2 * r - e, e - r - 1, 0

if (c1, c2, c3) != (1, 91625968980, 0):
    raise SystemExit("boundary profile failed")
if c1 + c2 + c3 != r - 1:
    raise SystemExit("rank count failed")
if c1 + 2 * c2 + 3 * c3 != m:
    raise SystemExit("degree count failed")
if n + 2 != 274877906943:
    raise SystemExit("small class failed")

print(
    "RATE_HALF_SHAPE_A_LIVE_LINEAR_QUADRATIC_SYZYGY_DEFECT_AUDIT_PASS",
    f"boundary={(r, c1, c2, c3)}",
    f"small_class={n + 2}",
)
