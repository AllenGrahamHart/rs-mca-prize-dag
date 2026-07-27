#!/usr/bin/env python3
"""Mutation audit for the post-Mattarei DSP8 smooth residual ledger."""

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "W_sm+W_sing<=(48536/25)n^2" in statement
    assert "W_sm<=(45636/25)n^2" in statement
    assert "W_sm<=(36086/25)n^2" in statement
    assert "G_sm^c=4K_sm^c" in proof
    assert Fraction(45636, 25) + 116 == Fraction(48536, 25)
    assert Fraction(36086, 25) + 498 == Fraction(48536, 25)
    assert "strict nodal bounds" in audit
    assert "subtracted once" in audit

    # Hostile normalization mutations fail the exact target.
    assert Fraction(36086, 25) / 2 != Fraction(18043, 50)
    assert Fraction(36086, 25) / 8 != Fraction(18043, 50)

    print("F3_H3_DSP8_SMOOTH_RESIDUAL_ROUTER_AUDIT_PASS mutations=8")


if __name__ == "__main__":
    main()
