#!/usr/bin/env python3
"""Independent arithmetic audit of the refuted affine-span bound."""

from fractions import Fraction

terms = (Fraction(100 * 99, 21 * 20), Fraction(100 * 99, 20 * 21))
bound = max(value.numerator // value.denominator for value in terms)
if bound != 23 or 31 <= bound:
    raise ValueError("refutation")
print("RATE_HALF_MCA_SUPPORTWISE_AFFINE_SPAN_COMPILER_REFUTED_AUDIT_PASS slopes=31 bound=23")
