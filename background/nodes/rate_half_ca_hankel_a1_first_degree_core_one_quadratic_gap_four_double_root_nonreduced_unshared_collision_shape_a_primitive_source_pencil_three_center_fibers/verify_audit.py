#!/usr/bin/env python3
"""Independent audit of the primitive source-pencil degrees."""

from __future__ import annotations


e = (2**39 + 1) // 3
n = (3 * e - 7) // 2
d = 3 * e - 2
total = (9 * e - 7) // 2
before = total - 1

if before != 824633720829:
    raise SystemExit("pencil degree failed")
if (before - (n + 2), before - (n + 3)) != (d - 1, d - 2):
    raise SystemExit("fiber residual degrees failed")
if d - 2 != 549755813885:
    raise SystemExit("fixed degree cap failed")

print(
    "RATE_HALF_SHAPE_A_PRIMITIVE_SOURCE_PENCIL_AUDIT_PASS",
    f"degree={before}",
    f"residuals={(d - 1, d - 2)}",
)
