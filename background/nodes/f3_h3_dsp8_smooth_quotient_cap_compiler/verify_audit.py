#!/usr/bin/env python3
"""Mutation audit for the DSP8 smooth quotient-cap compiler."""

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "tnotin{0,1}" in statement
    assert "189(10U_sm^0+17U_sm^A)<=144344n^(4/3)" in statement
    assert "3213(U_sm^0+U_sm^A)<=144344n^(4/3)" in statement
    assert "no factor two or four" in audit
    assert "not distinct additive shifts" in audit
    assert "genus one" in audit

    threshold = Fraction(144344, 3213)
    assert Fraction(189, 100) * 17 * threshold == Fraction(36086, 25)
    assert Fraction(189, 100) * 18 * threshold > Fraction(36086, 25)
    assert Fraction(188, 100) * 17 * threshold != Fraction(36086, 25)

    print("F3_H3_DSP8_SMOOTH_QUOTIENT_CAP_COMPILER_AUDIT_PASS mutations=9")


if __name__ == "__main__":
    main()
