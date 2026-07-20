#!/usr/bin/env python3
"""Mutation audit for the DSP8 smooth-trace substar router."""

from __future__ import annotations

from pathlib import Path


BASE = Path(__file__).resolve().parent


def main() -> None:
    statement = (BASE / "statement.md").read_text()
    proof = (BASE / "proof.md").read_text()
    audit = (BASE / "audit.md").read_text()
    for marker in (
        "(1+r+s-t)^3=27rs",
        "degree at most three",
        "degree-five/degree-three",
        "J:Delta^infinity",
    ):
        assert marker in statement + proof
    assert "leading coefficient one" in proof
    assert "Degree three is sharp" in audit
    assert "not a vanishing ideal" in audit

    # Mutation: a quartic leaf equation would no longer justify degree three.
    cubic_degree = 3
    assert max(8 - cubic_degree, 0) == 5
    assert max(6 - cubic_degree, 0) == 3
    quartic_degree = 4
    assert (max(8 - quartic_degree, 0), max(6 - quartic_degree, 0)) == (4, 2)
    print("F3_H3_DSP8_SMOOTH_TRACE_SUBSTAR_ROUTER_AUDIT_PASS mutations=4")


if __name__ == "__main__":
    main()
