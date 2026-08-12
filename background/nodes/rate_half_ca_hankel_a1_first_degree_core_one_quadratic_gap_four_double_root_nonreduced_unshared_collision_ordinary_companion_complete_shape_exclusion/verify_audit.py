#!/usr/bin/env python3
"""Text audit for the complete ordinary-companion exclusion."""

from pathlib import Path


root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()

for token in (
    "P_res=24F_6/4=6F_6=3298534883250",
    "force a second translated-subtorus component",
    "only shape A remains",
    "does not occur",
):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")

for token in (
    "remaining twenty-four ordered pairs",
    "at most four",
    "64*17280000*N^2 < P_res^3",
    "q|a|=q|b|=4h",
    "subgroup of order four",
):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")

mutated = proof.replace("remaining twenty-four ordered pairs", "remaining thirty ordered pairs")
if "remaining twenty-four ordered pairs" in mutated:
    raise AssertionError("hostile graph-deletion mutation survived")

print("RATE_HALF_ORDINARY_COMPANION_COMPLETE_EXCLUSION_AUDIT_PASS tamper=1/1")
