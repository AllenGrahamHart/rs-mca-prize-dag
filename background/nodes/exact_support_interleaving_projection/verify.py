#!/usr/bin/env python3
"""Audit the exact-support projection arithmetic and finite bounds."""

from __future__ import annotations

from fractions import Fraction


def bound(q: int, r: int, base: int) -> int:
    denominator = (q - r) ** 2 - base * q
    if denominator <= 0:
        raise ValueError("vacuous parameter range")
    return int(Fraction(base * q * (q - r - 1), denominator))


def main() -> None:
    rows = 0
    for q in (17, 97, 257, 65_537):
        for r in range(0, min(12, q)):
            for base in range(1, q):
                denominator = (q - r) ** 2 - base * q
                if denominator <= 0:
                    continue
                value = bound(q, r, base)
                exact = Fraction(base * q * (q - r - 1), denominator)
                if not value <= exact < value + 1:
                    raise AssertionError((q, r, base, value, exact))
                if r == 0:
                    unrestricted = Fraction(base * (q - 1), q - base)
                    if exact != unrestricted:
                        raise AssertionError((q, base, exact, unrestricted))
                rows += 1

    # Removing one outside-support hyperplane from the good-projection count
    # must change a nontrivial row.
    if bound(17, 8, 1) == bound(17, 7, 1):
        raise AssertionError("outside-support mutation undetected")
    print(f"EXACT_SUPPORT_INTERLEAVING_PROJECTION_PASS rows={rows}")


if __name__ == "__main__":
    main()
