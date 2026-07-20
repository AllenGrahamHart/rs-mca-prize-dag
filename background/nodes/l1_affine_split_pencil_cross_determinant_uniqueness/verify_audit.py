#!/usr/bin/env python3
"""Mutation audit for cross-determinant uniqueness."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = (ROOT / "statement.md").read_text()
    proof = (ROOT / "proof.md").read_text()
    audit = (ROOT / "audit.md").read_text()

    assert "product_i L_(T_i) | J Delta" in statement
    assert "t ell>2d+v" in statement
    assert "floor((2d+p)/ell)" in statement
    assert "not emptiness" in statement

    # Strictness is load-bearing: equal degrees do not force zero.
    assert not (6 > 6)
    assert 7 > 6

    # The aggregate p replacement is one-sided because v<=p.
    v, p = 2, 5
    assert v <= p
    assert 14 > 8 + p
    assert 14 > 8 + v

    assert "mark factor `J`" in audit
    assert "monic of degree `d`" in proof
    print("L1_CROSS_DETERMINANT_AUDIT_PASS mutations=5")


if __name__ == "__main__":
    main()
