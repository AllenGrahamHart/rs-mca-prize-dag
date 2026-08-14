#!/usr/bin/env python3
"""Independent dimension audit for the source-multiplier normal form."""

from __future__ import annotations


e = (2**39 + 1) // 3
n = (3 * e - 7) // 2
r = (e + 1) // 2
total = (9 * e - 7) // 2

if total != 3 * n + 7:
    raise SystemExit("source algebra dimension failed")
if 3 * r != n + 5 or 3 * r != 274877906946:
    raise SystemExit("three-multiplier dimension failed")
if total - 3 * r != 2 * n + 2 or total - 3 * r != 549755813884:
    raise SystemExit("orthogonal dimension failed")
if e - 3 != 183251937960:
    raise SystemExit("intersection floor failed")

print(
    "RATE_HALF_SHAPE_A_GLOBAL_SOURCE_MULTIPLIER_AUDIT_PASS",
    f"algebra={total}",
    f"multiplier={3 * r}",
    f"orthogonal={total - 3 * r}",
)
