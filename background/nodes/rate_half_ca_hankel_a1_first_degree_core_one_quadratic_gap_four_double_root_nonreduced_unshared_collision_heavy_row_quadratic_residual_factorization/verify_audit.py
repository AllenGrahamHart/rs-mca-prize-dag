#!/usr/bin/env python3
"""Text-contract audit for the nonreduced heavy-row quadratic residual."""

from pathlib import Path

root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()
for token in ("G(t,x_*)=g_*(t)S_B(t)T_2(t)", "deg T_2<=2", "T_2(tau)!=0", "B_NR lambda=0"):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")
for token in ("all-excess vertical-fiber", "R=g_*K_4", "Polynomial remainder is linear"):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")
print("RATE_HALF_NONREDUCED_HEAVY_ROW_QUADRATIC_RESIDUAL_AUDIT_PASS")
