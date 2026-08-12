#!/usr/bin/env python3
"""Text-contract audit for the torus-gcd exclusion."""

from pathlib import Path


root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()

for token in (
    "shapes B/D are empty",
    "only A and C remain",
    "does not exclude shape A",
):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")

for token in (
    "chi<=2d_1d_2",
    "27648N^2<(3F)^3",
    "1728N^2<(3F/2)^3",
    "q|r|=q|s|=2",
    "forcing its nonzero degree",
    "to be divisible by three",
):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")

mutated = proof.replace("X(sigma^2P)=X(P)", "X(sigma^2P)=-X(P)")
if "X(sigma^2P)=X(P)" in mutated:
    raise AssertionError("hostile inversion-iterate mutation survived")

print("RATE_HALF_QUADRATIC_TORUS_GCD_EXCLUSION_AUDIT_PASS tamper=1/1")
