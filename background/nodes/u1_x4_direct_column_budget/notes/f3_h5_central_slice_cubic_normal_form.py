#!/usr/bin/env python3
"""Cubic normal form for the h=5 central weighted-slice fixed map."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h5_central_slice_quadratic_normal_form import (
    SLICE_TOP,
    slice_graph_components,
    truncate_total_degree,
)
from f3_h5_central_slice_tangent import slice_tangent_summary


@dataclass(frozen=True)
class CubicNormalForm:
    variable: str
    graph_component: sp.Expr
    fixed_equation: sp.Expr


def cubic_graph_components() -> tuple[sp.Expr, ...]:
    return tuple(truncate_total_degree(component, 3) for component in slice_graph_components())


def cubic_fixed_components() -> tuple[sp.Expr, ...]:
    graph = slice_graph_components()
    cubic_graph = cubic_graph_components()
    substitutions = dict(zip(SLICE_TOP, cubic_graph))
    return tuple(
        truncate_total_degree(component.subs(substitutions, simultaneous=True), 3)
        for component in graph
    )


def cubic_normal_form_rows() -> tuple[CubicNormalForm, ...]:
    rows: list[CubicNormalForm] = []
    for variable, graph_component, fixed_component in zip(
        SLICE_TOP, cubic_graph_components(), cubic_fixed_components()
    ):
        rows.append(
            CubicNormalForm(
                variable=str(variable),
                graph_component=sp.factor(graph_component),
                fixed_equation=sp.factor(variable - fixed_component),
            )
        )
    return tuple(rows)


def cubic_normal_form_summary() -> dict[str, int]:
    tangent = slice_tangent_summary()
    if tangent["fixed_equation_det_numerator"] != 81 or tangent["fixed_equation_det_denominator"] != 256:
        raise AssertionError(tangent)

    l6, l7, l8, l9 = SLICE_TOP
    expected_graph = {
        "l6": (
            4 * l6 * l8
            - 3 * l6 * l9**2
            + 2 * l7**2
            - 6 * l7 * l8 * l9
            - l8**3
            + 4 * l9
        )
        / 8,
        "l7": (
            4 * l6 * l7
            - 4 * l6 * l8 * l9
            - 2 * l7**2 * l9
            - 3 * l7 * l8**2
            + 4 * l8
            - l9**2
        )
        / 8,
        "l8": (
            4 * l6**2
            - 8 * l6 * l7 * l9
            - 2 * l6 * l8**2
            - 4 * l7**2 * l8
            + 8 * l7
            - 4 * l8 * l9
            + l9**3
        )
        / 16,
        "l9": -(
            4 * l6**2 * l9
            + 4 * l6 * l7 * l8
            - 8 * l6
            + 4 * l7 * l9
            + 2 * l8**2
            - 3 * l8 * l9**2
        )
        / 16,
    }
    expected_fixed_equations = {
        "l6": (7 * l6**2 * l9 - 2 * l6 * l7 * l8 + 48 * l6 - 3 * l7**3) / 64,
        "l7": -(6 * l6**2 - 10 * l6 * l7 * l9 + 3 * l6 * l8**2 - 7 * l7**2 * l8 - 48 * l7)
        / 64,
        "l8": (
            3 * l6**3
            - 24 * l6 * l7
            + 20 * l6 * l8 * l9
            + 6 * l7**2 * l9
            + 26 * l7 * l8**2
            + 96 * l8
        )
        / 128,
        "l9": (
            9 * l6**2 * l7
            - 24 * l6 * l8
            + 26 * l6 * l9**2
            - 12 * l7**2
            + 44 * l7 * l8 * l9
            + 6 * l8**3
            + 96 * l9
        )
        / 128,
    }
    rows = cubic_normal_form_rows()
    actual_graph = {row.variable: row.graph_component for row in rows}
    actual_fixed_equations = {row.variable: row.fixed_equation for row in rows}
    if any(sp.factor(actual_graph[name] - expected_graph[name]) != 0 for name in expected_graph):
        raise AssertionError(actual_graph)
    if any(
        sp.factor(actual_fixed_equations[name] - expected_fixed_equations[name]) != 0
        for name in expected_fixed_equations
    ):
        raise AssertionError(actual_fixed_equations)

    fixed_terms = [
        len(sp.Poly(row.fixed_equation, *SLICE_TOP, domain=sp.QQ).terms())
        for row in rows
    ]
    graph_terms = [
        len(sp.Poly(row.graph_component, *SLICE_TOP, domain=sp.QQ).terms())
        for row in rows
    ]
    return {
        "cubic_rows": len(rows),
        "min_fixed_terms": min(fixed_terms),
        "max_fixed_terms": max(fixed_terms),
        "min_graph_terms": min(graph_terms),
        "max_graph_terms": max(graph_terms),
        "fixed_equation_det_numerator": tangent["fixed_equation_det_numerator"],
        "fixed_equation_det_denominator": tangent["fixed_equation_det_denominator"],
    }


def main() -> None:
    summary = cubic_normal_form_summary()
    print("h=5 central slice cubic normal form")
    print("variables: l6,l7,l8,l9")
    print("cubic graph components:")
    for row in cubic_normal_form_rows():
        print(f"  G_{row.variable} = {row.graph_component}")
    print("fixed equations through degree three:")
    for row in cubic_normal_form_rows():
        print(f"  {row.fixed_equation} = 0")
    print(
        "summary: "
        f"rows={summary['cubic_rows']} "
        f"graph_terms={summary['min_graph_terms']}..{summary['max_graph_terms']} "
        f"fixed_terms={summary['min_fixed_terms']}..{summary['max_fixed_terms']} "
        f"linear_det={summary['fixed_equation_det_numerator']}/"
        f"{summary['fixed_equation_det_denominator']}"
    )
    print("This is a local degree-three normal form; it does not prove central-chart emptiness.")
    print("H5_CENTRAL_SLICE_CUBIC_NORMAL_FORM_PASS")


if __name__ == "__main__":
    main()
