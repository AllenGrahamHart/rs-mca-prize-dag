#!/usr/bin/env python3
"""Exact low/mid-row private-linear h=3 bridge-budget compiler."""

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
    Row(18, 75, 4_173_028, 1_439, 202, 2_841, 4_240_468, 1_472, 201, 2_819, 298),
    Row(19, 94, 8_298_869, 2_247, 256, 4_543, 8_404_213, 2_289, 255, 4_516, 382),
    Row(20, 119, 16_700_092, 3_622, 321, 7_173, 16_868_649, 3_652, 321, 7_161, 478),
    Row(21, 150, 33_431_732, 5_768, 404, 11_376, 33_699_610, 5_778, 405, 11_389, 604),
    Row(22, 189, 66_887_366, 9_090, 511, 18_133, 67_313_595, 9_174, 510, 18_078, 763),
    Row(23, 238, 133_723_269, 14_419, 644, 28_800, 134_397_130, 14_480, 644, 28_776, 964),
    Row(24, 300, 267_645_521, 22_929, 811, 45_697, 268_716_310, 22_949, 812, 45_723, 1_216),
    Row(25, 378, 535_409_905, 36_253, 1_024, 72_703, 537_113_560, 36_634, 1_020, 72_380, 1_534),
    Row(26, 477, 1_072_973_600, 57_933, 1_287, 115_099, 1_075_674_599, 57_606, 1_292, 115_498, 1_928),
    Row(27, 601, 2_146_226_110, 91_699, 1_624, 182_999, 2_150_510_707, 91_739, 1_625, 183_051, 2_432),
    Row(28, 757, 4_291_331_796, 145_842, 2_044, 290_224, 4_298_141_013, 146_035, 2_044, 290_147, 3_067),
    Row(29, 954, 8_585_758_442, 230_566, 2_581, 461_722, 8_596_562_775, 230_629, 2_582, 461_804, 3_865),
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
    print("h=3 private-linear low/mid-row bridge-budget compiler")
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

    print("maximality check: Z_private passes and Z_private+1 fails for s=13..29")
    print("conditional track: private-linear rank theorem + bridge => low/mid-row H3-ACT(16)")
    print("H3_PRIVATE_LINEAR_LOWROW_BUDGET_PASS")


if __name__ == "__main__":
    main()
