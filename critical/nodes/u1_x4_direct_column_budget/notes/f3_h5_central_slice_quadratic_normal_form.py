#!/usr/bin/env python3
"""Quadratic normal form for the h=5 central weighted-slice fixed map."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h5_basefree_reciprocal_system import reciprocal_slots
from f3_h5_central_slice_tangent import slice_tangent_summary
from f3_h5_central_weighted_slice import CENTRAL_SUBS, central_slice_summary
from f3_h5_reciprocal_compatibility_compiler import TOP


SLICE_TOP = TOP[1:]


@dataclass(frozen=True)
class QuadraticNormalForm:
    variable: str
    graph_component: sp.Expr
    fixed_component: sp.Expr
    fixed_equation: sp.Expr
    normalized_equation: sp.Expr


def truncate_total_degree(expression: sp.Expr, degree: int) -> sp.Expr:
    poly = sp.Poly(sp.expand(expression), *SLICE_TOP, domain=sp.QQ)
    result = sp.Integer(0)
    for monomial, coefficient in poly.terms():
        if sum(monomial) > degree:
            continue
        term = coefficient
        for variable, exponent in zip(SLICE_TOP, monomial):
            term *= variable**exponent
        result += term
    return sp.factor(result)


def slice_graph_components() -> tuple[sp.Expr, ...]:
    """Return the central graph in the order l6,l7,l8,l9 after conjugation."""
    central_slice_summary()
    slots = {slot[0]: slot for slot in reciprocal_slots()}
    components: list[sp.Expr] = []
    for key_index in (4, 3, 2, 1):
        _, denominator, high_part, _ = slots[key_index]
        components.append(sp.factor(high_part.subs(CENTRAL_SUBS) / denominator))
    return tuple(components)


def quadratic_graph_components() -> tuple[sp.Expr, ...]:
    return tuple(truncate_total_degree(component, 2) for component in slice_graph_components())


def quadratic_fixed_components() -> tuple[sp.Expr, ...]:
    graph = slice_graph_components()
    quadratic_graph = quadratic_graph_components()
    substitutions = dict(zip(SLICE_TOP, quadratic_graph))
    # This must be simultaneous: graph components contain the same variables.
    return tuple(
        truncate_total_degree(component.subs(substitutions, simultaneous=True), 2)
        for component in graph
    )


def normal_form_rows() -> tuple[QuadraticNormalForm, ...]:
    fixed = quadratic_fixed_components()
    graph = quadratic_graph_components()
    normalized = (
        SLICE_TOP[0],
        SLICE_TOP[1] - SLICE_TOP[0] ** 2 / 8,
        SLICE_TOP[2] - SLICE_TOP[0] * SLICE_TOP[1] / 4,
        SLICE_TOP[3] - SLICE_TOP[0] * SLICE_TOP[2] / 4 - SLICE_TOP[1] ** 2 / 8,
    )
    rows: list[QuadraticNormalForm] = []
    for variable, graph_component, fixed_component, normalized_equation in zip(
        SLICE_TOP, graph, fixed, normalized
    ):
        fixed_equation = sp.factor(variable - fixed_component)
        if sp.factor(fixed_equation - sp.Rational(3, 4) * normalized_equation) != 0:
            raise AssertionError((variable, fixed_equation, normalized_equation))
        rows.append(
            QuadraticNormalForm(
                variable=str(variable),
                graph_component=graph_component,
                fixed_component=fixed_component,
                fixed_equation=fixed_equation,
                normalized_equation=sp.expand(normalized_equation),
            )
        )
    return tuple(rows)


def quadratic_normal_form_summary() -> dict[str, int]:
    tangent = slice_tangent_summary()
    if tangent["fixed_equation_det_numerator"] != 81 or tangent["fixed_equation_det_denominator"] != 256:
        raise AssertionError(tangent)
    rows = normal_form_rows()
    expected_graph = {
        "l6": (2 * SLICE_TOP[0] * SLICE_TOP[2] + SLICE_TOP[1] ** 2 + 2 * SLICE_TOP[3]) / 4,
        "l7": (4 * SLICE_TOP[0] * SLICE_TOP[1] + 4 * SLICE_TOP[2] - SLICE_TOP[3] ** 2) / 8,
        "l8": (SLICE_TOP[0] ** 2 + 2 * SLICE_TOP[1] - SLICE_TOP[2] * SLICE_TOP[3]) / 4,
        "l9": (4 * SLICE_TOP[0] - 2 * SLICE_TOP[1] * SLICE_TOP[3] - SLICE_TOP[2] ** 2) / 8,
    }
    expected_fixed = {
        "l6": SLICE_TOP[0] / 4,
        "l7": (3 * SLICE_TOP[0] ** 2 + 8 * SLICE_TOP[1]) / 32,
        "l8": (3 * SLICE_TOP[0] * SLICE_TOP[1] + 4 * SLICE_TOP[2]) / 16,
        "l9": (6 * SLICE_TOP[0] * SLICE_TOP[2] + 3 * SLICE_TOP[1] ** 2 + 8 * SLICE_TOP[3]) / 32,
    }
    actual_graph = {row.variable: row.graph_component for row in rows}
    actual_fixed = {row.variable: row.fixed_component for row in rows}
    if any(sp.factor(actual_graph[name] - expected_graph[name]) != 0 for name in expected_graph):
        raise AssertionError(actual_graph)
    if any(sp.factor(actual_fixed[name] - expected_fixed[name]) != 0 for name in expected_fixed):
        raise AssertionError(actual_fixed)
    triangular_rows = 0
    for index, row in enumerate(rows):
        expression = row.normalized_equation
        current = SLICE_TOP[index]
        later = SLICE_TOP[index + 1 :]
        if sp.diff(expression, current) == 1 and all(sp.diff(expression, var) == 0 for var in later):
            triangular_rows += 1
    return {
        "quadratic_rows": len(rows),
        "triangular_rows": triangular_rows,
        "fixed_equation_common_denominator": 4,
        "fixed_equation_det_numerator": tangent["fixed_equation_det_numerator"],
        "fixed_equation_det_denominator": tangent["fixed_equation_det_denominator"],
        "max_graph_quadratic_terms": max(
            len(sp.Poly(row.graph_component, *SLICE_TOP, domain=sp.QQ).terms()) for row in rows
        ),
        "max_fixed_quadratic_terms": max(
            len(sp.Poly(row.fixed_component, *SLICE_TOP, domain=sp.QQ).terms()) for row in rows
        ),
    }


def main() -> None:
    summary = quadratic_normal_form_summary()
    print("h=5 central slice quadratic normal form")
    print("variables: l6,l7,l8,l9")
    print("quadratic graph components:")
    for row in normal_form_rows():
        print(f"  G_{row.variable} = {row.graph_component}")
    print("quadratic fixed-map components:")
    for row in normal_form_rows():
        print(f"  F_{row.variable} = {row.fixed_component}")
    print("normalized fixed equations through degree two:")
    for row in normal_form_rows():
        print(f"  {row.normalized_equation} = 0")
    print(
        "summary: "
        f"rows={summary['quadratic_rows']} "
        f"triangular_rows={summary['triangular_rows']} "
        f"max_graph_terms={summary['max_graph_quadratic_terms']} "
        f"max_fixed_terms={summary['max_fixed_quadratic_terms']} "
        f"linear_det={summary['fixed_equation_det_numerator']}/"
        f"{summary['fixed_equation_det_denominator']}"
    )
    print("This is a local degree-two normal form; it does not expand the global fixed equations.")
    print("H5_CENTRAL_SLICE_QUADRATIC_NORMAL_FORM_PASS")


if __name__ == "__main__":
    main()
