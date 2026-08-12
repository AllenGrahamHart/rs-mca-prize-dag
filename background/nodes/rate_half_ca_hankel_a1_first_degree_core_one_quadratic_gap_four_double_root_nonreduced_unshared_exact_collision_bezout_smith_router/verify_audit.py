#!/usr/bin/env python3
"""Text-contract audit for the exact collision Smith router."""

from pathlib import Path

root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()
for token in ("ord_z a>=1", "[1,3]", "[2,2]", "lambda_1=[z]a(z)"):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")
for token in ("Hensel", "multiplication by `p=b+ay`", "b^2-a b c_1+a^2c_0"):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")
print("RATE_HALF_NONREDUCED_COLLISION_BEZOUT_SMITH_AUDIT_PASS")
