#!/usr/bin/env python3
"""Replay the Mobius-overlap compiler for the repaired C36' threshold."""

from __future__ import annotations

from collections import Counter


ROWS = {
    (97, 32): (9_692, 12, 14),
    (4_289, 64): (3_639, 0, 6),
    (7_937, 64): (5_765, 12, 14),
}


def prime_factors(value: int) -> tuple[int, ...]:
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return tuple(factors)


def subgroup(prime: int, order: int) -> tuple[int, ...]:
    group_order = prime - 1
    primitive = next(
        candidate
        for candidate in range(2, prime)
        if all(
            pow(candidate, group_order // factor, prime) != 1
            for factor in prime_factors(group_order)
        )
    )
    generator = pow(primitive, group_order // order, prime)
    return tuple(pow(generator, exponent, prime) for exponent in range(order))


def verify_row(prime: int, order: int) -> tuple[int, int, int]:
    roots = subgroup(prime, order)
    root_set = set(roots)
    shifted = tuple((1 - root) % prime for root in roots if root != 1)
    products = Counter(
        left * right % prime for left in shifted for right in shifted
    )
    quotients = Counter(
        left * pow(right, -1, prime) % prime
        for left in shifted
        for right in shifted
    )

    three_to_one = sum(products[value] * multiplicity
                       for value, multiplicity in quotients.items())
    identity_fiber = products[1]
    one_shift = sum(1 for root in roots if (1 - root) % prime in root_set)
    if identity_fiber != one_shift:
        raise AssertionError((prime, order, identity_fiber, one_shift))

    overlap_max = max(
        (products[value] for value in quotients if value != 1),
        default=0,
    )
    if sum(quotients.values()) != (order - 1) ** 2:
        raise AssertionError((prime, order, "quotient mass"))
    if quotients[1] != order - 1:
        raise AssertionError((prime, order, "identity quotient"))
    return three_to_one, identity_fiber, overlap_max


def verify_official_compiler() -> None:
    for exponent in range(13, 42):
        order = 1 << exponent

        # order >= 20^3 gives
        #   4 n^(5/3) <= n^2/5 and 16 n^(4/3) <= n^2/25.
        if order < 20**3:
            raise AssertionError((exponent, order, "cube-root floor"))

        # Under M35 and P(1)<4n^(2/3),
        # N < 35(n-1)(n-2) + 4n^(2/3)(n-1).
        # Moving the C36' correction to the left and applying the two bounds
        # above leaves this exact rational inequality (multiplied by 50).
        left = 50 * 35 * (order - 1) * (order - 2) + 12 * order**2
        right = 50 * 36 * order**2 - 25 * order
        if left >= right:
            raise AssertionError((exponent, order, right - left))


def main() -> None:
    for row, expected in ROWS.items():
        actual = verify_row(*row)
        if actual != expected:
            raise AssertionError((row, actual, expected))
    verify_official_compiler()
    print(
        "H3_MOBIUS_OVERLAP_CAP_COMPILER_PASS "
        f"small_rows={len(ROWS)} official_orders=29 cap=35"
    )


if __name__ == "__main__":
    main()
