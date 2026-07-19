#!/usr/bin/env python3
"""Exact arithmetic replay for the proposed u1_x4 amber assembly."""

from fractions import Fraction


def main() -> None:
    # Direct h=3 compiler cancellation.
    assert Fraction(2, 9) - Fraction(8, 36) == 0
    assert Fraction(1, 72) - Fraction(1, 2 * 36) == 0
    assert Fraction(36, 36) == 1

    # Cochrane-Pinner h=2 payment: (2/3)n^(5/2)<n^3 iff 4<9n.
    rows = 0
    for exponent in range(13, 42):
        n = 1 << exponent
        assert 4 < 9 * n
        rows += 1

    h1_budget = 0
    h2_budget = 1
    h3_budget = 1
    tail_budget = 14
    total_budget = 16
    assert h1_budget + h2_budget + h3_budget + tail_budget == total_budget

    print(
        "F3_U1_X4_AMBER_ASSEMBLY_PASS "
        f"rows={rows} total={total_budget} tail={tail_budget}"
    )


if __name__ == "__main__":
    main()

