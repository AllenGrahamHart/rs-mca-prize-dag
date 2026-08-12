#!/usr/bin/env python3
"""Text-contract audit for the collision Pade/split-jet dictionary."""

from pathlib import Path

root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()
for token in ("A=a mod z^3", "lambda_1 W_tau(x_*)", "G_X(tau,x_*)", "[2,2]"):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")
for token in ("P_F=b+ay+qR", "ord U_*>=3", "Pade syzygy", "assigned center"):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")
print("RATE_HALF_COLLISION_PADE_SPLIT_JET_DICTIONARY_AUDIT_PASS")
