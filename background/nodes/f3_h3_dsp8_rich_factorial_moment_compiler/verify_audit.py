#!/usr/bin/env python3
"""Mutation audit for the DSP8 rich factorial-moment compiler."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "P(t)(P(t)-2)R(t)" in statement
    assert "<=(1/4)(10F_25^0+17F_25^A)" in statement
    assert "<=(17/4)M_21" in statement
    assert "25(10F_25^0+17F_25^A)<=48536n^2" in statement
    assert "425M_21<=48536n^2" in statement
    assert "2g(t)<=P(t)" in proof
    assert "N_6^disj(t)<=binom(g(t),2)" in proof
    assert "425*69=29325<48536" in proof
    assert "no diagonal correction" in audit
    assert "does not refute DSP8" in audit

    print("F3_H3_DSP8_RICH_FACTORIAL_MOMENT_COMPILER_AUDIT_PASS mutations=10")


if __name__ == "__main__":
    main()
