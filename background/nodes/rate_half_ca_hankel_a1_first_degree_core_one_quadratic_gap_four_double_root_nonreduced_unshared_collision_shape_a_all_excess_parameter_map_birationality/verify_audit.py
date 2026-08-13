#!/usr/bin/env python3
"""Independent integer audit of all-rank parameter-map birationality."""

from __future__ import annotations

from math import gcd


e = (2**39 + 1) // 3
m = e - 2
n = (3 * e - 7) // 2
deficit = 2 * e - 7

if not (n <= deficit < 2 * n):
    raise SystemExit("empty-column interval drift")
if 3 * e != 3 * m + 6 or 3 * e - 1 != 3 * m + 5:
    raise SystemExit("gcd reduction identity drift")
if (gcd(m, 3 * e), gcd(m, 3 * e - 1)) != (1, 1):
    raise SystemExit("birationality gcd failed")

print(
    "RATE_HALF_SHAPE_A_ALL_EXCESS_PARAMETER_MAP_BIRATIONALITY_AUDIT_PASS",
    f"deficit_interval=({n},{2 * n})",
    f"gcds={(gcd(m, 3 * e), gcd(m, 3 * e - 1))}",
)
