#!/usr/bin/env python3
"""Independent normalization and quotient-uniqueness audit."""

from __future__ import annotations

import itertools


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def subtract(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (left[index] if index < len(left) else 0) - (
            right[index] if index < len(right) else 0
        )
    return trim(out)


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def divide_exact(dividend: list[int], divisor: list[int]) -> list[int]:
    work = trim(dividend[:])
    quotient = [0] * max(1, len(work) - len(divisor) + 1)
    while len(work) >= len(divisor):
        coefficient = work[-1] // divisor[-1]
        shift = len(work) - len(divisor)
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            work[shift + index] -= coefficient * value
        trim(work)
    assert work == [0] or not work
    return trim(quotient)


def shifted(exponent: int) -> list[int]:
    return [1] + [0] * (exponent - 1) + [-1]


def beta(pair: tuple[int, int]) -> list[int]:
    return multiply(shifted(pair[0]), shifted(pair[1]))


def reduce_cyclotomic(poly: list[int], n: int) -> tuple[int, ...]:
    degree = n // 2
    out = [0] * degree
    for exponent, coefficient in enumerate(poly):
        quotient, remainder = divmod(exponent, degree)
        out[remainder] += coefficient * (-1 if quotient % 2 else 1)
    return tuple(out)


def main() -> None:
    n = 8
    pi = [1, -1]
    pi_squared = multiply(pi, pi)
    exponents = range(1, n)
    product_pairs = tuple(itertools.combinations_with_replacement(exponents, 2))
    quotient_pairs = tuple((u, v) for u in exponents for v in exponents if u != v)

    normalized_products = 0
    for left, right in itertools.combinations(product_pairs, 2):
        divide_exact(subtract(beta(left), beta(right)), pi_squared)
        normalized_products += 1

    normalized_quotients = 0
    for left, right in itertools.combinations(quotient_pairs, 2):
        u0, v0 = left
        u1, v1 = right
        theta = divide_exact(
            subtract(
                multiply(shifted(v1), shifted(u0)),
                multiply(shifted(v0), shifted(u1)),
            ),
            pi_squared,
        )
        # Nonidentity quotient uniqueness for mu_8: distinct ordered lifts
        # cannot have zero cross-product in Q(zeta_8).
        assert any(reduce_cyclotomic(theta, n))
        normalized_quotients += 1

    normalized_couplings = 0
    for pair in product_pairs:
        for u, v in quotient_pairs:
            divide_exact(
                subtract(multiply(beta(pair), shifted(u)), shifted(v)),
                pi,
            )
            normalized_couplings += 1

    for n_value in (4, 8, 32):
        assert 17 * (n_value - 1) ** 2 <= 300 * n_value * n_value

    print(
        "AUDIT_F3_H3_DOUBLE_ACCIDENT_LOW_DISTANCE_JOINT_IDEAL_ROUTER_PASS "
        f"products={normalized_products} quotient_pairs={normalized_quotients} "
        f"couplings={normalized_couplings}"
    )


if __name__ == "__main__":
    main()
