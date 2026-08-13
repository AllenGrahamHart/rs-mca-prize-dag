#!/usr/bin/env python3
"""Independent arithmetic audit of the birational singularity router."""

from __future__ import annotations

from math import gcd


e = (2**39 + 1) // 3
m = e - 2
n = (3 * e - 7) // 2
deficit = 2 * e - 7

if deficit // n != 1 or 2 * n <= deficit:
    raise SystemExit("empty-column audit failed")
if (gcd(m, 3 * e), gcd(m, 3 * e - 1)) != (1, 1):
    raise SystemExit("normalization-degree gcd audit failed")

total = m - 6
low, extra = divmod(total, 6)
branches = [low + 1] * extra + [low] * (6 - extra)
delta_sum = sum(value * (value - 1) // 2 for value in branches)
pair_floor = max(branches)
local_delta = pair_floor * (pair_floor - 1) // 2

if branches != [30541989660] + [30541989659] * 5:
    raise SystemExit("balanced branch ledger drift")
if local_delta != 466406566180502462970:
    raise SystemExit("local delta drift")
if delta_sum != 2798439396930304829525:
    raise SystemExit("six-vertex delta drift")

print(
    "RATE_HALF_SHAPE_A_TENSOR_RANK_THREE_BIRATIONAL_ROUTER_AUDIT_PASS",
    f"gcds={(gcd(m, 3 * e), gcd(m, 3 * e - 1))}",
    f"branches={branches}",
    f"delta={delta_sum}",
)
