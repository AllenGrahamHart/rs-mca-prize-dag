#!/usr/bin/env python3
"""Text-contract audit for the quintic Cauchy closed form."""

from pathlib import Path

root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()
for token in ("D_i(t)=sum_", "D_(i+1)=x_*D_i-h_i", "C_i(t)=-Lambda_0", "route fence"):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")
for token in ("3p-5=n_0-3", "leading-coefficient identity", "J_*Lambda_0", "F_i=H_NR"):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")
print("RATE_HALF_COLLISION_QUINTIC_CAUCHY_CLOSED_FORM_AUDIT_PASS")
