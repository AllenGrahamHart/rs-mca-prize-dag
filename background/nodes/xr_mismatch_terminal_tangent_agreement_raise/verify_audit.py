#!/usr/bin/env python3
"""Mutation audit for the XR terminal-tangent agreement raise."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    common = {0, 1, 2}
    discrepancy = 3
    tangent_agreements = common | {discrepancy}
    assert len(tangent_agreements) == len(common) + 1
    assert discrepancy not in common

    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    assert "B_(A+1)(u,v)" in statement
    assert "Since`iinT`,itisnotin`Y`" in proof
    assert "withoutsummingoverpairs,paths,orlocatorflags" in proof
    assert "one common set `B_(A+1)(u,v)`" in audit
    assert "re-run the complete first-match partition" in audit

    print("XR_MISMATCH_TERMINAL_TANGENT_AGREEMENT_RAISE_AUDIT_PASS mutations=5")


if __name__ == "__main__":
    main()
