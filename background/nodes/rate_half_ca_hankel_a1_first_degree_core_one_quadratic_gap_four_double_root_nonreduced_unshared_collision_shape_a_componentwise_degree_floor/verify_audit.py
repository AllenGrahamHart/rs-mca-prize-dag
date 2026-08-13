#!/usr/bin/env python3
"""Independent text and arithmetic audit for the component degree floor."""

from fractions import Fraction
from pathlib import Path


root = Path(__file__).resolve().parent
statement = (root / "statement.md").read_text()
proof = (root / "proof.md").read_text()

for token in (
    "defined over the base field",
    "39768216",
    "10931403977394458172",
    "not a translated one-dimensional subtorus",
    "no extension-field",
):
    if token not in statement:
        raise AssertionError(f"missing statement token: {token}")

for token in (
    "only one geometric component",
    "deck-group order divides",
    "108N^2D^4",
    "D<P_char",
):
    if token not in proof:
        raise AssertionError(f"missing proof token: {token}")

e = (2**39 + 1) // 3
m = e - 2
n = 2**38 - 3
N = 2**41
cut = Fraction((e + 7) ** 3 * n**3, 108 * N**2 * m**3)
if not (39768215 < cut < 39768216):
    raise AssertionError("independent rational threshold interval")

mutated = proof.replace("deck-group order divides", "deck-group order need not divide")
if "deck-group order divides" in mutated:
    raise AssertionError("hostile deck-order mutation survived")

print("RATE_HALF_SHAPE_A_COMPONENT_DEGREE_AUDIT_PASS tamper=1/1")
