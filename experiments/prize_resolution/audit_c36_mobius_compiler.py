#!/usr/bin/env python3
"""Independent consumer-backward audit of the M35 -> C36' arithmetic."""

from __future__ import annotations

from fractions import Fraction


def main() -> None:
    for exponent in range(13, 42):
        n = 1 << exponent
        if n < 20**3:
            raise AssertionError((exponent, n))

        radical_budget = Fraction(1, 5) + Fraction(1, 25)
        left = Fraction(35 * (n - 1) * (n - 2), 1) + radical_budget * n**2
        right = Fraction(36 * n**2, 1) - Fraction(n, 2)
        if not left < right:
            raise AssertionError((exponent, left, right))

        # Mutation control: cap 36 cannot use this compiler. Its leading
        # n^2 term already exhausts the C36' leading allowance.
        mutated = Fraction(36 * (n - 1) * (n - 2), 1) + radical_budget * n**2
        if mutated < right:
            raise AssertionError((exponent, "cap-36 mutation was not detected"))

        weighted = left + Fraction(n**2, 2)
        if not weighted < right:
            raise AssertionError((exponent, "weighted excess compiler"))
        weighted_mutation = left + Fraction(4 * n**2, 5)
        if weighted_mutation < right:
            raise AssertionError((exponent, "weighted mutation was not detected"))

    print(
        "C36_MOBIUS_COMPILER_AUDIT_PASS "
        "official_orders=29 mutations=cap36,excess4n2/5"
    )


if __name__ == "__main__":
    main()
