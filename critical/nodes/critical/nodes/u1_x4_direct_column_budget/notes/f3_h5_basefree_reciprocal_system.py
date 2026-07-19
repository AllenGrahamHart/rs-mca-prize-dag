#!/usr/bin/env python3
"""Compile the base-free h=5 reciprocal compatibility system."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h5_reciprocal_compatibility_compiler import CENTER_BAR, TOP, reciprocal_part
from f3_h5_x83_triangular_norm_gate import BAR_HIGH, LOCATOR


ALL_BARS = (CENTER_BAR,) + tuple(BAR_HIGH[index] for index in range(6, 10))


@dataclass(frozen=True)
class PairwiseRow:
    name: str
    terms: int
    total_degree: int
    top_total_degree: int
    bar_total_degree: int
    top_degrees: tuple[int, ...]
    bar_degrees: tuple[int, ...]


def reciprocal_slots() -> tuple[tuple[int, int, sp.Expr, sp.Symbol], ...]:
    rows = []
    for index in range(1, 5):
        denominator, high_part, bar_var = reciprocal_part(index)
        rows.append((index, denominator, high_part, bar_var))
    rows.append((5, 1, LOCATOR[5], CENTER_BAR))
    return tuple(rows)


def pairwise_polynomial(
    left: tuple[int, int, sp.Expr, sp.Symbol],
    right: tuple[int, int, sp.Expr, sp.Symbol],
) -> sp.Expr:
    _, left_denominator, left_part, left_bar = left
    _, right_denominator, right_part, right_bar = right
    return sp.factor(
        right_denominator * right_bar * left_part
        - left_denominator * left_bar * right_part
    )


def pairwise_rows() -> tuple[PairwiseRow, ...]:
    slots = reciprocal_slots()
    variables = TOP + ALL_BARS
    rows = []
    for left_index, left in enumerate(slots):
        for right in slots[left_index + 1 :]:
            polynomial = pairwise_polynomial(left, right)
            poly = sp.Poly(polynomial, *variables, domain=sp.ZZ)
            top_total = max(sum(monom[: len(TOP)]) for monom, _ in poly.terms())
            bar_total = max(sum(monom[len(TOP) :]) for monom, _ in poly.terms())
            rows.append(
                PairwiseRow(
                    name=f"C{left[0]}{right[0]}",
                    terms=len(poly.terms()),
                    total_degree=poly.total_degree(),
                    top_total_degree=top_total,
                    bar_total_degree=bar_total,
                    top_degrees=tuple(poly.degree(variable) for variable in TOP),
                    bar_degrees=tuple(poly.degree(variable) for variable in ALL_BARS),
                )
            )
    return tuple(rows)


def basefree_summary() -> dict[str, int]:
    expected = {
        "C12": (40, 10, 9, 1, (1, 2, 2, 4, 9), (0, 0, 0, 1, 1)),
        "C13": (35, 10, 9, 1, (1, 2, 2, 4, 9), (0, 0, 1, 0, 1)),
        "C14": (32, 10, 9, 1, (1, 2, 2, 4, 9), (0, 1, 0, 0, 1)),
        "C15": (23, 10, 9, 1, (1, 2, 2, 4, 9), (1, 0, 0, 0, 1)),
        "C23": (31, 9, 8, 1, (1, 2, 2, 4, 8), (0, 0, 1, 1, 0)),
        "C24": (28, 9, 8, 1, (1, 2, 2, 4, 8), (0, 1, 0, 1, 0)),
        "C25": (19, 9, 8, 1, (1, 2, 2, 4, 8), (1, 0, 0, 1, 0)),
        "C34": (23, 8, 7, 1, (1, 1, 2, 3, 7), (0, 1, 1, 0, 0)),
        "C35": (14, 8, 7, 1, (1, 1, 2, 3, 7), (1, 0, 1, 0, 0)),
        "C45": (11, 7, 6, 1, (1, 1, 2, 3, 6), (1, 1, 0, 0, 0)),
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
        for row in pairwise_rows()
    }
    if actual != expected:
        raise AssertionError(actual)
    return {
        "pairwise_equations": len(actual),
        "max_terms": max(row[0] for row in actual.values()),
        "max_total_degree": max(row[1] for row in actual.values()),
        "max_top_total_degree": max(row[2] for row in actual.values()),
        "max_bar_total_degree": max(row[3] for row in actual.values()),
    }


def main() -> None:
    summary = basefree_summary()
    print("h=5 base-free reciprocal system")
    print("slots: E1,E2,E3,E4,central-l5")
    for row in pairwise_rows():
        print(
            f"  {row.name}: terms={row.terms} total={row.total_degree} "
            f"top_total={row.top_total_degree} bar_total={row.bar_total_degree} "
            f"top_degrees={row.top_degrees} "
            f"bar_degrees(bar_l5..bar_l9)={row.bar_degrees}"
        )
    print(
        "summary: "
        f"pairwise_equations={summary['pairwise_equations']} "
        f"max_total_degree={summary['max_total_degree']} "
        f"max_top_total_degree={summary['max_top_total_degree']} "
        f"max_bar_total_degree={summary['max_bar_total_degree']} "
        f"max_terms={summary['max_terms']}"
    )
    print("H5_BASEFREE_RECIPROCAL_SYSTEM_PASS")


if __name__ == "__main__":
    main()
