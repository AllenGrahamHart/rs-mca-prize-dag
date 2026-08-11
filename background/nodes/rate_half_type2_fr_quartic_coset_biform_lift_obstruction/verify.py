#!/usr/bin/env python3
"""Finite-scale interpolation checks for the quartic biform lift obstruction."""

from __future__ import annotations

from math import gcd


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def prime_factors(value: int) -> set[int]:
    factors: set[int] = set()
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            factors.add(divisor)
            value //= divisor
        divisor += 1
    if value > 1:
        factors.add(value)
    return factors


def primitive_root(prime: int) -> int:
    factors = prime_factors(prime - 1)
    for candidate in range(2, prime):
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError("primitive root not found")


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    rows = [row[:] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next((r for r in range(pivot_row, row_count) if rows[r][column] % prime), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column] % prime, -1, prime)
        rows[pivot_row] = [(entry * inverse) % prime for entry in rows[pivot_row]]
        for r in range(row_count):
            if r == pivot_row:
                continue
            multiplier = rows[r][column] % prime
            if not multiplier:
                continue
            rows[r] = [
                (left - multiplier * right) % prime
                for left, right in zip(rows[r], rows[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def interpolation_rank(n: int, prime: int, shifts: tuple[int, int, int, int]) -> int:
    order = 4 * n
    check((prime - 1) % order == 0, f"mu_{order} missing mod {prime}")
    generator = primitive_root(prime)
    zeta = pow(generator, (prime - 1) // order, prime)
    check(pow(zeta, order, prime) == 1 and pow(zeta, order // 2, prime) != 1, "domain order")
    subgroup = [pow(zeta, 4 * j, prime) for j in range(n)]
    representatives = [pow(zeta, i + 4 * shifts[i], prime) for i in range(4)]

    rows: list[list[int]] = []
    for i in (1, 2, 3):
        tau = representatives[i]
        for x in subgroup:
            y = tau * x % prime
            powers = [1]
            for _ in range(1, n):
                powers.append(powers[-1] * y % prime)
            rows.append([(-x * value) % prime for value in powers] + powers)
    return rank_mod(rows, prime)


def main() -> None:
    # Five independent cyclic-domain scales. Full rank means A=B=0 is the
    # only degree-at-most-(n-1) solution on the three complete cosets.
    cases = [
        (4, 17),
        (8, 97),
        (16, 193),
        (32, 257),
        (64, 257),
    ]
    ranks = []
    for index, (n, prime) in enumerate(cases):
        shifts = (index % n, (2 * index + 1) % n, (3 * index + 2) % n, (5 * index + 3) % n)
        rank = interpolation_rank(n, prime, shifts)
        check(rank == 2 * n, f"nonzero interpolation solution at n={n}")
        ranks.append(rank)

    m = 64
    n = 4 * m
    order = 4 * n
    check((m, n, order, n - 1) == (64, 256, 1024, 255), "pinned endpoint tuple")
    check(gcd(n - 1, order) == 1, "power map is not injective")
    check(pow(257, 4, order) == 1, "F_(257^4) does not contain mu_1024")
    check(64 % 257 != 0, "leading coefficient division")

    # The second coefficient of (Gamma-x)^m-c is -m*x.
    prime = 1009
    x = 37
    check((-m * x) % prime == (m * pow(-x, 1, prime)) % prime, "binomial coefficient")

    print(
        "RH_TYPE2_FR_QUARTIC_BIFORM_LIFT_OBSTRUCTION_PASS "
        f"scales={len(cases)} ranks={','.join(map(str, ranks))} "
        f"m={m} n={n} N={order} rho={n-1} gcd={gcd(n-1, order)}"
    )


if __name__ == "__main__":
    main()
