#!/usr/bin/env python3
"""Independent finite-field polynomial audit of the layered gcd compiler."""

from __future__ import annotations


def trim(poly: list[int], prime: int) -> list[int]:
    poly = [value % prime for value in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % prime
    return trim(answer, prime)


def power(poly: list[int], exponent: int, prime: int) -> list[int]:
    answer = [1]
    base = poly
    while exponent:
        if exponent & 1:
            answer = multiply(answer, base, prime)
        exponent //= 2
        if exponent:
            base = multiply(base, base, prime)
    return answer


def divide_with_remainder(dividend: list[int], divisor: list[int], prime: int) -> tuple[list[int], list[int]]:
    remainder = trim(dividend[:], prime)
    divisor = trim(divisor, prime)
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], prime - 2, prime)
    while len(remainder) >= len(divisor) and remainder != [0]:
        shift = len(remainder) - len(divisor)
        scale = remainder[-1] * inverse % prime
        quotient[shift] = scale
        for index, value in enumerate(divisor):
            remainder[index + shift] = (remainder[index + shift] - scale * value) % prime
        remainder = trim(remainder, prime)
    return trim(quotient, prime), remainder


def monic(poly: list[int], prime: int) -> list[int]:
    poly = trim(poly, prime)
    if poly == [0]:
        return poly
    inverse = pow(poly[-1], prime - 2, prime)
    return [(value * inverse) % prime for value in poly]


def polynomial_gcd(left: list[int], right: list[int], prime: int) -> list[int]:
    left, right = trim(left, prime), trim(right, prime)
    while right != [0]:
        _, remainder = divide_with_remainder(left, right, prime)
        left, right = right, remainder
    return monic(left, prime)


def derivative(poly: list[int], order: int, prime: int) -> list[int]:
    answer = poly
    for _ in range(order):
        answer = [index * answer[index] % prime for index in range(1, len(answer))] or [0]
    return trim(answer, prime)


def polynomial_from_roots(roots: list[int], prime: int) -> list[int]:
    answer = [1]
    for root in roots:
        answer = multiply(answer, [(-root) % prime, 1], prime)
    return answer


def order_generator(order: int, prime: int) -> int:
    for value in range(2, prime):
        if pow(value, order, prime) == 1 and pow(value, order // 2, prime) != 1:
            return value
    raise AssertionError("no subgroup generator")


def audit_row(order: int, prime: int, cutoff: int, expected: tuple[int, int]) -> None:
    generator = order_generator(order, prime)
    group = {pow(generator, exponent, prime) for exponent in range(order)}
    shifted = {(1 - value) % prime for value in group if value != 1}
    product_count: dict[int, int] = {}
    quotient_count: dict[int, int] = {}
    for left in shifted:
        for right in shifted:
            product = left * right % prime
            product_count[product] = product_count.get(product, 0) + 1
            quotient = right * pow(left, prime - 2, prime) % prime
            if quotient != 1:
                quotient_count[quotient] = quotient_count.get(quotient, 0) + 1

    product_roots = [target for target, count in product_count.items() for _ in range(count)]
    quotient_roots = [target for target, count in quotient_count.items() for _ in range(count)]
    product_poly = polynomial_from_roots(product_roots, prime)
    quotient_poly = polynomial_from_roots(quotient_roots, prime)

    rich = product_poly
    for index in range(1, cutoff + 1):
        rich = polynomial_gcd(rich, derivative(product_poly, index, prime), prime)
    quotient_extra = polynomial_gcd(quotient_poly, derivative(quotient_poly, 1, prime), prime)

    total = extra = 0
    layer = rich
    d = order - 1
    for index in range(1, d - cutoff + 1):
        if index > 1:
            layer = polynomial_gcd(layer, derivative(rich, index - 1, prime), prime)
        saturated = power(layer, d, prime)
        total += len(polynomial_gcd(quotient_poly, saturated, prime)) - 1
        extra += len(polynomial_gcd(quotient_extra, saturated, prime)) - 1

    direct_total = sum(
        max(count - cutoff, 0) * quotient_count.get(target, 0)
        for target, count in product_count.items()
    )
    direct_extra = sum(
        max(count - cutoff, 0) * max(quotient_count.get(target, 0) - 1, 0)
        for target, count in product_count.items()
    )
    assert (total, extra) == expected == (direct_total, direct_extra)


def main() -> None:
    audit_row(8, 17, 2, (48, 32))
    audit_row(16, 97, 2, (153, 90))
    print("AUDIT_F3_H3_CUTOFF_LAYERED_GCD_COMPILER_PASS rows=2 positive_double_accidents=2")


if __name__ == "__main__":
    main()
