#!/usr/bin/env python3
"""Non-diagonal h=3 bridge-budget lift for low/mid official rows."""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt


C_RED = 13
H3_ACT_C = 16
B_MAX = 50_000


@dataclass(frozen=True)
class Row:
    s: int
    old_z: int
    z: int
    bound: int
    a: int
    b: int
    d: int
    next_bound: int
    next_a: int
    next_b: int
    next_d: int


EXPECTED_ROWS = (
    Row(13, 11, 16, 123_137, 195, 63, 396, 132_401, 214, 62, 385),
    Row(14, 14, 21, 259_244, 296, 83, 653, 274_061, 303, 84, 655),
    Row(15, 18, 26, 508_053, 527, 98, 976, 531_877, 477, 105, 1_038),
    Row(16, 23, 33, 1_026_191, 824, 125, 1_568, 1_063_869, 809, 128, 1_596),
    Row(17, 29, 42, 2_079_745, 1_251, 162, 2_557, 2_139_141, 1_265, 163, 2_561),
    Row(18, 36, 53, 4_170_160, 1_974, 205, 4_078, 4_264_529, 2_011, 205, 4_063),
    Row(19, 46, 67, 8_378_221, 3_179, 257, 6_440, 8_528_431, 3_226, 257, 6_421),
    Row(20, 58, 84, 16_665_312, 5_145, 320, 10_116, 16_903_661, 5_110, 323, 10_187),
    Row(21, 73, 106, 33_406_481, 8_032, 407, 16_210, 33_785_625, 8_029, 409, 16_259),
    Row(22, 92, 134, 67_102_386, 12_889, 511, 25_630, 67_704_006, 12_935, 512, 25_642),
    Row(23, 116, 168, 133_444_877, 20_294, 645, 40_807, 134_399_623, 20_477, 644, 40_695),
    Row(24, 146, 212, 267_445_392, 32_247, 813, 64_793, 268_958_977, 32_320, 814, 64_812),
    Row(25, 184, 267, 534_721_741, 51_515, 1_021, 102_538, 537_126_791, 51_306, 1_025, 102_863),
    Row(26, 232, 337, 1_071_865_237, 81_605, 1_289, 163_056, 1_075_682_598, 81_721, 1_290, 163_086),
    Row(27, 292, 425, 2_146_397_498, 129_532, 1_625, 258_956, 2_152_461_918, 129_837, 1_625, 258_834),
    Row(28, 368, 535, 4_288_634_358, 205_741, 2_046, 410_884, 4_298_256_663, 205_523, 2_049, 411_333),
    Row(29, 463, 674, 8_576_904_803, 327_055, 2_576, 651_820, 8_592_176_604, 326_779, 2_579, 652_386),
    Row(30, 584, 850, 17_174_343_107, 518_286, 3_250, 1_035_952, 17_198_591_653, 518_258, 3_252, 1_036_346),
    Row(31, 736, 1_071, 34_352_567_550, 822_729, 4_095, 1_644_596, 34_391_068_221, 822_693, 4_097, 1_645_092),
    Row(32, 927, 1_349, 68_684_283_285, 1_306_907, 5_157, 2_609_628, 68_745_394_540, 1_307_368, 5_158, 2_609_747),
    Row(33, 1_168, 1_700, 137_407_385_857, 2_072_826, 6_501, 4_144_702, 137_504_389_373, 2_073_408, 6_502, 4_144_852),
    Row(34, 1_472, 2_142, 274_840_663_040, 3_290_514, 8_191, 6_579_509, 274_994_647_714, 3_291_246, 8_192, 6_579_698),
    Row(35, 1_855, 2_699, 549_750_537_835, 5_225_005, 10_319, 10_443_206, 549_994_990_701, 5_225_927, 10_320, 10_443_444),
)


def witness_bound(n: int, z: int, a: int, b: int, d: int) -> tuple[int, int, int, int]:
    conditions = C_RED * d * (a + d) * z
    coeffs = a * b**3
    degree = (a - 1) + 6 * n * (b - 1)
    image_cap = z * (degree + 1)
    if not (conditions < coeffs and conditions < image_cap):
        raise AssertionError((n, z, a, b, d, conditions, coeffs, image_cap))
    bound = (z * degree + d - 1) // d
    return bound, conditions, coeffs, image_cap


def minimal_a(n: int, z: int, b: int, d: int) -> int | None:
    del n
    denominator = b**3 - C_RED * d * z
    if denominator <= 0:
        return None
    return (C_RED * d * d * z) // denominator + 1


def feasible_witness(n: int, z: int, b: int, d: int) -> tuple[int, int, int, int, int, int, int] | None:
    a = minimal_a(n, z, b, d)
    if a is None:
        return None
    conditions = C_RED * d * (a + d) * z
    coeffs = a * b**3
    degree = (a - 1) + 6 * n * (b - 1)
    image_cap = z * (degree + 1)
    if conditions < coeffs and conditions < image_cap:
        bound = (z * degree + d - 1) // d
        return bound, a, b, d, degree, conditions, image_cap
    return None


def best_nondiagonal_bound(n: int, z: int, b_max: int = B_MAX) -> tuple[int, int, int, int]:
    best: tuple[int, int, int, int] | None = None
    for b in range(2, b_max + 1):
        coeff_cap = (b**3 - 1) // (C_RED * z)
        image_cap = isqrt(max(0, (6 * n * (b - 1) - 1) // C_RED))
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
            if witness is None:
                continue
            bound, a, got_b, got_d, *_ = witness
            row = (bound, a, got_b, got_d)
            if best is None or row < best:
                best = row

    if best is None:
        raise AssertionError(("no admissible non-diagonal box", n, z))
    return best


def next_failure_b_cap(n: int, z: int) -> int:
    """Return an exact B cap for any box that could beat the H3_ACT_C*n target."""
    target = H3_ACT_C * n
    lo = 0
    hi = target // (C_RED * z) + 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if C_RED * mid * (mid + 1) * z < target * mid + z:
            lo = mid
        else:
            hi = mid
    return (target * lo) // (6 * n * z) + 1


def main() -> None:
    print("h=3 non-diagonal low/mid-row bridge-budget lift")
    print(f"C_red={C_RED} H3_ACT_C={H3_ACT_C} default_B_max={B_MAX}")
    print(" s      n       old_Z   new_Z       bound          16n     next_bound    A     B      D  next_B_cap")
    for row in EXPECTED_ROWS:
        n = 2**row.s
        target = H3_ACT_C * n
        got_bound, *_ = witness_bound(n, row.z, row.a, row.b, row.d)
        if got_bound != row.bound:
            raise AssertionError((row.s, got_bound, row.bound))
        if got_bound > target:
            raise AssertionError((row.s, "passing witness exceeds target", got_bound, target))

        b_cap = next_failure_b_cap(n, row.z + 1)
        next_bound, next_a, next_b, next_d = best_nondiagonal_bound(n, row.z + 1, b_cap)
        got_next = (next_bound, next_a, next_b, next_d)
        expected_next = (row.next_bound, row.next_a, row.next_b, row.next_d)
        if got_next != expected_next:
            raise AssertionError((row.s, got_next, expected_next))
        if next_b > b_cap:
            raise AssertionError((row.s, "next witness outside analytic B cap", next_b, b_cap))
        if next_bound <= target:
            raise AssertionError((row.s, "next budget passes", next_bound, target))

        print(
            f"{row.s:2d} {n:8d} {row.old_z:10d} {row.z:7d}"
            f" {row.bound:11d} {target:12d} {row.next_bound:14d}"
            f" {row.a:5d} {row.b:5d} {row.d:6d} {b_cap:11d}"
        )

    print("maximality check: new_Z passes and new_Z+1 fails for s=13..35")
    print("the Z+1 failure scan reaches the exact analytic B cap for any possible pass")
    print("conditional conclusion: non-diagonal boxes enlarge the low/mid-row H3-BRIDGE budgets")
    print("H3_NONDIAGONAL_LOWROW_BUDGET_PASS")


if __name__ == "__main__":
    main()
