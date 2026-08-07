#!/usr/bin/env python3
"""Exact parameter compiler for the h=3 rank-form Stepanov box."""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt


C_RED = 13
B_MAX = 20_000


@dataclass(frozen=True)
class Row:
    n: int
    z: int
    bound: int
    a: int
    b: int
    d: int
    degree: int
    conditions: int
    coeffs: int
    image_cap: int


def best_diagonal_box(n: int, z: int, b_max: int = B_MAX) -> Row:
    best: Row | None = None
    for b in range(2, b_max + 1):
        # Use A=D.  These conservative caps imply both LS3 and the
        # necessary image-cap inequality for rank-form nonvanishing.
        rank_cap = (1 + 6 * n * (b - 1)) // (4 * C_RED)
        ls_cap = (b**3 - 1) // (4 * C_RED * z)
        d = min(isqrt(rank_cap), ls_cap)
        if d < 1:
            continue
        a = d
        coeffs = a * b**3
        conditions = C_RED * d * (a + d) * z
        degree = (a - 1) + 6 * n * (b - 1)
        image_cap = z * (degree + 1)
        if not (conditions < coeffs and conditions < image_cap):
            continue
        bound = (z * degree + d - 1) // d
        row = Row(
            n=n,
            z=z,
            bound=bound,
            a=a,
            b=b,
            d=d,
            degree=degree,
            conditions=conditions,
            coeffs=coeffs,
            image_cap=image_cap,
        )
        if best is None or row.bound < best.bound:
            best = row
    if best is None:
        raise AssertionError(("no admissible diagonal box", n, z, b_max))
    return best


def ratio_milli(bound: int, n: int) -> int:
    return (1000 * bound + n - 1) // n


def main() -> None:
    cases = [
        (2**13, 1),
        (2**13, 8),
        (2**16, 16),
        (2**20, 32),
        (2**23, 64),
        (2**32, 128),
        (2**40, 256),
        (2**41, 256),
        (2**41, 512),
    ]
    expected = {
        (2**13, 1): (6807, 130, 19, 130),
        (2**13, 8): (84129, 201, 44, 201),
        (2**16, 16): (674932, 811, 88, 811),
        (2**20, 32): (8206612, 4931, 202, 4931),
        (2**23, 64): (65729374, 19750, 404, 19750),
        (2**32, 128): (6380025160, 958536, 1855, 958536),
        (2**40, 256): (408399380318, 30675581, 7419, 30675581),
        (2**41, 256): (619017527995, 46500714, 8523, 46500714),
        (2**41, 512): (1422138529491, 53415659, 11246, 53415659),
    }

    print("h=3 rank-form parameter compiler")
    print(f"C_red={C_RED} B_max={B_MAX} diagonal box A=D")
    print(" n              |Z|    bound        ceil(1000*bound/n)   A        B      D")
    for n, z in cases:
        row = best_diagonal_box(n, z)
        got = (row.bound, row.a, row.b, row.d)
        if got != expected[(n, z)]:
            raise AssertionError((n, z, got, expected[(n, z)]))
        print(
            f"{row.n:14d} {row.z:6d} {row.bound:14d}"
            f" {ratio_milli(row.bound, row.n):21d}"
            f" {row.a:8d} {row.b:6d} {row.d:8d}"
        )

    print("checked inequalities: conditions < coeffs and conditions < image_cap")
    print("interpretation: conditional on RC-RANK, sum_z T(z) <= bound")
    print("H3_RANK_PARAMETER_COMPILER_PASS")


if __name__ == "__main__":
    main()
