#!/usr/bin/env python3
"""Official-row crossover table for the repeat-boundary support compiler."""

from __future__ import annotations

from fractions import Fraction


def residue_constant(c: Fraction) -> Fraction:
    return 4752 * c + 1602


def sufficient_threshold(c: Fraction) -> int:
    """Return N such that n > N implies the repeat residue is < n^3."""
    k = residue_constant(c)
    return (k.numerator**3) // (k.denominator**3) + 1


def first_official_s(c: Fraction) -> int | None:
    threshold = sufficient_threshold(c)
    for s in range(13, 42):
        if 2**s > threshold:
            return s
    return None


def format_fraction(c: Fraction) -> str:
    if c.denominator == 1:
        return str(c.numerator)
    return f"{c.numerator}/{c.denominator}"


def main() -> None:
    print("h=3 repeat-support official crossover")
    constants = [
        Fraction(1, 4),
        Fraction(1, 3),
        Fraction(1, 2),
        Fraction(2, 3),
        Fraction(1, 1),
        Fraction(3, 2),
        Fraction(2, 1),
        Fraction(4, 1),
    ]
    for c in constants:
        k = residue_constant(c)
        threshold = sufficient_threshold(c)
        first_s = first_official_s(c)
        coverage = "none" if first_s is None else f"2^{first_s}..2^41"
        print(
            f"C={format_fraction(c):>3} K={format_fraction(k):>8} "
            f"threshold_n>{threshold} first_official={first_s} coverage={coverage}"
        )
        if first_s is not None and 2**first_s <= threshold:
            raise AssertionError((c, threshold, first_s))
        if first_s is not None and first_s > 13 and 2 ** (first_s - 1) > threshold:
            raise AssertionError((c, threshold, first_s, "not first"))

    print("Uses sufficient bound: repeat_residue <= (4752C+1602) n^(8/3)")
    print("H3_REPEAT_SUPPORT_CROSSOVER_PASS")


if __name__ == "__main__":
    main()
