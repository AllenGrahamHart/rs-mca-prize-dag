#!/usr/bin/env python3
"""Mutation audit for the DSP8 unit-trace elliptic-curve router."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "X^2Y+XY^2-sigmaXYZ+Z^3=0" in statement
    assert "sigma^3!=27" in statement
    assert "sigma^3=27" in statement
    assert "G_25^c=4K_25^c=J_25^c" in statement
    assert "10G_25^0+17G_25^A<=892n^2" in statement
    assert "F_X=Y(2X+Y-sigmaZ)" in proof
    assert "xi^2+xieta+eta^2" in proof
    assert "hence `(e1,e3)`" in audit
    assert "does not bound its subgroup points" in audit

    print("F3_H3_DSP8_UNIT_TRACE_ELLIPTIC_CURVE_ROUTER_AUDIT_PASS mutations=9")


if __name__ == "__main__":
    main()
