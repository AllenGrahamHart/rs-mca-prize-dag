#!/usr/bin/env python3
"""Sparse degree skeleton for central-chart fixed-point compatibility."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h5_basefree_reciprocal_system import reciprocal_slots
from f3_h5_central_chart_graph import central_graph_summary
from f3_h5_reciprocal_compatibility_compiler import TOP


@dataclass(frozen=True)
class FixedPointSkeletonRow:
    key_index: int
    denominator_l5_power: int
    high_terms: int
    pre_cancellation_terms: int
    top_degree_bound: int
    bar_l5_degree_bound: int
    total_degree_bound: int


def high_part_profiles() -> dict[int, tuple[int, int]]:
    slots = {slot[0]: slot for slot in reciprocal_slots()}
    profiles = {}
    for key_index in range(1, 5):
        poly = sp.Poly(slots[key_index][2], *TOP, domain=sp.ZZ)
        profiles[key_index] = (len(poly.terms()), poly.total_degree())
    return profiles


def fixedpoint_skeleton_rows() -> tuple[FixedPointSkeletonRow, ...]:
    slots = {slot[0]: slot for slot in reciprocal_slots()}
    profiles = high_part_profiles()
    rows: list[FixedPointSkeletonRow] = []
    for key_index in range(1, 5):
        poly = sp.Poly(slots[key_index][2], *TOP, domain=sp.ZZ)
        denominator_power = max(sum(monom[1:]) for monom, _ in poly.terms())

        pre_cancellation_terms = 1
        top_degree_bound = denominator_power + 1
        bar_l5_degree_bound = 1
        total_degree_bound = top_degree_bound + bar_l5_degree_bound
        for monom, _ in poly.terms():
            noncentral_degree = sum(monom[1:])
            term_bound = 1
            product_top_degree = 0
            for offset in range(1, 5):
                exponent = monom[offset]
                if exponent == 0:
                    continue
                graph_key = 5 - offset  # l6->P4, l7->P3, l8->P2, l9->P1.
                graph_terms, graph_degree = profiles[graph_key]
                term_bound *= graph_terms**exponent
                product_top_degree += graph_degree * exponent

            pre_cancellation_terms += term_bound
            top_degree = 1 + (denominator_power - noncentral_degree) + product_top_degree
            bar_l5_degree = sum(monom)
            top_degree_bound = max(top_degree_bound, top_degree)
            bar_l5_degree_bound = max(bar_l5_degree_bound, bar_l5_degree)
            total_degree_bound = max(total_degree_bound, top_degree + bar_l5_degree)

        rows.append(
            FixedPointSkeletonRow(
                key_index=key_index,
                denominator_l5_power=denominator_power,
                high_terms=profiles[key_index][0],
                pre_cancellation_terms=pre_cancellation_terms,
                top_degree_bound=top_degree_bound,
                bar_l5_degree_bound=bar_l5_degree_bound,
                total_degree_bound=total_degree_bound,
            )
        )
    return tuple(rows)


def fixedpoint_skeleton_summary() -> dict[str, int]:
    graph = central_graph_summary()
    rows = fixedpoint_skeleton_rows()
    expected = {
        1: (9, 22, 1255488415957, 82, 9, 91),
        2: (8, 18, 57067651704, 73, 8, 81),
        3: (7, 13, 2593979107, 64, 7, 71),
        4: (6, 10, 117907944, 55, 6, 61),
    }
    actual = {
        row.key_index: (
            row.denominator_l5_power,
            row.high_terms,
            row.pre_cancellation_terms,
            row.top_degree_bound,
            row.bar_l5_degree_bound,
            row.total_degree_bound,
        )
        for row in rows
    }
    if actual != expected:
        raise AssertionError(actual)
    return {
        "fixedpoint_rows": len(rows),
        "graph_terms": graph["total_graph_terms"],
        "max_denominator_l5_power": max(row.denominator_l5_power for row in rows),
        "max_pre_cancellation_terms": max(row.pre_cancellation_terms for row in rows),
        "min_pre_cancellation_terms": min(row.pre_cancellation_terms for row in rows),
        "max_total_degree_bound": max(row.total_degree_bound for row in rows),
    }


def main() -> None:
    summary = fixedpoint_skeleton_summary()
    print("h=5 central chart fixed-point skeleton")
    print("profiles are sparse upper bounds; no expanded fixed-point numerators are formed")
    for row in fixedpoint_skeleton_rows():
        print(
            f"  F{row.key_index}: l5_denom_power={row.denominator_l5_power} "
            f"high_terms={row.high_terms} "
            f"pre_cancel_terms<={row.pre_cancellation_terms} "
            f"top_degree<={row.top_degree_bound} "
            f"bar_l5_degree<={row.bar_l5_degree_bound} "
            f"total_degree<={row.total_degree_bound}"
        )
    print(
        "summary: "
        f"fixedpoint_rows={summary['fixedpoint_rows']} "
        f"graph_terms={summary['graph_terms']} "
        f"pre_cancel_terms={summary['min_pre_cancellation_terms']}.."
        f"{summary['max_pre_cancellation_terms']} "
        f"max_l5_denom_power={summary['max_denominator_l5_power']} "
        f"max_total_degree={summary['max_total_degree_bound']}"
    )
    print("H5_CENTRAL_FIXEDPOINT_SKELETON_PASS")


if __name__ == "__main__":
    main()
