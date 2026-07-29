#!/usr/bin/env python3
"""Independent two-adic audit of the degree-eight field router."""

from __future__ import annotations


EXPONENTS = (13, 17, 19, 31)


def valuation_two(value: int) -> int:
    assert value
    count = 0
    while value % 2 == 0:
        value //= 2
        count += 1
    return count


def main() -> None:
    for t in EXPONENTS:
        prime = 2**t - 1
        modulus_exponent = t + 3
        assert valuation_two(prime - 1) < modulus_exponent
        assert valuation_two(prime**2 - 1) == t + 1
        assert valuation_two(prime**4 - 1) == t + 2
        assert valuation_two(prime**8 - 1) >= modulus_exponent

    eligible = tuple(degree for degree in range(1, 9) if 8 % degree == 0)
    assert eligible == (1, 2, 4, 8)
    assert all(8 % degree for degree in (3, 5, 6, 7))
    print("AUDIT_L1_M8_H7_CUBIC_COEFFICIENT_FIELD_DEGREE_EIGHT_PASS rows=4")


if __name__ == "__main__":
    main()
