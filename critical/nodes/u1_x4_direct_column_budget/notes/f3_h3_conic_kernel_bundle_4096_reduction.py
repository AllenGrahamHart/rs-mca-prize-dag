#!/usr/bin/env python3
"""Kernel-bundle reduction for the H3-ACT(4096) conic rank target."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_conic_chart_linear_relation_guard import linear_relation_guard_summary
from f3_h3_conic_kernel_bundle_reduction import ceil_div
from f3_h3_exact_profile_4096_budget_floor import EXPECTED_ROWS
from f3_h3_exact_profile_4096_rank_deficit_budget import retarget_deficit_summary


@dataclass(frozen=True)
class Kernel4096Row:
    s: int
    a_count: int
    b_count: int
    h_order: int
    base_degree: int
    max_base_windows: int
    balanced_slope_ceil: int
    balanced_margin: int
    allowance: int


def kernel_4096_row(row, allowance: int) -> Kernel4096Row:
    h_order = 1 << row.s
    base_degree = 6 * h_order * (row.b - 1)
    max_base_windows = row.b**3
    balanced_slope_ceil = ceil_div(base_degree, max_base_windows - 1)
    return Kernel4096Row(
        s=row.s,
        a_count=row.a,
        b_count=row.b,
        h_order=h_order,
        base_degree=base_degree,
        max_base_windows=max_base_windows,
        balanced_slope_ceil=balanced_slope_ceil,
        balanced_margin=row.a - balanced_slope_ceil,
        allowance=allowance,
    )


def conic_kernel_4096_summary() -> dict[str, int]:
    deficit = retarget_deficit_summary()
    allowance = deficit["min_allowed_deficit"]
    if allowance != 2899:
        raise AssertionError(deficit)

    relation = linear_relation_guard_summary()
    if relation["max_gcd_degree"] != 0:
        raise AssertionError(relation)

    rows = tuple(kernel_4096_row(row, allowance) for row in EXPECTED_ROWS)
    if any(row.balanced_margin <= 0 for row in rows):
        raise AssertionError(rows)
    tight_margin = min(rows, key=lambda row: row.balanced_margin)
    high_slope = max(rows, key=lambda row: row.balanced_slope_ceil)
    tight_allowance_gap = min(row.balanced_margin - row.allowance for row in rows)
    return {
        "rows": len(rows),
        "first_s": rows[0].s,
        "last_s": rows[-1].s,
        "allowance": allowance,
        "min_balanced_margin": tight_margin.balanced_margin,
        "min_balanced_margin_s": tight_margin.s,
        "min_balanced_margin_a": tight_margin.a_count,
        "min_balanced_margin_slope": tight_margin.balanced_slope_ceil,
        "min_margin_minus_allowance": tight_allowance_gap,
        "max_balanced_slope": high_slope.balanced_slope_ceil,
        "max_balanced_slope_s": high_slope.s,
        "min_base_windows": min(row.max_base_windows for row in rows),
        "max_base_windows": max(row.max_base_windows for row in rows),
        "pairwise_gcd_checks": relation["pairwise_gcd_checks"],
        "max_gcd_degree": relation["max_gcd_degree"],
    }


def main() -> None:
    summary = conic_kernel_4096_summary()
    expected = {
        "rows": 29,
        "first_s": 13,
        "last_s": 41,
        "allowance": 2899,
        "min_balanced_margin": 2951,
        "min_balanced_margin_s": 13,
        "min_balanced_margin_a": 2953,
        "min_balanced_margin_slope": 2,
        "min_margin_minus_allowance": 52,
        "max_balanced_slope": 918,
        "max_balanced_slope_s": 41,
        "min_base_windows": 6_539_203,
        "max_base_windows": 1_724_546_303_488_000,
        "pairwise_gcd_checks": 6,
        "max_gcd_degree": 0,
    }
    if summary != expected:
        raise AssertionError(summary)

    print("h=3 conic H3-ACT(4096) kernel-bundle reduction")
    print(
        "exact formula unchanged: codim H0(O(A-1))*W = "
        "sum_i max(e_i-A,0)"
    )
    print(
        "official retuned rows: "
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
        "allowance comparison: "
        f"min_margin_minus_allowance={summary['min_margin_minus_allowance']}"
    )
    print(
        "basepoint guard input: "
        f"pairwise_gcd_checks={summary['pairwise_gcd_checks']} "
        f"max_gcd_degree={summary['max_gcd_degree']}"
    )
    print("H3_CONIC_KERNEL_BUNDLE_4096_REDUCTION_PASS")


if __name__ == "__main__":
    main()
