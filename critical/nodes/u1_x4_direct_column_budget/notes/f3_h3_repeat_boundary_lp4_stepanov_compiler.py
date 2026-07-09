#!/usr/bin/env python3
"""Arithmetic checks for the repeat-boundary LP4 Stepanov compiler."""

from __future__ import annotations

from dataclasses import dataclass


C_RED = 5


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
    ls_slack: int
    image_slack: int


def row(h: int, z: int, a: int, b: int, d: int, c_red: int = C_RED) -> Row:
    if min(h, z, a, b, d, c_red) < 1:
        raise ValueError((h, z, a, b, d, c_red))
    coeffs = a * b**4
    conditions = c_red * d * (a + d) * z
    degree = (a - 1) + 4 * h * (b - 1)
    image_cap = z * (degree + 1)
    if conditions >= coeffs:
        raise AssertionError(("LP4-LS fails", h, z, a, b, d, coeffs, conditions))
    if conditions >= image_cap:
        raise AssertionError(("LP4 image-cap fails", h, z, a, b, d, image_cap))
    return Row(
        h=h,
        z=z,
        a=a,
        b=b,
        d=d,
        coeffs=coeffs,
        conditions=conditions,
        degree=degree,
        ls_slack=coeffs - conditions,
        image_slack=image_cap - conditions,
    )


def ceil_div(num: int, den: int) -> int:
    return -(-num // den)


def main() -> None:
    rows = [
        row(h=2**13, z=1, a=256, b=16, d=16),
        row(h=2**13, z=64, a=1024, b=32, d=16),
        row(h=2**16, z=128, a=4096, b=64, d=32),
        row(h=2**23, z=256, a=16384, b=128, d=64),
        row(h=2**32, z=512, a=65536, b=256, d=128),
    ]

    print("h=3 repeat-boundary LP4 Stepanov compiler")
    print(f"C_red = {C_RED}")
    print(" h        |R|      A     B    D        LS_slack     image_slack   ceil(|R|*L/D)")
    for item in rows:
        expected_degree = (item.a - 1) + 4 * item.h * (item.b - 1)
        if item.degree != expected_degree:
            raise AssertionError((item, expected_degree))
        bound = ceil_div(item.z * item.degree, item.d)
        print(
            f"{item.h:9d} {item.z:6d} {item.a:6d} {item.b:5d} {item.d:4d}"
            f" {item.ls_slack:15d} {item.image_slack:15d} {bound:18d}"
        )
    print("LP4-RED supplied; remaining gate: LP4-RANK/LP4-NV")
    print("H3_REPEAT_BOUNDARY_LP4_STEPANOV_COMPILER_PASS")


if __name__ == "__main__":
    main()
