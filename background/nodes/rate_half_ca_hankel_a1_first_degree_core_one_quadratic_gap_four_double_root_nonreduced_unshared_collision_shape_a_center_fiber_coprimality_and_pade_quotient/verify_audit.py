#!/usr/bin/env python3
"""Independent audit of center Pade quotient degrees."""

from __future__ import annotations


e = (2**39 + 1) // 3
n = (3 * e - 7) // 2
d = 3 * e - 2
total = (9 * e - 7) // 2
small = total - 1 - (n + 2)
large = total - 1 - (n + 3)

if (small, large) != (d - 1, d - 2):
    raise SystemExit("quotient degree audit failed")
if (d - 1, d - 2) != (549755813886, 549755813885):
    raise SystemExit("official quotient degrees failed")

print(
    "RATE_HALF_SHAPE_A_CENTER_FIBER_COPRIMALITY_PADE_AUDIT_PASS",
    f"degrees={(d, small, large)}",
)
