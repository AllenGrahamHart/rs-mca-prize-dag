#!/usr/bin/env python3
"""Arithmetic compiler for the h=3 per-row accident pose."""

from __future__ import annotations

from fractions import Fraction


def toral_bound(n: int) -> int:
    if n % 3:
        return 0
    m = n // 3
    return m * (m - 1) // 2


def compiled_bound(n: int, c: int) -> Fraction:
    # toral + poisson_boundary + n * (C n)
    return Fraction(toral_bound(n), 1) + Fraction(n * n, 72) + c * n * n


def main() -> None:
    c = 16
    threshold = None
    for n in range(2, 1000):
        if compiled_bound(n, c) < n**3:
            threshold = n
            break
    if threshold is None:
        raise AssertionError("no threshold found")

    for n in (16, 32, 64, 96, 128, 256, 512):
        b = compiled_bound(n, c)
        print(
            f"n={n:4d} C={c:2d} compiled_bound={float(b):12.2f} "
            f"n^3={n**3:12d} ratio={float(b / (n**3)):.6f}"
        )
        if n >= threshold and not b < n**3:
            raise AssertionError((n, b, n**3))

    print(f"H3-ACCIDENT({c}) implies T3<n^3 for all n >= {threshold}")
    print("H3_PER_ROW_ACCIDENT_POSE_PASS")


if __name__ == "__main__":
    main()
