#!/usr/bin/env python3
"""Official-row crossover table for quotient-support theorems."""

from __future__ import annotations

from fractions import Fraction

from f3_h3_repeat_boundary_q0_cell import ceil_cuberoot


OFFICIAL_RANGE = range(13, 42)


def floor_fraction_times(frac: Fraction, n: int) -> int:
    return (frac.numerator * n) // frac.denominator


def support_residue_bound(n: int, r_orb_bound: int) -> int:
    q0_cap = ceil_cuberoot((132**3) * (n**2))
    fiber_cap = ceil_cuberoot((66**3) * (n**2))
    b_line_bound = q0_cap + 6 * r_orb_bound * fiber_cap
    return 12 * n * b_line_bound + 18 * n * n


def covered_exponents_for_linear_c(c_value: Fraction) -> list[int]:
    covered: list[int] = []
    for exponent in OFFICIAL_RANGE:
        n = 2**exponent
        r_bound = floor_fraction_times(c_value, n)
        if support_residue_bound(n, r_bound) < n**3:
            covered.append(exponent)
    return covered


def first_tail_coverage(covered: list[int]) -> int | None:
    for exponent in OFFICIAL_RANGE:
        tail = list(range(exponent, 42))
        if all(item in covered for item in tail):
            return exponent
    return None


def main() -> None:
    print("h=3 repeat support crossover")
    print("integer model: R_orb <= floor(C*n), q0/fiber caps use ceil cuberoots")
    rows = (
        ("1/4", Fraction(1, 4)),
        ("1/2", Fraction(1, 2)),
        ("1", Fraction(1, 1)),
        ("2", Fraction(2, 1)),
        ("4", Fraction(4, 1)),
    )
    expected_first = {
        "1/4": 31,
        "1/2": 34,
        "1": 37,
        "2": 40,
        "4": None,
    }
    actual_first: dict[str, int | None] = {}
    for label, value in rows:
        covered = covered_exponents_for_linear_c(value)
        first = first_tail_coverage(covered)
        actual_first[label] = first
        coverage = "none" if first is None else f"2^{first}..2^41"
        first_official = 2**13
        first_bound = support_residue_bound(first_official, floor_fraction_times(value, first_official))
        print(
            f"C={label:>3s} first_tail={first} coverage={coverage} "
            f"n=2^13_bound={first_bound}"
        )
    if actual_first != expected_first:
        raise AssertionError(actual_first)
    print("H3_REPEAT_SUPPORT_CROSSOVER_PASS")


if __name__ == "__main__":
    main()
