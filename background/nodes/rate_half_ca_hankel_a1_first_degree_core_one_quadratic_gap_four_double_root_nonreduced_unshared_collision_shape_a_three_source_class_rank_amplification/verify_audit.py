#!/usr/bin/env python3
"""Independent audit of the source-class rank floor."""

from __future__ import annotations


e = (2**39 + 1) // 3
n = (3 * e - 7) // 2
d = 3 * e - 2
rows = (9 * e - 7) // 2
floor = -(-(e + 1) // 3)

if not rows > d > n:
    raise SystemExit("evaluation-degree ordering failed")
if floor != 61083979322:
    raise SystemExit("official rank floor failed")
if not 3 * (floor - 1) < e + 1 <= 3 * floor:
    raise SystemExit("ceiling interval failed")

print(
    "RATE_HALF_SHAPE_A_THREE_SOURCE_CLASS_RANK_AMPLIFICATION_AUDIT_PASS",
    f"degrees={(n, d, rows)}",
    f"rank_floor={floor}",
)
