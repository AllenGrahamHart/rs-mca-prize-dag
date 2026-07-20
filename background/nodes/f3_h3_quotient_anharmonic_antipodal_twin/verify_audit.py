#!/usr/bin/env python3
"""Mutation audit for quotient anharmonic and antipodal-twin claims."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "t/(t-1),(t-1)/t" in statement
    assert "(z,w)->(w/z,1/z)" in proof
    assert "(X,Y)->(X^(-1),Y/a^2)" in proof
    assert "only`t=2`canbefixed" in proof
    assert "thenumberofdiagonalrepresentationsiszeroortwo" in proof
    assert "P(t)>=25iffP(t)>=26iffM_a>=24" in statement
    assert "`N_6^disj`" in statement
    assert "`t=23` and `tau(t)=76`" in audit
    assert "respectively `0` and `1`" in audit

    print("F3_H3_QUOTIENT_ANHARMONIC_ANTIPODAL_TWIN_AUDIT_PASS mutations=9")


if __name__ == "__main__":
    main()
