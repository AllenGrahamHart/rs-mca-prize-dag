#!/usr/bin/env python3
"""Audit non-antipodal harmonic lift sets at small two-power orders."""

from __future__ import annotations


def primitive_root(prime: int) -> int:
    factors: list[int] = []
    remainder = prime - 1
    divisor = 2
    while divisor * divisor <= remainder:
        if remainder % divisor == 0:
            factors.append(divisor)
            while remainder % divisor == 0:
                remainder //= divisor
        divisor += 1
    if remainder > 1:
        factors.append(remainder)
    return next(
        candidate
        for candidate in range(2, prime)
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors)
    )


def normalized_sets(order: int, prime: int) -> int:
    generator = primitive_root(prime)
    zeta = pow(generator, (prime - 1) // order, prime)
    powers = [pow(zeta, exponent, prime) for exponent in range(order)]
    exponents = {value: exponent for exponent, value in enumerate(powers)}
    answers: set[tuple[int, ...]] = set()
    for x in powers:
        for y in powers:
            denominator = (1 + x - 2 * y) % prime
            if denominator == 0:
                continue
            z = (2 * x - y * (1 + x)) * pow(denominator, -1, prime) % prime
            values = (1, x, y, z)
            if z not in exponents or len(set(values)) != 4:
                continue
            if len({value * value % prime for value in values}) != 4:
                continue
            answers.add(tuple(sorted(exponents[value] for value in values)))
    return len(answers)


def main() -> None:
    rows = (
        (8, 97, 0),
        (16, 97, 4),
        (32, 193, 40),
        (64, 193, 500),
        (128, 257, 3660),
    )
    observed = []
    for order, prime, expected in rows:
        count = normalized_sets(order, prime)
        assert count == expected
        observed.append(count)
    print(
        "AUDIT_RATE_HALF_ANTIPODAL_PURE_HARMONIC_FERMAT_PASS "
        f"orders=8,16,32,64,128 normalized_sets={','.join(map(str, observed))}"
    )


if __name__ == "__main__":
    main()
