#!/usr/bin/env python3
"""Independent Fraction replay of the M31 two-block incidence constants."""

from fractions import Fraction

G = 354_972
E = 981_129 - 282_544
N = G + E
K = 4_981
T = K - 1
W = 67_447
M = K + W
FORBIDDEN = 9_806_394 - 6_466_046 - 1_182_419


def constant_weight_cap(universe: int, weight: int, overlap: int) -> int:
    numerator = universe * (weight - overlap)
    denominator = weight * weight - universe * overlap
    assert denominator > 0
    return numerator // denominator


assert FORBIDDEN == 2_157_929
assert constant_weight_cap(E, M - (K - 1), T) == 40
assert constant_weight_cap(G, M - (K - 1), T) == 7

center = Fraction(M * G, N)
width2 = Fraction(G * E, N) * (
    Fraction(M - T, FORBIDDEN) + Fraction(N * T - M * M, N)
)
assert Fraction(24_402) < center < Fraction(24_403)
assert width2 < 457**2
assert 24_402 - 457 > 23_945
assert 24_403 + 457 == 24_860
assert FORBIDDEN - 47 == 2_157_882

print("L1_M31_TWO_BLOCK_INCIDENCE_AUDIT_PASS")
