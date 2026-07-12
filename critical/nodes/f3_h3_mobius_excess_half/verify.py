#!/usr/bin/env python3
"""Replay the cutoff-18 weighted-rich-fiber compiler for C36'."""

from __future__ import annotations

from fractions import Fraction


def minimum_fixed_points(multiplicity: int) -> int:
    return multiplicity % 2


def main() -> None:
    for multiplicity in range(0, 1000):
        fixed = minimum_fixed_points(multiplicity)
        lhs = 68 * max(multiplicity - 18, 0)
        rhs = multiplicity * (multiplicity - 2) + fixed
        if lhs > rhs:
            raise AssertionError((multiplicity, fixed, lhs, rhs))

    # The coefficient 68 is sharp at even multiplicities 34 and 36.
    mutation_lhs = 69 * (34 - 18)
    mutation_rhs = 34 * (34 - 2)
    if mutation_lhs <= mutation_rhs:
        raise AssertionError("coefficient mutation undetected")

    for exponent in range(13, 42):
        n = 1 << exponent
        if n < 20**3:
            raise AssertionError((exponent, n))

        # Since n^(1/3)>20, the identity and C36' radical corrections obey
        # 4n^(5/3)+16n^(4/3) < (1/5+1/25)n^2.
        radical_budget = Fraction(6, 25) * n**2
        paid = 18 * (n - 1) * (n - 2)
        excess = Fraction(300, 17) * n**2
        target_without_radicals = 36 * n**2 - Fraction(n, 2)
        if not paid + excess + radical_budget < target_without_radicals:
            raise AssertionError((exponent, "cutoff-18 compiler"))

        # Spending the full asymptotic 18n^2 remainder must fail. This pins
        # the rational 300/17 allowance used by the compiler.
        mutated = paid + 18 * n**2 + radical_budget
        if mutated < target_without_radicals:
            raise AssertionError((exponent, "excess mutation undetected"))

    print(
        "H3_MOBIUS_EXCESS_COMPILER_PASS "
        "official_orders=29 baseline=18 weighted_excess=300n2/17 "
        "nonswap_sufficient=1200n2"
    )


if __name__ == "__main__":
    main()
