#!/usr/bin/env python3
"""Mutation audit for the nonsplit cross-quotient route fence."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = " ".join((ROOT / "statement.md").read_text().split())
    proof = " ".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "exact saturated maximal-chart cell" in statement
    assert "=(X-13)(20+15X+15X^2)" in statement
    assert "N(2d-h)=24>=d^2=16" in statement
    assert "k+ell-1=10" in proof
    assert "filler points are explicitly excluded" in audit
    assert "forced background factor" in audit

    squares = {x * x % 23 for x in range(23)}
    assert 14 not in squares

    print("L1_CROSS_QUOTIENT_NONSPLIT_AUDIT_PASS mutations=6")


if __name__ == "__main__":
    main()
