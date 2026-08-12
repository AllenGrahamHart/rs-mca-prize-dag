#!/usr/bin/env python3
"""Text-contract audit for the collision barycentric split-jet gate."""

from pathlib import Path

root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()
for token in ("P_x(tau)!=0", "R_0=R_1=0", "R_2!=0", "J_0=J_1=0"):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")
for token in ("all-excess vertical-fiber", "Lagrange interpolation", "ord_tau G(t,x_*)=2"):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")
print("RATE_HALF_COLLISION_BARYCENTRIC_SPLIT_JET_AUDIT_PASS")
