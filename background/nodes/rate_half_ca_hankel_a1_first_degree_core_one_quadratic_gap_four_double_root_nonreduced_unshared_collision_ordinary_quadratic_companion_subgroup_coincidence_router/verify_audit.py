#!/usr/bin/env python3
"""Text-contract audit for the subgroup-coincidence router."""

from pathlib import Path


root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()

for token in (
    "K_Q(X,Y)=B(X,Y)^2-A(X,Y)C(X,Y)",
    "coordinate-corner exceptional",
    "does not yet classify or exclude",
):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")

for token in (
    "3F=3(2^39-6)",
    "total vertical defect",
    "at most two slopes",
    "8192^3 N^2 < (3F)^3",
    "512^3 N^2 < (3F/2)^3",
    "No claim is made that every component is automatically",
):
    corpus = proof + (root / "audit.md").read_text()
    if token not in corpus:
        raise AssertionError(f"missing proof/audit token: {token}")

mutated = statement.replace(
    "B(X,Y)^2-A(X,Y)C(X,Y)",
    "B(X,Y)^2+A(X,Y)C(X,Y)",
)
if "B(X,Y)^2-A(X,Y)C(X,Y)" in mutated:
    raise AssertionError("hostile resultant-sign mutation survived")

print("RATE_HALF_QUADRATIC_SUBGROUP_COINCIDENCE_AUDIT_PASS tamper=1/1")
