#!/usr/bin/env python3
"""Exact official-row private-linear h=3 bridge-budget compiler."""

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
    Row(30, 1_202, 17_172_947_561, 366_234, 3_251, 732_764, 17_190_093_206, 366_088, 3_253, 733_093, 4_871),
    Row(31, 1_514, 34_335_631_981, 582_371, 4_092, 1_162_148, 34_362_837_967, 581_902, 4_095, 1_162_847, 6_142),
    Row(32, 1_908, 68_694_037_411, 923_874, 5_158, 1_845_600, 68_737_242_787, 922_926, 5_162, 1_846_838, 7_737),
    Row(33, 2_404, 137_396_223_112, 1_464_709, 6_503, 2_931_688, 137_464_810_366, 1_464_868, 6_504, 2_931_895, 9_758),
    Row(34, 3_029, 274_813_976_903, 2_328_261, 8_188, 4_650_786, 274_922_854_180, 2_328_461, 8_189, 4_651_047, 12_293),
    Row(35, 3_816, 549_584_202_033, 3_692_989, 10_320, 7_385_550, 549_757_030_110, 3_693_957, 10_320, 7_385_163, 15_490),
    Row(36, 4_809, 1_099_494_671_630, 5_864_111, 13_002, 11_723_020, 1_099_769_021_910, 5_863_526, 13_004, 11_724_336, 19_506),
    Row(37, 6_058, 2_198_592_015_702, 9_306_792, 16_382, 18_610_418, 2_199_027_504_610, 9_306_056, 16_384, 18_612_076, 24_584),
    Row(38, 7_633, 4_397_492_580_239, 14_773_175, 20_641, 29_543_431, 4_398_183_970_702, 14_769_386, 20_645, 29_548_382, 30_970),
    Row(39, 9_617, 8_795_062_707_928, 23_447_692, 26_008, 46_900_991, 8_796_160_167_298, 23_448_327, 26_009, 46_901_819, 39_019),
    Row(40, 12_117, 17_590_800_118_865, 37_229_105, 32_765, 74_443_625, 17_592_542_302_047, 37_232_177, 32_765, 74_442_396, 49_158),
    Row(41, 15_267, 35_183_217_144_062, 59_092_277, 41_284, 118_179_047, 35_185_982_564_334, 59_096_148, 41_284, 118_177_499, 61_931),
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
    print("h=3 private-linear official-row bridge-budget compiler")
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

    print("maximality check: Z_private passes and Z_private+1 fails for s=13..41")
    print("conditional track: private-linear rank theorem + bridge => official-row H3-ACT(16)")
    print("H3_PRIVATE_LINEAR_LOWROW_BUDGET_PASS")


if __name__ == "__main__":
    main()
