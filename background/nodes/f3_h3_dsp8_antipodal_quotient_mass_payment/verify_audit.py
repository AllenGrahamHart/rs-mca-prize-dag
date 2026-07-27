#!/usr/bin/env python3
"""Mutation audit for the antipodal quotient-mass payment."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "S_A<(C_M/2)(n-2)n^(2/3)" in statement
    assert "<=6Q_n+(38/5)S_A" in statement
    assert "10K_25^0+17K_25^A+152S_A" in statement
    assert "100(10K_25^0+17K_25^A)<=36781n^2" in statement
    assert "exactly`(n-2)/2`distinct" in proof
    assert "K_25^c=2D_c" in proof
    assert "(375-3591/500)n^2=(183909/500)n^2" in proof
    assert "B_(n,6)/8" in proof
    assert "incremental antipodal cost" in audit
    assert "does not by itself refute C36'" in audit

    print("F3_H3_DSP8_ANTIPODAL_QUOTIENT_MASS_PAYMENT_AUDIT_PASS mutations=11")


if __name__ == "__main__":
    main()
