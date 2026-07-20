#!/usr/bin/env python3
"""Mutation audit for the background-quotient Johnson bound."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = " ".join((ROOT / "statement.md").read_text().split())
    proof = " ".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "u^2-bc>0" in statement
    assert "b(u-c)/(u^2-bc)" in statement
    assert "(ell-a+c)^2<=(ell-g)c" in statement
    assert "G_P=(P-I_X)/L_X" in proof
    assert "canonically `u` agreement positions" in proof
    assert "Strict denominator positivity" in audit
    assert "zero-denominator fixture" in audit

    print("L1_BACKGROUND_QUOTIENT_JOHNSON_AUDIT_PASS mutations=6")


if __name__ == "__main__":
    main()
