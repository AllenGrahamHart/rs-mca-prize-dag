#!/usr/bin/env python3
"""Replay the exact source/target crosswalk and covariance obstruction."""

from fractions import Fraction
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SOURCE = (
    ROOT
    / "critical/nodes/rate_half_band_closure/notes/"
    "kb_c2_112_positive_qslice_symmetric.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


c, d, r, leading = sp.symbols("c d r leading", nonzero=True)
p = c * d
t = -(c + d)

# Each tuple is (M/L, C/L) after the local pair equations are solved.
same = (-2 / r, 1 / r**2)
swap = (-2 * r / p, r**2 / p**2)
mixed = (t / p, 1 / p)

require(
    all(sp.simplify(left - right) == 0 for left, right in zip(
        same, (-2 / r, 1 / r**2)
    )),
    "same/R20",
)
require(
    all(sp.simplify(value.subs(r, c) - target) == 0 for value, target in zip(
        swap, (-2 / d, 1 / d**2)
    )),
    "swap at c/R02",
)
require(
    all(sp.simplify(value.subs(r, d) - target) == 0 for value, target in zip(
        swap, (-2 / c, 1 / c**2)
    )),
    "swap at d/R02",
)
balanced = (-(1 / c + 1 / d), 1 / (c * d))
require(
    all(sp.simplify(left - right) == 0 for left, right in zip(mixed, balanced)),
    "mixed/R11",
)

source = SOURCE.read_text(encoding="ascii")
require(
    "first, second = edge(a, 1 / a), edge(a, b_value)" in source,
    "fixed-moving source pair",
)
require(
    "first, second = edge(a, b_value), edge(a, 1 / b_value)" in source,
    "moving-moving source pair",
)

def mobius(x):
    return (2 * x + 1) / (x + 2)


x = Fraction(3, 1)
require(mobius(1 / x) == 1 / mobius(x), "inversion centralizer")
require(1 / x == Fraction(1, 3), "original target")
require(1 / mobius(x) == Fraction(5, 7), "moved target")
require(1 / x != 1 / mobius(x), "covariance obstruction")

print(
    "KB_C2_112_ALIGNED_POSITIVE_LITERAL_CELL_CROSSWALK_PASS "
    "source=F00,M00 target=same:R20,swap:R02,mixed:R11 covariance=false"
)
