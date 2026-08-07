#!/usr/bin/env python3
"""Rank-deficit budget for the H3-ACT(4096) exact-profile floor."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_exact_profile_4096_budget_floor import EXPECTED_ROWS, RetargetRow
from f3_h3_exact_profile_rank_deficit_budget import rank_deficit_budget_summary
from f3_h3_rich_curve_condition_profile import exact_conditions_per_curve


@dataclass(frozen=True)
class RetargetDeficitRow:
    s: int
    z: int
    a: int
    b: int
    d: int
    degree_dim: int
    exact_conditions: int
    rank_room: int
    allowed_deficit: int


def deficit_row(row: RetargetRow) -> RetargetDeficitRow:
    s = row.s
    n = 1 << s
    degree_dim = row.a + 6 * n * (row.b - 1)
    conditions = exact_conditions_per_curve(row.a, row.d)
    room = degree_dim - conditions
    allowed_deficit = room - 1
    if room <= 0 or allowed_deficit < 0:
        raise AssertionError((row, degree_dim, conditions, room))
    return RetargetDeficitRow(
        s=s,
        z=row.z,  # type: ignore[attr-defined]
        a=row.a,  # type: ignore[attr-defined]
        b=row.b,  # type: ignore[attr-defined]
        d=row.d,  # type: ignore[attr-defined]
        degree_dim=degree_dim,
        exact_conditions=conditions,
        rank_room=room,
        allowed_deficit=allowed_deficit,
    )


def retarget_deficit_summary() -> dict[str, int]:
    old = rank_deficit_budget_summary()
    if old["min_allowed_deficit"] != 1847:
        raise AssertionError(old)
    rows = tuple(deficit_row(row) for row in EXPECTED_ROWS)
    tight = min(rows, key=lambda row: row.allowed_deficit)
    return {
        "rows": len(rows),
        "first_s": rows[0].s,
        "last_s": rows[-1].s,
        "min_z": min(row.z for row in rows),
        "max_z": max(row.z for row in rows),
        "old_min_allowed_deficit": old["min_allowed_deficit"],
        "min_rank_room": min(row.rank_room for row in rows),
        "max_rank_room": max(row.rank_room for row in rows),
        "min_allowed_deficit": tight.allowed_deficit,
        "max_allowed_deficit": max(row.allowed_deficit for row in rows),
        "tight_s": tight.s,
        "tight_degree_dim": tight.degree_dim,
        "tight_conditions": tight.exact_conditions,
        "tight_rank_room": tight.rank_room,
        "tight_z": tight.z,
    }


def main() -> None:
    print("h=3 exact-profile H3-ACT(4096) rank-deficit budget")
    print("rank target per repaired image: rank > C_exact = DA+6D(D-1)")
    print(" s Z_4096_floor       degree_dim          C_exact       room  allowed_deficit")
    for source_row in EXPECTED_ROWS:
        row = deficit_row(source_row)
        print(
            f"{row.s:2d} {row.z:12d} {row.degree_dim:16d}"
            f" {row.exact_conditions:16d} {row.rank_room:10d}"
            f" {row.allowed_deficit:16d}"
        )
    summary = retarget_deficit_summary()
    expected = {
        "rows": 29,
        "first_s": 13,
        "last_s": 41,
        "min_z": 2112,
        "max_z": 1_370_944,
        "old_min_allowed_deficit": 1847,
        "min_rank_room": 2900,
        "min_allowed_deficit": 2899,
        "tight_s": 13,
        "tight_degree_dim": 9_145_225,
        "tight_conditions": 9_142_325,
        "tight_rank_room": 2900,
        "tight_z": 2112,
    }
    for key, value in expected.items():
        if summary[key] != value:
            raise AssertionError((key, summary[key], value))
    print(
        "summary: "
        f"rows={summary['rows']} "
        f"Z_4096_floor={summary['min_z']}..{summary['max_z']} "
        f"allowed_deficit={summary['min_allowed_deficit']}.."
        f"{summary['max_allowed_deficit']} "
        f"old_allowed_deficit={summary['old_min_allowed_deficit']} "
        f"tight_s={summary['tight_s']}"
    )
    print("H3_EXACT_PROFILE_4096_RANK_DEFICIT_BUDGET_PASS")


if __name__ == "__main__":
    main()
