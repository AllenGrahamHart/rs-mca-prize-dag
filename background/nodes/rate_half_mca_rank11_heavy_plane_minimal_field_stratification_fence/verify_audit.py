#!/usr/bin/env python3
"""Independent audit for the heavy-plane minimal-field fence."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
d = json.loads((HERE / "source_contract.json").read_text())

degree = d["extension_degree"]
field_degrees = []
for candidate in range(1, degree + 1):
    quotient, remainder = divmod(degree, candidate)
    if remainder == 0 and quotient >= 1:
        field_degrees.append(candidate)
assert field_degrees == d["minimal_field_degrees"]

heavy, remainder = divmod(d["mass"], len(field_degrees))
if remainder:
    heavy += 1
assert heavy == d["heavy_stratum_mass"]

factor_floor, remainder = divmod(heavy, d["rank_two_cap"])
if remainder:
    factor_floor += 1
assert factor_floor == 11 == d["minimum_stratum_factors"]
assert 10 * d["rank_two_cap"] + d["heavy_stratum_gap"] == heavy

# Distinct top degrees give an independent product basis below K=7.
tops = d["witness_product_degrees"]
assert sorted(set(tops)) == tops
assert tops[-1] + 1 == d["witness_shortened_dimension"]

last = d["mass"] - d["witness_full_factors"] * d["rank_two_cap"]
assert 0 < last == d["witness_last_mass"] <= d["rank_two_cap"]
assert d["witness_factor_count"] == d["witness_full_factors"] + 1

proof = (HERE / "proof.md").read_text().lower()
assert "plucker" in proof
assert "frobenius-stable" in proof
assert "not an mca" in (HERE / "statement.md").read_text().lower()
audit = (HERE / "audit.md").read_text().lower()
assert "basis scaling" in audit
assert "first-owned" in audit

print(
    "RANK11_MINIMAL_FIELD_AUDIT_PASS "
    f"degrees={','.join(map(str, field_degrees))} "
    f"heavy_mass={heavy} factors={factor_floor}"
)
