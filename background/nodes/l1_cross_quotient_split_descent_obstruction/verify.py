#!/usr/bin/env python3
"""Replay the exact F_23 nonsplit cross-quotient witness."""

from __future__ import annotations


P = 23
ELL = 2
CORE = tuple(range(8))
BACKGROUND = (13,)
SUPPORT = (8, 9, 10, 11, 12)
FILLERS = (14, 15, 16, 17, 18)
LABELS = (1, 2, 4, 3, 8)
D0 = (0, 1, 5, 7)
D1 = (2, 3, 4, 6)
F0 = (0, 11, 1, 10, 1)
W0 = (20, 5, 19, 13, 5)
F1 = (6, 4, 11, 8, 1)
W1 = (3, 9, 16, 2, 13)


def trim(poly: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    out = [value % P for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def sub(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return trim([
        (left[i] if i < len(left) else 0)
        - (right[i] if i < len(right) else 0)
        for i in range(size)
    ])


def mul(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % P
    return trim(out)


def evaluate(poly: tuple[int, ...], point: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % P
    return value


def locator(points: tuple[int, ...]) -> tuple[int, ...]:
    out = (1,)
    for point in points:
        out = mul(out, ((-point) % P, 1))
    return out


def divmod_poly(
    numerator: tuple[int, ...], denominator: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    work = list(trim(numerator))
    divisor = trim(denominator)
    quotient = [0] * max(1, len(work) - len(divisor) + 1)
    while len(work) >= len(divisor) and trim(work) != (0,):
        shift = len(work) - len(divisor)
        factor = work[-1] * pow(divisor[-1], -1, P) % P
        quotient[shift] = factor
        for index, value in enumerate(divisor):
            work[index + shift] = (work[index + shift] - factor * value) % P
        work = list(trim(work))
    return trim(quotient), trim(work)


def gcd_poly(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    a, b = trim(left), trim(right)
    while b != (0,):
        _, remainder = divmod_poly(a, b)
        a, b = b, remainder
    inverse = pow(a[-1], -1, P)
    return trim([inverse * value for value in a])


def check_pair(
    defect: tuple[int, ...], f: tuple[int, ...], w: tuple[int, ...]
) -> None:
    assert f == locator(defect)
    assert gcd_poly(f, w) == (1,)
    assert all(evaluate(w, point) != 0 for point in defect)
    assert all(
        evaluate(w, point) == label * evaluate(f, point) % P
        for point, label in zip(SUPPORT, LABELS)
    )
    assert all(
        evaluate(w, point) != label * evaluate(f, point) % P
        for point, label in zip(FILLERS, LABELS)
    )
    assert evaluate(w, BACKGROUND[0]) == 0


def main() -> None:
    check_pair(D0, F0, W0)
    check_pair(D1, F1, W1)
    assert set(D0).isdisjoint(D1)

    agreement = (len(CORE) - len(D0)) + len(SUPPORT) + len(BACKGROUND)
    k = len(CORE) + 1
    assert agreement == k + ELL - 1 == 10

    delta = sub(mul(W0, F1), mul(W1, F0))
    quotient, remainder = divmod_poly(delta, locator(SUPPORT))
    assert remainder == (0,)
    assert quotient == (16, 9, 4, 15)

    cofactor, remainder = divmod_poly(quotient, ((-13) % P, 1))
    assert remainder == (0,)
    assert cofactor == (20, 15, 15)
    assert not any(evaluate(cofactor, point) == 0 for point in range(P))
    discriminant = (15 * 15 - 4 * 20 * 15) % P
    assert discriminant == 14
    assert discriminant not in {x * x % P for x in range(P)}

    n_core, d, h = len(CORE), len(D0), len(SUPPORT)
    assert n_core * (2 * d - h) >= d * d

    print(
        "L1_CROSS_QUOTIENT_NONSPLIT_PASS "
        f"agreement={agreement} quotient={quotient} "
        f"cofactor={cofactor} discriminant={discriminant}"
    )


if __name__ == "__main__":
    main()
