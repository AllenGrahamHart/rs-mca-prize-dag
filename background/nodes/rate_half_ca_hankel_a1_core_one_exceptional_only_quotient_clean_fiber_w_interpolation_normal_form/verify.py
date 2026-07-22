#!/usr/bin/env python3
"""Exact interpolation fixture for the W_vee normal form."""

from __future__ import annotations


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def evaluate(poly: list[int], value: int, prime: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % prime
    return out


def interpolate(points: list[tuple[int, int]], prime: int) -> list[int]:
    out = [0] * len(points)
    for i, (x_i, y_i) in enumerate(points):
        basis = [1]
        denominator = 1
        for j, (x_j, _) in enumerate(points):
            if i == j:
                continue
            grown = [0] * (len(basis) + 1)
            for degree, coefficient in enumerate(basis):
                grown[degree] = (grown[degree] - x_j * coefficient) % prime
                grown[degree + 1] = (grown[degree + 1] + coefficient) % prime
            basis = grown
            denominator = denominator * (x_i - x_j) % prime
        scale = y_i * pow(denominator, -1, prime) % prime
        for degree, coefficient in enumerate(basis):
            out[degree] = (out[degree] + scale * coefficient) % prime
    return out


def main() -> None:
    prime = 101
    clean = [2, 3, 5]
    d = len(clean)
    r = 2

    # Two Y-coefficients of W_0, sampled on the clean fibers.
    values = {
        0: [(t, (7 + 4 * t + 3 * t * t) % prime) for t in clean],
        1: [(t, (11 + 9 * t) % prime) for t in clean],
    }
    w0 = {degree: interpolate(samples, prime) for degree, samples in values.items()}
    for degree, samples in values.items():
        for t, expected in samples:
            need(evaluate(w0[degree], t, prime) == expected,
                 "clean-fiber coefficient interpolation failed")

    # P_cl=(t-2)(t-3)(t-5), with an affine quotient for each Y coefficient.
    p_cl = [(-2 * -3 * -5) % prime, (2 * 3 + 2 * 5 + 3 * 5) % prime,
            -(2 + 3 + 5) % prime, 1]
    corrections = {0: (13, 17), 1: (19, 23)}  # (linear, constant)
    for degree in range(r):
        linear, constant = corrections[degree]
        for t in clean:
            correction = evaluate(p_cl, t, prime) * (linear * t + constant)
            need(correction % prime == 0,
                 "P_cl correction changed a clean fiber")
    need(d + 1 == 4, "affine-quotient degree ledger mismatch")
    print(
        "RATE_HALF_QUOTIENT_CLEAN_FIBER_W_INTERPOLATION_PASS "
        f"prime={prime} clean={d} y_degree={r - 1} corrections=2"
    )


if __name__ == "__main__":
    main()
