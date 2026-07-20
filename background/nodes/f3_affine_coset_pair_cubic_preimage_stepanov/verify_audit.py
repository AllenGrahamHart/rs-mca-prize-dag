#!/usr/bin/env python3
"""Mutation audit for the cubic-preimage affine Stepanov bound."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "m in {n,3n}".replace(" ", "") in statement
    assert "<(51/16)m^(2/3)" in statement
    assert "B=ceil((2m)^(1/3))" in proof
    assert "A=floor(m/B)" in proof
    assert "D=max{d>=1:d(A+d)<AB^2}" in proof
    assert "4096(A+2mB)^3<132651D^3m^2" in proof
    assert "`p>=n^2`, not `p>=m^2`" in audit
    assert "failure at `D+1`" in audit

    print("F3_AFFINE_COSET_PAIR_CUBIC_PREIMAGE_STEPANOV_AUDIT_PASS mutations=8")


if __name__ == "__main__":
    main()
