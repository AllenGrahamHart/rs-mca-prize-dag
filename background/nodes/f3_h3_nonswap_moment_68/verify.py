#!/usr/bin/env python3
"""Audit the non-swap identity, multiplier bijection, and sharp compiler."""

from __future__ import annotations

import itertools


def inverse(a: int, p: int) -> int:
    return pow(a, p - 2, p)


def moments(a_set: frozenset[int], p: int) -> tuple[int, int, int]:
    product_reps: dict[int, list[tuple[int, int]]] = {}
    quotient_reps: dict[int, list[tuple[int, int]]] = {}
    for a in a_set:
        for b in a_set:
            product_reps.setdefault(a * b % p, []).append((a, b))
            quotient_reps.setdefault(b * inverse(a, p) % p, []).append((a, b))

    formula = 0
    direct = 0
    for t, products in product_reps.items():
        if t == 1:
            continue
        quotients = quotient_reps.get(t, [])
        diagonal = sum(x == y for x, y in products)
        formula += (len(products) * (len(products) - 2) + diagonal) * len(quotients)
        for first in products:
            for second in products:
                if second != first and second != first[::-1]:
                    direct += len(quotients)

    multiplier = 0
    for lam in range(1, p):
        if lam == 1:
            continue
        lam_inv = inverse(lam, p)
        for a in a_set:
            for b in a_set:
                if a * b % p == 1 or lam == b * inverse(a, p) % p:
                    continue
                if lam * a % p not in a_set or b * lam_inv % p not in a_set:
                    continue
                for c in a_set:
                    if a * b * c % p in a_set:
                        multiplier += 1
    return formula, direct, multiplier


def check_compiler() -> None:
    for m in range(100_001):
        for d in range(3):
            if d <= m and d % 2 == m % 2:
                if 136 * max(m - 35, 0) > m * (m - 2) + d:
                    raise AssertionError((m, d))

    # Mutation control: increasing 136 to 137 breaks the sharp boundary case.
    if 137 * (68 - 35) <= 68 * 66:
        raise AssertionError("mutation 137 unexpectedly survived")


def main() -> None:
    check_compiler()
    checked = 0
    for p, max_size in ((7, 5), (11, 5), (13, 4)):
        nonzero = range(1, p)
        for size in range(2, min(max_size, p - 1) + 1):
            for values in itertools.combinations(nonzero, size):
                result = moments(frozenset(values), p)
                if result[0] != result[1] or result[0] != result[2]:
                    raise AssertionError((p, values, result))
                checked += 1
    print(
        "H3_NONSWAP_68_PASS "
        f"subsets={checked} compiler=0..100000 mutation=137-rejected"
    )


if __name__ == "__main__":
    main()

