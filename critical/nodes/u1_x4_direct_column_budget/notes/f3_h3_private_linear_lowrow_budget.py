#!/usr/bin/env python3
"""Exact low-row private-linear h=3 bridge-budget compiler."""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt


C_RED = 13
H3_ACT_C = 16
DEGREE_FACTOR = 3


@dataclass(frozen=True)
class Row:
    s: int
    z: int
    bound: int
    a: int
    b: int
    d: int
    next_bound: int
    next_a: int
    next_b: int
    next_d: int
    next_b_cap: int


EXPECTED_ROWS = (
    Row(13, 23, 125_622, 132, 65, 288, 132_251, 142, 64, 281, 94),
    Row(14, 29, 251_932, 220, 80, 447, 262_159, 222, 81, 450, 120),
    Row(15, 37, 512_086, 375, 98, 689, 528_998, 385, 98, 685, 149),
    Row(16, 47, 1_035_036, 578, 126, 1_116, 1_061_500, 563, 129, 1_138, 187),
    Row(17, 59, 2_062_810, 912, 159, 1_777, 2_105_127, 916, 160, 1_782, 239),
)


def private_degree(n: int, a: int, b: int) -> int:
    return (a - 1) + DEGREE_FACTOR * n * (b - 1)


def minimal_a(z: int, b: int, d: int) -> int | None:
    denominator = b**3 - C_RED * d * z
    if denominator <= 0:
        return None
    return (C_RED * d * d * z) // denominator + 1


def feasible_witness(
    n: int, z: int, b: int, d: int
) -> tuple[int, int, int, int] | None:
    a = minimal_a(z, b, d)
    if a is None:
        return None
    conditions = C_RED * d * (a + d) * z
    coeffs = a * b**3
    degree = private_degree(n, a, b)
    image_cap = z * (degree + 1)
    if conditions < coeffs and conditions < image_cap:
        bound = (z * degree + d - 1) // d
        return bound, a, b, d
    return None


def best_private_bound(n: int, z: int, b_cap: int) -> tuple[int, int, int, int]:
    best: tuple[int, int, int, int] | None = None
    for b in range(2, b_cap + 1):
        coeff_cap = (b**3 - 1) // (C_RED * z)
        image_cap = isqrt(max(0, (DEGREE_FACTOR * n * (b - 1) - 1) // C_RED))
        hi = min(coeff_cap, image_cap)
        if hi < 1:
            continue

        lo = 0
        upper = hi + 1
        while lo + 1 < upper:
            mid = (lo + upper) // 2
            if feasible_witness(n, z, b, mid) is not None:
                lo = mid
            else:
                upper = mid

        for d in range(max(1, lo - 4), min(hi, lo + 4) + 1):
            witness = feasible_witness(n, z, b, d)
            if witness is not None and (best is None or witness < best):
                best = witness

    if best is None:
        raise AssertionError(("no private-linear box", n, z, b_cap))
    return best


def main() -> None:
    print("h=3 private-linear low-row bridge-budget compiler")
    print(f"C_red={C_RED} H3_ACT_C={H3_ACT_C} degree_factor={DEGREE_FACTOR}")
    print(" s      n   Z_private       bound        16n    next_bound  next_B_cap")
    for row in EXPECTED_ROWS:
        n = 2**row.s
        target = H3_ACT_C * n

        passing = feasible_witness(n, row.z, row.b, row.d)
        expected_passing = (row.bound, row.a, row.b, row.d)
        if passing != expected_passing:
            raise AssertionError((row.s, passing, expected_passing))
        if row.bound > target:
            raise AssertionError((row.s, row.bound, target))

        next_witness = best_private_bound(n, row.z + 1, row.next_b_cap)
        expected_next = (row.next_bound, row.next_a, row.next_b, row.next_d)
        if next_witness != expected_next:
            raise AssertionError((row.s, next_witness, expected_next))
        if row.next_bound <= target:
            raise AssertionError((row.s, row.next_bound, target))

        print(
            f"{row.s:2d} {n:8d} {row.z:11d} {row.bound:11d} "
            f"{target:10d} {row.next_bound:13d} {row.next_b_cap:11d}"
        )

    print("maximality check: Z_private passes and Z_private+1 fails for s=13..17")
    print("conditional track: private-linear rank theorem + bridge => low-row H3-ACT(16)")
    print("H3_PRIVATE_LINEAR_LOWROW_BUDGET_PASS")


if __name__ == "__main__":
    main()
