#!/usr/bin/env python3
"""Independent local-order audit for positive ramified loops."""

import sympy as sp


def order(polynomial, variable):
    terms = sp.Poly(sp.expand(polynomial), variable).terms()
    return min(monomial[0] for monomial, coefficient in terms if coefficient)


def main():
    u = sp.Symbol("u")
    targets = (-7, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 7)
    checks = 0
    for a, d, e, c in (
        (1, 3 + 2 * u**2, -3 + 5 * u**2, 7 + 11 * u**2),
        (3, 2 + 5 * u**2, -18 + 7 * u**2, 11 + 13 * u**2),
    ):
        product = sp.prod(t**2 * d + e + t * u * c for t in targets)
        if order(product, u) != 2:
            raise RuntimeError("row-product order")
        if order((u**2 * (1 + 2 * u)) ** 2, u) != 4:
            raise RuntimeError("complete-square order")
        checks += 1
    print(
        "RATE_HALF_KB_POSITIVE_RAMIFIED_LOOP_MULTIPLICITY_AUDIT_PASS "
        f"independent_samples={checks} orders=2/4"
    )


if __name__ == "__main__":
    main()
