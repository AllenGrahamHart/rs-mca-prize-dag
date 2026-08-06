#!/usr/bin/env python3
"""Kernel-bundle reduction for the h=3 conic codimension theorem."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_conic_chart_linear_relation_guard import linear_relation_guard_summary
from f3_h3_exact_profile_bridge_budget import EXPECTED_ROWS
from f3_h3_exact_profile_rank_deficit_budget import rank_deficit_budget_summary


@dataclass(frozen=True)
class KernelBundleRow:
    s: int
    a_count: int
    b_count: int
    h_order: int
    base_degree: int
    max_base_windows: int
    balanced_slope_ceil: int
    balanced_margin: int
    annihilator_allowance: int


def ceil_div(num: int, den: int) -> int:
    return -(-num // den)


def kernel_bundle_row(row, allowance: int) -> KernelBundleRow:
    h_order = 2**row.s
    base_degree = 6 * h_order * (row.b - 1)
    max_base_windows = row.b**3
    # If the B^3 base product windows are independent, the kernel bundle has
    # rank B^3-1 and total splitting degree base_degree.
    balanced_slope_ceil = ceil_div(base_degree, max_base_windows - 1)
    return KernelBundleRow(
        s=row.s,
        a_count=row.a,
        b_count=row.b,
        h_order=h_order,
        base_degree=base_degree,
        max_base_windows=max_base_windows,
        balanced_slope_ceil=balanced_slope_ceil,
        balanced_margin=row.a - balanced_slope_ceil,
        annihilator_allowance=allowance,
    )


def conic_kernel_bundle_summary() -> dict[str, int]:
    deficit = rank_deficit_budget_summary()
    allowance = deficit["min_allowed_deficit"]
    if allowance != 1847:
        raise AssertionError(deficit)

    relation = linear_relation_guard_summary()
    if relation["max_gcd_degree"] != 0:
        raise AssertionError(relation)

    rows = tuple(kernel_bundle_row(row, allowance) for row in EXPECTED_ROWS)
    if any(row.balanced_margin <= 0 for row in rows):
        raise AssertionError(rows)
    tight_margin = min(rows, key=lambda row: row.balanced_margin)
    high_slope = max(rows, key=lambda row: row.balanced_slope_ceil)
    return {
        "rows": len(rows),
        "first_s": rows[0].s,
        "last_s": rows[-1].s,
        "allowance": allowance,
        "min_balanced_margin": tight_margin.balanced_margin,
        "min_balanced_margin_s": tight_margin.s,
        "min_balanced_margin_a": tight_margin.a_count,
        "min_balanced_margin_slope": tight_margin.balanced_slope_ceil,
        "max_balanced_slope": high_slope.balanced_slope_ceil,
        "max_balanced_slope_s": high_slope.s,
        "min_base_windows": min(row.max_base_windows for row in rows),
        "max_base_windows": max(row.max_base_windows for row in rows),
        "pairwise_gcd_checks": relation["pairwise_gcd_checks"],
        "max_gcd_degree": relation["max_gcd_degree"],
    }


def main() -> None:
    summary = conic_kernel_bundle_summary()
    print("h=3 conic kernel-bundle reduction")
    print(
        "exact formula: codim H0(O(A-1))*W = "
        "sum_i max(e_i-A,0) for M_W = direct sum O(-e_i)"
    )
    print(
        "official rows: "
        f"s={summary['first_s']}..{summary['last_s']} "
        f"base_windows={summary['min_base_windows']}.."
        f"{summary['max_base_windows']} "
        f"allowance={summary['allowance']}"
    )
    print(
        "full-window balanced slope check: "
        f"max ceil(d/(B^3-1))={summary['max_balanced_slope']} "
        f"(s={summary['max_balanced_slope_s']}), "
        f"min A-ceil(slope)={summary['min_balanced_margin']} "
        f"(s={summary['min_balanced_margin_s']}, "
        f"A={summary['min_balanced_margin_a']}, "
        f"slope={summary['min_balanced_margin_slope']})"
    )
    print(
        "basepoint guard input: "
        f"pairwise_gcd_checks={summary['pairwise_gcd_checks']} "
        f"max_gcd_degree={summary['max_gcd_degree']}"
    )
    print("H3_CONIC_KERNEL_BUNDLE_REDUCTION_PASS")


if __name__ == "__main__":
    main()
