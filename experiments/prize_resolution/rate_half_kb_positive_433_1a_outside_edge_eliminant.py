#!/usr/bin/env python3
"""Exact one-edge eliminant for the positive 433-1a common kernel."""

import sympy as sp


def quadratic_quartic_eliminant(A, B, C, coefficients):
    q0, q1, q2, q3, q4 = coefficients
    r1 = (
        q4 * (-B**3 + 2 * A * B * C)
        + q3 * A * (B**2 - A * C)
        - q2 * A**2 * B
        + q1 * A**3
    )
    r0 = (
        q4 * (-B**2 * C + A * C**2)
        + q3 * A * B * C
        - q2 * A**2 * C
        + q0 * A**3
    )
    numerator = sp.expand(A * r0**2 - B * r0 * r1 + C * r1**2)
    quotient, remainder = sp.div(numerator, A**3)
    if remainder != 0:
        raise RuntimeError("generic divisibility")
    return sp.expand(quotient), r0, r1


def linear_quartic_eliminant(B, C, coefficients):
    q0, q1, q2, q3, q4 = coefficients
    return sp.expand(
        q4 * C**4 - q3 * C**3 * B + q2 * C**2 * B**2
        - q1 * C * B**3 + q0 * B**4
    )


def edge_coefficients():
    d0, d1, d2, e0, e1, e2, beta0, beta1, p, s2 = sp.symbols(
        "d0 d1 d2 e0 e1 e2 beta0 beta1 p s2"
    )
    A = e2 - p * d2
    B = e1 - p * d1
    C = e0 - p * d0
    coefficients = (
        -s2 * d0**2,
        beta0**2 - 2 * s2 * d0 * d1,
        2 * beta0 * beta1 - s2 * (d1**2 + 2 * d0 * d2),
        beta1**2 - 2 * s2 * d1 * d2,
        -s2 * d2**2,
    )
    symbols = (d0, d1, d2, e0, e1, e2, beta0, beta1, p, s2)
    return symbols, (A, B, C), coefficients


def verify():
    A, B, C, w = sp.symbols("A B C w")
    coefficients = sp.symbols("q0:5")
    polynomial = A * w**2 + B * w + C
    quartic = sum(coefficients[index] * w**index for index in range(5))
    generic, r0, r1 = quadratic_quartic_eliminant(A, B, C, coefficients)
    if sp.expand(generic - sp.resultant(polynomial, quartic, w)) != 0:
        raise RuntimeError("generic resultant")
    if sp.expand(sp.rem(A**3 * quartic, polynomial, w) - r1 * w - r0) != 0:
        raise RuntimeError("pseudo-remainder")

    linear = linear_quartic_eliminant(B, C, coefficients)
    if sp.expand(B**4 * quartic.subs(w, -C / B) - linear) != 0:
        raise RuntimeError("linear evaluation")

    symbols, edge_abc, edge_q = edge_coefficients()
    d0, d1, d2, e0, e1, e2, beta0, beta1, p, s2 = symbols
    denominator = d0 + d1 * w + d2 * w**2
    numerator = e0 + e1 * w + e2 * w**2
    b1 = beta0 + beta1 * w
    if sp.expand(
        sum(edge_abc[index] * w ** (2 - index) for index in range(3))
        - (numerator - p * denominator)
    ) != 0:
        raise RuntimeError("product coefficients")
    edge_quartic = sum(edge_q[index] * w**index for index in range(5))
    if sp.expand(edge_quartic - (w * b1**2 - s2 * denominator**2)) != 0:
        raise RuntimeError("sum coefficients")

    return {
        "generic_terms": len(sp.Poly(generic, A, B, C, *coefficients).terms()),
        "generic_total_degree": sp.total_degree(generic),
        "linear_total_degree": sp.total_degree(linear),
    }


def main():
    result = verify()
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_EDGE_ELIMINANT_PASS "
        f"generic_terms={result['generic_terms']} "
        f"generic_degree={result['generic_total_degree']} "
        f"linear_degree={result['linear_total_degree']}"
    )


if __name__ == "__main__":
    main()
