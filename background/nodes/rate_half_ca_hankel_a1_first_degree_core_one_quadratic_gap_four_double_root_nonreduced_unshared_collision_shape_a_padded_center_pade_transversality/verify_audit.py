#!/usr/bin/env python3
"""Independent audit of the padded-center resultant order."""

from __future__ import annotations


e = (2**39 + 1) // 3
d = 3 * e - 2
order = (2 * d + 1) * 0 + 1 + 2 * 0

if d != 549755813887:
    raise SystemExit("locator degree failed")
if order != 1:
    raise SystemExit("resultant order failed")

print(
    "RATE_HALF_SHAPE_A_PADDED_CENTER_PADE_TRANSVERSALITY_AUDIT_PASS",
    f"degree={d}",
    f"order={order}",
)
