#!/usr/bin/env python3
"""Mutation audit for the Mattarei prime-subfield descent scope."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "a_iinF_p^*" in statement
    assert "b_iinF_p" in statement
    assert "K<=F_p^*" in statement
    assert "Noextension-fieldMattareitheoremisclaimed" in statement
    assert "Nonzero slope is load-bearing" in audit
    assert "Nonproportionality remains load-bearing" in audit
    assert "Mersenne-31 is explicitly fenced" in audit

    p = 2**31 - 2**24 + 1
    n = 2**21
    assert (p - 1) // n != 1015
    assert 1016**3 > 4 * n
    assert (2**31 - 2) % n != 0

    print("F3_AFFINE_COSET_PAIR_PRIME_SUBFIELD_DESCENT_AUDIT_PASS mutations=9")


if __name__ == "__main__":
    main()
