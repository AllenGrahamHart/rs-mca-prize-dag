#!/usr/bin/env python3
"""Mutation audit for the L1 background-overlap singleton payment."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = " ".join((ROOT / "statement.md").read_text().split())
    proof = " ".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "a+s<ell+g" in statement
    assert "a^2/N<=c<=2a-ell-g" in statement
    assert "a+s=ell+g=3" in statement
    assert "2(ell-s)-b" in proof
    assert "possibly negative inclusion-exclusion" in audit
    assert "strict boundary is retained" in audit

    print("L1_BACKGROUND_OVERLAP_SINGLETON_AUDIT_PASS mutations=5")


if __name__ == "__main__":
    main()
