#!/usr/bin/env python3
"""Falsification sweep for primary-gap fourth-root rigidity."""

from __future__ import annotations

from itertools import combinations
from math import isqrt


HEIGHTS = tuple(range(3, 13))
PRIMES_PER_HEIGHT = 2


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, isqrt(value) + 1):
        if value % divisor == 0:
            return False
    return True


def prime_divisors(value: int) -> tuple[int, ...]:
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


def admissible_primes(order: int) -> list[int]:
    out: list[int] = []
    multiplier = 1
    while len(out) < PRIMES_PER_HEIGHT:
        candidate = 2 * order * multiplier + 1
        if is_prime(candidate):
            out.append(candidate)
        multiplier += 1
    return out


def subgroup_generator(prime: int, order: int) -> int:
    factors = prime_divisors(order)
    exponent = (prime - 1) // order
    for candidate in range(2, prime):
        root = pow(candidate, exponent, prime)
        if root != 1 and all(
            pow(root, order // factor, prime) != 1 for factor in factors
        ):
            return root
    raise AssertionError("subgroup generator not found")


def denominator_coefficients(
    t: int, c: int, d: int, prime: int
) -> tuple[int, int, int, int, int]:
    total = (c + d) % prime
    product = c * d % prime
    return (
        1,
        -(1 + t + total) % prime,
        (t + (1 + t) * total + product) % prime,
        -(t * total + (1 + t) * product) % prime,
        t * product % prime,
    )


def primary_packet(
    denominator: tuple[int, int, int, int, int], height: int, prime: int
) -> list[int]:
    maximum = 2 * height
    coefficients = [1]
    for n in range(1, maximum + 1):
        value = sum(
            (4 * n - 3 * j) * denominator[j] * coefficients[n - j]
            for j in range(1, min(4, n) + 1)
        )
        coefficients.append(-value * pow(4 * n, -1, prime) % prime)
    return coefficients


def extend_coefficients(
    denominator: tuple[int, int, int, int, int],
    coefficients: list[int],
    maximum: int,
    prime: int,
) -> None:
    for n in range(len(coefficients), maximum + 1):
        value = sum(
            (4 * n - 3 * j) * denominator[j] * coefficients[n - j]
            for j in range(1, min(4, n) + 1)
        )
        coefficients.append(-value * pow(4 * n, -1, prime) % prime)


def secondary_passes(
    denominator: tuple[int, int, int, int, int],
    coefficients: list[int],
    height: int,
    prime: int,
) -> bool:
    extend_coefficients(denominator, coefficients, 3 * height - 1, prime)
    leading = coefficients[2 * height]
    low = coefficients[:height]
    high = coefficients[2 * height : 3 * height]
    square = [0] * height
    for i, left in enumerate(low):
        for j, right in enumerate(high):
            if i + j >= height:
                break
            square[i + j] = (square[i + j] + left * right) % prime
    leading_inverse = pow(leading, -1, prime)
    square = [value * leading_inverse % prime for value in square]
    assert square[0] == 1

    root = [1]
    inverse_two = pow(2, -1, prime)
    for n in range(1, height):
        cross = sum(root[index] * root[n - index] for index in range(1, n))
        root.append((square[n] - cross) * inverse_two % prime)
    return root[height - 2] == 0 and root[height - 1] == 0


def is_pure_fourth_root_set(
    roots: tuple[int, int, int, int], prime: int
) -> bool:
    if 1 not in roots or prime - 1 not in roots:
        return False
    remaining = [root for root in roots if root not in (1, prime - 1)]
    return (
        len(remaining) == 2
        and (remaining[0] + remaining[1]) % prime == 0
        and remaining[0] * remaining[0] % prime == prime - 1
    )


def main() -> None:
    aggregate_sets = 0
    aggregate_survivors = 0
    aggregate_nonpure = 0
    aggregate_secondary = 0
    aggregate_secondary_nonpure = 0
    for height in HEIGHTS:
        order = 8 * height - 8
        for prime in admissible_primes(order):
            generator = subgroup_generator(prime, order)
            subgroup = [pow(generator, exponent, prime) for exponent in range(order)]
            sets = 0
            survivors = 0
            pure_survivors = 0
            secondary_survivors = 0
            secondary_pure = 0
            nonpure: list[tuple[int, int, int, int]] = []
            secondary_nonpure: list[tuple[int, int, int, int]] = []
            for tail in combinations(subgroup[1:], 3):
                roots = (1,) + tail
                sets += 1
                e_poly = denominator_coefficients(*tail, prime)
                coefficients = primary_packet(e_poly, height, prime)
                first = coefficients[2 * height - 2]
                second = coefficients[2 * height - 1]
                leading = coefficients[2 * height]
                if first or second or leading == 0:
                    continue
                survivors += 1
                pure = is_pure_fourth_root_set(roots, prime)
                if pure:
                    pure_survivors += 1
                elif len(nonpure) < 3:
                    nonpure.append(roots)
                if secondary_passes(e_poly, coefficients, height, prime):
                    secondary_survivors += 1
                    if pure:
                        secondary_pure += 1
                    elif len(secondary_nonpure) < 3:
                        secondary_nonpure.append(roots)
            aggregate_sets += sets
            aggregate_survivors += survivors
            aggregate_nonpure += survivors - pure_survivors
            aggregate_secondary += secondary_survivors
            aggregate_secondary_nonpure += secondary_survivors - secondary_pure
            print(
                "PRIMARY_RIGIDITY_SWEEP "
                f"H={height} N={order} p={prime} sets={sets} "
                f"survivors={survivors} pure={pure_survivors} "
                f"nonpure={survivors-pure_survivors} witnesses={nonpure} "
                f"secondary={secondary_survivors} secondary_pure={secondary_pure} "
                f"secondary_nonpure={secondary_survivors-secondary_pure} "
                f"secondary_witnesses={secondary_nonpure}",
                flush=True,
            )
    print(
        "PRIMARY_RIGIDITY_TOTAL "
        f"rows={len(HEIGHTS) * PRIMES_PER_HEIGHT} sets={aggregate_sets} "
        f"survivors={aggregate_survivors} nonpure={aggregate_nonpure} "
        f"secondary={aggregate_secondary} "
        f"secondary_nonpure={aggregate_secondary_nonpure}",
        flush=True,
    )


if __name__ == "__main__":
    main()
