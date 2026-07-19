#!/usr/bin/env python3
"""Verify the G3 canonical-support/profile conversion identity."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb


def coefficient(m: int, power: int, degree: int) -> int:
    """Return [x^degree](sum_{j=0}^{m-1} C(m,j)x^j)^power."""
    values = [1] + [0] * degree
    atom = [comb(m, j) for j in range(min(m - 1, degree) + 1)]
    for _ in range(power):
        nxt = [0] * (degree + 1)
        for i, left in enumerate(values):
            for j, right in enumerate(atom[: degree - i + 1]):
                nxt[i + j] += left * right
        values = nxt
    return values[degree]


def direct_count(n: int, m: int, a: int) -> int:
    blocks = [set(range(i, i + m)) for i in range(0, n, m)]
    total = 0
    for support_tuple in combinations(range(n), a):
        support = set(support_tuple)
        full = set().union(*(block for block in blocks if block <= support))
        if len(support - full) < m:
            total += 1
    return total


def formula(n: int, m: int, a: int) -> tuple[int, Fraction]:
    quotient_order = n // m
    h, b = divmod(a, m)
    tail_count = coefficient(m, quotient_order - h, b)
    raw = comb(quotient_order, h) * tail_count
    converted = (
        Fraction(comb(quotient_order - 1, h) * quotient_order, quotient_order - h)
        * tail_count
    )
    return raw, converted


def main() -> None:
    checks = 0
    for n in (8, 12, 16):
        for m in (d for d in range(2, n + 1) if n % d == 0):
            quotient_order = n // m
            for a in range(n):
                h, _ = divmod(a, m)
                if h >= quotient_order:
                    continue
                raw, converted = formula(n, m, a)
                direct = direct_count(n, m, a)
                if raw != direct or converted.denominator != 1 or converted != raw:
                    raise AssertionError((n, m, a, direct, raw, converted))
                checks += 1

    # Mutation: deleting N/(N-h) fails away from h=0.
    n, m, a = 16, 4, 6
    quotient_order = n // m
    h, b = divmod(a, m)
    q_count = comb(quotient_order - 1, h)
    mutated = q_count * coefficient(m, quotient_order - h, b)
    correct, _ = formula(n, m, a)
    if mutated == correct:
        raise AssertionError("normalization mutation survived")

    print(
        "PETAL_G3_PROFILE_CONVERSION_PASS "
        f"exact_cases={checks} mutation=missing-N-over-N-minus-h"
    )


if __name__ == "__main__":
    main()
