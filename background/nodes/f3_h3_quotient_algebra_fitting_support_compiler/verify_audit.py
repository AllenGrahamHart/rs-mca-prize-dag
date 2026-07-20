#!/usr/bin/env python3
"""Independent multiplicity audit of quotient-algebra support depths."""

from __future__ import annotations


def order_generator(order: int, prime: int) -> int:
    for value in range(2, prime):
        if pow(value, order, prime) == 1 and pow(value, order // 2, prime) != 1:
            return value
    raise AssertionError("no subgroup generator")


def row_depths(order: int, prime: int, cutoff: int) -> tuple[int, int, int, int]:
    generator = order_generator(order, prime)
    group = {pow(generator, exponent, prime) for exponent in range(order)}
    shifted = {(1 - value) % prime for value in group if value != 1}
    products: dict[int, int] = {}
    quotients: dict[int, int] = {}
    for left in shifted:
        for right in shifted:
            product = left * right % prime
            products[product] = products.get(product, 0) + 1
            quotient = right * pow(left, prime - 2, prime) % prime
            if quotient != 1:
                quotients[quotient] = quotients.get(quotient, 0) + 1

    zx = zy = weighted_x = weighted_y = 0
    for target, multiplicity in products.items():
        excess = max(multiplicity - cutoff, 0)
        quotient = quotients.get(target, 0)
        zx += min(quotient, excess)
        zy += min(max(quotient - 1, 0), excess)
        weighted_x += quotient * excess
        weighted_y += max(quotient - 1, 0) * excess
    return zx, zy, weighted_x, weighted_y


def main() -> None:
    fixtures = {
        (16, 257, 2): (16, 7, 36, 14),
        (16, 337, 2): (11, 1, 20, 1),
        (16, 401, 2): (2, 0, 3, 0),
    }
    for key, expected in fixtures.items():
        actual = row_depths(*key)
        assert actual == expected
        assert actual[0] <= actual[2] and actual[1] <= actual[3]
        assert (actual[0] > 0) == (actual[2] > 0)
        assert (actual[1] > 0) == (actual[3] > 0)
    print("AUDIT_F3_H3_QUOTIENT_ALGEBRA_FITTING_SUPPORT_PASS fixtures=3 support_vs_weight=exact")


if __name__ == "__main__":
    main()
