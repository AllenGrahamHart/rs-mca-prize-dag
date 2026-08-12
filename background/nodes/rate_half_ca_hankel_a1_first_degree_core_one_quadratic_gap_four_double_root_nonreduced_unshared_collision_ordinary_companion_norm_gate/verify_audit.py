#!/usr/bin/env python3
"""Text-contract audit for the ordinary-companion norm gate."""

from pathlib import Path

root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()

for token in (
    "N_Q(X)=L_0(X)^m S_Q(X)",
    "gcd(S_Q,L_0)=1",
    "(X-x_*)^(m/2) divides S_Q",
    "deg E_Q<=6",
    "deg E_Q<=12",
):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")

for token in (
    "ord_(X=x)N_Q=m",
    "does not by itself force",
    "L_0'(x)^mS_Q(x)",
):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")

print("RATE_HALF_COLLISION_ORDINARY_COMPANION_NORM_AUDIT_PASS")
