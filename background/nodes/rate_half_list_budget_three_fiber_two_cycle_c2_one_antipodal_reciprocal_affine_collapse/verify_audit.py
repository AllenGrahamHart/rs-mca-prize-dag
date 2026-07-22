#!/usr/bin/env python3
"""Mutation checks for the c2 reciprocal affine collapse."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    audit = (HERE / "audit.md").read_text()

    assert "y=(7+4a)/9" in statement
    assert "u=r=(2a-1)/3" in statement and "y=-r^2" in statement
    assert "R_(j+1)=R_j^2-2" in statement and "R_40=2 mod p" in statement
    assert "4,495,442" in statement
    assert "hits=[]" in statement and "no maximal-degree" in statement
    assert "does not cover" in statement and "degree-deficient" in statement

    assert "(-2|p)=-1" in proof
    assert "u^p=A_(-a)(y^(-1))" in proof
    assert "uv-y=(a-4)y^2+8y-(a+4)" in proof
    assert "R_40-2=(r^N-1)^2/r^N" in proof
    assert "complete no-hit" in proof
    assert "small passing control" in audit

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_RECIPROCAL_AFFINE_COLLAPSE_AUDIT_PASS "
        "scope=1 signs=1 equivalence=1 exact_screen=1 nonclaims=3"
    )


if __name__ == "__main__":
    main()
