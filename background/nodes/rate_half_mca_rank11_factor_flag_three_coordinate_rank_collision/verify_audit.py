#!/usr/bin/env python3
"""Independent audit for the three-coordinate residual rank collision."""

from __future__ import annotations

import json
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "source_contract.json").read_text())
u = data["anchor_good_universe"]
r = data["residual_roots"]


def ceiling(numerator: int, denominator: int) -> int:
    quotient, remainder = divmod(numerator, denominator)
    return quotient + (remainder != 0)


m2 = ceiling((r - 1) * data["initial_mass"], u - 1)
m3 = ceiling((r - 2) * m2, u - 2)
assert (m2, m3) == (data["second_mass"], data["third_mass"])

n, k, agreement, d = 2_097_152, 1_048_576, 1_114_369, 4
numerator = prod(n - k + i for i in range(1, d + 1))
denominator = prod(agreement - k + i for i in range(1, d + 1))
cap = (n - agreement) * (numerator // denominator)
assert cap == data["rank_three_slope_cap"]
assert m3 > cap

contract = (HERE / "claim_contract.md").read_text().lower()
assert "rank one" in contract
assert "aggregate payment" in contract
audit = (HERE / "audit.md").read_text().lower()
assert "distinct" in audit
assert "first-owned" in audit

print(f"RANK11_THREE_COORD_AUDIT_PASS mass3={m3} cap4={cap} ratio_floor={m3 // cap}")
