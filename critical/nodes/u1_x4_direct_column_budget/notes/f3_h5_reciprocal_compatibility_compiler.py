#!/usr/bin/env python3
"""Compile h=5 reciprocal compatibility equations for the x83 norm gate."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h5_x83_triangular_norm_gate import (
    BAR_HIGH,
    LOCATOR,
    integer_denominator,
    low_obstructions,
    require_triangular,
)


TOP = tuple(LOCATOR[5:10])
BARS = tuple(BAR_HIGH[index] for index in range(6, 10))


@dataclass(frozen=True)
class ReciprocalRow:
    key_index: int
    denominator: int
    bar_name: str
    terms: int
    top_total_degree: int
    top_degrees: tuple[int, ...]


@dataclass(frozen=True)
class CompatibilityRow:
    name: str
    terms: int
    total_degree: int
    top_total_degree: int
    bar_total_degree: int
    top_degrees: tuple[int, ...]
    bar_degrees: tuple[int, ...]


def reciprocal_part(key_index: int) -> tuple[int, sp.Expr, sp.Symbol]:
    expr = low_obstructions()[key_index]
    denominator = integer_denominator(expr)
    cleared = sp.expand(expr * denominator)
    poly = sp.Poly(cleared, *LOCATOR, domain=sp.ZZ)
    require_triangular(key_index, poly, denominator)
    high_part = sp.expand(cleared + denominator * LOCATOR[key_index])
    bar_var = BAR_HIGH[10 - key_index]
    return denominator, sp.factor(high_part), bar_var


def reciprocal_rows() -> tuple[ReciprocalRow, ...]:
    rows = []
    for key_index in range(1, 5):
        denominator, high_part, bar_var = reciprocal_part(key_index)
        poly = sp.Poly(high_part, *TOP, domain=sp.ZZ)
        rows.append(
            ReciprocalRow(
                key_index=key_index,
                denominator=denominator,
                bar_name=str(bar_var),
                terms=len(poly.terms()),
                top_total_degree=poly.total_degree(),
                top_degrees=tuple(poly.degree(variable) for variable in TOP),
            )
        )
    return tuple(rows)


def compatibility_polynomial(key_index: int, base_index: int = 4) -> sp.Expr:
    denominator, high_part, bar_var = reciprocal_part(key_index)
    base_denominator, base_high_part, base_bar_var = reciprocal_part(base_index)
    return sp.factor(
        base_denominator * base_bar_var * high_part
        - denominator * bar_var * base_high_part
    )


def compatibility_rows() -> tuple[CompatibilityRow, ...]:
    rows = []
    variables = TOP + BARS
    for key_index in range(1, 4):
        polynomial = compatibility_polynomial(key_index, 4)
        poly = sp.Poly(polynomial, *variables, domain=sp.ZZ)
        top_total = max(sum(monom[: len(TOP)]) for monom, _ in poly.terms())
        bar_total = max(sum(monom[len(TOP) :]) for monom, _ in poly.terms())
        rows.append(
            CompatibilityRow(
                name=f"C{key_index}4",
                terms=len(poly.terms()),
                total_degree=poly.total_degree(),
                top_total_degree=top_total,
                bar_total_degree=bar_total,
                top_degrees=tuple(poly.degree(variable) for variable in TOP),
                bar_degrees=tuple(poly.degree(variable) for variable in BARS),
            )
        )
    return tuple(rows)


def compatibility_summary() -> dict[str, int]:
    reciprocal_expected = {
        1: (16384, "bar_l9", 22, 9, (1, 2, 2, 4, 9)),
        2: (16384, "bar_l8", 18, 8, (1, 2, 2, 4, 8)),
        3: (256, "bar_l7", 13, 7, (1, 1, 2, 3, 7)),
        4: (512, "bar_l6", 10, 6, (1, 1, 2, 3, 6)),
    }
    reciprocal_actual = {
        row.key_index: (
            row.denominator,
            row.bar_name,
            row.terms,
            row.top_total_degree,
            row.top_degrees,
        )
        for row in reciprocal_rows()
    }
    if reciprocal_actual != reciprocal_expected:
        raise AssertionError(reciprocal_actual)

    compatibility_expected = {
        "C14": (32, 10, 9, 1, (1, 2, 2, 4, 9), (1, 0, 0, 1)),
        "C24": (28, 9, 8, 1, (1, 2, 2, 4, 8), (1, 0, 1, 0)),
        "C34": (23, 8, 7, 1, (1, 1, 2, 3, 7), (1, 1, 0, 0)),
    }
    compatibility_actual = {
        row.name: (
            row.terms,
            row.total_degree,
            row.top_total_degree,
            row.bar_total_degree,
            row.top_degrees,
            row.bar_degrees,
        )
        for row in compatibility_rows()
    }
    if compatibility_actual != compatibility_expected:
        raise AssertionError(compatibility_actual)

    return {
        "reciprocal_equations": len(reciprocal_actual),
        "compatibility_equations": len(compatibility_actual),
        "max_reciprocal_top_degree": max(row[3] for row in reciprocal_actual.values()),
        "max_compatibility_total_degree": max(row[1] for row in compatibility_actual.values()),
        "max_compatibility_terms": max(row[0] for row in compatibility_actual.values()),
    }


def main() -> None:
    summary = compatibility_summary()
    print("h=5 reciprocal compatibility compiler")
    print("reciprocal rows P_j = D_j delta*bar_l_{10-j}:")
    for row in reciprocal_rows():
        print(
            f"  E{row.key_index}: D={row.denominator} bar={row.bar_name} "
            f"terms={row.terms} top_total={row.top_total_degree} "
            f"top_degrees={row.top_degrees}"
        )
    print("delta-free compatibility rows against E4:")
    for row in compatibility_rows():
        print(
            f"  {row.name}: terms={row.terms} total={row.total_degree} "
            f"top_total={row.top_total_degree} bar_total={row.bar_total_degree} "
            f"top_degrees={row.top_degrees} bar_degrees={row.bar_degrees}"
        )
    print(
        "summary: "
        f"reciprocal_equations={summary['reciprocal_equations']} "
        f"compatibility_equations={summary['compatibility_equations']} "
        f"max_compatibility_total_degree={summary['max_compatibility_total_degree']} "
        f"max_compatibility_terms={summary['max_compatibility_terms']}"
    )
    print("H5_RECIPROCAL_COMPATIBILITY_COMPILER_PASS")


if __name__ == "__main__":
    main()
