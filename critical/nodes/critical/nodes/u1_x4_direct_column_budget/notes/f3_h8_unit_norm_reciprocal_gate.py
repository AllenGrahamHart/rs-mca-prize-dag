#!/usr/bin/env python3
"""Compile h=8 unit-norm reciprocal equations for the x83 obstruction."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

import sympy as sp

from f3_h8_reciprocal_compatibility_compiler import ALL_BARS, TOP, reciprocal_part
from f3_h8_x83_triangular_obstruction import LOCATOR


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
    paired_top = LOCATOR[16 - key_index]
    return sp.expand(high_part * high_bar - denominator * denominator * paired_top * bar_var)


@lru_cache(maxsize=1)
def unit_norm_rows() -> tuple[UnitNormRow, ...]:
    rows = []
    for key_index in range(1, 8):
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
        "N1": (19601, 30, 15, 15, (1, 2, 2, 2, 3, 4, 7, 15), (1, 2, 2, 2, 3, 4, 7, 15)),
        "N2": (13226, 28, 14, 14, (1, 2, 2, 2, 3, 4, 7, 14), (1, 2, 2, 2, 3, 4, 7, 14)),
        "N3": (7922, 26, 13, 13, (1, 1, 2, 2, 3, 4, 6, 13), (1, 1, 2, 2, 3, 4, 6, 13)),
        "N4": (4901, 24, 12, 12, (1, 1, 2, 2, 3, 4, 6, 12), (1, 1, 2, 2, 3, 4, 6, 12)),
        "N5": (2705, 22, 11, 11, (1, 1, 1, 2, 2, 3, 5, 11), (1, 1, 1, 2, 2, 3, 5, 11)),
        "N6": (1601, 20, 10, 10, (1, 1, 1, 2, 2, 3, 5, 10), (1, 1, 1, 2, 2, 3, 5, 10)),
        "N7": (842, 18, 9, 9, (1, 1, 1, 1, 2, 3, 4, 9), (1, 1, 1, 1, 2, 3, 4, 9)),
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
    print("h=8 unit-norm reciprocal gate")
    print("using delta*bar_delta=1 for the support product")
    for row in unit_norm_rows():
        print(
            f"  {row.name}: terms={row.terms} total={row.total_degree} "
            f"top_total={row.top_total_degree} bar_total={row.bar_total_degree} "
            f"top_degrees={row.top_degrees} "
            f"bar_degrees(bar_c8..bar_c15)={row.bar_degrees}"
        )
    print(
        "summary: "
        f"equations={summary['equations']} "
        f"max_total_degree={summary['max_total_degree']} "
        f"max_top_total_degree={summary['max_top_total_degree']} "
        f"max_bar_total_degree={summary['max_bar_total_degree']} "
        f"max_terms={summary['max_terms']}"
    )
    print("H8_UNIT_NORM_RECIPROCAL_GATE_PASS")


if __name__ == "__main__":
    main()
