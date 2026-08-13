#!/usr/bin/env python3
"""Text-contract audit for the contact-module presentation."""

from pathlib import Path

root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()
for token in (
    "Bez_(Q,P_F)=T_Q H T_Q^T",
    "det T_Q=+-lc_X(Q)^d",
    "A_tau/P_F A_tau",
    "degree-preserving",
):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")
for token in ("Q(Z)R", "unimodular", "Sylvester", "contact-module presentation"):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")
print("RATE_HALF_PADE_BEZOUT_CONTACT_MODULE_AUDIT_PASS")
