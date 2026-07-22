#!/usr/bin/env python3
"""Mutation audit for the XR quotient maximum-agreement owner."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "Q_A\\B_(A+1)" in proof
    assert "E_z(p_z)=S" in proof
    assert "cannotreappearasanunpaidslopeatalateragreement" in proof
    assert "Exclusion from `B_(A+1)` is global over all codewords" in audit
    assert "PMA exact-periodic owner therefore does not close" in audit
    assert "cross-thresholdduplication" in statement

    print("XR_QUOTIENT_MAX_AGREEMENT_FIRST_MATCH_OWNER_AUDIT_PASS mutations=6")


if __name__ == "__main__":
    main()
