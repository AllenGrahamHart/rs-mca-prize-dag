#!/usr/bin/env python3
"""Verify the WCL (2,7) quadruple-cubic router and orbit count."""

from __future__ import annotations

import itertools
import random

ORDER = 1024
HALF = 512


def invariant_legal_count(multiplier: int, weight: int) -> int:
    seen = set()
    cycles = []
    owner = {}
    for start in range(ORDER):
        if start in seen:
            continue
        cycle = []
        value = start
        while value not in seen:
            seen.add(value)
            cycle.append(value)
            value = multiplier * value % ORDER
        frozen = tuple(sorted(cycle))
        cycles.append(frozen)
        for item in cycle:
            owner[item] = frozen

    pairs = []
    used = set()
    for cycle in cycles:
        if cycle in used:
            continue
        mate = owner[(cycle[0] + HALF) % ORDER]
        used.add(cycle)
        used.add(mate)
        if mate != cycle:
            pairs.append(len(cycle))

    coefficients = [0] * (weight + 1)
    coefficients[0] = 1
    for length in pairs:
        for degree in range(weight, length - 1, -1):
            coefficients[degree] += 2 * coefficients[degree - length]
    return coefficients[weight]


def orbit_count(weight: int) -> int:
    total = sum(invariant_legal_count(a, weight) for a in range(1, ORDER, 2))
    assert total % HALF == 0
    return total // HALF


def primitive_root(prime: int) -> int:
    for value in range(2, prime):
        if pow(value, (prime - 1) // 2, prime) != 1 and pow(value, (prime - 1) // 3, prime) != 1:
            return value
    raise AssertionError("primitive root not found")


def recurrence_controls() -> int:
    prime = 12289
    root = pow(primitive_root(prime), (prime - 1) // ORDER, prime)
    assert pow(root, ORDER, prime) == 1 and pow(root, HALF, prime) == prime - 1
    rng = random.Random(0x271024)
    checks = 0
    while checks < 256:
        exponents = rng.sample(range(ORDER), 3)
        roots = [pow(root, exponent, prime) for exponent in exponents]
        u = (-sum(roots)) % prime
        if u == 0:
            continue
        e2 = sum(roots[i] * roots[j] for i in range(3) for j in range(i + 1, 3)) % prime
        d = roots[0] * roots[1] * roots[2] % prime
        selected_e2 = rng.randrange(prime)
        selected_e3 = (u * selected_e2 - d - u * e2) % prime
        w = (u * selected_e2 - selected_e3 - d) % prime
        assert w == u * e2 % prime

        sigma = -u * u % prime
        theta = u * w % prime
        product = pow(u, 3, prime) * d % prime
        power = 1
        while power < ORDER:
            sigma, theta, product = (
                (sigma * sigma - 2 * theta) % prime,
                (theta * theta - 2 * product * sigma) % prime,
                product * product % prime,
            )
            power *= 2
        assert sigma == 3 * pow(u, ORDER, prime) % prime
        assert theta == 3 * pow(u, 2 * ORDER, prime) % prime
        checks += 1
    return checks


def main():
    weight6_control = orbit_count(3)
    weight7 = orbit_count(4)
    assert weight6_control == 404_740
    assert weight7 == 94_652_815
    recurrence = recurrence_controls()
    print(
        "DLI_WCL_ELL2_WEIGHT7_QUADRUPLE_CUBIC_ROUTER_PASS "
        f"weight6_control={weight6_control} weight7_orbits={weight7} "
        f"recurrence_controls={recurrence}"
    )


if __name__ == "__main__":
    main()
