#!/usr/bin/env python3
"""Rank-deficit budget for the h=3 private-linear alternate route."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_private_linear_lowrow_budget import (
    C_RED,
    EXPECTED_ROWS,
    private_degree,
)


@dataclass(frozen=True)
class PrivateDeficitRow:
    s: int
    z: int
    a: int
    b: int
    d: int
    degree_dim: int
    conditions_per_image: int
    rank_room: int
    allowed_deficit: int


def deficit_row(row) -> PrivateDeficitRow:
    n = 1 << row.s
    degree_dim = private_degree(n, row.a, row.b) + 1
    conditions = C_RED * row.d * (row.a + row.d)
    room = degree_dim - conditions
    allowed_deficit = room - 1
    if room <= 0 or allowed_deficit < 0:
        raise AssertionError((row.s, degree_dim, conditions, room))
    return PrivateDeficitRow(
        s=row.s,
        z=row.z,
        a=row.a,
        b=row.b,
        d=row.d,
        degree_dim=degree_dim,
        conditions_per_image=conditions,
        rank_room=room,
        allowed_deficit=allowed_deficit,
    )


def private_rank_deficit_budget_summary() -> dict[str, int]:
    rows = tuple(deficit_row(row) for row in EXPECTED_ROWS)
    tight = min(rows, key=lambda row: row.allowed_deficit)
    return {
        "rows": len(rows),
        "first_s": rows[0].s,
        "last_s": rows[-1].s,
        "min_z": min(row.z for row in rows),
        "max_z": max(row.z for row in rows),
        "min_rank_room": min(row.rank_room for row in rows),
        "max_rank_room": max(row.rank_room for row in rows),
        "min_allowed_deficit": tight.allowed_deficit,
        "max_allowed_deficit": max(row.allowed_deficit for row in rows),
        "tight_s": tight.s,
        "tight_degree_dim": tight.degree_dim,
        "tight_conditions": tight.conditions_per_image,
        "tight_rank_room": tight.rank_room,
        "tight_z": tight.z,
    }


def main() -> None:
    print("h=3 private-linear rank-deficit budget")
    print("rank target per repaired private-linear image: rank > 13 D(A+D)")
    print("A rank lower bound degree_dim-deficit is enough when deficit <= allowed_deficit.")
    print(" s Z_private       degree_dim        conditions       room  allowed_deficit")
    for source_row in EXPECTED_ROWS:
        row = deficit_row(source_row)
        print(
            f"{row.s:2d} {row.z:9d} {row.degree_dim:16d}"
            f" {row.conditions_per_image:17d} {row.rank_room:10d}"
            f" {row.allowed_deficit:16d}"
        )
    summary = private_rank_deficit_budget_summary()
    expected = {
        "rows": 29,
        "first_s": 13,
        "last_s": 41,
        "min_z": 23,
        "max_z": 15267,
        "min_rank_room": 26,
        "min_allowed_deficit": 25,
        "tight_s": 16,
        "tight_degree_dim": 24576578,
        "tight_conditions": 24576552,
        "tight_rank_room": 26,
        "tight_z": 47,
    }
    for key, value in expected.items():
        if summary[key] != value:
            raise AssertionError((key, summary[key], value))
    print(
        "summary: "
        f"rows={summary['rows']} "
        f"Z={summary['min_z']}..{summary['max_z']} "
        f"rank_room={summary['min_rank_room']}..{summary['max_rank_room']} "
        f"allowed_deficit={summary['min_allowed_deficit']}.."
        f"{summary['max_allowed_deficit']} "
        f"tight_s={summary['tight_s']}"
    )
    print("H3_PRIVATE_LINEAR_RANK_DEFICIT_BUDGET_PASS")


if __name__ == "__main__":
    main()
