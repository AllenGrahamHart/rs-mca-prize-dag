#!/usr/bin/env python3
"""Replay the exact intrinsic-scale geometric ledger."""

from __future__ import annotations

from fractions import Fraction


def main() -> None:
    for exponent in range(13, 45):
        total = sum(Fraction(1, 2 ** (6 * j)) for j in range(1, exponent + 1))
        if not total < Fraction(1, 63):
            raise AssertionError((exponent, total))
        combined = Fraction(63, 64) * (1 + total)
        if not combined < 1:
            raise AssertionError((exponent, combined))

    # The denominator 63 is specific to B=6; replacing it by the B=5 value
    # must be visible to the checker.
    mutated = sum(Fraction(1, 2 ** (5 * j)) for j in range(1, 14))
    if mutated < Fraction(1, 63):
        raise AssertionError("exponent mutation undetected")
    print("INTRINSIC_SCALE_GEOMETRIC_LEDGER_PASS rows=32 B=6 reserve=63/64")


if __name__ == "__main__":
    main()

