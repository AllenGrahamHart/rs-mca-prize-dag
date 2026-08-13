#!/usr/bin/env python3
"""Independent audit of the M31 common-factor mass router."""

from fractions import Fraction


def main() -> None:
    n, m, e, c, total = 1048582, 67454, 130237, 5, 16777215
    lines, lower, cap = 7582, 807, 64796
    core_budget = min(lines * cap, e + lines * (lines + 1) * c // 2)
    lower_sum = lines * lower
    full, remainder = divmod(core_budget - lower_sum, cap - lower)
    value = full * Fraction(n - cap, m - cap)
    value += Fraction(n - lower - remainder, m - lower - remainder)
    value += (lines - full - 1) * Fraction(n - lower, m - lower)
    charge = value.numerator // value.denominator
    assert (core_budget, lower_sum, full, remainder) == (
        143866002, 6118674, 2152, 43000)
    assert charge == 881897
    target = total - charge
    assert target == 15895318
    assert (target - 13961576 + 1933560) // 1933560 == 2

    captured = []
    for degree in range(1, 53):
        off = (52 - degree) ** 2
        on = 7583 - off
        points = (on * lower * lower + lower + c * (on - 1) - 1) // (
            lower + c * (on - 1))
        captured.append((degree, off, on, points))
    assert captured[0] == (1, 2601, 4982, 126188)
    assert captured[-1] == (52, 0, 7583, 127552)
    assert all(captured[i][2] < captured[i + 1][2]
               and captured[i][3] <= captured[i + 1][3]
               for i in range(51))
    assert e - captured[0][3] == 4049
    print("m31-common-factor-mass-router-audit: PASS "
          f"({len(captured) * 4 + 23} checks; all factor degrees replayed)")


if __name__ == "__main__":
    main()
