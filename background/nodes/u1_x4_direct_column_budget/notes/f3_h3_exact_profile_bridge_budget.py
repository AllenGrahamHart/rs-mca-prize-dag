#!/usr/bin/env python3
"""Exact-profile h=3 bridge-budget lift.

This compiler reuses the non-diagonal box search, but replaces the legacy
condition count 13D(A+D)|Z| by the proved exact profile
|Z|*(DA+6D(D-1)).
"""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_nondiagonal_highrow_budget import EXPECTED_ROWS as HIGH_ROWS
from f3_h3_nondiagonal_lowrow_budget import EXPECTED_ROWS as LOW_ROWS
from f3_h3_rich_curve_condition_profile import exact_conditions_per_curve


H3_ACT_C = 16


@dataclass(frozen=True)
class ExactProfileRow:
    s: int
    old_z: int
    z: int
    bound: int
    a: int
    b: int
    d: int
    next_b_cap: int


EXPECTED_ROWS = (
    ExactProfileRow(13, 16, 33, 127_856, 1_362, 34, 419, 51),
    ExactProfileRow(14, 21, 42, 260_014, 1_991, 45, 699, 64),
    ExactProfileRow(15, 26, 53, 522_118, 3_263, 56, 1_098, 80),
    ExactProfileRow(16, 33, 66, 1_032_147, 5_530, 68, 1_685, 104),
    ExactProfileRow(17, 42, 84, 2_092_785, 8_628, 87, 2_715, 130),
    ExactProfileRow(18, 53, 105, 4_151_731, 13_282, 111, 4_376, 166),
    ExactProfileRow(19, 67, 133, 8_366_839, 20_602, 142, 7_051, 208),
    ExactProfileRow(20, 84, 167, 16_679_342, 32_973, 178, 11_150, 265),
    ExactProfileRow(21, 106, 211, 33_493_578, 53_149, 223, 17_598, 332),
    ExactProfileRow(22, 134, 266, 67_071_247, 84_477, 281, 27_946, 419),
    ExactProfileRow(23, 168, 335, 134_135_939, 134_168, 354, 44_373, 529),
    ExactProfileRow(24, 212, 422, 268_309_374, 212_126, 447, 70_613, 667),
    ExactProfileRow(25, 267, 531, 535_935_052, 336_672, 563, 112_104, 844),
    ExactProfileRow(26, 337, 669, 1_072_073_349, 536_632, 708, 177_645, 1_064),
    ExactProfileRow(27, 425, 843, 2_144_862_085, 848_453, 894, 282_645, 1_340),
    ExactProfileRow(28, 535, 1_063, 4_294_617_361, 1_349_155, 1_126, 448_490, 1_687),
    ExactProfileRow(29, 674, 1_339, 8_587_903_250, 2_140_575, 1_419, 712_182, 2_127),
    ExactProfileRow(30, 850, 1_687, 17_176_879_129, 3_397_726, 1_788, 1_130_698, 2_680),
    ExactProfileRow(31, 1_071, 2_125, 34_346_701_308, 5_391_688, 2_253, 1_795_244, 3_379),
    ExactProfileRow(32, 1_349, 2_678, 68_717_736_734, 8_559_293, 2_839, 2_850_134, 4_256),
    ExactProfileRow(33, 1_700, 3_374, 137_438_113_071, 13_587_103, 3_577, 4_524_562, 5_363),
    ExactProfileRow(34, 2_142, 4_250, 274_810_201_255, 21_571_545, 4_506, 7_181_613, 6_761),
    ExactProfileRow(35, 2_699, 5_355, 549_676_804_604, 34_224_754, 5_679, 11_403_773, 8_518),
    ExactProfileRow(36, 3_400, 6_747, 1_099_401_566_936, 54_317_583, 7_156, 18_104_857, 10_732),
    ExactProfileRow(37, 4_284, 8_501, 2_198_938_206_056, 86_229_353, 9_016, 28_739_805, 13_521),
    ExactProfileRow(38, 5_397, 10_710, 4_397_646_668_084, 136_862_876, 11_360, 45_624_732, 17_038),
    ExactProfileRow(39, 6_800, 13_494, 8_795_581_212_490, 217_285_521, 14_312, 72_421_452, 21_467),
    ExactProfileRow(40, 8_568, 17_002, 17_592_091_071_295, 344_898_289, 18_033, 114_968_145, 27_045),
    ExactProfileRow(41, 10_795, 21_421, 35_184_073_533_562, 547_452_969, 22_721, 182_508_469, 34_076),
)


def ceil_div(num: int, den: int) -> int:
    return -(-num // den)


def minimal_a(z: int, b: int, d: int) -> int | None:
    denominator = b**3 - z * d
    if denominator <= 0:
        return None
    return (6 * z * d * (d - 1)) // denominator + 1


def witness_bound(n: int, z: int, a: int, b: int, d: int) -> tuple[int, int, int, int]:
    conditions = exact_conditions_per_curve(a, d) * z
    coeffs = a * b**3
    degree = (a - 1) + 6 * n * (b - 1)
    image_cap = z * (degree + 1)
    if not (conditions < coeffs and conditions < image_cap):
        raise AssertionError((n, z, a, b, d, conditions, coeffs, image_cap))
    return ceil_div(z * degree, d), conditions, coeffs, image_cap


def feasible_witness(n: int, z: int, b: int, d: int) -> tuple[int, int, int, int] | None:
    a = minimal_a(z, b, d)
    if a is None:
        return None
    try:
        bound, *_ = witness_bound(n, z, a, b, d)
    except AssertionError:
        return None
    return bound, a, b, d


def image_cap_min_a(n: int, b: int) -> int:
    """Largest D not ruled out by the image inequality with A=1."""

    def ok(d: int) -> bool:
        return (d - 1) * (1 + 6 * d) < 6 * n * (b - 1)

    hi = 2
    while ok(hi):
        hi *= 2
    lo = 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            lo = mid
        else:
            hi = mid
    return lo


def b_cap_for_possible_pass(n: int, z: int) -> int:
    """Safe B cap for any box that could beat H3_ACT_C*n.

    If a box has bound <=16n, then D >= ceil(3Z(B-1)/8).  The image
    inequality and A>=1 imply D(D-1) < n(B-1).  When this necessary condition
    fails at the lower-bound D, no larger D can pass.
    """

    def possible_b(b: int) -> bool:
        d_low = ceil_div(3 * z * (b - 1), 8)
        return d_low * (d_low - 1) < n * (b - 1)

    hi = 4
    while possible_b(hi):
        hi *= 2
    lo = 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if possible_b(mid):
            lo = mid
        else:
            hi = mid
    return lo


def best_exact_profile_bound(n: int, z: int) -> tuple[tuple[int, int, int, int] | None, int]:
    b_cap = b_cap_for_possible_pass(n, z)
    best: tuple[int, int, int, int] | None = None
    for b in range(2, b_cap + 1):
        d_low = ceil_div(3 * z * (b - 1), 8)
        d_high = min((b**3 - 1) // z, image_cap_min_a(n, b))
        if d_high < d_low:
            continue

        lo = d_low - 1
        hi = d_high + 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if feasible_witness(n, z, b, mid) is not None:
                lo = mid
            else:
                hi = mid
        if lo < d_low:
            continue
        witness = feasible_witness(n, z, b, lo)
        if witness is None:
            continue
        if best is None or witness < best:
            best = witness
    return best, b_cap


def exact_profile_budget_summary() -> dict[str, int]:
    legacy_rows = (*LOW_ROWS, *HIGH_ROWS)
    if [row.s for row in legacy_rows] != [row.s for row in EXPECTED_ROWS]:
        raise AssertionError("official exponent drift")
    if [row.z for row in legacy_rows] != [row.old_z for row in EXPECTED_ROWS]:
        raise AssertionError("legacy non-diagonal budget drift")

    exact_total = 0
    old_total = 0
    for row in EXPECTED_ROWS:
        n = 2**row.s
        target = H3_ACT_C * n
        bound, *_ = witness_bound(n, row.z, row.a, row.b, row.d)
        if bound != row.bound or bound > target:
            raise AssertionError((row, bound, target))
        best, _ = best_exact_profile_bound(n, row.z)
        expected = (row.bound, row.a, row.b, row.d)
        if best != expected:
            raise AssertionError((row.s, best, expected))
        next_best, next_b_cap = best_exact_profile_bound(n, row.z + 1)
        if next_best is not None:
            raise AssertionError((row.s, row.z + 1, next_best))
        if next_b_cap != row.next_b_cap:
            raise AssertionError((row.s, next_b_cap, row.next_b_cap))
        exact_total += row.z
        old_total += row.old_z
    return {
        "rows": len(EXPECTED_ROWS),
        "first_s": EXPECTED_ROWS[0].s,
        "last_s": EXPECTED_ROWS[-1].s,
        "old_min": min(row.old_z for row in EXPECTED_ROWS),
        "old_max": max(row.old_z for row in EXPECTED_ROWS),
        "exact_min": min(row.z for row in EXPECTED_ROWS),
        "exact_max": max(row.z for row in EXPECTED_ROWS),
        "old_total": old_total,
        "exact_total": exact_total,
        "gain_min": min(row.z - row.old_z for row in EXPECTED_ROWS),
        "gain_max": max(row.z - row.old_z for row in EXPECTED_ROWS),
        "gain_total": exact_total - old_total,
    }


def main() -> None:
    print("h=3 exact-profile bridge-budget compiler")
    print("conditions = |Z|*(DA + 6D(D-1)); target bound <= 16n")
    print(" s          n   old_Z exact_Z          bound            16n       A      B          D  next_B_cap")
    for row in EXPECTED_ROWS:
        n = 2**row.s
        target = H3_ACT_C * n
        bound, conditions, coeffs, image_cap = witness_bound(n, row.z, row.a, row.b, row.d)
        if bound != row.bound or bound > target:
            raise AssertionError((row, bound, target))
        next_best, next_b_cap = best_exact_profile_bound(n, row.z + 1)
        if next_best is not None or next_b_cap != row.next_b_cap:
            raise AssertionError((row.s, next_best, next_b_cap, row.next_b_cap))
        print(
            f"{row.s:2d} {n:10d} {row.old_z:7d} {row.z:7d}"
            f" {row.bound:14d} {target:14d}"
            f" {row.a:7d} {row.b:6d} {row.d:10d} {row.next_b_cap:11d}"
        )
        if not (conditions < coeffs and conditions < image_cap):
            raise AssertionError((row.s, conditions, coeffs, image_cap))

    summary = exact_profile_budget_summary()
    print(
        "summary: "
        f"rows={summary['rows']} "
        f"exact_Z={summary['exact_min']}..{summary['exact_max']} "
        f"old_Z={summary['old_min']}..{summary['old_max']} "
        f"total_gain={summary['gain_total']} "
        f"gain_range={summary['gain_min']}..{summary['gain_max']}"
    )
    print("maximality check: exact_Z passes and exact_Z+1 has no feasible box under the analytic B cap")
    print("H3_EXACT_PROFILE_BRIDGE_BUDGET_PASS")


if __name__ == "__main__":
    main()
