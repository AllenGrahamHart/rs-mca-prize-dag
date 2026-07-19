#!/usr/bin/env python3
"""Shared-core degree split for the h=3 loose special branches."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h3_repeat_loose_branch_degree_compiler import MapDegree, degree_row
from f3_h3_repeat_loose_branch_geometry import shared_slope_matches
from f3_h3_repeat_loose_branch_slope_maps import branch_slope_map


@dataclass(frozen=True)
class DegreeBlock:
    names: tuple[str, ...]
    sum_a_degrees: int
    sum_total_degrees: int
    max_total_degree: int


def branch_rows(label: str) -> dict[str, MapDegree]:
    return {
        name: degree_row(name, expression)
        for name, expression in branch_slope_map(label).expressions
    }


def block_from_rows(rows: dict[str, MapDegree], names: tuple[str, ...]) -> DegreeBlock:
    selected = tuple(rows[name] for name in names)
    return DegreeBlock(
        names=names,
        sum_a_degrees=sum(row.deg_a for row in selected),
        sum_total_degrees=sum(row.total_degree for row in selected),
        max_total_degree=max(row.total_degree for row in selected),
    )


def verify_shared_expressions() -> tuple[tuple[str, str], ...]:
    matches = shared_slope_matches()
    branch_a = dict(branch_slope_map("A").expressions)
    branch_b = dict(branch_slope_map("B").expressions)
    pairs = tuple(matches.items())
    expected = (
        ("C_1", "C_1"),
        ("C_a", "C_a"),
        ("C_b", "C_1b"),
        ("C_1a", "C_1a"),
        ("C_1b", "C_b"),
        ("L_b", "L_b"),
    )
    if pairs != expected:
        raise AssertionError((pairs, expected))
    for left, right in pairs:
        numerator, _ = sp.together(branch_a[left] - branch_b[right]).as_numer_denom()
        if sp.factor(numerator) != 0:
            raise AssertionError((left, right, branch_a[left], branch_b[right]))
    return pairs


def loose_shared_core_summary() -> dict[str, int]:
    pairs = verify_shared_expressions()
    a_rows = branch_rows("A")
    b_rows = branch_rows("B")
    shared_a_names = tuple(left for left, _ in pairs)
    shared_b_names = tuple(right for _, right in pairs)
    private_a_names = tuple(name for name in a_rows if name not in shared_a_names)
    private_b_names = tuple(name for name in b_rows if name not in shared_b_names)
    if private_a_names != ("C_ab", "L_ab"):
        raise AssertionError(private_a_names)
    if private_b_names != ("C_ab", "L_ab"):
        raise AssertionError(private_b_names)

    shared_a = block_from_rows(a_rows, shared_a_names)
    shared_b = block_from_rows(b_rows, shared_b_names)
    private_a = block_from_rows(a_rows, private_a_names)
    private_b = block_from_rows(b_rows, private_b_names)

    if shared_a.sum_a_degrees != shared_b.sum_a_degrees:
        raise AssertionError((shared_a, shared_b))
    if shared_a.sum_total_degrees != shared_b.sum_total_degrees:
        raise AssertionError((shared_a, shared_b))
    if shared_a.max_total_degree != shared_b.max_total_degree:
        raise AssertionError((shared_a, shared_b))

    full_a_total = shared_a.sum_total_degrees + private_a.sum_total_degrees
    full_b_total = shared_b.sum_total_degrees + private_b.sum_total_degrees
    if full_a_total != 22 or full_b_total != 24:
        raise AssertionError((full_a_total, full_b_total))

    return {
        "shared_maps": len(shared_a.names),
        "shared_sum_a": shared_a.sum_a_degrees,
        "shared_sum_total": shared_a.sum_total_degrees,
        "shared_max_total": shared_a.max_total_degree,
        "branch_a_private_maps": len(private_a.names),
        "branch_a_private_sum_a": private_a.sum_a_degrees,
        "branch_a_private_sum_total": private_a.sum_total_degrees,
        "branch_a_private_max_total": private_a.max_total_degree,
        "branch_b_private_maps": len(private_b.names),
        "branch_b_private_sum_a": private_b.sum_a_degrees,
        "branch_b_private_sum_total": private_b.sum_total_degrees,
        "branch_b_private_max_total": private_b.max_total_degree,
        "branch_a_full_total": full_a_total,
        "branch_b_full_total": full_b_total,
    }


def main() -> None:
    print("h=3 repeat loose shared-core degree split")
    pairs = verify_shared_expressions()
    print("shared_branch_maps:")
    for left, right in pairs:
        print(f"  branch_A.{left} = branch_B.{right}")
    summary = loose_shared_core_summary()
    expected = {
        "shared_maps": 6,
        "shared_sum_a": 10,
        "shared_sum_total": 14,
        "shared_max_total": 5,
        "branch_a_private_maps": 2,
        "branch_a_private_sum_a": 7,
        "branch_a_private_sum_total": 8,
        "branch_a_private_max_total": 5,
        "branch_b_private_maps": 2,
        "branch_b_private_sum_a": 9,
        "branch_b_private_sum_total": 10,
        "branch_b_private_max_total": 7,
        "branch_a_full_total": 22,
        "branch_b_full_total": 24,
    }
    if summary != expected:
        raise AssertionError(summary)
    print(
        "shared_core: "
        f"maps={summary['shared_maps']} "
        f"sum_a={summary['shared_sum_a']} "
        f"sum_total={summary['shared_sum_total']} "
        f"max_total={summary['shared_max_total']}"
    )
    print(
        "branch_A_private: "
        f"maps={summary['branch_a_private_maps']} "
        f"sum_a={summary['branch_a_private_sum_a']} "
        f"sum_total={summary['branch_a_private_sum_total']} "
        f"max_total={summary['branch_a_private_max_total']}"
    )
    print(
        "branch_B_private: "
        f"maps={summary['branch_b_private_maps']} "
        f"sum_a={summary['branch_b_private_sum_a']} "
        f"sum_total={summary['branch_b_private_sum_total']} "
        f"max_total={summary['branch_b_private_max_total']}"
    )
    print(
        "full_branch_totals: "
        f"A={summary['branch_a_full_total']} "
        f"B={summary['branch_b_full_total']}"
    )
    print("H3_REPEAT_LOOSE_SHARED_CORE_DEGREE_PASS")


if __name__ == "__main__":
    main()
