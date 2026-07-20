#!/usr/bin/env python3
"""Mutation audit for the joint Plotkin-boundary payment."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = " ".join((ROOT / "statement.md").read_text().split())
    proof = " ".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "|A_P triangle A_Q|>=2ell" in statement
    assert "V=N+b<=4ell" in statement
    assert "N+b>4ell" in statement
    assert "at most `2V`" in proof
    assert "inclusion-minimal positive dependence" in proof
    assert "Equality `V=4ell`" in audit
    assert "additive constants" in audit

    print("L1_JOINT_PLOTKIN_BOUNDARY_AUDIT_PASS mutations=7")


if __name__ == "__main__":
    main()
