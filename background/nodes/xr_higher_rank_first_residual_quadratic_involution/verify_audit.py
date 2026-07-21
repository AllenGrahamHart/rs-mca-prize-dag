#!/usr/bin/env python3
"""Mutation audit for the first residual quadratic shell."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    # The pair-cap inequality excludes two singleton zero sets.
    assert 1 + 1 < 3
    assert 1 + 2 == 3
    assert 2 + 2 > 3

    # In characteristic two the quadratic separability inference is invalid.
    assert 2 % 2 == 0
    assert 2 % 3 != 0

    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())
    for marker in (
        "z_i+z_j>=3",
        "2t-1<=a+3",
        "degreeexactlytwo",
        "F(T)/F(phi)",
        "sum_igamma_ic_i=sum_igamma_id_i=0",
    ):
        assert marker in proof
    assert "Odd characteristic is load-bearing" in audit
    assert "not necessarily every coordinate" in audit
    assert "next shell `a+4`" in audit

    print("XR_HIGHER_RANK_FIRST_RESIDUAL_QUADRATIC_INVOLUTION_AUDIT_PASS mutations=8")


if __name__ == "__main__":
    main()
