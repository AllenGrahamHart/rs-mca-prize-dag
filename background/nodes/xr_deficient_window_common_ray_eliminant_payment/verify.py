#!/usr/bin/env python3
"""Verify the common-ray eliminant model and official row cutoffs."""

from fractions import Fraction
from itertools import permutations
from math import prod


ROWS = (
    (
        "1/4,1/8", 2**41, 2**33 + 1, 11, 8_500_560_263,
        3_288_277_985_160_426_079_436_569,
        3_288_278_431_308_817_786_569_954,
    ),
    (
        "1/16", 2**41, 2**32 + 1, 10, 4_265_559_234,
        3_288_277_482_901_370_162_501_687,
        3_288_278_721_352_163_199_241_837,
    ),
)


def falling(value: int, length: int) -> int:
    return prod(value - j for j in range(length))


def cap_fraction(h: int, s: int, x: int) -> tuple[int, int]:
    e = x - 3
    r = h - x + 1
    return (s + 1) * falling(e, s + 1), 2 * falling(r, s + 1)


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
    assert (last - 2) * (h - last + 1) > (
        (last - s - 3) * (h - last - s)
    ) > 0
    checks += 7


def add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out


def multiply(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    while len(out) > 1 and not out[-1]:
        out.pop()
    return out


def determinant(matrix: list[list[list[Fraction]]]) -> list[Fraction]:
    size = len(matrix)
    total = [Fraction(0)]
    for permutation in permutations(range(size)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(size) for j in range(i + 1, size)
        )
        term = [Fraction(-1 if inversions % 2 else 1)]
        for row, column in enumerate(permutation):
            term = multiply(term, matrix[row][column])
        total = add(total, term)
    return total


# A full-rank direction-evaluation model has an eliminant of exact degree
# m+1. Colliding two phi directions duplicates rows and kills it.
for m in range(1, 6):
    points = tuple(range(1, m + 2))

    def matrix_for(values: tuple[int, ...]):
        matrix = []
        for p in values:
            # rho=(1,z), W_i=(1,p), E_i=(p^m,0), and
            # delta_j(x_i)=p^j for 0<=j<m.
            row = [[Fraction(0), Fraction(p**m)]]
            row.extend(
                [Fraction(-(p ** (j + 1))), Fraction(p**j)]
                for j in range(m)
            )
            matrix.append(row)
        return matrix

    eliminant = determinant(matrix_for(points))
    assert len(eliminant) - 1 == m + 1
    assert eliminant[-1]

    collided = list(points)
    collided[-1] = collided[-2]
    assert determinant(matrix_for(tuple(collided))) == [Fraction(0)]
    checks += 3

print(
    "XR_DEFICIENT_WINDOW_COMMON_RAY_ELIMINANT_PAYMENT_PASS "
    f"rows={len(ROWS)} checks={checks}"
)
