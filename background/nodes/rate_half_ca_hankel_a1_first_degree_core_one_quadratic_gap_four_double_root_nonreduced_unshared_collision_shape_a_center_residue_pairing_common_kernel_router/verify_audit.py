#!/usr/bin/env python3
"""Independent arithmetic audit of the common-kernel boundary."""

from __future__ import annotations


e = (2**39 + 1) // 3
n = (3 * e - 7) // 2
r0 = (e + 1) // 2
kappa_floor = n + 1 - r0

if (e, n, r0) != (183251937963, 274877906941, 91625968982):
    raise SystemExit("official Shape-A parameters failed")
if kappa_floor != e - 3 or kappa_floor != 183251937960:
    raise SystemExit("common-kernel boundary failed")
if (5 * e - 3) // 6 != 152709948302:
    raise SystemExit("zero-kappa rank floor failed")

print(
    "RATE_HALF_SHAPE_A_CENTER_RESIDUE_PAIRING_AUDIT_PASS",
    f"kappa_boundary={kappa_floor}",
    f"zero_kappa_floor={(5 * e - 3) // 6}",
)
