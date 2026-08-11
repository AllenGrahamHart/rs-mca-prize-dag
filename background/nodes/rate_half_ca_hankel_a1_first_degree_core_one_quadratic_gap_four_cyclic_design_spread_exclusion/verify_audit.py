#!/usr/bin/env python3
"""Audit semantic pins for the cyclic-design spread exclusion."""

from pathlib import Path


root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()
contract = (root / "claim_contract.md").read_text()

for token in ["exactly", "e+3", "ceil((3e+6)/2)", "official row"]:
    assert token in statement
for token in ["more than seven", "3e-4", "2rho", "length-`e`"]:
    assert token in proof
for token in ["explicit Cycle-107 cyclic design", "no exclusion of arbitrary designs"]:
    assert token in contract

print("QUADRATIC_GAP_FOUR_CYCLIC_DESIGN_SPREAD_EXCLUSION_AUDIT_PASS")
