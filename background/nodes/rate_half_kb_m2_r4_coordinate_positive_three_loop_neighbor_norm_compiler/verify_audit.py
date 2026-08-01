#!/usr/bin/env python3
"""Independent exact audit of the target-neighbor norm identity."""

import sympy as sp


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    W, X, r = sp.symbols("W X r")
    samples = (
        ((2, 3, 5), (7, 11, 13), 17),
        ((1, -2, 4), (3, 6, -5), 19),
        ((5, 1, 2), (-4, 7, 3), 23),
    )
    for d_values, e_values, beta in samples:
        D = sum(d_values[index] * W**index for index in range(3))
        E = sum(e_values[index] * W**index for index in range(3))
        B = beta * (W - 1)
        F = sp.expand(
            r**2 * D.subs(W, X**2)
            + E.subs(W, X**2)
            + r * X * B.subs(W, X**2)
        )
        numerator = sp.resultant(E, r**2 * D**2 - W * B**2, W)
        denominator = sp.resultant(D, E**2 - r**2 * W * B**2, W)
        require(
            sp.expand(sp.resultant(F, E.subs(W, X**2), X) - r**4 * numerator)
            == 0,
            "numerator identity",
        )
        require(
            sp.expand(sp.resultant(F, D.subs(W, X**2), X) - denominator)
            == 0,
            "denominator identity",
        )
    print("RATE_HALF_KB_POSITIVE_THREE_LOOP_NEIGHBOR_NORM_AUDIT_PASS samples=3")


if __name__ == "__main__":
    main()
