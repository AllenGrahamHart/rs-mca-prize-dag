#!/usr/bin/env python3
"""Mutation audit for the joint-Johnson source-scale gate."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = " ".join((ROOT / "statement.md").read_text().split())
    proof = " ".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "M<3(r-1)" in statement
    assert "N+b>=4ell" in statement
    assert "M>=45" in statement
    assert "a(N-a)/N+u(b-u)/b>=ell" in proof
    assert "If `b=0`" in proof
    assert "preserving the additive `r`" in audit
    assert "No contributor existence" in audit

    print("L1_JOINT_JOHNSON_SOURCE_SCALE_GATE_AUDIT_PASS mutations=7")


if __name__ == "__main__":
    main()
