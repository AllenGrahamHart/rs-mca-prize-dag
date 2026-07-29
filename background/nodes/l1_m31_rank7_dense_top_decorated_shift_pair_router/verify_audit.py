#!/usr/bin/env python3
"""Independent rational audit of the dense-top threshold."""

from fractions import Fraction

domain = 354_972 + (981_129 - 282_544)
dimension = 4_981
overlap = dimension - 1
weight = dimension + 67_447
mass = 9_806_394 - 6_466_046 - 1_182_419

gap = domain * overlap - weight**2
deficit_fraction = Fraction(mass * gap, domain * (mass - 1)) + Fraction(
    weight - overlap, mass - 1
)

assert gap == 898_676
assert deficit_fraction < Fraction(9, 10)
assert Fraction(1) - deficit_fraction > Fraction(1, 10)
assert (mass - 1) // 10 + 1 == 215_793
assert weight - overlap == 67_448
line_size = (domain - overlap) // (weight - overlap)
assert line_size == 15
assert (215_793 + 13) // 14 == 15_414

print("L1_M31_DENSE_TOP_SHIFT_PAIR_AUDIT_PASS")
