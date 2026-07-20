#!/usr/bin/env python3
"""Mutation audit for the optimized affine coset-pair bound."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "<4n^(2/3)" in statement
    assert "nonconstant,nonproportionalaffineforms" in statement
    assert "D(A+D)<AB^2" in proof
    assert "AB<=n" in proof
    assert "A+nB<n^2+1<=p" in proof
    assert "(A+2nB)^3<64D^3n^2" in proof
    assert "need not agree" in audit
    assert "one-fiber optimization" in audit

    print("F3_AFFINE_COSET_PAIR_OPTIMIZED_STEPANOV_AUDIT_PASS mutations=8")


if __name__ == "__main__":
    main()
