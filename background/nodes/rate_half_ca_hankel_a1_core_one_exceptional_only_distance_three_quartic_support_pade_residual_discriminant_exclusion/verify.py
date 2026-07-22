#!/usr/bin/env python3
"""Exact controls for the Pade residual discriminant exclusion."""

from __future__ import annotations


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return trim(out)


def derivative(poly: list[int], prime: int) -> list[int]:
    return trim([index * value % prime for index, value in enumerate(poly)][1:] or [0])


def divmod_poly(
    numerator: list[int], denominator: list[int], prime: int
) -> tuple[list[int], list[int]]:
    remainder = trim(numerator[:])
    quotient = [0] * max(1, len(remainder) - len(denominator) + 1)
    inverse = pow(denominator[-1], -1, prime)
    while len(remainder) >= len(denominator) and remainder != [0]:
        degree = len(remainder) - len(denominator)
        coefficient = remainder[-1] * inverse % prime
        quotient[degree] = coefficient
        for index, value in enumerate(denominator):
            remainder[index + degree] = (
                remainder[index + degree] - coefficient * value
            ) % prime
        trim(remainder)
    return trim(quotient), trim(remainder)


def gcd_poly(left: list[int], right: list[int], prime: int) -> list[int]:
    while right != [0]:
        _, remainder = divmod_poly(left, right, prime)
        left, right = right, remainder
    return trim([value * pow(left[-1], -1, prime) % prime for value in left])


def square_fixture() -> tuple[int, int]:
    prime = 101
    # R(U,Z)=(U-Z)^2, so every specialization has a repeated root.
    for u in (3, 5, 7, 11):
        residual = [u * u % prime, -2 * u % prime, 1]
        repeated = gcd_poly(residual, derivative(residual, prime), prime)
        need(len(repeated) - 1 == 1, "zero-discriminant residual became squarefree")
    return 0, 4


def main() -> None:
    discriminant, tested = square_fixture()
    e = 2**38 - 1
    need(e - 8 > 8, "too few good indices for discriminant identity")
    need(e - 44 > 4, "too few aligned coordinates for polynomial identity")
    print(
        "RATE_HALF_DISTANCE_THREE_PADE_RESIDUAL_DISCRIMINANT_PASS "
        f"discriminant={discriminant} repeated_specializations={tested}"
    )


if __name__ == "__main__":
    main()
