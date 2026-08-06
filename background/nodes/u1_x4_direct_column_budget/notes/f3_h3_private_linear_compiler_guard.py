#!/usr/bin/env python3
"""Guardrail for using private-linear rank in the h=3 compiler."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_nondiagonal_highrow_budget import EXPECTED_ROWS as HIGH_ROWS
from f3_h3_nondiagonal_lowrow_budget import C_RED, H3_ACT_C
from f3_h3_nondiagonal_lowrow_budget import EXPECTED_ROWS as LOW_ROWS


@dataclass(frozen=True)
class PrivateWitness:
    s: int
    z: int
    bound: int
    a: int
    b: int
    d: int


PRIVATE_WITNESSES = (
    PrivateWitness(13, 23, 125_622, 132, 65, 288),
    PrivateWitness(16, 47, 1_035_036, 578, 126, 1_116),
    PrivateWitness(20, 119, 16_700_092, 3_622, 321, 7_173),
    PrivateWitness(23, 238, 133_723_269, 14_419, 644, 28_800),
    PrivateWitness(32, 1_908, 68_694_037_411, 923_874, 5_158, 1_845_600),
    PrivateWitness(41, 11_563, 35_183_058_376_390, 190_695_246, 20_000, 43_360_701),
)


def private_degree(a: int, b: int, n: int) -> int:
    return (a - 1) + 3 * n * (b - 1)


def general_degree(a: int, b: int, n: int) -> int:
    return (a - 1) + 6 * n * (b - 1)


def verify_witness(w: PrivateWitness) -> tuple[int, int, int, int]:
    n = 2**w.s
    target = H3_ACT_C * n
    degree = private_degree(w.a, w.b, n)
    conditions = C_RED * w.d * (w.a + w.d) * w.z
    coeffs = w.a * w.b**3
    image_cap = w.z * (degree + 1)
    bound = (w.z * degree + w.d - 1) // w.d
    if bound != w.bound:
        raise AssertionError((w, bound))
    if not (conditions < coeffs and conditions < image_cap):
        raise AssertionError((w, conditions, coeffs, image_cap))
    if bound > target:
        raise AssertionError((w, bound, target))
    return bound, conditions, coeffs, image_cap


def main() -> None:
    rows = (*LOW_ROWS, *HIGH_ROWS)
    failing_current = []
    for row in rows:
        n = 2**row.s
        per_curve_conditions = C_RED * row.d * (row.a + row.d)
        private_dim = min(row.a * row.b**3, private_degree(row.a, row.b, n) + 1)
        general_dim = min(row.a * row.b**3, general_degree(row.a, row.b, n) + 1)
        if private_dim > per_curve_conditions:
            raise AssertionError(("current witness unexpectedly private-linear safe", row.s))
        if general_dim <= per_curve_conditions:
            raise AssertionError(("current witness lacks general degree-2 room", row.s))
        failing_current.append(row.s)

    print("h=3 private-linear compiler guard")
    print("current non-diagonal witnesses needing degree-2 rank room:", failing_current)
    print("representative private-linear retuned witnesses:")
    for witness in PRIVATE_WITNESSES:
        bound, conditions, coeffs, image_cap = verify_witness(witness)
        print(
            f"s={witness.s:2d} Z={witness.z:5d} bound={bound:14d} "
            f"A={witness.a:9d} B={witness.b:6d} D={witness.d:9d} "
            f"conditions={conditions}"
        )

    print("current h=3 bridge boxes cannot be justified by private-linear degree rank")
    print("private-linear rank may still support a separately retuned compiler")
    print("H3_PRIVATE_LINEAR_COMPILER_GUARD_PASS")


if __name__ == "__main__":
    main()
