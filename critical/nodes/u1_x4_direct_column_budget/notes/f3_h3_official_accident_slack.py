#!/usr/bin/env python3
"""Official-row slack for the h=3 accident constant."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_per_row_accident_pose import compiled_bound


OFFICIAL_EXPONENTS = tuple(range(13, 42))
REFERENCE_C = 16
MIDPOINT_C = 4096


@dataclass(frozen=True)
class AccidentSlackRow:
    exponent: int
    n: int
    max_safe_c: int
    reference_ratio_ppm: int
    midpoint_ratio_ppm: int
    max_ratio_ppm: int


def ratio_ppm(n: int, c: int) -> int:
    bound = compiled_bound(n, c)
    return 1_000_000 * bound.numerator // (bound.denominator * n**3)


def max_safe_c(n: int) -> int:
    lo = 0
    hi = n
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if compiled_bound(n, mid) < n**3:
            lo = mid
        else:
            hi = mid
    return lo


def accident_slack_rows() -> tuple[AccidentSlackRow, ...]:
    rows: list[AccidentSlackRow] = []
    for exponent in OFFICIAL_EXPONENTS:
        n = 2**exponent
        row = AccidentSlackRow(
            exponent=exponent,
            n=n,
            max_safe_c=max_safe_c(n),
            reference_ratio_ppm=ratio_ppm(n, REFERENCE_C),
            midpoint_ratio_ppm=ratio_ppm(n, MIDPOINT_C),
            max_ratio_ppm=ratio_ppm(n, max_safe_c(n)),
        )
        if compiled_bound(n, row.max_safe_c) >= n**3:
            raise AssertionError(row)
        if compiled_bound(n, row.max_safe_c + 1) < n**3:
            raise AssertionError(row)
        rows.append(row)
    return tuple(rows)


def official_accident_slack_summary() -> dict[str, int]:
    rows = accident_slack_rows()
    if min(row.max_safe_c for row in rows) != 8191:
        raise AssertionError(rows)
    if rows[0].reference_ratio_ppm != 1954:
        raise AssertionError(rows[0])
    if rows[0].midpoint_ratio_ppm != 500001:
        raise AssertionError(rows[0])
    return {
        "rows": len(rows),
        "first_s": rows[0].exponent,
        "last_s": rows[-1].exponent,
        "reference_c": REFERENCE_C,
        "midpoint_c": MIDPOINT_C,
        "min_max_safe_c": min(row.max_safe_c for row in rows),
        "tight_s": min(rows, key=lambda row: row.max_safe_c).exponent,
        "first_reference_ratio_ppm": rows[0].reference_ratio_ppm,
        "first_midpoint_ratio_ppm": rows[0].midpoint_ratio_ppm,
        "first_max_ratio_ppm": rows[0].max_ratio_ppm,
    }


def main() -> None:
    summary = official_accident_slack_summary()
    print("h=3 official-row accident constant slack")
    print(
        "official rows: "
        f"s={summary['first_s']}..{summary['last_s']} "
        f"reference_C={summary['reference_c']} "
        f"midpoint_C={summary['midpoint_c']} "
        f"uniform_max_safe_C={summary['min_max_safe_c']} "
        f"tight_s={summary['tight_s']}"
    )
    print(
        "first-row ratios ppm: "
        f"C={summary['reference_c']} -> "
        f"{summary['first_reference_ratio_ppm']}, "
        f"C={summary['midpoint_c']} -> "
        f"{summary['first_midpoint_ratio_ppm']}, "
        f"C={summary['min_max_safe_c']} -> "
        f"{summary['first_max_ratio_ppm']}"
    )
    print("H3_OFFICIAL_ACCIDENT_SLACK_PASS")


if __name__ == "__main__":
    main()
