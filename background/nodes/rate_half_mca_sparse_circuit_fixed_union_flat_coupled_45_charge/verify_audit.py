#!/usr/bin/env python3
"""Independent audit of the K'=72 fixed-union control."""

from __future__ import annotations

import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
EXPECTED_SHA256 = "295d82f01e6a8cb9f9ef1d9dd4a0966e14d729cfde5a8259bb0df07ca9a66cd4"
raw = CONTRACT.read_bytes()
assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
row = json.loads(raw)["k72_control"]

N = row["m"] - row["u"]
R = row["K"] - row["u"] - row["g"]
B = R + 3
assert (N, R, B) == (row["N"], row["R"], row["B"])

lower = {}
for d in (4, 5):
    lower[d] = comb(row["u"], d) + sum(
        comb(row["u"], d - j) * comb(N, j - 1) * R // j
        for j in range(1, d)
    )
x4 = min(R * comb(N, 3) // 4, R * comb(N, 4) // (N - B))
x5 = (R * comb(N, 4) - (N - B) * x4) // 5
i4 = (lower[4] + x4) * comb(row["m"] - 4, 7)
i5 = (lower[5] + x5) * comb(row["m"] - 5, 6)
assert (x4, x5, i4, i5) == (row["X4"], row["X5"], row["I4"], row["I5"])
assert 21 * i4 + 15 * i5 == row["weighted"]

print(json.dumps({
    "contract_sha256": EXPECTED_SHA256,
    "independent_checks": 6,
}, sort_keys=True))
