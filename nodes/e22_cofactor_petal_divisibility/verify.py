#!/usr/bin/env python3
"""Tiny finite-field check for the E22 cofactor divisibility translation."""

from __future__ import annotations


def trim(poly: list[int] | tuple[int, ...]) -> tuple[int, ...]:
    out = list(poly)
    while out and out[-1] == 0:
        out.pop()
    return tuple(out)


def add(a: tuple[int, ...], b: tuple[int, ...], p: int) -> tuple[int, ...]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return trim(out)


def scale(a: tuple[int, ...], s: int, p: int) -> tuple[int, ...]:
    return trim([(s * x) % p for x in a])


def mul(a: tuple[int, ...], b: tuple[int, ...], p: int) -> tuple[int, ...]:
    if not a or not b:
        return ()
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = (out[i + j] + ai * bj) % p
    return trim(out)


def locator(points: list[int], p: int) -> tuple[int, ...]:
    out = (1,)
    for x in points:
        out = mul(out, ((-x) % p, 1), p)
    return out


def eval_poly(poly: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for c in reversed(poly):
        value = (value * x + c) % p
    return value


def divmod_poly(num: tuple[int, ...], den: tuple[int, ...], p: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    if not den:
        raise ZeroDivisionError
    rem = list(num)
    quot = [0] * max(0, len(num) - len(den) + 1)
    den_lc_inv = pow(den[-1], -1, p)
    while len(rem) >= len(den) and rem:
        coeff = rem[-1] * den_lc_inv % p
        shift = len(rem) - len(den)
        quot[shift] = coeff
        for i, di in enumerate(den):
            rem[shift + i] = (rem[shift + i] - coeff * di) % p
        rem = list(trim(rem))
    return trim(quot), trim(rem)


def main() -> None:
    p = 101
    touched = [3, 8, 19, 42]
    base = (7, 5, 0, 3)
    h = mul(locator(touched, p), base, p)
    assert all(eval_poly(h, x, p) == 0 for x in touched)
    _, rem = divmod_poly(h, locator(touched, p), p)
    assert rem == ()

    not_touched = touched[:-1]
    bad_h = add(h, locator(not_touched, p), p)
    assert all(eval_poly(bad_h, x, p) == 0 for x in not_touched)
    assert eval_poly(bad_h, touched[-1], p) != 0
    _, bad_rem = divmod_poly(bad_h, locator(touched, p), p)
    assert bad_rem != ()

    print("e22_cofactor_petal_divisibility checks passed")


if __name__ == "__main__":
    main()
