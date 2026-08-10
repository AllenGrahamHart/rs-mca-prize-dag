#!/usr/bin/env python3
"""Independent fraction audit of the deep-point ceiling formula."""

from fractions import Fraction
from math import ceil


def main() -> None:
    checks = 0
    for n, k, q, numerator in (
        (17, 3, 257, 4),
        (63, 11, 65537, 19),
        (511, 99, 1 << 180, 1 << 66),
    ):
        eta = Fraction(k * numerator, q - n)
        assert 0 <= eta < 1
        theorem_rhs = Fraction(numerator, 1) / (1 - eta)
        direct_rhs = Fraction(numerator * (q - n), q - n - k * numerator)
        assert theorem_rhs == direct_rhs
        assert ceil(theorem_rhs) == (
            direct_rhs.numerator + direct_rhs.denominator - 1
        ) // direct_rhs.denominator
        checks += 1
    print(f"RS_DEEP_POINT_LIST_TO_CA_CONVERSION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
