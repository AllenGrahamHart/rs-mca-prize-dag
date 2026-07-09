#!/usr/bin/env python3
"""Compile the central-chart graph form of the h=5 reciprocal gate."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h5_basefree_reciprocal_system import ALL_BARS, pairwise_polynomial, reciprocal_slots
from f3_h5_reciprocal_compatibility_compiler import TOP
from f3_h5_x83_triangular_norm_gate import LOCATOR


CENTER_BAR = ALL_BARS[0]
VARIABLES = TOP + ALL_BARS


@dataclass(frozen=True)
class CentralGraphRow:
    key_index: int
    solved_bar: str
    denominator: int
    high_terms: int
    high_total_degree: int
    graph_terms: int
    graph_total_degree: int


def central_graph_rows() -> tuple[CentralGraphRow, ...]:
    slots = {slot[0]: slot for slot in reciprocal_slots()}
    rows: list[CentralGraphRow] = []
    for key_index in range(1, 5):
        slot = slots[key_index]
        denominator, high_part, solved_bar = slot[1], slot[2], slot[3]
        equation = pairwise_polynomial(slot, slots[5])
        expected = sp.expand(CENTER_BAR * high_part - denominator * solved_bar * LOCATOR[5])
        if sp.factor(equation - expected) != 0:
            raise AssertionError((key_index, sp.factor(equation - expected)))
        if sp.diff(equation, solved_bar) != -denominator * LOCATOR[5]:
            raise AssertionError((key_index, sp.diff(equation, solved_bar)))
        other_bars = [bar for bar in ALL_BARS[1:] if bar != solved_bar]
        if any(sp.diff(equation, bar) != 0 for bar in other_bars):
            raise AssertionError((key_index, solved_bar, other_bars))

        high_poly = sp.Poly(high_part, *TOP, domain=sp.ZZ)
        graph_poly = sp.Poly(equation, *VARIABLES, domain=sp.ZZ)
        rows.append(
            CentralGraphRow(
                key_index=key_index,
                solved_bar=str(solved_bar),
                denominator=denominator,
                high_terms=len(high_poly.terms()),
                high_total_degree=high_poly.total_degree(),
                graph_terms=len(graph_poly.terms()),
                graph_total_degree=graph_poly.total_degree(),
            )
        )
    return tuple(rows)


def central_graph_summary() -> dict[str, int]:
    rows = central_graph_rows()
    expected = {
        1: ("bar_l9", 16384, 22, 9, 23, 10),
        2: ("bar_l8", 16384, 18, 8, 19, 9),
        3: ("bar_l7", 256, 13, 7, 14, 8),
        4: ("bar_l6", 512, 10, 6, 11, 7),
    }
    actual = {
        row.key_index: (
            row.solved_bar,
            row.denominator,
            row.high_terms,
            row.high_total_degree,
            row.graph_terms,
            row.graph_total_degree,
        )
        for row in rows
    }
    if actual != expected:
        raise AssertionError(actual)
    return {
        "graph_rows": len(rows),
        "total_graph_terms": sum(row.graph_terms for row in rows),
        "max_graph_degree": max(row.graph_total_degree for row in rows),
        "max_high_degree": max(row.high_total_degree for row in rows),
        "max_high_terms": max(row.high_terms for row in rows),
    }


def main() -> None:
    summary = central_graph_summary()
    print("h=5 central reciprocal chart graph")
    print("on bar_l5 != 0, l5 != 0 and Cj5 solves bar_l(10-j)")
    for row in central_graph_rows():
        print(
            f"  C{row.key_index}5: solves={row.solved_bar} "
            f"denominator={row.denominator} high_terms={row.high_terms} "
            f"high_degree={row.high_total_degree} graph_terms={row.graph_terms} "
            f"graph_degree={row.graph_total_degree}"
        )
    print(
        "summary: "
        f"graph_rows={summary['graph_rows']} "
        f"total_graph_terms={summary['total_graph_terms']} "
        f"max_graph_degree={summary['max_graph_degree']} "
        f"max_high_degree={summary['max_high_degree']} "
        f"max_high_terms={summary['max_high_terms']}"
    )
    print("H5_CENTRAL_CHART_GRAPH_PASS")


if __name__ == "__main__":
    main()
