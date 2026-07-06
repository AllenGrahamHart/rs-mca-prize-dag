#!/usr/bin/env python3
"""Tiny Artin-Schreier sanity check over a prime field."""

from __future__ import annotations

import cmath
import math


def psi(p: int, x: int) -> complex:
    return cmath.exp(2j * math.pi * (x % p) / p)


def g(p: int, x: int) -> int:
    return (x * x + 2 * x + 1) % p


def main() -> None:
    p = 5
    c = 3

    values = []
    for x in range(p):
        f = (pow(g(p, x), p, p) - g(p, x) + c) % p
        values.append(psi(p, f))

    assert all(abs(v - values[0]) < 1e-12 for v in values)
    assert abs(values[0] - psi(p, c)) < 1e-12

    print("dli Artin-Schreier criterion sanity check passed:", {"p": p, "constant": c})


if __name__ == "__main__":
    main()
