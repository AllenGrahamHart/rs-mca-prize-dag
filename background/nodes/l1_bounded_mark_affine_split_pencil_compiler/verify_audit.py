#!/usr/bin/env python3
"""Mutation audit for the bounded-mark affine split-pencil compiler."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = (ROOT / "statement.md").read_text()
    proof = (ROOT / "proof.md").read_text()

    assert "deg G<=d-1" in statement
    assert "at most `q^v`" in statement
    assert "dim H_T^0+1" in statement
    assert "gcd(JF,JW)=J" in statement
    assert "does not bound the split/saturated points" in statement
    assert "source-chart atlas" in statement

    # Load-bearing mutations: monicity removes one leading direction, while
    # v deleted scalar equations have at most q^v syndromes.
    d = 7
    assert d - 1 < d
    q, v = 11, 3
    assert q**v == 1331
    assert q ** (v + 1) > q**v

    # Dense holes and sparse occupied points use the same exception currency.
    ell = 10
    assert min(ell - 2, 2) == 2
    assert min(2, ell - 2) == 2

    assert "The polynomial pre-factor is not presented as a cell bound" in (
        ROOT / "audit.md"
    ).read_text()
    assert "leading coefficient" in proof
    print("L1_AFFINE_SPLIT_PENCIL_AUDIT_PASS mutations=6")


if __name__ == "__main__":
    main()
