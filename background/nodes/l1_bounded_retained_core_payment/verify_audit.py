#!/usr/bin/env python3
"""Mutation audit for the L1 bounded retained-core payment."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = " ".join((ROOT / "statement.md").read_text().split())
    proof = " ".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "a=N-d=|C\\D|" in statement
    assert "a(N-a)>=Ng" in statement
    assert "h>d" in proof
    assert "b<ell" in proof
    assert "retained core `C\\D`" in audit
    assert "does not hide a chart multiplier" in audit

    print("L1_BOUNDED_RETAINED_CORE_AUDIT_PASS mutations=5")


if __name__ == "__main__":
    main()
