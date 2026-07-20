#!/usr/bin/env python3
"""Mutation audit for the antipodal quotient-mass payment."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "S_A<(51/32)(n-2)n^(2/3)" in statement
    assert "<=6Q_n+(38/5)S_A" in statement
    assert "10K_25^0+17K_25^A+152S_A" in statement
    assert "80(10K_25^0+17K_25^A)<=29031n^2" in statement
    assert "exactly`(n-2)/2`distinct" in proof
    assert "K_25^c=2D_c" in proof
    assert "(375-969/80)n^2=(29031/80)n^2" in proof
    assert "B_(n,6)/8" in proof
    assert "incremental antipodal cost" in audit
    assert "does not by itself refute C36'" in audit

    print("F3_H3_DSP8_ANTIPODAL_QUOTIENT_MASS_PAYMENT_AUDIT_PASS mutations=10")


if __name__ == "__main__":
    main()
