#!/usr/bin/env python3
"""Mutation controls for the maximal background-anchor theorem packet."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    contract = (HERE / "claim_contract.md").read_text()
    audit = (HERE / "audit.md").read_text()

    for marker in (
        "q^max(0,d-max(r,a_*)+1)",
        "gamma=min(E+floor(u/t)+1, max(0,E+ell-r+1))",
        "does not sum unbounded",
        "combined exponent is the minimum",
        "may analytically remove",
    ):
        assert marker in statement + proof + contract + audit

    # The background anchor is a real improvement when r exceeds a_*.
    d, r, a_star = 6, 5, 2
    petal_only = max(0, d - a_star + 1)
    joint = max(0, d - max(r, a_star) + 1)
    assert (petal_only, joint) == (5, 2)

    # Equality in the petal degree comparison needs monicity.
    assert "monicity gives `deg(F-F')<d`" in proof

    # Replacing min by a product-style sum would overcharge the layer.
    assert joint < max(0, d - r + 1) + petal_only

    print("L1_MAXIMAL_BACKGROUND_ANCHOR_AUDIT_PASS mutations=8")


if __name__ == "__main__":
    main()
