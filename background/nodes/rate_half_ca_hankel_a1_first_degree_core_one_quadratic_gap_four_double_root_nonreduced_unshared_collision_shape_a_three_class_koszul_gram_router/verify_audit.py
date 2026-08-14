#!/usr/bin/env python3
"""Independent arithmetic audit of the Koszul/Gram thresholds."""

from __future__ import annotations


e = (2**39 + 1) // 3
n = (3 * e - 7) // 2
p = (3 * e - 1) // 2
r0 = -(-(e + 1) // 3)
threshold = (n + 2) // 2 + 1

if p != n + 3:
    raise SystemExit("p/n identity failed")
if 3 * r0 - (e + 1) != 2:
    raise SystemExit("minimum Koszul kernel failed")
if threshold != 137438953472:
    raise SystemExit("Gram threshold failed")
if not 2 * (threshold - 1) <= n + 2 < 2 * threshold:
    raise SystemExit("Gram threshold interval failed")

print(
    "RATE_HALF_SHAPE_A_THREE_CLASS_KOSZUL_GRAM_AUDIT_PASS",
    f"classes={(p - 1, p - 1, p)}",
    f"kernel_min={3 * r0 - (e + 1)}",
    f"gram_nonzero_from={threshold}",
)
