#!/usr/bin/env python3
"""Arithmetic audit for the h=3 rich-curve nonvanishing/rank target."""

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
    one_curve_degree: int
    image_cap: int
    kernel_lower: int
    image_room: int


def make_row(h: int, z: int, a: int, b: int, d: int) -> Row:
    coeffs = a * b**3
    conditions = C_RED * d * (a + d) * z
    one_curve_degree = (a - 1) + 6 * h * (b - 1)
    image_cap = z * (one_curve_degree + 1)
    kernel_lower = max(0, coeffs - image_cap)
    image_room = image_cap - conditions
    if conditions >= coeffs:
        raise AssertionError(("linear-system failure", h, z, a, b, d))
    if image_room <= 0:
        raise AssertionError(("no rank room", h, z, a, b, d, image_cap, conditions))
    return Row(
        h=h,
        z=z,
        a=a,
        b=b,
        d=d,
        coeffs=coeffs,
        conditions=conditions,
        one_curve_degree=one_curve_degree,
        image_cap=image_cap,
        kernel_lower=kernel_lower,
        image_room=image_room,
    )


def main() -> None:
    rows = [
        make_row(h=2**13, z=1, a=512, b=16, d=16),
        make_row(h=2**13, z=8, a=512, b=32, d=16),
        make_row(h=2**16, z=16, a=2048, b=64, d=32),
        make_row(h=2**20, z=32, a=8192, b=128, d=64),
        make_row(h=2**23, z=64, a=32768, b=256, d=128),
    ]

    impossible_injective = [row for row in rows if row.kernel_lower > 0]
    if len(impossible_injective) != 3:
        raise AssertionError(("unexpected injectivity profile", impossible_injective))

    print("h=3 rich-curve nonvanishing rank audit")
    print(f"C_red = {C_RED}")
    print(
        " h        |Z|      A     B    D        coeffs       conditions"
        "        image_cap     ker_lower       rank_room"
    )
    for row in rows:
        print(
            f"{row.h:9d} {row.z:6d} {row.a:6d} {row.b:5d} {row.d:4d}"
            f" {row.coeffs:13d} {row.conditions:16d}"
            f" {row.image_cap:16d} {row.kernel_lower:13d}"
            f" {row.image_room:15d}"
        )

    print("full substitution injectivity is impossible in the first three rows")
    print("sufficient rank target: rank(substitution to Z curves) > conditions")
    print("all audited rows have positive image-cap room above the condition count")
    print("H3_RICH_CURVE_NV_RANK_AUDIT_PASS")


if __name__ == "__main__":
    main()
