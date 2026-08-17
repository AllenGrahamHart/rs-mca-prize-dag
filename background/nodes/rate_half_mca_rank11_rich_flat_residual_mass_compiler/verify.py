#!/usr/bin/env python3
"""Exact primary replay for the rich-flat residual mass compiler."""

from math import comb

N, K, A = 2_097_152, 1_048_576, 1_114_501
B_STAR = 274_980_728_111_395_087
PAID = 274_978_720_888_758_363
OUTSIDE = N - A
FIELD = 2_130_706_433**6

residual = B_STAR + 1 - PAID
m2 = comb(N - K + 2, 2) // comb(A - K + 2, 2)
m3 = comb(N - K + 3, 3) // comb(A - K + 3, 3)
r2, r3 = OUTSIDE * m2, OUTSIDE * m3

assert residual == 2_007_222_636_725
assert (m2, m3) == (252, 4023)
assert m2**2 < FIELD and m3**2 < FIELD
assert (r2, r3) == (247_628_052, 3_953_204_973)
assert (residual + r2 - 1) // r2 == 8_106
assert (residual + r3 - 1) // r3 == 508
assert 8_105 * r2 < residual <= 8_106 * r2
assert 507 * r3 < residual <= 508 * r3
print("RANK11_RICH_FLAT_RESIDUAL_MASS_OK", residual, 8_106, 508)
