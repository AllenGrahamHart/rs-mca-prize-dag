#!/usr/bin/env python3
"""Replay the h=8 locator parity criterion for antipodal supports."""

from __future__ import annotations

import random

from f3_h8_n64_x83_obstruction_interface import (
    h4_anchored_trades,
    is_antipodal_support,
    locator_from_exponents,
    root_table,
)


PRIMES = (193, 4289, 262337)


def antipodal_lift(quotient: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(quotient + tuple(e + 32 for e in quotient)))


def quotient_support(support: tuple[int, ...]) -> tuple[int, ...]:
    quotient = tuple(sorted({exponent % 32 for exponent in support}))
    if len(quotient) != 8:
        raise AssertionError(("bad quotient size", support, quotient))
    return quotient


def odd_coefficients(locator: list[int], p: int) -> list[tuple[int, int]]:
    return [
        (degree, coeff % p)
        for degree, coeff in enumerate(locator)
        if degree % 2 and coeff % p
    ]


def check_support(p: int, support: tuple[int, ...]) -> bool:
    vals64 = root_table(p, 64)
    locator64 = locator_from_exponents(support, vals64, p)
    locator_even = not odd_coefficients(locator64, p)
    antipodal = is_antipodal_support(support)
    if locator_even != antipodal:
        raise AssertionError((p, support, locator_even, antipodal, locator64))

    if antipodal:
        quotient = quotient_support(support)
        vals32 = root_table(p, 32)
        locator32 = locator_from_exponents(quotient, vals32, p)
        even_coeffs = [locator64[2 * degree] % p for degree in range(9)]
        if even_coeffs != [coeff % p for coeff in locator32]:
            raise AssertionError((p, support, quotient, even_coeffs, locator32))

    return antipodal


def paid_quotient_supports(p: int) -> list[tuple[int, ...]]:
    quotients = []
    for left4, right4, _ in h4_anchored_trades(p):
        quotient = tuple(sorted(set(left4) | set(right4)))
        if len(quotient) != 8:
            raise AssertionError((p, left4, right4, quotient))
        quotients.append(quotient)
    return sorted(set(quotients))


def one_exchange_control(support: tuple[int, ...]) -> tuple[int, ...]:
    support_set = set(support)
    remove = next(exponent for exponent in support if exponent not in (0, 32))
    for add in range(1, 64):
        if add in support_set:
            continue
        candidate = tuple(sorted((support_set - {remove}) | {add}))
        if not is_antipodal_support(candidate):
            return candidate
    raise AssertionError(("no non-antipodal one-exchange control", support))


def random_supports(p: int) -> tuple[int, int]:
    rng = random.Random(64083 + p)
    antipodal_count = 0
    nonantipodal_count = 0

    for _ in range(80):
        quotient = tuple(sorted(rng.sample(range(32), 8)))
        support = antipodal_lift(quotient)
        if not check_support(p, support):
            raise AssertionError(("random antipodal rejected", p, quotient))
        antipodal_count += 1

    while nonantipodal_count < 160:
        support = tuple(sorted(rng.sample(range(64), 16)))
        if is_antipodal_support(support):
            continue
        if check_support(p, support):
            raise AssertionError(("random non-antipodal accepted", p, support))
        nonantipodal_count += 1

    return antipodal_count, nonantipodal_count


def main() -> None:
    paid_support_count = 0
    control_count = 0
    random_antipodal_count = 0
    random_nonantipodal_count = 0

    for p in PRIMES:
        for quotient in paid_quotient_supports(p):
            support = antipodal_lift(quotient)
            if not check_support(p, support):
                raise AssertionError(("paid support rejected", p, quotient))
            paid_support_count += 1

            control = one_exchange_control(support)
            if check_support(p, control):
                raise AssertionError(("one-exchange control accepted", p, control))
            control_count += 1

        a_count, na_count = random_supports(p)
        random_antipodal_count += a_count
        random_nonantipodal_count += na_count

    print("h=8 locator parity criterion for antipodal supports")
    print(f"paid antipodal quotient supports checked: {paid_support_count}")
    print(f"one-exchange non-antipodal controls checked: {control_count}")
    print(f"random antipodal supports checked: {random_antipodal_count}")
    print(f"random non-antipodal supports checked: {random_nonantipodal_count}")
    print("H8_LOCATOR_PARITY_ANTIPODAL_PASS")


if __name__ == "__main__":
    main()
