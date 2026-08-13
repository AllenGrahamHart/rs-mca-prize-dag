#!/usr/bin/env python3
"""Independent arithmetic audit of residue-zero core absorption."""

from fractions import Fraction


def main() -> None:
    e, K, m, N, c = 98232, 6, 67454, 1048582, 5
    core = m - 2
    inside = core - c
    sync = e - inside + K
    if (inside, sync) != (67447, 30791):
        raise ValueError("synchronization")

    agreement = m - (sync - 1)
    n = N - e
    ratio = Fraction(n * (agreement - c), agreement * agreement - n * c)
    cap = ratio.numerator // ratio.denominator
    if agreement != 36664 or cap != 26 or not (26 <= ratio < 27):
        raise ValueError("Johnson cap")

    low = e * cap
    line = N - m + 1
    total = low + line
    budget = 16777215
    if (low, line, total, budget - total) != (
            2554032, 981129, 3535161, 13242054):
        raise ValueError("payment")
    print(
        "RATE_HALF_MCA_M31_RESIDUE_ZERO_CORE_ABSORPTION_AUDIT_PASS "
        "sync=30791 list=26 total=3535161 slack=13242054"
    )


if __name__ == "__main__":
    main()
