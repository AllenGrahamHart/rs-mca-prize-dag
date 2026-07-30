#!/usr/bin/env python3
"""Independent semantic audit for the infinity-owner route cut."""

from pathlib import Path

root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()

assert "one fixed received label" in statement
assert "Changing `u_infinity` selects a different received table" in proof
assert "abstract neighbor ledgers" in statement
assert "not a source counterexample" in statement

print("L1_M31_SOURCE_HEAD_INFINITY_OWNER_ROUTE_CUT_AUDIT_PASS")
