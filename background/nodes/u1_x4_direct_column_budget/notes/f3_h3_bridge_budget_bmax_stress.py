#!/usr/bin/env python3
"""Stress the h=3 bridge budgets against a larger diagonal B cap."""

from __future__ import annotations

from f3_h3_bridge_budget_compiler import EXPECTED_BUDGETS, H3_ACT_C, best_bound


STRESS_B_MAX = 500_000

EXPECTED_CLOSEST_FAILURES = (
    (13, 12, 6_297, 137_369),
    (14, 15, 9_836, 271_980),
    (15, 19, 22_892, 547_180),
    (16, 24, 51_554, 1_100_130),
    (18, 37, 53_037, 4_247_341),
)


def main() -> None:
    closest: list[tuple[int, int, int, int]] = []
    passing: list[tuple[int, int, int, int]] = []
    for s, budget in EXPECTED_BUDGETS.items():
        n = 2**s
        target = H3_ACT_C * n
        z_next = budget + 1
        bound = best_bound(n, z_next, b_max=STRESS_B_MAX)
        margin = bound - target
        if bound <= target:
            passing.append((s, z_next, bound, target))
        closest.append((margin, s, z_next, bound))

    if passing:
        raise AssertionError(("next budget passed under stress cap", passing))

    got = tuple((s, z, margin, bound) for margin, s, z, bound in sorted(closest)[:5])
    if got != EXPECTED_CLOSEST_FAILURES:
        raise AssertionError((got, EXPECTED_CLOSEST_FAILURES))

    print("h=3 bridge-budget B_max stress")
    print(f"stress B_max={STRESS_B_MAX}")
    print("all Z_budget+1 rows still fail")
    print("closest failures:")
    for s, z, margin, bound in got:
        print(f"  s={s} z={z} margin={margin} bound={bound}")
    print("H3_BRIDGE_BUDGET_BMAX_STRESS_PASS")


if __name__ == "__main__":
    main()
