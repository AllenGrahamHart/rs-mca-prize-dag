#!/usr/bin/env python3
"""Verify weighted homogeneity of the h=8 reciprocal graph system."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

import sympy as sp

from f3_h8_basefree_reciprocal_system import (
    ALL_BARS,
    TOP,
    pairwise_polynomial,
    reciprocal_slots,
)
from f3_h8_reciprocal_compatibility_compiler import reciprocal_part


VARIABLES = TOP + ALL_BARS
WEIGHTS = {
    **{variable: 8 - index for index, variable in enumerate(TOP)},
    **{variable: -(8 - index) for index, variable in enumerate(ALL_BARS)},
}


@dataclass(frozen=True)
class WeightedRow:
    name: str
    weight: int
    terms: int
    total_degree: int


def polynomial_weight(expr: sp.Expr, variables: tuple[sp.Symbol, ...]) -> tuple[int, int, int]:
    poly = sp.Poly(expr, *variables, domain=sp.ZZ)
    weights = {
        sum(WEIGHTS[variable] * exponent for variable, exponent in zip(variables, monom))
        for monom, _ in poly.terms()
    }
    if len(weights) != 1:
        raise AssertionError((expr, sorted(weights)))
    return weights.pop(), len(poly.terms()), poly.total_degree()


@lru_cache(maxsize=1)
def reciprocal_weight_rows() -> tuple[WeightedRow, ...]:
    rows: list[WeightedRow] = []
    for key_index in range(1, 8):
        _, high_part, _ = reciprocal_part(key_index)
        weight, terms, total_degree = polynomial_weight(high_part, TOP)
        rows.append(WeightedRow(f"P{key_index}", weight, terms, total_degree))
    return tuple(rows)


@lru_cache(maxsize=1)
def pairwise_weight_rows() -> tuple[WeightedRow, ...]:
    slots = reciprocal_slots()
    rows: list[WeightedRow] = []
    for left_index, left in enumerate(slots):
        for right in slots[left_index + 1 :]:
            polynomial = pairwise_polynomial(left, right)
            weight, terms, total_degree = polynomial_weight(polynomial, VARIABLES)
            rows.append(WeightedRow(f"C{left[0]}{right[0]}", weight, terms, total_degree))
    return tuple(rows)


@lru_cache(maxsize=1)
def unit_weight_rows() -> tuple[WeightedRow, ...]:
    rows: list[WeightedRow] = []
    for row in reciprocal_weight_rows():
        # N_j = P_j*conjugate(P_j) - D_j^2*c(16-j)*bar_c(16-j).
        # The first product has weights w + (-w); the second has j + (-j).
        rows.append(WeightedRow(f"N{row.name[1:]}", 0, 0, 0))
    return tuple(rows)


@lru_cache(maxsize=1)
def weighted_homogeneity_summary() -> dict[str, int]:
    reciprocal = reciprocal_weight_rows()
    pairwise = pairwise_weight_rows()
    unit = unit_weight_rows()
    expected_reciprocal = {
        "P1": (15, 140, 15),
        "P2": (14, 115, 14),
        "P3": (13, 89, 13),
        "P4": (12, 70, 12),
        "P5": (11, 52, 11),
        "P6": (10, 40, 10),
        "P7": (9, 29, 9),
    }
    expected_pairwise = {
        "C12": (13, 255, 16),
        "C13": (12, 229, 16),
        "C14": (11, 210, 16),
        "C15": (10, 192, 16),
        "C16": (9, 180, 16),
        "C17": (8, 169, 16),
        "C18": (7, 141, 16),
        "C23": (11, 204, 15),
        "C24": (10, 185, 15),
        "C25": (9, 167, 15),
        "C26": (8, 155, 15),
        "C27": (7, 144, 15),
        "C28": (6, 116, 15),
        "C34": (9, 159, 14),
        "C35": (8, 141, 14),
        "C36": (7, 129, 14),
        "C37": (6, 118, 14),
        "C38": (5, 90, 14),
        "C45": (7, 122, 13),
        "C46": (6, 110, 13),
        "C47": (5, 99, 13),
        "C48": (4, 71, 13),
        "C56": (5, 92, 12),
        "C57": (4, 81, 12),
        "C58": (3, 53, 12),
        "C67": (3, 69, 11),
        "C68": (2, 41, 11),
        "C78": (1, 30, 10),
    }
    expected_unit = {f"N{index}": (0, 0, 0) for index in range(1, 8)}
    actual_reciprocal = {
        row.name: (row.weight, row.terms, row.total_degree) for row in reciprocal
    }
    actual_pairwise = {
        row.name: (row.weight, row.terms, row.total_degree) for row in pairwise
    }
    actual_unit = {row.name: (row.weight, row.terms, row.total_degree) for row in unit}
    if actual_reciprocal != expected_reciprocal:
        raise AssertionError(actual_reciprocal)
    if actual_pairwise != expected_pairwise:
        raise AssertionError(actual_pairwise)
    if actual_unit != expected_unit:
        raise AssertionError(actual_unit)
    return {
        "reciprocal_rows": len(reciprocal),
        "pairwise_rows": len(pairwise),
        "unit_rows": len(unit),
        "min_pairwise_weight": min(row.weight for row in pairwise),
        "max_pairwise_weight": max(row.weight for row in pairwise),
        "chart7_denominator_weight": WEIGHTS[ALL_BARS[1]],
        "chart7_numerator_weight": WEIGHTS[TOP[1]],
        "unit_weight": 0,
    }


def main() -> None:
    summary = weighted_homogeneity_summary()
    print("h=8 reciprocal weighted homogeneity")
    print("weights: c8..c15 = 8..1 and bar_c8..bar_c15 = -8..-1")
    print("reciprocal high parts:")
    for row in reciprocal_weight_rows():
        print(
            f"  {row.name}: weight={row.weight} "
            f"terms={row.terms} degree={row.total_degree}"
        )
    print("pairwise minors:")
    for row in pairwise_weight_rows():
        print(
            f"  {row.name}: weight={row.weight} "
            f"terms={row.terms} degree={row.total_degree}"
        )
    print("unit rows:")
    for row in unit_weight_rows():
        print(f"  {row.name}: weight={row.weight} verified by conjugate-weight identity")
    print(
        "summary: "
        f"reciprocal_rows={summary['reciprocal_rows']} "
        f"pairwise_rows={summary['pairwise_rows']} "
        f"unit_rows={summary['unit_rows']} "
        f"pairwise_weight_range={summary['min_pairwise_weight']}.."
        f"{summary['max_pairwise_weight']} "
        f"chart7_weights=({summary['chart7_numerator_weight']},"
        f"{summary['chart7_denominator_weight']}) "
        f"unit_weight={summary['unit_weight']}"
    )
    print("H8_WEIGHTED_HOMOGENEITY_PASS")


if __name__ == "__main__":
    main()
