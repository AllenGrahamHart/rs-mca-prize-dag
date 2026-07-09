#!/usr/bin/env python3
"""Reciprocal compatibility equations for the h=8 x83 obstruction surface."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h8_x83_triangular_obstruction import (
    LOCATOR,
    integer_denominator,
    low_obstructions,
    require_triangular,
)


TOP = tuple(LOCATOR[8:16])
CENTER_BAR = sp.Symbol("bar_c8")
BAR_HIGH = {index: sp.Symbol(f"bar_c{index}") for index in range(9, 16)}
BARS = tuple(BAR_HIGH[index] for index in range(9, 16))
ALL_BARS = (CENTER_BAR,) + BARS


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
    bar_var = BAR_HIGH[16 - key_index]
    return denominator, sp.factor(high_part), bar_var


def reciprocal_rows() -> tuple[ReciprocalRow, ...]:
    rows = []
    for key_index in range(1, 8):
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


def compatibility_polynomial(key_index: int, base_index: int = 7) -> sp.Expr:
    denominator, high_part, bar_var = reciprocal_part(key_index)
    base_denominator, base_high_part, base_bar_var = reciprocal_part(base_index)
    return sp.factor(
        base_denominator * base_bar_var * high_part
        - denominator * bar_var * base_high_part
    )


def compatibility_rows() -> tuple[CompatibilityRow, ...]:
    rows = []
    variables = TOP + BARS
    for key_index in range(1, 7):
        polynomial = compatibility_polynomial(key_index, 7)
        poly = sp.Poly(polynomial, *variables, domain=sp.ZZ)
        top_total = max(sum(monom[: len(TOP)]) for monom, _ in poly.terms())
        bar_total = max(sum(monom[len(TOP) :]) for monom, _ in poly.terms())
        rows.append(
            CompatibilityRow(
                name=f"C{key_index}7",
                terms=len(poly.terms()),
                total_degree=poly.total_degree(),
                top_total_degree=top_total,
                bar_total_degree=bar_total,
                top_degrees=tuple(poly.degree(variable) for variable in TOP),
                bar_degrees=tuple(poly.degree(variable) for variable in BARS),
            )
        )
    return tuple(rows)


def central_compatibility_polynomial(base_index: int = 7) -> sp.Expr:
    base_denominator, base_high_part, base_bar_var = reciprocal_part(base_index)
    return sp.factor(
        base_denominator * base_bar_var * LOCATOR[8] - base_high_part * CENTER_BAR
    )


def central_compatibility_row() -> CompatibilityRow:
    polynomial = central_compatibility_polynomial(7)
    variables = TOP + ALL_BARS
    poly = sp.Poly(polynomial, *variables, domain=sp.ZZ)
    top_total = max(sum(monom[: len(TOP)]) for monom, _ in poly.terms())
    bar_total = max(sum(monom[len(TOP) :]) for monom, _ in poly.terms())
    return CompatibilityRow(
        name="C87",
        terms=len(poly.terms()),
        total_degree=poly.total_degree(),
        top_total_degree=top_total,
        bar_total_degree=bar_total,
        top_degrees=tuple(poly.degree(variable) for variable in TOP),
        bar_degrees=tuple(poly.degree(variable) for variable in ALL_BARS),
    )


def reciprocal_compatibility_summary() -> dict[str, int]:
    reciprocal_expected = {
        1: (33_554_432, "bar_c15", 140, 15, (1, 2, 2, 2, 3, 4, 7, 15)),
        2: (16_777_216, "bar_c14", 115, 14, (1, 2, 2, 2, 3, 4, 7, 14)),
        3: (4_194_304, "bar_c13", 89, 13, (1, 1, 2, 2, 3, 4, 6, 13)),
        4: (2_097_152, "bar_c12", 70, 12, (1, 1, 2, 2, 3, 4, 6, 12)),
        5: (262_144, "bar_c11", 52, 11, (1, 1, 1, 2, 2, 3, 5, 11)),
        6: (131_072, "bar_c10", 40, 10, (1, 1, 1, 2, 2, 3, 5, 10)),
        7: (32_768, "bar_c9", 29, 9, (1, 1, 1, 1, 2, 3, 4, 9)),
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
        "C17": (169, 16, 15, 1, (1, 2, 2, 2, 3, 4, 7, 15), (1, 0, 0, 0, 0, 0, 1)),
        "C27": (144, 15, 14, 1, (1, 2, 2, 2, 3, 4, 7, 14), (1, 0, 0, 0, 0, 1, 0)),
        "C37": (118, 14, 13, 1, (1, 1, 2, 2, 3, 4, 6, 13), (1, 0, 0, 0, 1, 0, 0)),
        "C47": (99, 13, 12, 1, (1, 1, 2, 2, 3, 4, 6, 12), (1, 0, 0, 1, 0, 0, 0)),
        "C57": (81, 12, 11, 1, (1, 1, 1, 2, 2, 3, 5, 11), (1, 0, 1, 0, 0, 0, 0)),
        "C67": (69, 11, 10, 1, (1, 1, 1, 2, 2, 3, 5, 10), (1, 1, 0, 0, 0, 0, 0)),
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

    central = central_compatibility_row()
    expected_central = (
        "C87",
        30,
        10,
        9,
        1,
        (1, 1, 1, 1, 2, 3, 4, 9),
        (1, 1, 0, 0, 0, 0, 0, 0),
    )
    actual_central = (
        central.name,
        central.terms,
        central.total_degree,
        central.top_total_degree,
        central.bar_total_degree,
        central.top_degrees,
        central.bar_degrees,
    )
    if actual_central != expected_central:
        raise AssertionError(actual_central)

    return {
        "reciprocal_rows": len(reciprocal_actual),
        "compatibility_rows": len(compatibility_actual),
        "central_rows": 1,
        "delta_free_rows": len(compatibility_actual) + 1,
        "max_reciprocal_top_degree": max(row[3] for row in reciprocal_actual.values()),
        "max_compatibility_total_degree": max(
            max(row[1] for row in compatibility_actual.values()),
            central.total_degree,
        ),
        "max_compatibility_terms": max(row[0] for row in compatibility_actual.values()),
        "central_terms": central.terms,
        "central_total_degree": central.total_degree,
    }


def main() -> None:
    summary = reciprocal_compatibility_summary()
    print("h=8 reciprocal compatibility compiler")
    print("reciprocal rows P_j = D_j delta*bar_c_{16-j}:")
    for row in reciprocal_rows():
        print(
            f"  E{row.key_index}: D={row.denominator} bar={row.bar_name} "
            f"terms={row.terms} top_total={row.top_total_degree} "
            f"top_degrees={row.top_degrees}"
        )
    print("delta-free compatibility rows against E7:")
    for row in compatibility_rows():
        print(
            f"  {row.name}: terms={row.terms} total={row.total_degree} "
            f"top_total={row.top_total_degree} bar_total={row.bar_total_degree} "
            f"top_degrees={row.top_degrees} bar_degrees={row.bar_degrees}"
        )
    central = central_compatibility_row()
    print("central reciprocal row against E7:")
    print(
        f"  {central.name}: terms={central.terms} total={central.total_degree} "
        f"top_total={central.top_total_degree} bar_total={central.bar_total_degree} "
        f"top_degrees={central.top_degrees} "
        f"bar_degrees(bar_c8..bar_c15)={central.bar_degrees}"
    )
    print(
        "summary: "
        f"reciprocal_rows={summary['reciprocal_rows']} "
        f"compatibility_rows={summary['compatibility_rows']} "
        f"central_rows={summary['central_rows']} "
        f"delta_free_rows={summary['delta_free_rows']} "
        f"max_compatibility_total_degree={summary['max_compatibility_total_degree']} "
        f"max_compatibility_terms={summary['max_compatibility_terms']}"
    )
    print("H8_RECIPROCAL_COMPATIBILITY_COMPILER_PASS")


if __name__ == "__main__":
    main()
