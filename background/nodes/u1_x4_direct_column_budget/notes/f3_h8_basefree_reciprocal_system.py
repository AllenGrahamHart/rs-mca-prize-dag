#!/usr/bin/env python3
"""Compile the base-free h=8 reciprocal compatibility system."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

import sympy as sp

from f3_h8_reciprocal_compatibility_compiler import (
    ALL_BARS,
    CENTER_BAR,
    TOP,
    reciprocal_part,
)
from f3_h8_x83_triangular_obstruction import LOCATOR


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
    for index in range(1, 8):
        denominator, high_part, bar_var = reciprocal_part(index)
        rows.append((index, denominator, high_part, bar_var))
    rows.append((8, 1, LOCATOR[8], CENTER_BAR))
    return tuple(rows)


def pairwise_polynomial(
    left: tuple[int, int, sp.Expr, sp.Symbol],
    right: tuple[int, int, sp.Expr, sp.Symbol],
) -> sp.Expr:
    _, left_denominator, left_part, left_bar = left
    _, right_denominator, right_part, right_bar = right
    return sp.expand(
        right_denominator * right_bar * left_part
        - left_denominator * left_bar * right_part
    )


@lru_cache(maxsize=1)
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
        "C12": (255, 16, 15, 1, (1, 2, 2, 2, 3, 4, 7, 15), (0, 0, 0, 0, 0, 0, 1, 1)),
        "C13": (229, 16, 15, 1, (1, 2, 2, 2, 3, 4, 7, 15), (0, 0, 0, 0, 0, 1, 0, 1)),
        "C14": (210, 16, 15, 1, (1, 2, 2, 2, 3, 4, 7, 15), (0, 0, 0, 0, 1, 0, 0, 1)),
        "C15": (192, 16, 15, 1, (1, 2, 2, 2, 3, 4, 7, 15), (0, 0, 0, 1, 0, 0, 0, 1)),
        "C16": (180, 16, 15, 1, (1, 2, 2, 2, 3, 4, 7, 15), (0, 0, 1, 0, 0, 0, 0, 1)),
        "C17": (169, 16, 15, 1, (1, 2, 2, 2, 3, 4, 7, 15), (0, 1, 0, 0, 0, 0, 0, 1)),
        "C18": (141, 16, 15, 1, (1, 2, 2, 2, 3, 4, 7, 15), (1, 0, 0, 0, 0, 0, 0, 1)),
        "C23": (204, 15, 14, 1, (1, 2, 2, 2, 3, 4, 7, 14), (0, 0, 0, 0, 0, 1, 1, 0)),
        "C24": (185, 15, 14, 1, (1, 2, 2, 2, 3, 4, 7, 14), (0, 0, 0, 0, 1, 0, 1, 0)),
        "C25": (167, 15, 14, 1, (1, 2, 2, 2, 3, 4, 7, 14), (0, 0, 0, 1, 0, 0, 1, 0)),
        "C26": (155, 15, 14, 1, (1, 2, 2, 2, 3, 4, 7, 14), (0, 0, 1, 0, 0, 0, 1, 0)),
        "C27": (144, 15, 14, 1, (1, 2, 2, 2, 3, 4, 7, 14), (0, 1, 0, 0, 0, 0, 1, 0)),
        "C28": (116, 15, 14, 1, (1, 2, 2, 2, 3, 4, 7, 14), (1, 0, 0, 0, 0, 0, 1, 0)),
        "C34": (159, 14, 13, 1, (1, 1, 2, 2, 3, 4, 6, 13), (0, 0, 0, 0, 1, 1, 0, 0)),
        "C35": (141, 14, 13, 1, (1, 1, 2, 2, 3, 4, 6, 13), (0, 0, 0, 1, 0, 1, 0, 0)),
        "C36": (129, 14, 13, 1, (1, 1, 2, 2, 3, 4, 6, 13), (0, 0, 1, 0, 0, 1, 0, 0)),
        "C37": (118, 14, 13, 1, (1, 1, 2, 2, 3, 4, 6, 13), (0, 1, 0, 0, 0, 1, 0, 0)),
        "C38": (90, 14, 13, 1, (1, 1, 2, 2, 3, 4, 6, 13), (1, 0, 0, 0, 0, 1, 0, 0)),
        "C45": (122, 13, 12, 1, (1, 1, 2, 2, 3, 4, 6, 12), (0, 0, 0, 1, 1, 0, 0, 0)),
        "C46": (110, 13, 12, 1, (1, 1, 2, 2, 3, 4, 6, 12), (0, 0, 1, 0, 1, 0, 0, 0)),
        "C47": (99, 13, 12, 1, (1, 1, 2, 2, 3, 4, 6, 12), (0, 1, 0, 0, 1, 0, 0, 0)),
        "C48": (71, 13, 12, 1, (1, 1, 2, 2, 3, 4, 6, 12), (1, 0, 0, 0, 1, 0, 0, 0)),
        "C56": (92, 12, 11, 1, (1, 1, 1, 2, 2, 3, 5, 11), (0, 0, 1, 1, 0, 0, 0, 0)),
        "C57": (81, 12, 11, 1, (1, 1, 1, 2, 2, 3, 5, 11), (0, 1, 0, 1, 0, 0, 0, 0)),
        "C58": (53, 12, 11, 1, (1, 1, 1, 2, 2, 3, 5, 11), (1, 0, 0, 1, 0, 0, 0, 0)),
        "C67": (69, 11, 10, 1, (1, 1, 1, 2, 2, 3, 5, 10), (0, 1, 1, 0, 0, 0, 0, 0)),
        "C68": (41, 11, 10, 1, (1, 1, 1, 2, 2, 3, 5, 10), (1, 0, 1, 0, 0, 0, 0, 0)),
        "C78": (30, 10, 9, 1, (1, 1, 1, 1, 2, 3, 4, 9), (1, 1, 0, 0, 0, 0, 0, 0)),
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
    print("h=8 base-free reciprocal system")
    print("slots: E1,E2,E3,E4,E5,E6,E7,central-c8")
    for row in pairwise_rows():
        print(
            f"  {row.name}: terms={row.terms} total={row.total_degree} "
            f"top_total={row.top_total_degree} bar_total={row.bar_total_degree} "
            f"top_degrees={row.top_degrees} "
            f"bar_degrees(bar_c8..bar_c15)={row.bar_degrees}"
        )
    print(
        "summary: "
        f"pairwise_equations={summary['pairwise_equations']} "
        f"max_total_degree={summary['max_total_degree']} "
        f"max_top_total_degree={summary['max_top_total_degree']} "
        f"max_bar_total_degree={summary['max_bar_total_degree']} "
        f"max_terms={summary['max_terms']}"
    )
    print("H8_BASEFREE_RECIPROCAL_SYSTEM_PASS")


if __name__ == "__main__":
    main()
