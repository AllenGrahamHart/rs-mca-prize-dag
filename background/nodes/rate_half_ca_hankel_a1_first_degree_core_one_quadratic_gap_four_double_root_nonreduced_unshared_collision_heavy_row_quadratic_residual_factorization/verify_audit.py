#!/usr/bin/env python3
"""Text-contract audit for the center-adjusted heavy-row residual."""

from pathlib import Path

root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()
for token in ("J_*=gcd(Lambda,g_*)", "g_off=g_*/J_*", "deg T_(2+d_A)=2+d_A", "B_row lambda=0"):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")
for token in ("deg J_*=d_A", "off-line supported slope", "R=g_off K_(4+d_A)", "Polynomial remainder is linear"):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")
print("RATE_HALF_NONREDUCED_HEAVY_ROW_CENTER_ADJUSTED_AUDIT_PASS")
