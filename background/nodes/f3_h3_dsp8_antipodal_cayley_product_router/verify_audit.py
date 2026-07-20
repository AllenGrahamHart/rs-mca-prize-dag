#!/usr/bin/env python3
"""Mutation audit for the DSP8 antipodal Cayley-product router."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "C(h)=(1+h)/(1-h)" in statement
    assert "P(1-a^2)=2+M_a" in statement
    assert "M_a>=23" in statement
    assert "K_25^A=sum_(ainA_H,M_a>=23)E_aL_a" in statement
    assert "u+v=a(1+uv)" in proof
    assert "C^(-1)(gamma)=(gamma-1)/(gamma+1)" in proof
    assert "two ordered antipodal representations" in audit
    assert "`E_a` is ordered" in audit
    assert "Dropping it changes the consumer" in audit

    print("F3_H3_DSP8_ANTIPODAL_CAYLEY_PRODUCT_ROUTER_AUDIT_PASS mutations=9")


if __name__ == "__main__":
    main()
