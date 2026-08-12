#!/usr/bin/env python3
"""Contract audit for the truncated-source separation fence."""

from pathlib import Path

root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()
for token in ("F_101", "A_12", "A_11", "regular-corank"):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")
for token in ("four-dimensional nullspace", "three-dimensional nullspace", "all weights are nonzero"):
    if token not in proof.lower():
        raise AssertionError(f"missing proof token: {token}")
print("RATE_HALF_TRUNCATED_SOURCE_SEPARATION_AUDIT_PASS")
