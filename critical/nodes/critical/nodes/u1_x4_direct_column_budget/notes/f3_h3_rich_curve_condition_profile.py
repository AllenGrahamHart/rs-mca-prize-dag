#!/usr/bin/env python3
"""Exact reduced-condition profile for the h=3 rich-curve log-jet gate."""

from __future__ import annotations

from dataclasses import dataclass


LEGACY_C_RED = 13


@dataclass(frozen=True)
class ConditionProfileRow:
    a: int
    d: int
    z: int
    exact_per_curve: int
    legacy_per_curve: int
    exact_total: int
    legacy_total: int
    saved_total: int


def exact_conditions_per_curve(a: int, d: int) -> int:
    """Sum_j (A+12j), 0 <= j < D, from the log-jet degree profile."""
    if min(a, d) < 1:
        raise ValueError((a, d))
    return d * a + 6 * d * (d - 1)


def legacy_conditions_per_curve(a: int, d: int) -> int:
    if min(a, d) < 1:
        raise ValueError((a, d))
    return LEGACY_C_RED * d * (a + d)


def condition_profile_row(a: int, d: int, z: int) -> ConditionProfileRow:
    if z < 1:
        raise ValueError(z)
    exact = exact_conditions_per_curve(a, d)
    legacy = legacy_conditions_per_curve(a, d)
    if exact > legacy:
        raise AssertionError((a, d, exact, legacy))
    return ConditionProfileRow(
        a=a,
        d=d,
        z=z,
        exact_per_curve=exact,
        legacy_per_curve=legacy,
        exact_total=exact * z,
        legacy_total=legacy * z,
        saved_total=(legacy - exact) * z,
    )


def condition_profile_summary() -> dict[str, int]:
    rows = (
        condition_profile_row(a=512, d=16, z=1),
        condition_profile_row(a=512, d=16, z=8),
        condition_profile_row(a=2048, d=32, z=16),
        condition_profile_row(a=8192, d=64, z=32),
        condition_profile_row(a=32768, d=128, z=64),
    )
    # These rows mirror the reduced-condition compiler sample boxes.
    expected_savings = (100192, 801536, 12700672, 202256384, 3228614656)
    actual_savings = tuple(row.saved_total for row in rows)
    if actual_savings != expected_savings:
        raise AssertionError(actual_savings)
    return {
        "sample_rows": len(rows),
        "legacy_c_red": LEGACY_C_RED,
        "max_exact_to_legacy_percent": max(
            10_000 * row.exact_total // row.legacy_total for row in rows
        ),
        "min_exact_to_legacy_percent": min(
            10_000 * row.exact_total // row.legacy_total for row in rows
        ),
        "max_saved_total": max(row.saved_total for row in rows),
        "total_saved_conditions": sum(row.saved_total for row in rows),
    }


def main() -> None:
    print("h=3 rich-curve exact reduced-condition profile")
    print("legacy bound: 13 D(A+D)|Z|")
    print("exact profile: |Z| * sum_{j=0}^{D-1}(A+12j) = |Z|*(DA+6D(D-1))")
    print("    A     D    |Z|      exact_total      legacy_total       saved")
    for a, d, z in (
        (512, 16, 1),
        (512, 16, 8),
        (2048, 32, 16),
        (8192, 64, 32),
        (32768, 128, 64),
    ):
        row = condition_profile_row(a, d, z)
        print(
            f"{row.a:6d} {row.d:5d} {row.z:6d}"
            f" {row.exact_total:16d} {row.legacy_total:17d}"
            f" {row.saved_total:12d}"
        )
    summary = condition_profile_summary()
    print(
        "summary: "
        f"sample_rows={summary['sample_rows']} "
        f"legacy_c_red={summary['legacy_c_red']} "
        f"exact_to_legacy_percent="
        f"{summary['min_exact_to_legacy_percent'] / 100:.2f}.."
        f"{summary['max_exact_to_legacy_percent'] / 100:.2f} "
        f"total_saved_conditions={summary['total_saved_conditions']}"
    )
    print("This strengthens RC-RED arithmetic only; RC-NV remains open.")
    print("H3_RICH_CURVE_CONDITION_PROFILE_PASS")


if __name__ == "__main__":
    main()
