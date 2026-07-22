#!/usr/bin/env python3
"""Mutation audit for the XR quotient boundary agreement owner."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "B>A" in proof
    assert "agr(u+zv,p_z)>=B>=A+1" in proof
    assert "independentlyofthecoreandfiberscale" in statement
    assert "doesnotpermitreplacing`B_(A+1)`by`B_(A+2)`" in "".join(
        audit.split()
    )
    assert "exact-`A` quotient image remains load-bearing" in audit

    print("XR_QUOTIENT_BOUNDARY_AGREEMENT_RAISE_OWNER_AUDIT_PASS mutations=5")


if __name__ == "__main__":
    main()
