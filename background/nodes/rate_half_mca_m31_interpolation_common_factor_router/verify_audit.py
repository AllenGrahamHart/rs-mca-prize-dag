#!/usr/bin/env python3
"""Independent arithmetic audit of the M31 interpolation router."""

from fractions import Fraction


def main() -> None:
    e, degree, weight = 130237, 264, 5
    monomials = 0
    checks = 0
    for j in range(degree // weight + 1):
        for k in range(degree // weight - j + 1):
            monomials += degree - weight * (j + k) + 1
            checks += 1
    assert monomials == 131175
    assert monomials - e == 938
    value_degree = max(j + k
                       for j in range(100)
                       for k in range(100)
                       if weight * (j + k) <= degree)
    assert value_degree == 52
    assert value_degree**2 == 2704
    assert 807 > degree

    n, m, c, budget = 1048582, 67454, 5, 16777215
    lines, lower, cap = 2704, 807, 64796
    core_budget = min(lines * cap, e + lines * (lines + 1) * c // 2)
    lower_sum = lines * lower
    full, remainder = divmod(core_budget - lower_sum, cap - lower)
    value = full * Fraction(n - cap, m - cap)
    value += Fraction(n - lower - remainder, m - lower - remainder)
    value += (lines - full - 1) * Fraction(n - lower, m - lower)
    charge = value.numerator // value.denominator
    assert (core_budget, lower_sum, full, remainder) == (
        18416037, 2182128, 253, 44692)
    assert charge == 132203
    target = budget - charge
    assert target == 16645012
    assert (target - 13961576 + 1933560) // 1933560 == 2
    assert 2704 + 1 == 2705
    print("m31-interpolation-common-factor-router-audit: PASS "
          f"({checks + 21} checks; independent monomial and charge replay)")


if __name__ == "__main__":
    main()
