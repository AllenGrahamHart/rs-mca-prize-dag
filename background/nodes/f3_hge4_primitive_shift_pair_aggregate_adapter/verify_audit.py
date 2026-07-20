#!/usr/bin/env python3
"""Independent exact-arithmetic audit of the HGE4 summation compiler."""

from __future__ import annotations

from fractions import Fraction
from math import factorial


def main() -> None:
    partial = sum((Fraction(1, factorial(h) ** 2) for h in range(4, 65)), Fraction())
    first_omitted = Fraction(1, factorial(65) ** 2)
    remainder_bound = first_omitted / (1 - Fraction(1, 66**2))
    assert partial < partial + remainder_bound < Fraction(1, 553)

    worst = Fraction(3500, 2**13) + Fraction(7000, 553)
    assert worst < 14
    assert Fraction(3500, 2**12) + Fraction(7000, 553) < 14
    assert Fraction(3500, 1) + Fraction(7000, 553) > 14

    # Mutation controls: the chosen finite-track constant passes, while the
    # nearby round value 7500 would exceed the same 1/553 compiler allowance.
    assert Fraction(7000, 2 * 2**13) + Fraction(7000, 553) < 14
    assert Fraction(7500, 2 * 2**13) + Fraction(7500, 553) > 14

    print(
        "AUDIT_F3_HGE4_PRIMITIVE_SHIFT_PAIR_AGGREGATE_ADAPTER_PASS "
        "tail_terms=61 mutation=7500"
    )


if __name__ == "__main__":
    main()
