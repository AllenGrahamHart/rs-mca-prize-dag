#!/usr/bin/env python3
"""Text-contract audit for the nonreduced divided-row quintic quotient."""

from pathlib import Path

root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()
for token in ("F_i=H_mom C_i", "deg_t C<=5", "C_0(tau)", "Lambda_0"):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")
for token in ("Pade syzygy", "deg F_0<=e+1", "divide by `g_*S_B`", "J_*g_off S_B=g_*S_B"):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")
print("RATE_HALF_NONREDUCED_DIVIDED_ROW_QUINTIC_AUDIT_PASS")
