#!/usr/bin/env python3
"""Compile the chart-7 graph form of the h=8 reciprocal target."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h8_basefree_reciprocal_system import (
    ALL_BARS,
    TOP,
    pairwise_polynomial,
    reciprocal_slots,
)
from f3_h8_reciprocal_compatibility_compiler import reciprocal_part
from f3_h8_unit_norm_reciprocal_gate import unit_norm_polynomial
from f3_h8_x83_triangular_obstruction import LOCATOR


CHART = 7
VARIABLES = TOP + ALL_BARS


@dataclass(frozen=True)
class Chart7GraphRow:
    target_slot: int
    solved_bar: str
    denominator_scalar: int
    numerator_terms: int
    numerator_total_degree: int
    graph_terms: int
    graph_total_degree: int
    derivative_sign: int


def chart7_part(target_slot: int) -> tuple[int, sp.Expr, sp.Symbol]:
    if target_slot == 8:
        return 1, LOCATOR[8], ALL_BARS[0]
    return reciprocal_part(target_slot)


def chart7_pairwise_equation(target_slot: int) -> sp.Expr:
    slots = {slot[0]: slot for slot in reciprocal_slots()}
    if target_slot < CHART:
        return pairwise_polynomial(slots[target_slot], slots[CHART])
    if target_slot == 8:
        return pairwise_polynomial(slots[CHART], slots[target_slot])
    raise AssertionError(target_slot)


def chart7_expected_equation(target_slot: int) -> sp.Expr:
    chart_denominator, chart_part, chart_bar = reciprocal_part(CHART)
    denominator, part, solved_bar = chart7_part(target_slot)
    if target_slot < CHART:
        return sp.expand(chart_denominator * chart_bar * part - denominator * solved_bar * chart_part)
    if target_slot == 8:
        return sp.expand(solved_bar * chart_part - chart_denominator * chart_bar * part)
    raise AssertionError(target_slot)


def chart7_graph_rows() -> tuple[Chart7GraphRow, ...]:
    _, chart_part, _ = reciprocal_part(CHART)
    rows: list[Chart7GraphRow] = []
    for target_slot in (1, 2, 3, 4, 5, 6, 8):
        denominator, part, solved_bar = chart7_part(target_slot)
        equation = chart7_pairwise_equation(target_slot)
        expected = chart7_expected_equation(target_slot)
        if sp.factor(equation - expected) != 0:
            raise AssertionError((target_slot, sp.factor(equation - expected)))

        derivative = sp.diff(equation, solved_bar)
        if target_slot < CHART:
            expected_derivative = -denominator * chart_part
            derivative_sign = -1
        else:
            expected_derivative = chart_part
            derivative_sign = 1
        if derivative != expected_derivative:
            raise AssertionError((target_slot, derivative, expected_derivative))

        other_bars = [bar for bar in ALL_BARS if bar != solved_bar and str(bar) != "bar_c9"]
        if any(sp.diff(equation, bar) != 0 for bar in other_bars):
            raise AssertionError((target_slot, solved_bar, other_bars))

        numerator_poly = sp.Poly(part, *TOP, domain=sp.ZZ)
        graph_poly = sp.Poly(equation, *VARIABLES, domain=sp.ZZ)
        rows.append(
            Chart7GraphRow(
                target_slot=target_slot,
                solved_bar=str(solved_bar),
                denominator_scalar=denominator,
                numerator_terms=len(numerator_poly.terms()),
                numerator_total_degree=numerator_poly.total_degree(),
                graph_terms=len(graph_poly.terms()),
                graph_total_degree=graph_poly.total_degree(),
                derivative_sign=derivative_sign,
            )
        )
    return tuple(rows)


def chart7_graph_summary() -> dict[str, int]:
    rows = chart7_graph_rows()
    _, chart_part, chart_bar = reciprocal_part(CHART)
    unit = unit_norm_polynomial(CHART)
    unit_poly = sp.Poly(unit, *VARIABLES, domain=sp.ZZ)
    chart_poly = sp.Poly(chart_part, *TOP, domain=sp.ZZ)

    expected = {
        1: ("bar_c15", 33_554_432, 140, 15, 169, 16, -1),
        2: ("bar_c14", 16_777_216, 115, 14, 144, 15, -1),
        3: ("bar_c13", 4_194_304, 89, 13, 118, 14, -1),
        4: ("bar_c12", 2_097_152, 70, 12, 99, 13, -1),
        5: ("bar_c11", 262_144, 52, 11, 81, 12, -1),
        6: ("bar_c10", 131_072, 40, 10, 69, 11, -1),
        8: ("bar_c8", 1, 1, 1, 30, 10, 1),
    }
    actual = {
        row.target_slot: (
            row.solved_bar,
            row.denominator_scalar,
            row.numerator_terms,
            row.numerator_total_degree,
            row.graph_terms,
            row.graph_total_degree,
            row.derivative_sign,
        )
        for row in rows
    }
    if actual != expected:
        raise AssertionError(actual)
    if str(chart_bar) != "bar_c9":
        raise AssertionError(chart_bar)

    return {
        "chart": CHART,
        "graph_rows": len(rows),
        "total_graph_terms": sum(row.graph_terms for row in rows),
        "max_graph_degree": max(row.graph_total_degree for row in rows),
        "max_graph_terms": max(row.graph_terms for row in rows),
        "chart_part_terms": len(chart_poly.terms()),
        "chart_part_total_degree": chart_poly.total_degree(),
        "unit_terms": len(unit_poly.terms()),
        "unit_total_degree": unit_poly.total_degree(),
        "solved_bars": len({row.solved_bar for row in rows}),
    }


def main() -> None:
    summary = chart7_graph_summary()
    print("h=8 chart-7 reciprocal graph reduction")
    print("on bar_c9 != 0, official conjugation gives c9 != 0")
    print("N7 then forces P7 and conjugate(P7) nonzero, so the graph denominators are live")
    for row in chart7_graph_rows():
        print(
            f"  C{min(row.target_slot, CHART)}{max(row.target_slot, CHART)}: "
            f"solves={row.solved_bar} denominator_scalar={row.denominator_scalar} "
            f"numerator_terms={row.numerator_terms} "
            f"numerator_degree={row.numerator_total_degree} "
            f"graph_terms={row.graph_terms} graph_degree={row.graph_total_degree}"
        )
    print(
        "summary: "
        f"chart={summary['chart']} "
        f"graph_rows={summary['graph_rows']} "
        f"solved_bars={summary['solved_bars']} "
        f"total_graph_terms={summary['total_graph_terms']} "
        f"max_graph_terms={summary['max_graph_terms']} "
        f"max_graph_degree={summary['max_graph_degree']} "
        f"P7_terms={summary['chart_part_terms']} "
        f"P7_degree={summary['chart_part_total_degree']} "
        f"N7_terms={summary['unit_terms']} "
        f"N7_degree={summary['unit_total_degree']}"
    )
    print("H8_CHART7_GRAPH_REDUCTION_PASS")


if __name__ == "__main__":
    main()
