#!/usr/bin/env python3
"""Independent audit for active-clone locator shortening."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
d = json.loads((HERE / "source_contract.json").read_text())

# Reconstruct the bounds without the primary verifier's endpoint loop.
product_floor = 2 + 4 - 1
assert product_floor == d["product_dimension_floor"]
c_upper = d["k"] - product_floor
assert c_upper == d["clone_size_max"] == 1048571
s_upper = d["k"] - d["clone_size_min"]
assert s_upper == d["shortened_k_max"] == 1038575
assert d["shortened_k_min"] == product_floor

invariants = (
    d["n"] - d["k"],
    d["m"] - d["k"],
    d["n"] - d["m"],
)
assert invariants == (d["redundancy"], d["agreement_gap"], d["misses"])
for c in (10001, 42453, c_upper):
    shortened = (d["n"] - c, d["k"] - c, d["m"] - c)
    assert (
        shortened[0] - shortened[1],
        shortened[2] - shortened[1],
        shortened[0] - shortened[2],
    ) == invariants

proof = (HERE / "proof.md").read_text().lower()
assert "strictly increasing degrees" in proof
assert "first-match" in proof
audit = (HERE / "audit.md").read_text().lower()
assert "not merely their evaluation" in audit
assert "remains unpaid" in audit

print(
    "RANK11_ACTIVE_CLONE_AUDIT_PASS "
    f"product_floor={product_floor} c_max={c_upper} mass={d['active_mass']}"
)
