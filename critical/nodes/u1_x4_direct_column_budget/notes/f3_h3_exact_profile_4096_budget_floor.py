#!/usr/bin/env python3
"""Constructive h=3 exact-profile budget floor for H3-ACT(4096)."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_exact_profile_bridge_budget import (
    EXPECTED_ROWS as C16_ROWS,
    witness_bound,
)


TARGET_C = 4096
BUDGET_MULTIPLIER = 64


@dataclass(frozen=True)
class RetargetRow:
    s: int
    old_z: int
    z: int
    bound: int
    a: int
    b: int
    d: int


EXPECTED_ROWS = (
    RetargetRow(13, 33, 2_112, 19_066_845, 2_953, 187, 1_013),
    RetargetRow(14, 42, 2_688, 38_625_230, 4_725, 236, 1_608),
    RetargetRow(15, 53, 3_392, 77_433_909, 7_587, 296, 2_541),
    RetargetRow(16, 66, 4_224, 152_776_567, 12_100, 370, 4_012),
    RetargetRow(17, 84, 5_376, 309_387_879, 19_263, 468, 6_382),
    RetargetRow(18, 105, 6_720, 613_101_515, 30_519, 588, 10_120),
    RetargetRow(19, 133, 8_512, 1_234_353_127, 48_309, 744, 16_118),
    RetargetRow(20, 167, 10_688, 2_459_054_321, 76_672, 936, 25_568),
    RetargetRow(21, 211, 13_504, 4_935_431_085, 121_723, 1_181, 40_626),
    RetargetRow(22, 266, 17_024, 9_878_849_856, 194_146, 1_485, 64_358),
    RetargetRow(23, 335, 21_440, 19_749_524_842, 306_457, 1_876, 102_450),
    RetargetRow(24, 422, 27_008, 39_493_374_274, 487_103, 2_362, 162_531),
    RetargetRow(25, 531, 33_984, 78_868_533_766, 774_340, 2_972, 257_736),
    RetargetRow(26, 669, 42_816, 157_738_488_600, 1_226_937, 3_748, 409_528),
    RetargetRow(27, 843, 53_952, 315_538_108_806, 1_952_293, 4_717, 649_368),
    RetargetRow(28, 1_063, 68_032, 631_724_865_994, 3_097_673, 5_947, 1_031_339),
    RetargetRow(29, 1_339, 85_696, 1_263_140_911_149, 4_916_005, 7_493, 1_637_298),
    RetargetRow(30, 1_687, 107_968, 2_526_262_150_192, 7_806_354, 9_439, 2_598_650),
    RetargetRow(31, 2_125, 136_000, 5_051_201_900_712, 12_373_416, 11_900, 4_127_963),
    RetargetRow(32, 2_678, 171_392, 10_105_532_033_183, 19_654_837, 14_990, 6_551_114),
    RetargetRow(33, 3_374, 215_936, 20_210_738_692_116, 31_190_709, 18_889, 10_400_877),
    RetargetRow(34, 4_250, 272_000, 40_410_632_667_140, 49_516_546, 23_795, 16_508_660),
    RetargetRow(35, 5_355, 342_720, 80_827_763_560_173, 78_628_266, 29_976, 26_202_286),
    RetargetRow(36, 6_747, 431_808, 161_659_723_689_082, 124_787_281, 37_772, 41_598_573),
    RetargetRow(37, 8_501, 544_064, 323_334_778_588_168, 198_085_322, 47_591, 66_035_028),
    RetargetRow(38, 10_710, 685_440, 646_628_577_599_259, 314_465_856, 59_957, 104_818_584),
    RetargetRow(39, 13_494, 863_616, 1_293_288_064_666_246, 499_168_943, 75_543, 166_392_969),
    RetargetRow(40, 17_002, 1_088_128, 2_586_694_537_918_671, 792_432_861, 95_177, 264_127_345),
    RetargetRow(41, 21_421, 1_370_944, 5_173_344_309_592_726, 1_257_806_766, 119_920, 419_292_798),
)


def retarget_summary() -> dict[str, int]:
    c16_by_s = {row.s: row for row in C16_ROWS}
    if tuple(row.s for row in EXPECTED_ROWS) != tuple(row.s for row in C16_ROWS):
        raise AssertionError("official exponent drift")

    margins: list[int] = []
    ratios: list[int] = []
    for row in EXPECTED_ROWS:
        source = c16_by_s[row.s]
        if row.old_z != source.z or row.z != BUDGET_MULTIPLIER * source.z:
            raise AssertionError((row, source.z))
        n = 1 << row.s
        target = TARGET_C * n
        bound, conditions, coeffs, image_cap = witness_bound(
            n, row.z, row.a, row.b, row.d
        )
        if bound != row.bound:
            raise AssertionError((row.s, bound, row.bound))
        if bound > target:
            raise AssertionError((row.s, bound, target))
        if not (conditions < coeffs and conditions < image_cap):
            raise AssertionError((row.s, conditions, coeffs, image_cap))
        margins.append(target - bound)
        ratios.append(1_000_000 * bound // target)

    tight = min(EXPECTED_ROWS, key=lambda row: TARGET_C * (1 << row.s) - row.bound)
    return {
        "rows": len(EXPECTED_ROWS),
        "first_s": EXPECTED_ROWS[0].s,
        "last_s": EXPECTED_ROWS[-1].s,
        "target_c": TARGET_C,
        "budget_multiplier": BUDGET_MULTIPLIER,
        "min_old_z": min(row.old_z for row in EXPECTED_ROWS),
        "max_old_z": max(row.old_z for row in EXPECTED_ROWS),
        "min_z": min(row.z for row in EXPECTED_ROWS),
        "max_z": max(row.z for row in EXPECTED_ROWS),
        "min_margin": min(margins),
        "tight_s": tight.s,
        "max_ratio_ppm": max(ratios),
    }


def main() -> None:
    summary = retarget_summary()
    print("h=3 exact-profile H3-ACT(4096) budget floor")
    print(
        "constructive retarget: "
        f"rows=s{summary['first_s']}..s{summary['last_s']} "
        f"target_C={summary['target_c']} "
        f"budget_multiplier={summary['budget_multiplier']}"
    )
    print(
        "budget range: "
        f"old_Z={summary['min_old_z']}..{summary['max_old_z']} "
        f"retarget_Z={summary['min_z']}..{summary['max_z']}"
    )
    print(
        "slack: "
        f"min_margin={summary['min_margin']} "
        f"tight_s={summary['tight_s']} "
        f"max_bound_ratio_ppm={summary['max_ratio_ppm']}"
    )
    print("H3_EXACT_PROFILE_4096_BUDGET_FLOOR_PASS")


if __name__ == "__main__":
    main()
