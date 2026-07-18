#!/usr/bin/env python3
"""Independent polynomial-basis audit of the low-distance orbit action."""

from __future__ import annotations

import itertools


def reduce_exponent(order: int, exponent: int, coefficient: int) -> tuple[int, int]:
    exponent %= order
    if exponent >= order // 2:
        return exponent - order // 2, -coefficient
    return exponent, coefficient


def shifted_product_tail(order: int, pair: tuple[int, int]) -> tuple[int, ...]:
    row = [0] * (order // 2)
    left, right = pair
    for exponent, coefficient in ((left + right, 1), (left, -1), (right, -1)):
        index, signed = reduce_exponent(order, exponent, coefficient)
        row[index] += signed
    return tuple(row)


def squared_distance(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum((a - b) ** 2 for a, b in zip(left, right, strict=True))


def main() -> None:
    checks = 0
    sign_checks = 0
    for order in (8, 16):
        pairs = list(itertools.combinations_with_replacement(range(1, order), 2))
        rows = {pair: shifted_product_tail(order, pair) for pair in pairs}
        for left, right in itertools.combinations(pairs, 2):
            base = squared_distance(rows[left], rows[right])
            assert base % 2 == 0
            for multiplier in range(1, order, 2):
                moved_left = tuple(sorted((multiplier * left[0] % order, multiplier * left[1] % order)))
                moved_right = tuple(sorted((multiplier * right[0] % order, multiplier * right[1] % order)))
                assert squared_distance(rows[moved_left], rows[moved_right]) == base
                checks += 1
            assert squared_distance(rows[right], rows[left]) == base
            sign_checks += 1
    print(
        "AUDIT_F3_H3_LOW_DISTANCE_EXCEPTIONAL_PRIME_ROUTER_PASS "
        f"basis_orbit_checks={checks} exchange_sign_checks={sign_checks}"
    )


if __name__ == "__main__":
    main()
