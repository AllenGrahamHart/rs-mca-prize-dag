#!/usr/bin/env python3
"""Official-row rank-capacity guard for the exact h=3 condition profile."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_exact_profile_bridge_budget import EXPECTED_ROWS
from f3_h3_rich_curve_condition_profile import exact_conditions_per_curve


@dataclass(frozen=True)
class CapacityGuardRow:
    s: int
    z: int
    conditions_per_curve: int
    coefficient_capacity: int
    degree_space_capacity: int
    collapsed_capacity: int
    coefficient_room: int
    degree_space_room: int


def rank_capacity(rank_upper: int, conditions_per_curve: int) -> int:
    """Maximum m allowed by the strict rank inequality rank > m*C."""
    if rank_upper <= conditions_per_curve:
        return 0
    return (rank_upper - 1) // conditions_per_curve


def collapsed_constant_ratio_rank(a: int, b: int, h: int) -> int:
    """Rank of r_i=c_i X when H >= A, from the model lemma."""
    if h < a:
        raise AssertionError(("official exact-profile row has H<A", h, a))
    return a * (3 * b - 2)


def capacity_guard_row(row) -> CapacityGuardRow:
    h = 2**row.s
    conditions = exact_conditions_per_curve(row.a, row.d)
    coeffs = row.a * row.b**3
    degree_space_rank_cap = row.a + 6 * h * (row.b - 1)
    collapsed_rank = collapsed_constant_ratio_rank(row.a, row.b, h)

    coefficient_capacity = rank_capacity(coeffs, conditions)
    degree_space_capacity = rank_capacity(degree_space_rank_cap, conditions)
    collapsed_capacity = rank_capacity(collapsed_rank, conditions)

    if coefficient_capacity != row.z:
        raise AssertionError((row.s, coefficient_capacity, row.z))
    if degree_space_capacity != 1:
        raise AssertionError((row.s, degree_space_capacity))
    if collapsed_capacity != 0:
        raise AssertionError((row.s, collapsed_capacity))

    return CapacityGuardRow(
        s=row.s,
        z=row.z,
        conditions_per_curve=conditions,
        coefficient_capacity=coefficient_capacity,
        degree_space_capacity=degree_space_capacity,
        collapsed_capacity=collapsed_capacity,
        coefficient_room=coeffs - conditions * row.z,
        degree_space_room=degree_space_rank_cap - conditions,
    )


def exact_profile_capacity_guard_summary() -> dict[str, int]:
    rows = tuple(capacity_guard_row(row) for row in EXPECTED_ROWS)
    return {
        "rows": len(rows),
        "first_s": rows[0].s,
        "last_s": rows[-1].s,
        "z_min": min(row.z for row in rows),
        "z_max": max(row.z for row in rows),
        "coefficient_capacity_min": min(row.coefficient_capacity for row in rows),
        "coefficient_capacity_max": max(row.coefficient_capacity for row in rows),
        "degree_space_capacity_min": min(row.degree_space_capacity for row in rows),
        "degree_space_capacity_max": max(row.degree_space_capacity for row in rows),
        "collapsed_capacity_max": max(row.collapsed_capacity for row in rows),
        "coefficient_room_min": min(row.coefficient_room for row in rows),
        "degree_space_room_min": min(row.degree_space_room for row in rows),
    }


def main() -> None:
    print("h=3 exact-profile rank-capacity guard")
    print("capacity rule: rank > m*(DA+6D(D-1))")
    print(
        " s exact_Z      C_exact  coeff_cap  degree_cap  collapsed_cap"
        "       coeff_room   degree_room"
    )
    for source_row in EXPECTED_ROWS:
        row = capacity_guard_row(source_row)
        print(
            f"{row.s:2d} {row.z:7d} {row.conditions_per_curve:14d}"
            f" {row.coefficient_capacity:10d} {row.degree_space_capacity:11d}"
            f" {row.collapsed_capacity:14d} {row.coefficient_room:16d}"
            f" {row.degree_space_room:13d}"
        )

    summary = exact_profile_capacity_guard_summary()
    print(
        "summary: "
        f"rows={summary['rows']} "
        f"Z={summary['z_min']}..{summary['z_max']} "
        f"coefficient_capacity={summary['coefficient_capacity_min']}.."
        f"{summary['coefficient_capacity_max']} "
        f"degree_space_capacity={summary['degree_space_capacity_min']}.."
        f"{summary['degree_space_capacity_max']} "
        f"collapsed_capacity_max={summary['collapsed_capacity_max']}"
    )
    print(
        "exact-profile boxes buy more distinct rank-effective images; "
        "they do not permit duplicate-image capacity"
    )
    print("H3_EXACT_PROFILE_RANK_CAPACITY_GUARD_PASS")


if __name__ == "__main__":
    main()
