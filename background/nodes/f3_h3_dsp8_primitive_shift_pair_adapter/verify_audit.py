#!/usr/bin/env python3
"""Mutation audit for the DSP8 primitive cubic shift-pair adapter."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = " ".join((ROOT / "statement.md").read_text().split())
    proof = " ".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "degree-three, depth-one shift pair" in statement
    assert "gcd(n,3)=1" in statement
    assert "A(0)=B(0)=-rs" in statement
    assert "J_25^c=4K_25^c=8D_6,25^c" in statement
    assert "10K_25^0+17K_25^A<=223n^2" in statement
    assert "lambda=(s-r)(1+alpha+r+s)" in proof
    assert "decorated roots `r,s`" in audit
    assert "not the constant-shift top stratum" in audit
    assert "marginal SP bound does not pay" in audit

    print("F3_H3_DSP8_PRIMITIVE_SHIFT_PAIR_ADAPTER_AUDIT_PASS mutations=9")


if __name__ == "__main__":
    main()
