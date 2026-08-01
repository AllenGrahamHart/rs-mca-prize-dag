#!/usr/bin/env python3
"""Exact generic and degree-drop eliminants for one outside Vieta edge."""

import sympy as sp


def quadratic_quartic_eliminant(A, B, C, coefficients):
    q0, q1, q2, q3, q4 = coefficients
    remainder_linear = (
        q4 * (-B**3 + 2 * A * B * C)
        + q3 * A * (B**2 - A * C)
        - q2 * A**2 * B
        + q1 * A**3
    )
    remainder_constant = (
        q4 * (-B**2 * C + A * C**2)
        + q3 * A * B * C
        - q2 * A**2 * C
        + q0 * A**3
    )
    numerator = sp.expand(
        A * remainder_constant**2
        - B * remainder_constant * remainder_linear
        + C * remainder_linear**2
    )
    quotient, remainder = sp.div(numerator, A**3)
    if remainder != 0:
        raise RuntimeError("generic divisibility")
    return sp.expand(quotient), remainder_constant, remainder_linear


def linear_quartic_eliminant(B, C, coefficients):
    q0, q1, q2, q3, q4 = coefficients
    return sp.expand(
        q4 * C**4
        - q3 * C**3 * B
        + q2 * C**2 * B**2
        - q1 * C * B**3
        + q0 * B**4
    )


def edge_coefficients():
    a0, ai, a1, d0, d1, d2, beta, p, s2 = sp.symbols(
        "a0 ai a1 d0 d1 d2 beta p s2"
    )
    middle = (
        (a0**2 - a1**2) * d0
        - a1**2 * d1
        + (ai**2 - a1**2) * d2
    )
    A = -(ai**2 + p) * d2
    B = middle - p * d1
    C = -(a0**2 + p) * d0
    coefficients = (
        -s2 * d0**2,
        beta**2 - 2 * s2 * d0 * d1,
        -2 * beta**2 - s2 * (d1**2 + 2 * d0 * d2),
        beta**2 - 2 * s2 * d1 * d2,
        -s2 * d2**2,
    )
    return (a0, ai, a1, d0, d1, d2, beta, p, s2), (A, B, C), coefficients


def verify():
    A, B, C, w = sp.symbols("A B C w")
    coefficients = sp.symbols("q0:5")
    polynomial = A * w**2 + B * w + C
    quartic = sum(coefficients[index] * w**index for index in range(5))
    generic, remainder_constant, remainder_linear = quadratic_quartic_eliminant(
        A, B, C, coefficients
    )
    if sp.expand(generic - sp.resultant(polynomial, quartic, w)) != 0:
        raise RuntimeError("generic resultant")
    pseudo_remainder = sp.rem(A**3 * quartic, polynomial, w)
    if sp.expand(pseudo_remainder - remainder_linear * w - remainder_constant) != 0:
        raise RuntimeError("pseudo-remainder")

    linear = linear_quartic_eliminant(B, C, coefficients)
    if sp.expand(B**4 * quartic.subs(w, -C / B) - linear) != 0:
        raise RuntimeError("linear evaluation")

    symbols, (edge_A, edge_B, edge_C), edge_q = edge_coefficients()
    a0, ai, a1, d0, d1, d2, beta, p, s2 = symbols
    middle = (
        (a0**2 - a1**2) * d0
        - a1**2 * d1
        + (ai**2 - a1**2) * d2
    )
    denominator = d0 + d1 * w + d2 * w**2
    numerator = -a0**2 * d0 + middle * w - ai**2 * d2 * w**2
    if sp.expand(
        edge_A * w**2 + edge_B * w + edge_C - (numerator - p * denominator)
    ) != 0:
        raise RuntimeError("edge product coefficients")
    edge_quartic = sum(edge_q[index] * w**index for index in range(5))
    expected_quartic = beta**2 * w * (w - 1)**2 - s2 * denominator**2
    if sp.expand(edge_quartic - expected_quartic) != 0:
        raise RuntimeError("edge sum coefficients")

    return {
        "generic_terms": len(sp.Poly(generic, A, B, C, *coefficients).terms()),
        "generic_total_degree": sp.total_degree(generic),
        "linear_total_degree": sp.total_degree(linear),
    }


def main():
    result = verify()
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_EDGE_ELIMINANT_PASS "
        f"generic_terms={result['generic_terms']} "
        f"generic_degree={result['generic_total_degree']} "
        f"linear_degree={result['linear_total_degree']}"
    )


if __name__ == "__main__":
    main()
