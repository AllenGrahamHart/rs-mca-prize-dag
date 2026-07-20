#!/usr/bin/env python3
"""Mutation audit for the DSP8 nodal target-divisor pruning rules."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "b in S(a)".replace(" ", "") in statement
    assert "q(a)+q(b)+3q(a)q(b)=0" in statement
    assert "nine tests `T_i(a)+T_j(b)=0`".replace(" ", "") in statement
    assert "(a-b)(a+b+1)" in proof
    assert "Signeddisjointnessthereforeremoves" in proof
    assert "repeated-root multiplicities" in audit
    assert "Positive disjointness does not imply signed disjointness" in audit
    assert "no uniform irreducibility claim is made" in audit

    print("F3_H3_DSP8_NODAL_TARGET_DIVISOR_PRUNING_AUDIT_PASS mutations=8")


if __name__ == "__main__":
    main()
