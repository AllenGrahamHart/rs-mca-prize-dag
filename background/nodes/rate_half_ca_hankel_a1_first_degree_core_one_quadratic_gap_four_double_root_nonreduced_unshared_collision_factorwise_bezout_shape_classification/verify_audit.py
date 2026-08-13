#!/usr/bin/env python3
"""Text-contract audit for the factorwise Bezout shape classification."""

from pathlib import Path

root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()

for token in (
    "sum_j r_j=e-7",
    "ell_j=2b_j",
    "c_j:=e n_j",
    "plus two Q_2 factors",
    "total parameter degree at most four",
):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")

for token in (
    "sum_j ell_j=4",
    "force equality",
    "u_j^2-u_jv_jc_1+v_j^2c_0",
    "m_j=2(b_j-t_j)",
):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")

print("RATE_HALF_COLLISION_FACTORWISE_BEZOUT_SHAPES_AUDIT_PASS")
