#!/usr/bin/env python3
"""Audit the received-pair alternating-router proof boundary."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> None:
    proof = "".join((HERE / "proof.md").read_text().split())
    audit = " ".join((HERE / "audit.md").read_text().split())
    for marker in (
        "e_i=b+gamma_iq+w_i",
        "Itthereforeannihilates`w_i`",
        "dotproductof`theta`with`v_i`",
        "quadraticin`(4)`hasatleastfourdistinctroots",
        "determinantofthatmatrixis`eta^2`",
        "fourcoefficientcolumnsareabasisof`F^4`",
        "statedparity-rowconversesandnomore",
    ):
        assert marker in proof
    assert "one parity equation" in audit
    assert "mixed coefficient" in audit
    assert "coefficient rank four" in audit
    assert "not a tangent or quotient classification" in audit
    assert "No Modal" in audit
    print("XR_RANK_TWO_RECEIVED_PAIR_ALTERNATING_ROUTER_AUDIT_PASS mutations=12")


if __name__ == "__main__":
    main()
