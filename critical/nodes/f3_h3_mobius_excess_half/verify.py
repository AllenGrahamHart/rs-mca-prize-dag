#!/usr/bin/env python3
"""Replay the weighted-rich-fiber compiler for C36'."""

from __future__ import annotations

from fractions import Fraction


def main() -> None:
    for exponent in range(13, 42):
        n = 1 << exponent
        if n < 20**3:
            raise AssertionError((exponent, n))

        # 4n^(5/3)+16n^(4/3) <= (1/5+1/25)n^2.
        radical_budget = Fraction(6, 25) * n**2
        paid = 35 * (n - 1) * (n - 2)
        excess = Fraction(n**2, 2)
        target_without_radicals = 36 * n**2 - Fraction(n, 2)
        if not paid + excess + radical_budget < target_without_radicals:
            raise AssertionError((exponent, "weighted compiler"))

        # A 4n^2/5 excess allowance is too large for this compiler. This
        # mutation ensures the n^2/2 term is actually consumed.
        mutated = paid + Fraction(4 * n**2, 5) + radical_budget
        if mutated < target_without_radicals:
            raise AssertionError((exponent, "excess mutation undetected"))

    print(
        "H3_MOBIUS_EXCESS_COMPILER_PASS "
        "official_orders=29 baseline=35 excess=n2/2 mutation=4n2/5"
    )


if __name__ == "__main__":
    main()
