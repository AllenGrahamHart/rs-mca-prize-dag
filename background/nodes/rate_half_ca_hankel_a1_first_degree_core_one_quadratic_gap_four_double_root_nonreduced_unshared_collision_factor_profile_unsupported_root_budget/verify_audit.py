#!/usr/bin/env python3
"""Text-contract audit for the collision factor unsupported-root budget."""

from pathlib import Path

root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()
for token in ("sum_j u_j<=4+d_A", "3e-8-2d_A", "profiles II and III", "109951162777"):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")
for token in ("Rm_j+s_j<=Tn_j", "g_off=g_*/J_*", "e-6-d_A", "2sigma_j"):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")
print("RATE_HALF_COLLISION_FACTOR_UNSUPPORTED_ROOT_BUDGET_AUDIT_PASS")
