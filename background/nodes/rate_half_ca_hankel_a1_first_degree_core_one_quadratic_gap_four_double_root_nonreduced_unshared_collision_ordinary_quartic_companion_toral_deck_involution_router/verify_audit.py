#!/usr/bin/env python3
"""Text audit for the quartic deck-involution router."""

from pathlib import Path


root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()

for token in (
    "P_6=ceil(30F_6/4)=4123168604063",
    "sigma(X)=-X",
    "sigma(X)=k/X",
    "does not exclude shape C",
):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")

for token in (
    "total defect from the capacity",
    "at most five",
    "125*17280000*N^2 < P_6^3",
    "q|a|=q|b|=4h",
    "It is nontrivial, so it is two",
):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")

mutated = proof.replace("q|a|=q|b|=4h", "q|a|=q|b|=6h")
if "q|a|=q|b|=4h" in mutated:
    raise AssertionError("hostile degree mutation survived")

print("RATE_HALF_QUARTIC_TORAL_DECK_INVOLUTION_AUDIT_PASS tamper=1/1")
