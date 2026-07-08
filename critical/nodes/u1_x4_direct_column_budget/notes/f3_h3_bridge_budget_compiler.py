#!/usr/bin/env python3
"""Bridge-budget compiler for h=3 activated shapes under RC-RANK."""

from __future__ import annotations

from math import isqrt


C_RED = 13
H3_ACT_C = 16
B_MAX = 50_000


EXPECTED_BUDGETS = {
    13: 11,
    14: 14,
    15: 18,
    16: 23,
    17: 29,
    18: 36,
    19: 46,
    20: 58,
    21: 73,
    22: 92,
    23: 116,
    24: 146,
    25: 184,
    26: 232,
    27: 292,
    28: 368,
    29: 463,
    30: 584,
    31: 736,
    32: 927,
    33: 1168,
    34: 1472,
    35: 1855,
    36: 2337,
    37: 2944,
    38: 3710,
    39: 4674,
    40: 5889,
    41: 7420,
}


def best_bound(n: int, z: int) -> int:
    best: int | None = None
    for b in range(2, B_MAX + 1):
        rank_cap = (1 + 6 * n * (b - 1)) // (4 * C_RED)
        ls_cap = (b**3 - 1) // (4 * C_RED * z)
        d = min(isqrt(rank_cap), ls_cap)
        if d < 1:
            continue
        a = d
        conditions = C_RED * d * (a + d) * z
        coeffs = a * b**3
        degree = (a - 1) + 6 * n * (b - 1)
        image_cap = z * (degree + 1)
        if not (conditions < coeffs and conditions < image_cap):
            continue
        bound = (z * degree + d - 1) // d
        if best is None or bound < best:
            best = bound
    if best is None:
        return 10**100
    return best


def verified_budget_for_n(s: int) -> tuple[int, int, int]:
    n = 2**s
    target = H3_ACT_C * n
    budget = EXPECTED_BUDGETS[s]
    bound = best_bound(n, budget)
    next_bound = best_bound(n, budget + 1)
    if bound > target:
        raise AssertionError((s, "budget no longer passes", budget, bound, target))
    if next_bound <= target:
        raise AssertionError((s, "budget not maximal", budget, next_bound, target))
    return budget, bound, next_bound


def main() -> None:
    print("h=3 bridge-budget compiler")
    print(f"C_red={C_RED} H3_ACT_C={H3_ACT_C} B_max={B_MAX}")
    print(" s      n                 Z_budget       bound          16n       next_bound")
    for s in range(13, 42):
        n = 2**s
        budget, bound, next_bound = verified_budget_for_n(s)
        print(
            f"{s:2d} {n:16d} {budget:10d} {bound:14d}"
            f" {H3_ACT_C * n:14d} {next_bound:16d}"
        )

    print("bridge contract: activated shapes must batch into <= Z_budget repaired curves")
    print("maximality check: Z_budget passes and Z_budget+1 fails")
    print("conditional conclusion: RC-RANK + bridge contract => H3-ACT(16)")
    print("H3_BRIDGE_BUDGET_COMPILER_PASS")


if __name__ == "__main__":
    main()
