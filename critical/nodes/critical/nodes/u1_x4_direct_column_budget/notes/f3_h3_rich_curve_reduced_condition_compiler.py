#!/usr/bin/env python3
"""Arithmetic checks for the conditional h=3 rich-curve compiler."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_rich_curve_condition_profile import (
    exact_conditions_per_curve,
    legacy_conditions_per_curve,
)


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
    exact_conditions: int
    degree: int
    bound_num: int
    ls_slack: int
    exact_ls_slack: int


def row(h: int, z: int, a: int, b: int, d: int, c_red: int = C_RED) -> Row:
    if min(h, z, a, b, d, c_red) < 1:
        raise ValueError((h, z, a, b, d, c_red))
    coeffs = a * b**3
    conditions = legacy_conditions_per_curve(a, d) * z
    if conditions != c_red * d * (a + d) * z:
        raise AssertionError((conditions, c_red, a, d, z))
    exact_conditions = exact_conditions_per_curve(a, d) * z
    degree = (a - 1) + 6 * h * (b - 1)
    if conditions >= coeffs:
        raise AssertionError(("LS3 fails", h, z, a, b, d, coeffs, conditions))
    if exact_conditions >= coeffs:
        raise AssertionError(("exact LS3 fails", h, z, a, b, d, coeffs, exact_conditions))
    return Row(
        h=h,
        z=z,
        a=a,
        b=b,
        d=d,
        coeffs=coeffs,
        conditions=conditions,
        exact_conditions=exact_conditions,
        degree=degree,
        bound_num=z * degree,
        ls_slack=coeffs - conditions,
        exact_ls_slack=coeffs - exact_conditions,
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
    print("exact conditions per curve = DA + 6D(D-1)")
    print(
        " h        |Z|      A     B    D        LS_slack"
        "   exact_LS_slack        ceil(|Z|*L/D)"
    )
    for item in rows:
        bound = ceil_div(item.bound_num, item.d)
        # Degree formula must match the denominator compiler exactly.
        expected_degree = (item.a - 1) + 6 * item.h * (item.b - 1)
        if item.degree != expected_degree:
            raise AssertionError((item, expected_degree))
        print(
            f"{item.h:9d} {item.z:6d} {item.a:6d} {item.b:5d} {item.d:4d}"
            f" {item.ls_slack:15d} {item.exact_ls_slack:16d} {bound:20d}"
        )

    print("legacy RC-RED(13) is retained; exact profile is sharper for future optimizers")
    print("RC-RED supplied by log-jet reduction; remaining gate: RC-NV")
    print("H3_RICH_CURVE_REDUCED_CONDITION_COMPILER_PASS")


if __name__ == "__main__":
    main()
