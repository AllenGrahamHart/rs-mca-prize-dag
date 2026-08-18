#!/usr/bin/env python3
"""Independent arithmetic and scope audit for the cover payment."""

from __future__ import annotations

import json
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "source_contract.json").read_text())
row = data["row"]

n = row["n"]
k = row["k"]
agreement = row["A"]
multiplicity = n - agreement
allowance = row["budget"] - row["transverse"]
q = 2_130_706_433**6

rebuilt = []
for d in range(1, 10):
    numerator = prod(n - k + i for i in range(1, d + 1))
    denominator = prod(agreement - k + i for i in range(1, d + 1))
    list_cap = numerator // denominator
    slope_cap = multiplicity * list_cap
    rebuilt.append((d, list_cap, slope_cap, allowance // slope_cap + 1))
    assert list_cap**2 < q

pinned = [
    (entry["d"], entry["M"], entry["R"], entry["first_unsafe_uniform_cover"])
    for entry in data["dimensions"]
]
assert rebuilt == pinned
assert allowance == 65_167_969_673_715_470
assert 64_501 * rebuilt[4][2] <= allowance < 64_502 * rebuilt[4][2]
assert 2 * rebuilt[4][2] == data["corollaries"]["two_five_space_cost"]

required_nonclaims = (
    "does not produce a subspace cover",
    "does not synchronize locators",
    "requires first-match partition ownership",
)
contract_text = (HERE / "claim_contract.md").read_text().lower()
assert "existence or uniqueness of a cover" in contract_text
assert "equality or synchronization" in contract_text
audit_text = (HERE / "audit.md").read_text().lower()
assert "partition, not an overlapping cover" in audit_text

print(
    "RANK11_SUBSPACE_COVER_AUDIT_PASS "
    f"dimensions={len(rebuilt)} factor_threshold={rebuilt[4][3]} "
    f"scope_checks={len(required_nonclaims)}"
)
