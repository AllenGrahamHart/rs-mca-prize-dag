#!/usr/bin/env python3
"""Rank-deficit budget for the h=3 exact-profile conic-chart route."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_exact_profile_bridge_budget import EXPECTED_ROWS
from f3_h3_rich_curve_condition_profile import exact_conditions_per_curve


@dataclass(frozen=True)
class DeficitRow:
    s: int
    z: int
    a: int
    b: int
    d: int
    degree_dim: int
    exact_conditions: int
    rank_room: int
    allowed_deficit: int


def deficit_row(row) -> DeficitRow:
    n = 2**row.s
    degree_dim = row.a + 6 * n * (row.b - 1)
    conditions = exact_conditions_per_curve(row.a, row.d)
    room = degree_dim - conditions
    allowed_deficit = room - 1
    if room <= 0:
        raise AssertionError((row.s, degree_dim, conditions))
    if allowed_deficit < 0:
        raise AssertionError((row.s, allowed_deficit))
    return DeficitRow(
        s=row.s,
        z=row.z,
        a=row.a,
        b=row.b,
        d=row.d,
        degree_dim=degree_dim,
        exact_conditions=conditions,
        rank_room=room,
        allowed_deficit=allowed_deficit,
    )


def rank_deficit_budget_summary() -> dict[str, int]:
    rows = tuple(deficit_row(row) for row in EXPECTED_ROWS)
    return {
        "rows": len(rows),
        "first_s": rows[0].s,
        "last_s": rows[-1].s,
        "min_rank_room": min(row.rank_room for row in rows),
        "max_rank_room": max(row.rank_room for row in rows),
        "min_allowed_deficit": min(row.allowed_deficit for row in rows),
        "max_allowed_deficit": max(row.allowed_deficit for row in rows),
        "min_z": min(row.z for row in rows),
        "max_z": max(row.z for row in rows),
    }


def main() -> None:
    print("h=3 exact-profile rank-deficit budget")
    print("rank target per repaired image: rank > C_exact = DA+6D(D-1)")
    print("A rank lower bound degree_dim-deficit is enough when deficit <= allowed_deficit.")
    print(" s exact_Z       degree_dim          C_exact       room  allowed_deficit")
    for source_row in EXPECTED_ROWS:
        row = deficit_row(source_row)
        print(
            f"{row.s:2d} {row.z:7d} {row.degree_dim:16d}"
            f" {row.exact_conditions:16d} {row.rank_room:10d}"
            f" {row.allowed_deficit:16d}"
        )
    summary = rank_deficit_budget_summary()
    print(
        "summary: "
        f"rows={summary['rows']} "
        f"Z={summary['min_z']}..{summary['max_z']} "
        f"rank_room={summary['min_rank_room']}..{summary['max_rank_room']} "
        f"allowed_deficit={summary['min_allowed_deficit']}.."
        f"{summary['max_allowed_deficit']}"
    )
    print("H3_EXACT_PROFILE_RANK_DEFICIT_BUDGET_PASS")


if __name__ == "__main__":
    main()
