#!/usr/bin/env python3
"""Small exact aspect-ratio controls for the pure harmonic lift sieve."""

from __future__ import annotations

import json


ROWS = (
    (16, 97, 8),
    (32, 257, 64),
    (64, 1153, 160),
    (128, 2689, 640),
    (256, 7681, 2040),
    (512, 23041, 5680),
)


def prime_factors(value: int) -> list[int]:
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, int(value**0.5) + 1))


def primitive_root(prime: int) -> int:
    factors = prime_factors(prime - 1)
    return next(
        candidate
        for candidate in range(2, prime)
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors)
    )


def harmonic_count(order: int, prime: int) -> int:
    generator = primitive_root(prime)
    zeta = pow(generator, (prime - 1) // order, prime)
    subgroup = [pow(zeta, exponent, prime) for exponent in range(order)]
    members = set(subgroup)
    count = 0
    for x in subgroup:
        for y in subgroup:
            denominator = (1 + x - 2 * y) % prime
            if denominator == 0:
                continue
            w = (
                (2 * x - y * (1 + x))
                * pow(denominator, -1, prime)
                % prime
            )
            values = (1, x, y, w)
            if w in members and len({value * value % prime for value in values}) == 4:
                count += 1
    return count


def main() -> None:
    rows = []
    for order, prime, expected in ROWS:
        assert is_prime(prime)
        assert (prime - 1) % order == 0
        observed = harmonic_count(order, prime)
        assert observed == expected
        rows.append({
            "order": order,
            "prime": prime,
            "field_index": (prime - 1) // order,
            "harmonic_count": observed,
            "random_main_numerator": order**3,
            "random_main_denominator": prime,
        })
    print(json.dumps({"experiment": "pure-harmonic-aspect", "rows": rows}))
    print("RATE_HALF_PURE_HARMONIC_ASPECT_PASS rows=6 max_order=512")


if __name__ == "__main__":
    main()
