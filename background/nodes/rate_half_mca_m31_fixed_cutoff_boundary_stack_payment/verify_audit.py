#!/usr/bin/env python3
"""Independent endpoint audit for the fixed-cutoff boundary stack."""

from fractions import Fraction


def ceiling(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def main() -> None:
    N, m, c, budget = 1048582, 67454, 5, 16777215
    e, forcing = 101155, 16667033
    threshold = budget - forcing + 1
    core = ceiling(Fraction(threshold * m - N, threshold - 1))
    inside = core - c
    sync = e - inside + 6
    agreement = m - sync + 1
    n = N - e
    ratio = Fraction(n * (agreement - c), agreement * agreement - n * c)
    low = ratio.numerator // ratio.denominator
    bound = e * low + (N - m + 1)
    if (threshold, core, inside, sync, agreement, low, bound) != (
            110183, 67446, 67441, 33720, 33735, 28, 3813469):
        raise ValueError("endpoint")
    if not (28 <= ratio < 29) or budget - bound != 12963746:
        raise ValueError("endpoint guards")
    adjacent = 16951223
    if adjacent - budget != 174008:
        raise ValueError("adjacent wall")
    print(
        "RATE_HALF_MCA_M31_FIXED_CUTOFF_BOUNDARY_STACK_AUDIT_PASS "
        "endpoint=101155 bound=3813469 adjacent_excess=174008"
    )


if __name__ == "__main__":
    main()
