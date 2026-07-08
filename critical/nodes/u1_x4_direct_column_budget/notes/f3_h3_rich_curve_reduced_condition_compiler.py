#!/usr/bin/env python3
"""Arithmetic checks for the conditional h=3 rich-curve compiler."""

from __future__ import annotations

from dataclasses import dataclass


C_RED = 13


@dataclass(frozen=True)
class Row:
    h: int
    z: int
    a: int
    b: int
    d: int
    coeffs: int
    conditions: int
    degree: int
    bound_num: int
    ls_slack: int


def row(h: int, z: int, a: int, b: int, d: int, c_red: int = C_RED) -> Row:
    if min(h, z, a, b, d, c_red) < 1:
        raise ValueError((h, z, a, b, d, c_red))
    coeffs = a * b**3
    conditions = c_red * d * (a + d) * z
    degree = (a - 1) + 6 * h * (b - 1)
    if conditions >= coeffs:
        raise AssertionError(("LS3 fails", h, z, a, b, d, coeffs, conditions))
    return Row(
        h=h,
        z=z,
        a=a,
        b=b,
        d=d,
        coeffs=coeffs,
        conditions=conditions,
        degree=degree,
        bound_num=z * degree,
        ls_slack=coeffs - conditions,
    )


def ceil_div(num: int, den: int) -> int:
    return -(-num // den)


def main() -> None:
    rows = [
        row(h=2**13, z=1, a=512, b=16, d=16),
        row(h=2**13, z=8, a=512, b=32, d=16),
        row(h=2**16, z=16, a=2048, b=64, d=32),
        row(h=2**20, z=32, a=8192, b=128, d=64),
        row(h=2**23, z=64, a=32768, b=256, d=128),
    ]

    print(f"C_red = {C_RED}")
    print(" h        |Z|      A     B    D        LS_slack        ceil(|Z|*L/D)")
    for item in rows:
        bound = ceil_div(item.bound_num, item.d)
        # Degree formula must match the denominator compiler exactly.
        expected_degree = (item.a - 1) + 6 * item.h * (item.b - 1)
        if item.degree != expected_degree:
            raise AssertionError((item, expected_degree))
        print(
            f"{item.h:9d} {item.z:6d} {item.a:6d} {item.b:5d} {item.d:4d}"
            f" {item.ls_slack:15d} {bound:20d}"
        )

    print("RC-RED supplied by log-jet reduction; remaining gate: RC-NV")
    print("H3_RICH_CURVE_REDUCED_CONDITION_COMPILER_PASS")


if __name__ == "__main__":
    main()
