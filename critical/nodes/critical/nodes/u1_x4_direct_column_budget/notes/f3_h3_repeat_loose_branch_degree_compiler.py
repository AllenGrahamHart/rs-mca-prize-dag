#!/usr/bin/env python3
"""Degree compiler for the loose collision-branch membership maps."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h3_repeat_loose_branch_slope_maps import branch_slope_map


AVAR, XVAR = sp.symbols("a X")


@dataclass(frozen=True)
class MapDegree:
    name: str
    numerator: sp.Expr
    denominator: sp.Expr
    deg_a: int
    deg_x: int
    total_degree: int


@dataclass(frozen=True)
class BranchDegreeBudget:
    label: str
    maps: tuple[MapDegree, ...]
    sum_a_degrees: int
    sum_total_degrees: int
    max_a_degree: int
    max_x_degree: int
    max_total_degree: int


def membership_map(expression: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    numerator, denominator = sp.together(1 + XVAR * expression).as_numer_denom()
    if sp.degree(denominator, XVAR) != 0:
        raise AssertionError((expression, numerator, denominator, "denominator depends on X"))
    return sp.factor(numerator), sp.factor(denominator)


def degree_row(name: str, expression: sp.Expr) -> MapDegree:
    numerator, denominator = membership_map(expression)
    if sp.degree(numerator, XVAR) > 1:
        raise AssertionError((name, numerator, "unexpected X-degree"))
    deg_a = max(sp.degree(numerator, AVAR), sp.degree(denominator, AVAR))
    deg_x = sp.degree(numerator, XVAR)
    total_degree = max(
        sp.Poly(numerator, AVAR, XVAR).total_degree(),
        sp.Poly(denominator, AVAR, XVAR).total_degree(),
    )
    return MapDegree(
        name=name,
        numerator=numerator,
        denominator=denominator,
        deg_a=deg_a,
        deg_x=deg_x,
        total_degree=total_degree,
    )


def branch_degree_budget(label: str) -> BranchDegreeBudget:
    rows = tuple(degree_row(name, expression) for name, expression in branch_slope_map(label).expressions)
    return BranchDegreeBudget(
        label=label,
        maps=rows,
        sum_a_degrees=sum(row.deg_a for row in rows),
        sum_total_degrees=sum(row.total_degree for row in rows),
        max_a_degree=max(row.deg_a for row in rows),
        max_x_degree=max(row.deg_x for row in rows),
        max_total_degree=max(row.total_degree for row in rows),
    )


def cleared_degree_bounds(
    budget: BranchDegreeBudget, subgroup_order: int, aux_a: int, aux_x: int, aux_y: int
) -> dict[str, int]:
    if min(subgroup_order, aux_a, aux_x, aux_y) < 1:
        raise ValueError((subgroup_order, aux_a, aux_x, aux_y))
    y_power = subgroup_order * (aux_y - 1)
    return {
        "a_degree": (aux_a - 1) + y_power * budget.sum_a_degrees,
        "x_degree": (aux_x - 1) + y_power * len(budget.maps),
        "total_degree": (aux_a - 1) + (aux_x - 1) + y_power * budget.sum_total_degrees,
    }


def main() -> None:
    print("h=3 repeat loose branch degree compiler")
    for label in ("A", "B"):
        budget = branch_degree_budget(label)
        print(
            f"branch_{label}: maps={len(budget.maps)} "
            f"sum_a_degrees={budget.sum_a_degrees} "
            f"sum_total_degrees={budget.sum_total_degrees} "
            f"max_a_degree={budget.max_a_degree} "
            f"max_x_degree={budget.max_x_degree} "
            f"max_total_degree={budget.max_total_degree}"
        )
        for row in budget.maps:
            print(
                f"  {row.name}: P={sp.factor(row.numerator)} Q={sp.factor(row.denominator)} "
                f"deg_a={row.deg_a} deg_x={row.deg_x} total={row.total_degree}"
            )
        sample = cleared_degree_bounds(budget, subgroup_order=32, aux_a=16, aux_x=16, aux_y=4)
        print(
            f"  sample_clear_n32_A16_X16_B4: "
            f"a_degree={sample['a_degree']} x_degree={sample['x_degree']} "
            f"total_degree={sample['total_degree']}"
        )
    print("degree formula: a <= A-1+n(B-1)S_a, x <= X-1+8n(B-1)")
    print("total <= A+X-2+n(B-1)S_total")
    print("H3_REPEAT_LOOSE_BRANCH_DEGREE_COMPILER_PASS")


if __name__ == "__main__":
    main()
