#!/usr/bin/env python3
"""Verify the exact FM69 -> weighted-excess compiler."""

from __future__ import annotations


def main() -> None:
    for multiplicity in range(0, 100_001):
        excess = max(multiplicity - 35, 0)
        factorial = multiplicity * (multiplicity - 1)
        if 138 * excess > factorial:
            raise AssertionError(multiplicity)
    if 138 * (69 - 35) != 69 * 68:
        raise AssertionError("equality at 69")
    if 138 * (70 - 35) != 70 * 69:
        raise AssertionError("equality at 70")
    print("H3_FACTORIAL_69_COMPILER_PASS range=0..100000 equalities=69,70")


if __name__ == "__main__":
    main()
