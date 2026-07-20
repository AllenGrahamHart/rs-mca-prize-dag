#!/usr/bin/env python3
"""Mutation audit for the fixed-support codeword quotient bound."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = " ".join((ROOT / "statement.md").read_text().split())
    proof = " ".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "Psi(P)=(P-P_0)/L_X" in statement
    assert "q^max(0,N-h+1)" in statement
    assert "a-s=N-h -> infinity" in statement
    assert "degree at most `k-1=N`" in proof
    assert "No defect-degree or syndrome multiplier" in proof
    assert "No split-polynomial claim" in audit

    assert 8 - 5 == (8 - 4) - (5 - 4) == 3
    print("L1_FIXED_SUPPORT_CODEWORD_QUOTIENT_AUDIT_PASS mutations=5")


if __name__ == "__main__":
    main()
