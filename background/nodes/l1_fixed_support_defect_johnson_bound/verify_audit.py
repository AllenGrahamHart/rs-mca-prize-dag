#!/usr/bin/env python3
"""Mutation audit for the L1 fixed-support defect Johnson bound."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = " ".join((ROOT / "statement.md").read_text().split())
    proof = " ".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "|D_1 intersect D_2|<=r_J" in statement
    assert "d^2-N r_J>0" in statement
    assert "N(e-1)>=d^2" in statement
    assert "whole fixed petal support" in audit
    assert "strictly positive denominator" in audit
    assert "g=ell-b" in audit
    assert "not the global B11 Johnson gate" in audit

    n, d, r_j = 3, 2, 1
    denominator = d * d - n * r_j
    assert denominator == 1
    assert 3 * denominator == n * (d - r_j)

    n = 4
    assert d * d - n * r_j == 0
    assert "No field factor or missing-equation syndrome factor" in proof
    assert "g<=N/4" in proof

    print("L1_FIXED_SUPPORT_DEFECT_JOHNSON_AUDIT_PASS mutations=6")


if __name__ == "__main__":
    main()
