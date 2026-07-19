#!/usr/bin/env python3
"""Independent exact-resultant audit for dyadic binomial norms."""

from __future__ import annotations

from sympy import Poly, resultant, symbols


def main() -> None:
    x = symbols("x")
    checked = 0
    for order in (8, 16, 32, 64):
        degree = order // 2
        cyclotomic = Poly(x**degree + 1, x)
        for difference in range(1, degree):
            for sign in (-1, 1):
                value = abs(int(resultant(cyclotomic, Poly(1 + sign * x**difference, x))))
                assert value > 0
                assert value & (value - 1) == 0
                checked += 1
    assert checked == 112
    print(
        "AUDIT_F3_H3_DISTANCE_TWO_COLLISION_2PRIMARY_EXCLUSION_PASS "
        f"exact_resultants={checked} orders=4"
    )


if __name__ == "__main__":
    main()
