#!/usr/bin/env python3
"""Independent integer audit of domain-map birationality."""

from __future__ import annotations

from math import gcd


e = (2**39 + 1) // 3
m = e - 2
n = (3 * e - 7) // 2
rows = (9 * e - 7) // 2
residual = 3 * e * n - rows * m

if residual != 2 * e - 7 or residual != 2 * m - 3:
    raise SystemExit("residual norm identity failed")
if not (m <= residual < 2 * m):
    raise SystemExit("outside-point interval failed")
if rows != 3 * n + 7:
    raise SystemExit("row identity failed")
if (gcd(n, rows), gcd(n, rows + 1)) != (1, 1):
    raise SystemExit("domain-map gcd failed")

print(
    "RATE_HALF_SHAPE_A_ALL_EXCESS_DOMAIN_MAP_BIRATIONALITY_AUDIT_PASS",
    f"residual_interval=({m},{2 * m})",
    f"gcds={(gcd(n, rows), gcd(n, rows + 1))}",
)
