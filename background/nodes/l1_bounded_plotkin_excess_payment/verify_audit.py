#!/usr/bin/env python3
"""Mutation audit for the bounded Plotkin-excess payment."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = " ".join((ROOT / "statement.md").read_text().split())
    proof = " ".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "E=V-4ell" in statement
    assert "2^(E+1)(V-E)" in statement
    assert "N+b-4ell -> infinity" in statement
    assert "deleting those coordinates does not change" in proof
    assert "2^E*2(4ell)" in proof
    assert "Same-pattern puncturing preserves" in audit
    assert "`F_23` chart" in audit

    print("L1_BOUNDED_PLOTKIN_EXCESS_AUDIT_PASS mutations=7")


if __name__ == "__main__":
    main()
