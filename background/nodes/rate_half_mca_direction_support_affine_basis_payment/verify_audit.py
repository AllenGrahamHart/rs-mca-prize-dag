#!/usr/bin/env python3
"""Independent audit of the affine-basis violation."""

numerator = 100 * 99 - 20 * 19
denominator = 21 * 20
if numerator // denominator != 22 or 31 <= numerator // denominator:
    raise ValueError("refutation")
print("RATE_HALF_MCA_DIRECTION_SUPPORT_AFFINE_BASIS_REFUTED_AUDIT_PASS slopes=31 bound=22")
