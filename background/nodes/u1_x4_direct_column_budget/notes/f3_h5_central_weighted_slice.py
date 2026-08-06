#!/usr/bin/env python3
"""Weighted central-slice compiler for the h=5 reciprocal graph."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h5_basefree_reciprocal_system import (
    ALL_BARS,
    pairwise_polynomial,
    reciprocal_slots,
)
from f3_h5_reciprocal_compatibility_compiler import TOP
from f3_h5_weighted_homogeneity import WEIGHTS, weighted_homogeneity_summary
from f3_h5_x83_triangular_norm_gate import LOCATOR


TAU = sp.symbols("tau")
CENTRAL_SUBS = {LOCATOR[5]: sp.Integer(1), ALL_BARS[0]: sp.Integer(1)}
SLICE_VARIABLES = TOP[1:] + ALL_BARS[1:]


@dataclass(frozen=True)
class CentralSliceRow:
    key_index: int
    solved_bar: str
    denominator: int
    high_terms: int
    high_total_degree: int
    equation_terms: int
    equation_total_degree: int


def weighted_scale(expr: sp.Expr) -> sp.Expr:
    return sp.expand(expr.xreplace({var: TAU ** WEIGHTS[var] * var for var in TOP + ALL_BARS}))


def verify_central_action() -> tuple[int, int]:
    weighted_homogeneity_summary()
    slots = {slot[0]: slot for slot in reciprocal_slots()}
    checked = 0
    min_weight = 10**9
    for key_index in range(1, 5):
        equation = pairwise_polynomial(slots[key_index], slots[5])
        # The high part is not a variable; use the already-proved row weight
        # through direct Laurent action on the full central equation.
        scaled = weighted_scale(equation)
        row_weight = 5 - key_index
        if sp.factor(sp.together(scaled - TAU**row_weight * equation)) != 0:
            raise AssertionError((key_index, row_weight, scaled, equation))
        checked += 1
        min_weight = min(min_weight, row_weight)
    if WEIGHTS[LOCATOR[5]] != 5 or WEIGHTS[ALL_BARS[0]] != -5:
        raise AssertionError((LOCATOR[5], ALL_BARS[0], WEIGHTS[LOCATOR[5]], WEIGHTS[ALL_BARS[0]]))
    return checked, min_weight


def central_slice_rows() -> tuple[CentralSliceRow, ...]:
    slots = {slot[0]: slot for slot in reciprocal_slots()}
    rows: list[CentralSliceRow] = []
    for key_index in range(1, 5):
        slot = slots[key_index]
        denominator, high_part, solved_bar = slot[1], slot[2], slot[3]
        equation = pairwise_polynomial(slot, slots[5])
        normalized = sp.factor(equation.subs(CENTRAL_SUBS))
        expected = sp.factor(high_part.subs(CENTRAL_SUBS) - denominator * solved_bar)
        if sp.factor(normalized - expected) != 0:
            raise AssertionError((key_index, normalized, expected))
        if sp.diff(normalized, solved_bar) != -denominator:
            raise AssertionError((key_index, sp.diff(normalized, solved_bar), denominator))
        other_bars = [bar for bar in ALL_BARS[1:] if bar != solved_bar]
        if any(sp.diff(normalized, bar) != 0 for bar in other_bars):
            raise AssertionError((key_index, solved_bar, other_bars))

        high_poly = sp.Poly(high_part.subs(CENTRAL_SUBS), *TOP[1:], domain=sp.ZZ)
        equation_poly = sp.Poly(normalized, *SLICE_VARIABLES, domain=sp.ZZ)
        rows.append(
            CentralSliceRow(
                key_index=key_index,
                solved_bar=str(solved_bar),
                denominator=denominator,
                high_terms=len(high_poly.terms()),
                high_total_degree=high_poly.total_degree(),
                equation_terms=len(equation_poly.terms()),
                equation_total_degree=equation_poly.total_degree(),
            )
        )
    return tuple(rows)


def central_slice_summary() -> dict[str, int]:
    action_checked, min_weight = verify_central_action()
    rows = central_slice_rows()
    expected = {
        1: ("bar_l9", 16384, 22, 9, 23, 9),
        2: ("bar_l8", 16384, 18, 8, 19, 8),
        3: ("bar_l7", 256, 13, 7, 14, 7),
        4: ("bar_l6", 512, 10, 6, 11, 6),
    }
    actual = {
        row.key_index: (
            row.solved_bar,
            row.denominator,
            row.high_terms,
            row.high_total_degree,
            row.equation_terms,
            row.equation_total_degree,
        )
        for row in rows
    }
    if actual != expected:
        raise AssertionError(actual)
    return {
        "action_rows_checked": action_checked,
        "min_central_weight": min_weight,
        "slice_rows": len(rows),
        "total_slice_terms": sum(row.equation_terms for row in rows),
        "max_slice_degree": max(row.equation_total_degree for row in rows),
        "max_high_terms": max(row.high_terms for row in rows),
    }


def main() -> None:
    summary = central_slice_summary()
    print("h=5 central weighted slice")
    print("algebraic G_m action uses weights l5..l9=5..1 and bars=-5..-1")
    print("central unit l5*bar_l5 is invariant, so the central chart may be sliced at l5=bar_l5=1 for emptiness proofs")
    for row in central_slice_rows():
        print(
            f"  C{row.key_index}5 slice: solves={row.solved_bar} "
            f"denominator={row.denominator} high_terms={row.high_terms} "
            f"high_degree={row.high_total_degree} equation_terms={row.equation_terms} "
            f"equation_degree={row.equation_total_degree}"
        )
    print(
        "summary: "
        f"action_rows_checked={summary['action_rows_checked']} "
        f"min_central_weight={summary['min_central_weight']} "
        f"slice_rows={summary['slice_rows']} "
        f"total_slice_terms={summary['total_slice_terms']} "
        f"max_slice_degree={summary['max_slice_degree']} "
        f"max_high_terms={summary['max_high_terms']}"
    )
    print("This is an algebraic emptiness slice, not an official finite-row orbit quotient.")
    print("H5_CENTRAL_WEIGHTED_SLICE_PASS")


if __name__ == "__main__":
    main()
