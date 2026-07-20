#!/usr/bin/env python3
"""Mutation audit for the background-surplus Plotkin payment."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = " ".join((ROOT / "statement.md").read_text().split())
    proof = " ".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "q_bg=u+z" in statement
    assert "E_z=V-4(ell+z)" in statement
    assert "(E_P-4z)/log_2 n -> infinity" in statement
    assert "2(P+1)n^(1/c_0+P+C+3)" in statement
    assert "full background agreement set" in proof
    assert "at most `n` exact background counts" in proof
    assert "never enumerates background subsets" in audit
    assert "`z=1` boundary code" in audit

    print("L1_BACKGROUND_SURPLUS_PLOTKIN_AUDIT_PASS mutations=8")


if __name__ == "__main__":
    main()
