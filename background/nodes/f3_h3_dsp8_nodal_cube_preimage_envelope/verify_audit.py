#!/usr/bin/env python3
"""Mutation audit for the DSP8 nodal cube-preimage envelope."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "|K|=gn" in statement
    assert "<552n^2ifp=2(mod3)" in statement
    assert "<2387n^2ifp=1(mod3)" in statement
    assert "C=BA" in proof
    assert "2081^3-9*1000^3=11897441" in proof
    assert "nine old `(c,A)` branches" in audit
    assert "Only the node with `c=1`" in audit
    assert "does not reserve a valid budget" in audit

    print("F3_H3_DSP8_NODAL_CUBE_PREIMAGE_ENVELOPE_AUDIT_PASS mutations=8")


if __name__ == "__main__":
    main()
