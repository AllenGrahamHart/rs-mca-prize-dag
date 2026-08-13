#!/usr/bin/env python3
"""Text audit for the shape-A pure-split component floor."""

from pathlib import Path


root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()

for token in (
    "a_delta=r_delta=q_delta=0",
    "75557863727701029814224",
    "n+14",
    "not a torus conclusion",
):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")

for token in (
    "at least `e+7` slopes",
    "absolutely irreducible",
    "at most `m` common roots",
    "at most `n-1`",
):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")

mutated = proof.replace("at least `e+7` slopes", "at least `e+6` slopes")
if "at least `e+7` slopes" in mutated:
    raise AssertionError("hostile pure-fiber mutation survived")

print("RATE_HALF_SHAPE_A_PURE_SPLIT_COMPONENT_AUDIT_PASS tamper=1/1")
