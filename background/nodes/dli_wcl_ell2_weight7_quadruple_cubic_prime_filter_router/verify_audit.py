#!/usr/bin/env python3
"""Independent audit for the WCL (2,7) router and prime filter."""

from __future__ import annotations

import itertools
from math import comb, gcd


def clean_cycle_pairs(order: int, multiplier: int):
    half = order // 2
    unseen = set(range(order))
    cycles = []
    owner = {}
    while unseen:
        start = min(unseen)
        cycle = []
        value = start
        while value in unseen:
            unseen.remove(value)
            cycle.append(value)
            value = multiplier * value % order
        frozen = tuple(sorted(cycle))
        cycles.append(frozen)
        for item in cycle:
            owner[item] = frozen
    used = set()
    counts = {}
    for cycle in cycles:
        if cycle in used:
            continue
        mate = owner[(cycle[0] + half) % order]
        used.update((cycle, mate))
        if cycle != mate:
            counts[len(cycle)] = counts.get(len(cycle), 0) + 1
    return counts


def closed_n4(counts):
    m1 = counts.get(1, 0)
    m2 = counts.get(2, 0)
    m3 = counts.get(3, 0)
    m4 = counts.get(4, 0)
    return 2 * m4 + 4 * m3 * m1 + 4 * comb(m2, 2) + 8 * m2 * comb(m1, 2) + 16 * comb(m1, 4)


def production_count():
    total = sum(closed_n4(clean_cycle_pairs(1024, a)) for a in range(1, 1024, 2))
    assert total % 512 == 0
    return total // 512


def legal(subset, order):
    half = order // 2
    return all((a - b) % order not in (0, half) for a, b in itertools.combinations(subset, 2))


def direct_small_orbits(order=16):
    subsets = [subset for subset in itertools.combinations(range(order), 4) if legal(subset, order)]
    units = tuple(a for a in range(order) if gcd(a, order) == 1)
    seen = set()
    orbit_count = 0
    for subset in subsets:
        for c in range(order):
            key = (subset, c)
            if key in seen:
                continue
            orbit = set()
            for a in units:
                for r in range(order):
                    image = tuple(sorted((a * value + r) % order for value in subset))
                    orbit.add((image, (a * c + 3 * r) % order))
            seen.update(orbit)
            orbit_count += 1

    fixed_sum = 0
    for a in units:
        for r in range(order):
            fixed_q = sum(tuple(sorted((a * value + r) % order for value in subset)) == subset for subset in subsets)
            fixed_c = sum((a * c + 3 * r) % order == c for c in range(order))
            fixed_sum += fixed_q * fixed_c
    assert fixed_sum % (len(units) * order) == 0
    assert orbit_count == fixed_sum // (len(units) * order)
    return orbit_count, len(subsets)


def trim(poly, prime):
    answer = [value % prime for value in poly]
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


def divmod_poly(left, right, prime):
    left = trim(left, prime)
    right = trim(right, prime)
    quotient = [0] * max(1, len(left) - len(right) + 1)
    inverse = pow(right[-1], -1, prime)
    while len(left) >= len(right) and left != [0]:
        degree = len(left) - len(right)
        scale = left[-1] * inverse % prime
        quotient[degree] = scale
        for index, value in enumerate(right):
            left[index + degree] = (left[index + degree] - scale * value) % prime
        left = trim(left, prime)
    return trim(quotient, prime), left


def gcd_poly(left, right, prime):
    left, right = trim(left, prime), trim(right, prime)
    while right != [0]:
        _, remainder = divmod_poly(left, right, prime)
        left, right = right, remainder
    inverse = pow(left[-1], -1, prime)
    return trim([value * inverse for value in left], prime)


def mul_poly(left, right, prime):
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % prime
    return trim(answer, prime)


def prime_filter_controls():
    prime = 97
    zeta = pow(5, (prime - 1) // 16, prime)
    assert pow(zeta, 16, prime) == 1 and pow(zeta, 8, prime) == prime - 1
    phi = [-1] + [0] * 15 + [1]
    common = [(-zeta) % prime, 1]
    f = mul_poly(common, [(-pow(zeta, 2, prime)) % prime, 1], prime)
    g = mul_poly(common, [(-pow(zeta, 3, prime)) % prime, 1], prime)
    h = gcd_poly(gcd_poly(phi, f, prime), g, prime)
    assert len(h) - 1 == 1

    # If u vanishes at the sole common embedding, H*=1.
    u_zero = common
    divisor = gcd_poly(h, u_zero, prime)
    quotient, remainder = divmod_poly(h, divisor, prime)
    assert remainder == [0] and len(quotient) - 1 == 0

    # If u is nonzero there, the common factor survives.
    u_nonzero = [(-pow(zeta, 4, prime)) % prime, 1]
    divisor = gcd_poly(h, u_nonzero, prime)
    quotient, remainder = divmod_poly(h, divisor, prime)
    assert remainder == [0] and len(quotient) - 1 == 1
    return 2


def main():
    count = production_count()
    assert count == 94_652_815
    small_orbits, small_subsets = direct_small_orbits()
    filter_controls = prime_filter_controls()
    print(
        "DLI_WCL_ELL2_WEIGHT7_QUADRUPLE_CUBIC_ROUTER_AUDIT_PASS "
        f"weight7_orbits={count} small_subsets={small_subsets} "
        f"small_orbits={small_orbits} filter_controls={filter_controls}"
    )


if __name__ == "__main__":
    main()
