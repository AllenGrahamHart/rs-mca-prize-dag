#!/usr/bin/env python3
"""Verify the elementary forced-fiber degree bound."""

from __future__ import annotations

import sympy as sp

from f3_h3_repeat_support_forced_point_reduction import fixed_first_count


def lambda_numerator_minus_mu(a_value: int) -> tuple[int, int]:
    x, mu = sp.symbols("x mu")
    a = sp.Integer(a_value)
    w = sp.cancel(1 - (a - 1) * (x - 1) / (a + x - 2))
    lam = sp.cancel(a + x + w - 2)
    num, den = sp.fraction(lam)
    poly = sp.Poly(sp.expand(num - mu * den), x)
    return poly.degree(), int(poly.LC())


def main() -> None:
    print("h=3 repeat forced-fiber degree bound")
    for a_value in (2, 5, 17, 257):
        degree, leading = lambda_numerator_minus_mu(a_value)
        if degree != 2 or leading != 1:
            raise AssertionError((a_value, degree, leading))
        print(f"a={a_value} degree(lambda_a(X)-mu)=2 leading_coeff=1")

    rows = (
        (65537, 256, 2),
        (65537, 256, 4096),
        (65537, 256, 19752),
    )
    for p, n, a_value in rows:
        count = fixed_first_count(p, n, a_value)
        if count > 2 * n:
            raise AssertionError((p, n, a_value, count))
        print(f"p={p} n={n} a={a_value} N_a={count} degree_bound={2*n}")

    print("For every forced coordinate a, N_a <= 2n")
    print("H3_REPEAT_FORCED_FIBER_DEGREE_BOUND_PASS")


if __name__ == "__main__":
    main()
