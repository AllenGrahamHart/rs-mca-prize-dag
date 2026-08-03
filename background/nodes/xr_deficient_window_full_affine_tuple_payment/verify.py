#!/usr/bin/env python3
"""Verify full-affine tuple combinatorics and official ell=1 cutoffs."""

from fractions import Fraction
from itertools import combinations
from math import comb, factorial, prod


ROWS = (
    (
        "1/4,1/8", 2**41, 2**33 + 1, 11, 8_453_534_100,
        3_288_278_171_041_750_515_498_549,
        3_288_278_464_999_855_263_825_729,
    ),
    (
        "1/16", 2**41, 2**32 + 1, 10, 4_250_714_177,
        3_288_277_590_015_144_864_544_565,
        3_288_278_415_892_044_198_197_313,
    ),
)


def falling(value: int, length: int) -> int:
    return prod(value - j for j in range(length))


def cap_fraction(h: int, s: int, x: int) -> tuple[int, int]:
    e = x - 3
    r = h - x + 1
    return 2 ** (s - 1) * falling(e, s + 1), falling(r, s + 1)


checks = 0
for name, n, h, s, last, cap_at_last, cap_after in ROWS:
    budget = (17 * n * n - 25 * (n - 4)) // 25
    assert budget == 3_288_278_229_349_592_331_945_250

    numerator, denominator = cap_fraction(h, s, last)
    next_numerator, next_denominator = cap_fraction(h, s, last + 1)
    assert numerator // denominator == cap_at_last
    assert next_numerator // next_denominator == cap_after
    assert numerator <= budget * denominator
    assert next_numerator > budget * next_denominator

    # Exact monotonic ratio after cancellation.
    left = (last - 2) * (h - last + 1)
    right = (last - s - 3) * (h - last - s)
    assert left > right > 0
    checks += 7


def partitions(total: int, cap: int, ceiling: int | None = None):
    if total == 0:
        yield ()
        return
    top = min(total, cap, ceiling if ceiling is not None else cap)
    for first in range(top, 0, -1):
        for tail in partitions(total - first, cap, first):
            yield (first,) + tail


def elementary(parts: tuple[int, ...], order: int) -> int:
    return sum(prod(parts[index] for index in choice)
               for choice in combinations(range(len(parts)), order))


# Exhaust the ordered-avoidance lower bound at small capped profiles.
for ell in range(1, 6):
    for order in range(2, 6):
        s = order - 1
        for r in range(s * ell + 1, s * ell + 9):
            lower_numerator = prod(r - j * ell for j in range(order))
            for profile in partitions(r, ell):
                assert factorial(order) * elementary(profile, order) >= lower_numerator
                checks += 1


def polynomial_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def matrix_rank(columns: list[list[Fraction]]) -> int:
    rows = [list(row) for row in zip(*columns)]
    rank = 0
    for column in range(len(columns)):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [entry / scale for entry in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][column]:
                scale = rows[i][column]
                rows[i] = [a - scale * b for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


# After multiplication by the common denominator, 1 and the simple-pole
# functions at s+1 distinct poles are independent. A pole collision is the
# mutation control.
for s in range(1, 6):
    poles = tuple(range(1, s + 2))
    common = [Fraction(1)]
    for pole in poles:
        common = polynomial_mul(common, [Fraction(-pole), Fraction(1)])
    columns = [common]
    for omitted in range(len(poles)):
        numerator = [Fraction(1)]
        for index, pole in enumerate(poles):
            if index != omitted:
                numerator = polynomial_mul(
                    numerator, [Fraction(-pole), Fraction(1)]
                )
        numerator += [Fraction(0)] * (len(common) - len(numerator))
        columns.append(numerator)
    assert matrix_rank(columns) == s + 2

    collided = list(poles)
    collided[-1] = collided[-2]
    collision_common = [Fraction(1)]
    for pole in collided:
        collision_common = polynomial_mul(
            collision_common, [Fraction(-pole), Fraction(1)]
        )
    collision_columns = [collision_common]
    for omitted in range(len(collided)):
        numerator = [Fraction(1)]
        for index, pole in enumerate(collided):
            if index != omitted:
                numerator = polynomial_mul(
                    numerator, [Fraction(-pole), Fraction(1)]
                )
        numerator += [Fraction(0)] * (
            len(collision_common) - len(numerator)
        )
        collision_columns.append(numerator)
    assert matrix_rank(collision_columns) < s + 2
    assert 2**s >= s + 1
    checks += 3

print(
    "XR_DEFICIENT_WINDOW_FULL_AFFINE_TUPLE_PAYMENT_PASS "
    f"rows={len(ROWS)} checks={checks}"
)
