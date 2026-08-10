#!/usr/bin/env python3
from fractions import Fraction


n = 2097152
rows = ((1116048, 1048576), (1116024, 1048576))
expected = ((2299571, 1083345, 1015873), (2299499, 1083320, 1015872))

for (m, k), (xi_expected, g_expected, sunflower_expected) in zip(rows, expected):
    xi = 3 * m - k + 3
    q = Fraction(31 * m - n, 30)
    g = -(-q.numerator // q.denominator)
    sunflower = g - (m - k)
    assert (xi, g, sunflower) == (xi_expected, g_expected, sunflower_expected)

print("PASS independent order32 arithmetic audit rows=2")
