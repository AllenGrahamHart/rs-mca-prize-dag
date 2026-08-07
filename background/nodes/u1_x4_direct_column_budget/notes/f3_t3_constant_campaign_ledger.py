#!/usr/bin/env python3
"""T3 constant-campaign ledger for the F3 flip attempt."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h2_midrange_certificate_costs import (
    FEASIBLE_SHARD_LIMIT,
    INTEGER_COVERAGE_START,
    OFFICIAL_EXPONENTS,
    SHARD_UNIT,
    row_for_exponent,
)
from f3_h3_per_row_accident_pose import compiled_bound
from f3_h3_official_accident_slack import official_accident_slack_summary


H3_ACCIDENT_C = 16


@dataclass(frozen=True)
class CoverageSplit:
    theorem: tuple[int, ...]
    feasible_census: tuple[int, ...]
    residual: tuple[int, ...]


def h2_inhouse_split() -> CoverageSplit:
    rows = tuple(row_for_exponent(exponent) for exponent in OFFICIAL_EXPONENTS)
    theorem = tuple(row.exponent for row in rows if row.status == "theorem")
    feasible = tuple(row.exponent for row in rows if row.status == "feasible_exact_census")
    residual = tuple(row.exponent for row in rows if row.status == "residual_midrange")
    expected = CoverageSplit(
        theorem=tuple(range(23, 42)),
        feasible_census=tuple(range(13, 19)),
        residual=tuple(range(19, 23)),
    )
    actual = CoverageSplit(theorem=theorem, feasible_census=feasible, residual=residual)
    if actual != expected:
        raise AssertionError(actual)
    return actual


def h3_accident_threshold(c: int) -> int:
    for n in range(2, 1000):
        if compiled_bound(n, c) < n**3:
            return n
    raise AssertionError(("no threshold found", c))


def h3_conditional_split() -> dict[str, int | tuple[int, ...]]:
    threshold = h3_accident_threshold(H3_ACCIDENT_C)
    official = tuple(2**exponent for exponent in OFFICIAL_EXPONENTS)
    bad = tuple(n for n in official if compiled_bound(n, H3_ACCIDENT_C) >= n**3)
    if threshold != 17:
        raise AssertionError(threshold)
    if bad:
        raise AssertionError(bad)
    first = official[0]
    bound = compiled_bound(first, H3_ACCIDENT_C)
    # Store the first-row ratio as a reduced integer scale to keep replay text stable.
    ratio_ppm = 1_000_000 * bound.numerator // (bound.denominator * first**3)
    return {
        "threshold": threshold,
        "covered_exponents": tuple(OFFICIAL_EXPONENTS),
        "first_official_n": first,
        "first_ratio_ppm_floor": ratio_ppm,
    }


def t3_summary() -> dict[str, int]:
    h2 = h2_inhouse_split()
    h3 = h3_conditional_split()
    h3_slack = official_accident_slack_summary()
    return {
        "official_rows": len(tuple(OFFICIAL_EXPONENTS)),
        "h2_theorem_rows": len(h2.theorem),
        "h2_feasible_rows": len(h2.feasible_census),
        "h2_residual_rows": len(h2.residual),
        "h2_external_import_rows": len(tuple(OFFICIAL_EXPONENTS)),
        "h2_inhouse_start": INTEGER_COVERAGE_START,
        "h2_shard_unit": SHARD_UNIT,
        "h2_feasible_shard_limit": FEASIBLE_SHARD_LIMIT,
        "h3_accident_c": H3_ACCIDENT_C,
        "h3_threshold": int(h3["threshold"]),
        "h3_conditional_rows": len(h3["covered_exponents"]),  # type: ignore[arg-type]
        "h3_first_ratio_ppm_floor": int(h3["first_ratio_ppm_floor"]),
        "h3_official_max_safe_c": h3_slack["min_max_safe_c"],
        "h3_midpoint_c": h3_slack["midpoint_c"],
        "h3_midpoint_first_ratio_ppm": h3_slack["first_midpoint_ratio_ppm"],
    }


def main() -> None:
    print("F3 T3 constant-campaign ledger")
    h2 = h2_inhouse_split()
    h3 = h3_conditional_split()
    summary = t3_summary()
    expected = {
        "official_rows": 29,
        "h2_theorem_rows": 19,
        "h2_feasible_rows": 6,
        "h2_residual_rows": 4,
        "h2_external_import_rows": 29,
        "h2_inhouse_start": 7_639_006,
        "h2_shard_unit": 67_108_864,
        "h2_feasible_shard_limit": 2000,
        "h3_accident_c": 16,
        "h3_threshold": 17,
        "h3_conditional_rows": 29,
        "h3_first_ratio_ppm_floor": 1954,
        "h3_official_max_safe_c": 8191,
        "h3_midpoint_c": 4096,
        "h3_midpoint_first_ratio_ppm": 500001,
    }
    if summary != expected:
        raise AssertionError(summary)

    print(
        "h=2 in-house optimized coverage: "
        f"theorem=2^{h2.theorem[0]}..2^{h2.theorem[-1]}, "
        f"feasible_exact_census=2^{h2.feasible_census[0]}..2^{h2.feasible_census[-1]}, "
        f"residual_midrange=2^{h2.residual[0]}..2^{h2.residual[-1]}"
    )
    print(
        "h=2 external import: "
        f"closes all {summary['h2_external_import_rows']} official rows; "
        "in-house residual is accounting only"
    )
    print(
        "h=3 conditional accident coverage: "
        f"H3-ACCIDENT({H3_ACCIDENT_C}) gives T3<n^3 from n>={h3['threshold']}; "
        f"official exponents={min(h3['covered_exponents'])}.."
        f"{max(h3['covered_exponents'])}; "  # type: ignore[arg-type]
        f"first_ratio_ppm_floor={h3['first_ratio_ppm_floor']}"
    )
    print(
        "h=3 residual: prove H3-ACCIDENT(16), or replace it with official-row "
        "activation certificates"
    )
    print(
        "h=3 official-row slack: "
        f"uniform_max_safe_C={summary['h3_official_max_safe_c']} "
        f"midpoint_C={summary['h3_midpoint_c']} "
        f"first_midpoint_ratio_ppm={summary['h3_midpoint_first_ratio_ppm']}"
    )
    print("F3_T3_CONSTANT_CAMPAIGN_LEDGER_PASS")


if __name__ == "__main__":
    main()
