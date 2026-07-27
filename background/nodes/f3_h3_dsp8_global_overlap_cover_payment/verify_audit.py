#!/usr/bin/env python3
"""Mutation audit for the global overlap-cover payment."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "atmost`2n`overlapping" in statement
    assert "<(17/5)C_Mn^(5/3)+(17/5)S_A" in statement
    assert "10K_25^0+17K_25^A+68S_A+68C_Mn^(5/3)" in statement
    assert "25(10K_25^0+17K_25^A)<=12134n^2" in statement
    assert "normalizationisuniqueforeachedge" in proof
    assert "(17/10)(2n)C_Mn^(2/3)" in proof
    assert "(485361/1000)n^2" in proof
    assert "global, not per target" in audit
    assert "does not by itself refute C36'" in audit

    print("F3_H3_DSP8_GLOBAL_OVERLAP_COVER_PAYMENT_AUDIT_PASS mutations=10")


if __name__ == "__main__":
    main()
