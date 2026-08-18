#!/usr/bin/env python3
"""Independent audit for the factor-flag clone/line dichotomy."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
d = json.loads((HERE / "source_contract.json").read_text())
u = d["universe"]
low = d["deep_mass"] * comb(d["residual_roots"], 3) - d["rank_three_cap"] * comb(u, 3)
assert low == d["low_rank_incidence"]

cutoff = d["selected_clone_cutoff"]
blocks, rem = divmod(u, cutoff)
packed = blocks * (cutoff * (cutoff - 1) * (cutoff - 2) // 6)
packed += rem * (rem - 1) * (rem - 2) // 6
assert packed == d["selected_clone_triples"]

rank_two_incidence = low - d["clone_bucket_cap"] * packed
q, r = divmod(rank_two_incidence, comb(u, 3))
line_mass = q + (r != 0)
assert line_mass == d["selected_rank_two_mass"]
assert line_mass > 0

contract = (HERE / "claim_contract.md").read_text().lower()
assert "owner-pencil clone" in contract
assert "rank-two horn" in contract
audit = (HERE / "audit.md").read_text().lower()
assert "rank exactly two" in audit
assert "first-owned" in audit

print(
    "RANK11_CLONE_LINE_AUDIT_PASS "
    f"clone_cutoff={cutoff} clone_output={cutoff + 1} line_mass={line_mass}"
)
