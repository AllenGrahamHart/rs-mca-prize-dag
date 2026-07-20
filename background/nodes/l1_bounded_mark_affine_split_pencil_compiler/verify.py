#!/usr/bin/env python3
"""Exhaust the affine-syndrome and marked-pencil identities over F_7."""

from __future__ import annotations

from collections import defaultdict
from itertools import product


Q = 7
D = 2
PETALS = ((1, 2), (3, 4))
SUPPORTS = ((1,), (3,))
MARKS = ((2,), (4,))
LABELS = (1, 3)


def trim(poly: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    out = [value % Q for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return trim([
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(size)
    ])


def sub(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return trim([
        (left[i] if i < len(left) else 0)
        - (right[i] if i < len(right) else 0)
        for i in range(size)
    ])


def scale(poly: tuple[int, ...], scalar: int) -> tuple[int, ...]:
    return trim([scalar * value for value in poly])


def mul(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % Q
    return trim(out)


def evaluate(poly: tuple[int, ...], point: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % Q
    return value


def locator(points: tuple[int, ...]) -> tuple[int, ...]:
    out = (1,)
    for point in points:
        out = mul(out, ((-point) % Q, 1))
    return out


def divmod_poly(
    numerator: tuple[int, ...], denominator: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    work = list(trim(numerator))
    divisor = trim(denominator)
    if len(work) < len(divisor):
        return (0,), trim(work)
    quotient = [0] * (len(work) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, Q)
    while len(work) >= len(divisor) and any(work):
        shift = len(work) - len(divisor)
        factor = work[-1] * inverse % Q
        quotient[shift] = factor
        for index, value in enumerate(divisor):
            work[index + shift] = (work[index + shift] - factor * value) % Q
        work = list(trim(work))
    return trim(quotient), trim(work)


def gcd_poly(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    a, b = trim(left), trim(right)
    while b != (0,):
        _, remainder = divmod_poly(a, b)
        a, b = b, remainder
    return scale(a, pow(a[-1], -1, Q))


def pad(poly: tuple[int, ...]) -> tuple[int, ...]:
    return poly + (0,) * (D + 1 - len(poly))


def pair_add(
    left: tuple[tuple[int, ...], tuple[int, ...]],
    right: tuple[tuple[int, ...], tuple[int, ...]],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return pad(add(left[0], right[0])), pad(add(left[1], right[1]))


def satisfies(
    pair: tuple[tuple[int, ...], tuple[int, ...]],
    point_sets: tuple[tuple[int, ...], ...],
) -> bool:
    f, w = pair
    return all(
        evaluate(w, point) == label * evaluate(f, point) % Q
        for points, label in zip(point_sets, LABELS)
        for point in points
    )


def syndrome(
    pair: tuple[tuple[int, ...], tuple[int, ...]]
) -> tuple[int, ...]:
    f, w = pair
    return tuple(
        (evaluate(w, point) - label * evaluate(f, point)) % Q
        for points, label in zip(MARKS, LABELS)
        for point in points
    )


def main() -> None:
    monic_pairs = []
    for lower in product(range(Q), repeat=D):
        f = tuple(lower) + (1,)
        for w in product(range(Q), repeat=D + 1):
            pair = f, tuple(w)
            if satisfies(pair, SUPPORTS):
                monic_pairs.append(pair)

    directions = []
    for lower in product(range(Q), repeat=D):
        g = tuple(lower) + (0,)
        for b in product(range(Q), repeat=D + 1):
            pair = g, tuple(b)
            if satisfies(pair, PETALS):
                directions.append(pair)

    fibers: dict[tuple[int, ...], list[tuple[tuple[int, ...], tuple[int, ...]]]]
    fibers = defaultdict(list)
    for pair in monic_pairs:
        fibers[syndrome(pair)].append(pair)

    assert len(fibers) <= Q ** sum(len(points) for points in MARKS)
    direction_set = set(directions)
    for values in fibers.values():
        representative = values[0]
        translated = {pair_add(representative, direction) for direction in directions}
        assert translated == set(values)
        for pair in values:
            difference = (
                pad(sub(pair[0], representative[0])),
                pad(sub(pair[1], representative[1])),
            )
            assert difference in direction_set
            assert difference[0][-1] == 0

    petal_locators = tuple(locator(points) for points in PETALS)
    mark_locators = tuple(locator(points) for points in MARKS)
    support_locators = tuple(locator(points) for points in SUPPORTS)
    j = mul(mark_locators[0], mark_locators[1])
    saturated = 0
    for f, w in monic_pairs:
        if gcd_poly(f, w) != (1,):
            continue
        saturated += 1
        for index, label in enumerate(LABELS):
            fiber = sub(w, scale(f, label))
            a_i, remainder = divmod_poly(fiber, support_locators[index])
            assert remainder == (0,)
            j_i, remainder = divmod_poly(j, mark_locators[index])
            assert remainder == (0,)
            c_i = mul(j_i, a_i)
            assert mul(petal_locators[index], c_i) == mul(j, fiber)
            assert len(c_i) - 1 <= D - len(PETALS[index]) + sum(
                len(points) for points in MARKS
            )
        assert gcd_poly(mul(j, f), mul(j, w)) == j

    assert saturated > 0
    print(
        "L1_AFFINE_SPLIT_PENCIL_PASS "
        f"partial={len(monic_pairs)} syndromes={len(fibers)} "
        f"direction={len(directions)} saturated={saturated}"
    )


if __name__ == "__main__":
    main()
