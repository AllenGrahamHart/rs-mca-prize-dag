#!/usr/bin/env python3
"""Compile h=5 unit-norm reciprocal equations for the x83 norm gate."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h5_basefree_reciprocal_system import ALL_BARS
from f3_h5_reciprocal_compatibility_compiler import TOP, reciprocal_part
from f3_h5_x83_triangular_norm_gate import LOCATOR


VARIABLES = TOP + ALL_BARS
CONJUGATE_TOP = {TOP[index]: ALL_BARS[index] for index in range(len(TOP))}


@dataclass(frozen=True)
class UnitNormRow:
    name: str
    terms: int
    total_degree: int
    top_total_degree: int
    bar_total_degree: int
    top_degrees: tuple[int, ...]
    bar_degrees: tuple[int, ...]


def conjugate_high_part(poly: sp.Expr) -> sp.Expr:
    return sp.expand(poly.xreplace(CONJUGATE_TOP))


def unit_norm_polynomial(key_index: int) -> sp.Expr:
    denominator, high_part, bar_var = reciprocal_part(key_index)
    high_bar = conjugate_high_part(high_part)
    paired_top = LOCATOR[10 - key_index]
    return sp.factor(high_part * high_bar - denominator * denominator * paired_top * bar_var)


def unit_norm_rows() -> tuple[UnitNormRow, ...]:
    rows = []
    for key_index in range(1, 5):
        polynomial = unit_norm_polynomial(key_index)
        poly = sp.Poly(polynomial, *VARIABLES, domain=sp.ZZ)
        top_total = max(sum(monom[: len(TOP)]) for monom, _ in poly.terms())
        bar_total = max(sum(monom[len(TOP) :]) for monom, _ in poly.terms())
        rows.append(
            UnitNormRow(
                name=f"N{key_index}",
                terms=len(poly.terms()),
                total_degree=poly.total_degree(),
                top_total_degree=top_total,
                bar_total_degree=bar_total,
                top_degrees=tuple(poly.degree(variable) for variable in TOP),
                bar_degrees=tuple(poly.degree(variable) for variable in ALL_BARS),
            )
        )
    return tuple(rows)


def unit_norm_summary() -> dict[str, int]:
    expected = {
        "N1": (485, 18, 9, 9, (1, 2, 2, 4, 9), (1, 2, 2, 4, 9)),
        "N2": (325, 16, 8, 8, (1, 2, 2, 4, 8), (1, 2, 2, 4, 8)),
        "N3": (170, 14, 7, 7, (1, 1, 2, 3, 7), (1, 1, 2, 3, 7)),
        "N4": (101, 12, 6, 6, (1, 1, 2, 3, 6), (1, 1, 2, 3, 6)),
    }
    actual = {
        row.name: (
            row.terms,
            row.total_degree,
            row.top_total_degree,
            row.bar_total_degree,
            row.top_degrees,
            row.bar_degrees,
        )
        for row in unit_norm_rows()
    }
    if actual != expected:
        raise AssertionError(actual)
    return {
        "equations": len(actual),
        "max_terms": max(row[0] for row in actual.values()),
        "max_total_degree": max(row[1] for row in actual.values()),
        "max_top_total_degree": max(row[2] for row in actual.values()),
        "max_bar_total_degree": max(row[3] for row in actual.values()),
    }


def main() -> None:
    summary = unit_norm_summary()
    print("h=5 unit-norm reciprocal gate")
    print("using delta*bar_delta=1 for the support product")
    for row in unit_norm_rows():
        print(
            f"  {row.name}: terms={row.terms} total={row.total_degree} "
            f"top_total={row.top_total_degree} bar_total={row.bar_total_degree} "
            f"top_degrees={row.top_degrees} "
            f"bar_degrees(bar_l5..bar_l9)={row.bar_degrees}"
        )
    print(
        "summary: "
        f"equations={summary['equations']} "
        f"max_total_degree={summary['max_total_degree']} "
        f"max_top_total_degree={summary['max_top_total_degree']} "
        f"max_bar_total_degree={summary['max_bar_total_degree']} "
        f"max_terms={summary['max_terms']}"
    )
    print("H5_UNIT_NORM_RECIPROCAL_GATE_PASS")


if __name__ == "__main__":
    main()
