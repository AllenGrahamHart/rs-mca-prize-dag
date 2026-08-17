#!/usr/bin/env python3
"""Independent product/divmod replay of rich-flat residual mass."""

N, K, A = 2_097_152, 1_048_576, 1_114_501
UNSAFE = 274_980_728_111_395_088
PAID = 274_978_720_888_758_363


def choose(n: int, r: int) -> int:
    numerator = denominator = 1
    for j in range(1, r + 1):
        numerator *= n - r + j
        denominator *= j
    return numerator // denominator


e = UNSAFE - PAID
outside = N - A
r2 = outside * (choose(N - K + 2, 2) // choose(A - K + 2, 2))
r3 = outside * (choose(N - K + 3, 3) // choose(A - K + 3, 3))

q2, rem2 = divmod(e, r2)
q3, rem3 = divmod(e, r3)
assert (e, r2, r3) == (2_007_222_636_725, 247_628_052, 3_953_204_973)
assert (q2, rem2, q2 + bool(rem2)) == (8_105, 197_275_265, 8_106)
assert (q3, rem3, q3 + bool(rem3)) == (507, 2_947_715_414, 508)
print("RANK11_RICH_FLAT_RESIDUAL_MASS_AUDIT_OK", rem2, rem3)
