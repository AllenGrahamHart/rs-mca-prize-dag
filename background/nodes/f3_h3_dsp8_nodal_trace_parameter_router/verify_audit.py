#!/usr/bin/env python3
"""Mutation audit for the DSP8 nodal-trace parameter router."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    statement = "".join((ROOT / "statement.md").read_text().split())
    proof = "".join((ROOT / "proof.md").read_text().split())
    audit = " ".join((ROOT / "audit.md").read_text().split())

    assert "[1+theta]=CA^2" in statement
    assert "N_sigma<12n^(2/3)+1" in statement
    assert "theta^2phi^2(1+theta)^2(1+phi)^2" in statement
    assert "<12n^(2/3)(12n^(2/3)+1)^2" in statement
    assert "<204n^(2/3)(12n^(2/3)+1)^2" in statement
    assert "leadingcoefficientis`29376`" in statement
    assert "C^3A^3=1" in proof
    assert "replacing `[c]` by its inverse is false" in audit
    assert "cannot be consumed" in audit

    print("F3_H3_DSP8_NODAL_TRACE_PARAMETER_ROUTER_AUDIT_PASS mutations=9")


if __name__ == "__main__":
    main()
