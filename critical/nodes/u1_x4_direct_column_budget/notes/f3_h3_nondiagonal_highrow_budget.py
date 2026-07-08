#!/usr/bin/env python3
"""Optional high-row non-diagonal h=3 bridge-budget lift."""

from __future__ import annotations

from f3_h3_nondiagonal_lowrow_budget import (
    B_MAX,
    C_RED,
    H3_ACT_C,
    Row,
    best_nondiagonal_bound,
    witness_bound,
)


EXPECTED_ROWS = (
    Row(
        36,
        2_337,
        3_400,
        1_099_309_787_730,
        8_289_392,
        13_004,
        16_581_869,
        1_099_697_785_998,
        8_290_555,
        13_005,
        16_582_169,
    ),
    Row(
        37,
        2_944,
        4_284,
        2_198_805_809_166,
        13_162_858,
        16_382,
        26_318_679,
        2_199_421_740_501,
        13_164_324,
        16_383,
        26_319_057,
    ),
    Row(
        38,
        3_710,
        5_397,
        4_397_154_194_066,
        20_891_085,
        20_641,
        41_781_257,
        4_398_131_952_298,
        20_888_884,
        20_644,
        41_785_781,
    ),
    Row(
        39,
        4_674,
        6_800,
        8_794_681_029_148,
        33_161_394,
        26_007,
        66_325_947,
        8_796_233_064_817,
        33_161_170,
        26_009,
        66_329_097,
    ),
)


def main() -> None:
    print("h=3 optional non-diagonal high-row bridge-budget lift")
    print(f"C_red={C_RED} H3_ACT_C={H3_ACT_C} B_max={B_MAX}")
    print(" s          n   old_Z   new_Z          bound            16n      next_bound")
    for row in EXPECTED_ROWS:
        n = 2**row.s
        target = H3_ACT_C * n
        got_bound, *_ = witness_bound(n, row.z, row.a, row.b, row.d)
        if got_bound != row.bound:
            raise AssertionError((row.s, got_bound, row.bound))
        if got_bound > target:
            raise AssertionError((row.s, "passing witness exceeds target", got_bound, target))

        next_bound, next_a, next_b, next_d = best_nondiagonal_bound(n, row.z + 1)
        got_next = (next_bound, next_a, next_b, next_d)
        expected_next = (row.next_bound, row.next_a, row.next_b, row.next_d)
        if got_next != expected_next:
            raise AssertionError((row.s, got_next, expected_next))
        if next_bound <= target:
            raise AssertionError((row.s, "next budget passes", next_bound, target))

        print(
            f"{row.s:2d} {n:10d} {row.old_z:7d} {row.z:7d}"
            f" {row.bound:14d} {target:14d} {row.next_bound:15d}"
        )

    print("maximality check: new_Z passes and new_Z+1 fails for s=36..39")
    print("conditional conclusion: high-row non-diagonal boxes further enlarge H3-BRIDGE budgets")
    print("H3_NONDIAGONAL_HIGHROW_BUDGET_PASS")


if __name__ == "__main__":
    main()
