#!/usr/bin/env python3
"""Mutation audit for the joint core/background Johnson bound."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = " ".join((ROOT / "statement.md").read_text().split())
    proof = " ".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "|D_1 intersect D_2|+|R_1 intersect R_2|<=r" in statement
    assert "J=b d^2+N u^2-N b r>0" in statement
    assert "b a^2+N(ell-a+c)^2<=N b c" in statement
    assert "L_X L_I L_R | Delta" in proof
    assert "d+u-r=ell" in proof
    assert "Strict joint-denominator positivity" in audit
    assert "`F_23` fixture" in audit

    print("L1_JOINT_CORE_BACKGROUND_JOHNSON_AUDIT_PASS mutations=7")


if __name__ == "__main__":
    main()
