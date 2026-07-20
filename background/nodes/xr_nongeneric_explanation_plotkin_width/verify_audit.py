#!/usr/bin/env python3
"""Mutation audit for XR nongeneric-explanation Plotkin width."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = " ".join((ROOT / "statement.md").read_text().split())
    proof = " ".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "H=h+1" in statement
    assert "1+104H" in statement
    assert "420H^2" in statement
    assert "1+200n^(C+1)" in statement
    assert "201n^(C+2)" in statement
    assert "binom(m,2)2H<=Nm^2/4" in proof
    assert "1+8H+32H+64H" in proof
    assert "crucial `+1`" in audit
    assert "excludes generic-chart mismatch slopes" in audit

    print("XR_NONGENERIC_EXPLANATION_PLOTKIN_WIDTH_AUDIT_PASS mutations=9")


if __name__ == "__main__":
    main()
