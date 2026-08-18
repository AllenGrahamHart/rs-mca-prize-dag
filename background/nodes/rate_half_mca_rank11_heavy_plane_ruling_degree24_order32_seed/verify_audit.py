#!/usr/bin/env python3
"""Independent audit for the heavy-ruling degree-24 seed."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
d = json.loads((HERE / "source_contract.json").read_text())

heavy = d["orientation_mass"] - d["rank_four_pair_types"]
quotient, remainder = divmod(heavy, d["rank_four_pair_types"])
dense = quotient + (1 if remainder else 0)
assert heavy == 322417998 == d["heavy_record_mass"]
assert dense == 5525 == d["dense_pair_minimum"]

heavy_capacity = 0
for _ in range(d["rank_two_pair_types"]):
    heavy_capacity += d["fixed_pair_multiplicity"]
total_capacity = heavy_capacity + d["rank_four_pair_types"]
assert heavy_capacity == 236448715 == d["large_core_heavy_capacity"]
assert total_capacity == 236507076 == d["large_core_total_capacity"]
assert d["orientation_mass"] - total_capacity == 85969283

pair_types = 1 + d["maximum_additional_pair_types"]
anchor_records = d["seed_size"] - 2 * (pair_types - 1)
assert pair_types == 5 == d["maximum_selected_pair_types"]
assert anchor_records == 24 == d["minimum_anchor_records"]
assert dense > d["seed_size"]
assert d["minimum_slope_degree"] == anchor_records
assert d["maximum_slope_degree"] + 1 == d["seed_size"]

proof = (HERE / "proof.md").read_text().lower()
assert "subtracting the two scalar agreement equations" in proof
assert "coefficientwise interpolation" in proof
audit = (HERE / "audit.md").read_text().lower()
assert "narrower" in audit
assert "whole-line" in audit

print(
    "RANK11_RULING_DEG24_AUDIT_PASS "
    f"heavy={heavy} dense={dense} gap={d['large_core_gap']} "
    f"anchor={anchor_records}"
)
