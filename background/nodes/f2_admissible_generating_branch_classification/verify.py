#!/usr/bin/env python3
"""Fail-closed certificates for the five generating F2 row types."""

from __future__ import annotations

import math


CHECKS = 0


def check(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def v2(value: int) -> int:
    return (value & -value).bit_length() - 1


def dyadic_order(value: int, exponent: int) -> int:
    modulus = 1 << exponent
    current = value % modulus
    order = 1
    while current != 1:
        current = current * current % modulus
        order *= 2
        if order > 1 << (exponent - 2):
            raise AssertionError("dyadic order overflow")
    return order


def trial_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def pocklington(
    value: int, factors: dict[int, int], witnesses: dict[int, int]
) -> None:
    product = math.prod(prime**power for prime, power in factors.items())
    check(product == value - 1, "complete p-1 factorization")
    check(product > math.isqrt(value), "Pocklington size threshold")
    for prime in factors:
        check(trial_prime(prime), "factor primality")
        witness = witnesses[prime]
        check(pow(witness, value - 1, value) == 1, "Fermat condition")
        check(
            math.gcd(pow(witness, (value - 1) // prime, value) - 1, value)
            == 1,
            "Pocklington gcd condition",
        )


def lucas_lehmer(exponent: int) -> bool:
    modulus = (1 << exponent) - 1
    value = 4
    for _ in range(exponent - 2):
        value = (value * value - 2) % modulus
    return value == 0


def main() -> None:
    plus_rows = (
        (
            3 * (1 << 41) + 1,
            1,
            {2: 41, 3: 1},
            {2: 5, 3: 5},
            41,
        ),
        (
            27 * (1 << 40) + 1,
            2,
            {2: 40, 3: 3},
            {2: 5, 3: 3},
            40,
        ),
        (
            5 * (1 << 39) + 1,
            4,
            {2: 39, 5: 1},
            {2: 3, 5: 3},
            39,
        ),
    )
    observed: set[tuple[str, int, int]] = set()
    for prime, degree, factors, witnesses, valuation in plus_rows:
        pocklington(prime, factors, witnesses)
        check(prime % 4 == 1, "plus residue")
        check(v2(prime - 1) == valuation, "plus valuation")
        check(dyadic_order(prime, 41) == degree, "plus order")
        check(prime**degree < 1 << 256, "plus field cap")
        observed.add(("plus", valuation, degree))

    m61 = (1 << 61) - 1
    check(lucas_lehmer(61), "M61 primality")
    check(m61 % 4 == 3, "M61 residue")
    check(v2(m61 + 1) >= 40, "M61 valuation")
    check(dyadic_order(m61, 41) == 2, "M61 order")
    check(m61**2 < 1 << 256, "M61 field cap")
    observed.add(("minus", 40, 2))

    minus_four = 25 * (1 << 39) - 1
    pocklington(
        minus_four,
        {2: 1, 3: 2, 131: 1, 20011: 1, 291271: 1},
        {2: 3, 3: 2, 131: 2, 20011: 2, 291271: 2},
    )
    check(minus_four % 4 == 3, "minus-four residue")
    check(v2(minus_four + 1) == 39, "minus-four valuation")
    check(dyadic_order(minus_four, 41) == 4, "minus-four order")
    check(minus_four**4 < 1 << 256, "minus-four field cap")
    observed.add(("minus", 39, 4))

    check(
        observed
        == {
            ("plus", 41, 1),
            ("plus", 40, 2),
            ("plus", 39, 4),
            ("minus", 40, 2),
            ("minus", 39, 4),
        },
        "five witness types",
    )

    generated_types: set[tuple[str, int, int]] = set()
    for valuation in range(2, 48):
        plus_order = 1 << max(0, 41 - valuation)
        minus_order = 1 << max(1, 41 - valuation)
        for degree in range(1, 7):
            if plus_order == degree:
                generated_types.add(("plus", min(valuation, 41), degree))
            if minus_order == degree:
                generated_types.add(("minus", min(valuation, 40), degree))
    check(generated_types == observed, "symbolic exhaustive classification")

    print(
        "F2_ADMISSIBLE_GENERATING_BRANCH_CLASSIFICATION_PASS "
        f"checks={CHECKS} types={len(observed)}"
    )


if __name__ == "__main__":
    main()
