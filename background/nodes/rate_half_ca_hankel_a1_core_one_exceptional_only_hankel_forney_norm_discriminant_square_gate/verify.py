#!/usr/bin/env python3
"""Exact square-class checks for the Forney norm-discriminant gate."""

from __future__ import annotations


def main() -> None:
    prime = 101
    e = 3
    beta = [100, 5, 91, 10, 96, 1]
    q_1 = [2, 12, 30, 56, 90, 31]
    mu = [beta[i] * q_1[i] * q_1[i] % prime for i in range(2 * e)]
    determinant_class = pow(-1, e, prime)
    for weight in mu:
        determinant_class = determinant_class * weight % prime

    if determinant_class == 0 or pow(determinant_class, (prime - 1) // 2, prime) != 1:
        raise AssertionError("self-dual determinant class is not a square")
    roots = [20, 21, 22, 23, 24, 25]
    derivative_product = 1
    discriminant = 1
    for i, left in enumerate(roots):
        derivative = 1
        for j, right in enumerate(roots):
            if i != j:
                derivative = derivative * (left - right) % prime
        derivative_product = derivative_product * derivative % prime
    for i, left in enumerate(roots):
        for right in roots[i + 1 :]:
            discriminant = discriminant * (left - right) ** 2 % prime
    if derivative_product != pow(-1, e, prime) * discriminant % prime:
        raise AssertionError("discriminant sign conversion failed")

    print(
        "RATE_HALF_HANKEL_FORNEY_NORM_DISCRIMINANT_PASS "
        f"prime={prime} e={e} square_class={determinant_class}"
    )


if __name__ == "__main__":
    main()
