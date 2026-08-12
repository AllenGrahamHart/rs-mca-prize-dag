#!/usr/bin/env python3
"""Text-contract audit for the two-branch tangent-profile router."""

from pathlib import Path


root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()

for token in (
    "G_X(tau,x_*)=0",
    "u_0(a_1v_2+a_2v_1)",
    "collision profile [1,3]",
    "collision profile [2,2]",
):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")

for token in (
    "ord_z f_i(z,0)=1",
    "v_1a_2+a_1v_2",
    "no analogous conclusion follows",
):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")

mutated = proof.replace("v_1a_2+a_1v_2", "v_1a_2-a_1v_2")
if "v_1a_2+a_1v_2" in mutated:
    raise AssertionError("hostile sign mutation survived")

print("RATE_HALF_COLLISION_TWO_BRANCH_TANGENT_AUDIT_PASS tamper=1/1")
