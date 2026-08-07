#!/usr/bin/env python3
"""Replay the literal F00(b^-1)=F01(b) transport contract."""

from fractions import Fraction
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def edge(left, right):
    return frozenset((left, right))


for b in (Fraction(3), Fraction(5, 2), Fraction(-7, 3)):
    labels = (Fraction(2), Fraction(1, 2), b, 1 / b)
    inverse_labels = (Fraction(2), Fraction(1, 2), 1 / b, b)
    f01 = frozenset((edge(labels[0], labels[1]), edge(labels[0], labels[3])))
    f00_inverse = frozenset((
        edge(inverse_labels[0], inverse_labels[1]),
        edge(inverse_labels[0], inverse_labels[2]),
    ))
    require(f01 == f00_inverse, f"source pair at b={b}")
    require(frozenset(labels) == frozenset(inverse_labels), "carrier set")

crosswalk = (
    ROOT
    / "background/nodes/"
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_literal_cell_crosswalk/"
    "statement.md"
).read_text(encoding="ascii")
quotient = (
    ROOT
    / "background/nodes/"
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_colored_quotient_compiler/"
    "statement.md"
).read_text(encoding="ascii")
require("fixed-moving reconstruction uses `{E01,E02}`" in crosswalk,
        "canonical source pin")
require("quotient locators" in quotient and "Q_J,Q_I" in quotient,
        "set-locator quotient interface")

statement = (NODE / "statement.md").read_text(encoding="ascii")
for cell in ("F01-R02", "F01-R11", "F01-R20"):
    require(cell in statement, f"missing closure {cell}")

print(
    "KB_C2_112_ALIGNED_POSITIVE_FIXED_COMPANION_INVERSION_PASS "
    "cells=3 complete_system=true generic_mobius=false"
)
