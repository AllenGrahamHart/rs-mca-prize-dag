#!/usr/bin/env python3
"""Independent exact-integer audit of the field-degree trichotomy."""

from __future__ import annotations


def valuation_two(value: int) -> int:
    return (value & -value).bit_length() - 1


def main() -> None:
    lower = 3 << 128
    upper = 4 << 128
    candidates = []
    for coefficient in range(1, 8):
        prime_candidate = coefficient * (1 << 41) + 1
        if lower <= prime_candidate**3 < upper:
            candidates.append((coefficient, prime_candidate))
    assert candidates == [(5, 10_995_116_277_761)]
    assert candidates[0][1] // 7 == 1_570_730_896_823

    # For every possible e>=4 under e<130, the LTE lower exponent is fatal.
    for e in range(4, 130):
        lower_characteristic_exponent = 41 if e % 2 else 41 - valuation_two(e)
        assert lower_characteristic_exponent >= 34
        assert e * (lower_characteristic_exponent - 1) >= 132
    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_MAXIMAL_FIELD_DEGREE_COLLAPSE_PASS "
        "cubic_interval=1 divisor7=1 high_degree_exclusions=126"
    )


if __name__ == "__main__":
    main()
