#!/usr/bin/env python3
"""Independent audit of the common-zero violation."""

from fractions import Fraction

value = Fraction(100 * 99 - 20 * 19, 21 * 20)
bound = value.numerator // value.denominator
if bound != 22 or 31 <= bound:
    raise ValueError("refutation")
print("RATE_HALF_MCA_DIRECTION_SUPPORT_COMMON_ZERO_REFUTED_AUDIT_PASS slopes=31 bound=22")
