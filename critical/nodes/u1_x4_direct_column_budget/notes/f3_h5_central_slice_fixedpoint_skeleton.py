#!/usr/bin/env python3
"""Sparse fixed-point skeleton after the h=5 central weighted slice."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h5_basefree_reciprocal_system import reciprocal_slots
from f3_h5_central_fixedpoint_skeleton import fixedpoint_skeleton_rows
from f3_h5_central_weighted_slice import CENTRAL_SUBS, central_slice_summary
from f3_h5_reciprocal_compatibility_compiler import TOP


SLICE_TOP = TOP[1:]


@dataclass(frozen=True)
class SliceFixedPointRow:
    key_index: int
    high_terms: int
    pre_cancellation_terms: int
    slice_degree_bound: int
    unsliced_total_degree_bound: int
    degree_drop: int


def sliced_high_profiles() -> dict[int, tuple[int, int]]:
    slots = {slot[0]: slot for slot in reciprocal_slots()}
    profiles: dict[int, tuple[int, int]] = {}
    for key_index in range(1, 5):
        poly = sp.Poly(slots[key_index][2].subs(CENTRAL_SUBS), *SLICE_TOP, domain=sp.ZZ)
        profiles[key_index] = (len(poly.terms()), poly.total_degree())
    return profiles


def slice_fixedpoint_rows() -> tuple[SliceFixedPointRow, ...]:
    slots = {slot[0]: slot for slot in reciprocal_slots()}
    profiles = sliced_high_profiles()
    unsliced = {row.key_index: row.total_degree_bound for row in fixedpoint_skeleton_rows()}
    rows: list[SliceFixedPointRow] = []

    for key_index in range(1, 5):
        poly = sp.Poly(slots[key_index][2].subs(CENTRAL_SUBS), *SLICE_TOP, domain=sp.ZZ)
        pre_cancellation_terms = 1
        slice_degree_bound = 1
        for monom, _ in poly.terms():
            term_bound = 1
            product_degree = 0
            for offset, exponent in enumerate(monom):
                if exponent == 0:
                    continue
                graph_key = 4 - offset  # l6->P4, l7->P3, l8->P2, l9->P1.
                graph_terms, graph_degree = profiles[graph_key]
                term_bound *= graph_terms**exponent
                product_degree += graph_degree * exponent
            pre_cancellation_terms += term_bound
            slice_degree_bound = max(slice_degree_bound, product_degree)

        rows.append(
            SliceFixedPointRow(
                key_index=key_index,
                high_terms=len(poly.terms()),
                pre_cancellation_terms=pre_cancellation_terms,
                slice_degree_bound=slice_degree_bound,
                unsliced_total_degree_bound=unsliced[key_index],
                degree_drop=unsliced[key_index] - slice_degree_bound,
            )
        )
    return tuple(rows)


def slice_fixedpoint_summary() -> dict[str, int]:
    central_slice = central_slice_summary()
    rows = slice_fixedpoint_rows()
    expected = {
        1: (22, 1255488415957, 81, 91, 10),
        2: (18, 57067651704, 72, 81, 9),
        3: (13, 2593979107, 63, 71, 8),
        4: (10, 117907944, 54, 61, 7),
    }
    actual = {
        row.key_index: (
            row.high_terms,
            row.pre_cancellation_terms,
            row.slice_degree_bound,
            row.unsliced_total_degree_bound,
            row.degree_drop,
        )
        for row in rows
    }
    if actual != expected:
        raise AssertionError(actual)
    return {
        "slice_fixedpoint_rows": len(rows),
        "slice_graph_rows": central_slice["slice_rows"],
        "max_pre_cancellation_terms": max(row.pre_cancellation_terms for row in rows),
        "min_pre_cancellation_terms": min(row.pre_cancellation_terms for row in rows),
        "max_slice_degree_bound": max(row.slice_degree_bound for row in rows),
        "min_degree_drop": min(row.degree_drop for row in rows),
        "max_degree_drop": max(row.degree_drop for row in rows),
    }


def main() -> None:
    summary = slice_fixedpoint_summary()
    print("h=5 central slice fixed-point skeleton")
    print("profiles are sparse upper bounds after l5=bar_l5=1; no fixed-point expansion is formed")
    for row in slice_fixedpoint_rows():
        print(
            f"  F{row.key_index}: high_terms={row.high_terms} "
            f"pre_cancel_terms<={row.pre_cancellation_terms} "
            f"slice_degree<={row.slice_degree_bound} "
            f"unsliced_total_degree<={row.unsliced_total_degree_bound} "
            f"degree_drop={row.degree_drop}"
        )
    print(
        "summary: "
        f"rows={summary['slice_fixedpoint_rows']} "
        f"slice_graph_rows={summary['slice_graph_rows']} "
        f"pre_cancel_terms={summary['min_pre_cancellation_terms']}.."
        f"{summary['max_pre_cancellation_terms']} "
        f"max_slice_degree={summary['max_slice_degree_bound']} "
        f"degree_drop={summary['min_degree_drop']}..{summary['max_degree_drop']}"
    )
    print("The weighted slice lowers degree bounds but leaves expansion-size bounds prohibitive.")
    print("H5_CENTRAL_SLICE_FIXEDPOINT_SKELETON_PASS")


if __name__ == "__main__":
    main()
