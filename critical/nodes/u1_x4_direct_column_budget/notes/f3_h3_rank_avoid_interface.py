#!/usr/bin/env python3
"""Pin the h=3 rank-avoidance interface needed to close H3-ACT(16)."""

from __future__ import annotations

from f3_h3_nondiagonal_highrow_budget import EXPECTED_ROWS as HIGH_ROWS
from f3_h3_nondiagonal_lowrow_budget import C_RED, H3_ACT_C, EXPECTED_ROWS as LOW_ROWS
from f3_h3_nondiagonal_lowrow_budget import witness_bound


def main() -> None:
    rows = (*LOW_ROWS, *HIGH_ROWS)
    exponents = [row.s for row in rows]
    expected_exponents = list(range(13, 42))
    if exponents != expected_exponents:
        raise AssertionError((exponents, expected_exponents))

    print("h=3 rank-avoidance interface")
    print(f"C_red={C_RED} H3_ACT_C={H3_ACT_C}")
    print(" s          n       Z_budget       bound          16n      A      B       D")
    min_z = None
    max_z = None
    for row in rows:
        n = 2**row.s
        target = H3_ACT_C * n
        bound, conditions, coeffs, image_cap = witness_bound(
            n, row.z, row.a, row.b, row.d
        )
        if bound != row.bound:
            raise AssertionError((row.s, bound, row.bound))
        if not (bound <= target < row.next_bound):
            raise AssertionError((row.s, bound, target, row.next_bound))
        if not (conditions < coeffs and conditions < image_cap):
            raise AssertionError((row.s, conditions, coeffs, image_cap))
        min_z = row.z if min_z is None else min(min_z, row.z)
        max_z = row.z if max_z is None else max(max_z, row.z)
        print(
            f"{row.s:2d} {n:10d} {row.z:14d} {bound:11d} "
            f"{target:12d} {row.a:6d} {row.b:6d} {row.d:8d}"
        )

    if min_z != 16 or max_z != 10795:
        raise AssertionError((min_z, max_z))

    print("official h=3 rows covered by conditional rank-capacity budgets: s=13..41")
    print("theorem interface: F3-RANK-AVOID + H3-BRIDGE-RANKCAP(Z_budget) => H3-ACT(16)")
    print("H3_RANK_AVOID_INTERFACE_PASS")


if __name__ == "__main__":
    main()
