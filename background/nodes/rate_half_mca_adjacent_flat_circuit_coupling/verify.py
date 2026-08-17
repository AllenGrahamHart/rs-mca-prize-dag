#!/usr/bin/env python3
"""Verify exact controls for the adjacent-flat circuit coupling."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


data = json.loads(Path(__file__).with_name("source_contract.json").read_text())
assert data["schema"] == "rate-half-mca-adjacent-flat-circuit-coupling-v1"
assert data["formula"] == "(r+2)*C_high <= (B-r)*C(N,r+1)-(N-B)*C_low"

checks = 0
for row in data["sharp_uniform_rows"]:
    r, n, b = row["r"], row["N"], row["B"]
    left = (r + 2) * row["C_high"]
    right = (b - r) * comb(n, r + 1) - (n - b) * row["C_low"]
    assert b == n - 1
    assert left == right
    checks += 2

row = data["zero_control"]
left = (row["r"] + 2) * row["C_high"]
right = (row["B"] - row["r"]) * comb(row["N"], row["r"] + 1)
assert left == right == 0
checks += 1

print(json.dumps({"checks": checks, "sharp_rows": 4}, sort_keys=True))
