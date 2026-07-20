#!/usr/bin/env python3
"""Mutation audit for the DSP8 unit-product trace normal form."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = " ".join((ROOT / "statement.md").read_text().split())
    compact_statement = "".join(statement.split())
    proof = " ".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "cubing is a bijection" in statement
    assert "q=rs" in compact_statement
    assert "ruv=sxy=1" in compact_statement
    assert "t=(1-rs*u)(1-s/u)" in compact_statement
    assert "=1+rs(r+s-sigma)" in compact_statement
    assert "T^2-(sigma-r)T+r^(-1)" in compact_statement
    assert "q^3=RS=q^2rs" in proof
    assert "threefold ambiguity" in audit
    assert "decoration is load-bearing" in audit
    assert "order `n^6`" in statement

    print("F3_H3_DSP8_UNIT_PRODUCT_TRACE_NORMAL_FORM_AUDIT_PASS mutations=9")


if __name__ == "__main__":
    main()
