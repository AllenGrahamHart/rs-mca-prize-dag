#!/usr/bin/env python3
"""Verify weighted homogeneity of the h=5 reciprocal graph system."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h5_basefree_reciprocal_system import (
    ALL_BARS,
    pairwise_polynomial,
    reciprocal_slots,
)
from f3_h5_reciprocal_compatibility_compiler import TOP
from f3_h5_unit_norm_reciprocal_gate import unit_norm_polynomial


VARIABLES = TOP + ALL_BARS
WEIGHTS = {
    **{variable: 5 - index for index, variable in enumerate(TOP)},
    **{variable: -(5 - index) for index, variable in enumerate(ALL_BARS)},
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


def reciprocal_weight_rows() -> tuple[WeightedRow, ...]:
    rows: list[WeightedRow] = []
    for key_index, _, high_part, _ in reciprocal_slots()[:4]:
        weight, terms, total_degree = polynomial_weight(high_part, TOP)
        rows.append(WeightedRow(f"P{key_index}", weight, terms, total_degree))
    return tuple(rows)


def pairwise_weight_rows() -> tuple[WeightedRow, ...]:
    slots = reciprocal_slots()
    rows: list[WeightedRow] = []
    for left_index, left in enumerate(slots):
        for right in slots[left_index + 1 :]:
            polynomial = pairwise_polynomial(left, right)
            weight, terms, total_degree = polynomial_weight(polynomial, VARIABLES)
            rows.append(WeightedRow(f"C{left[0]}{right[0]}", weight, terms, total_degree))
    return tuple(rows)


def unit_weight_rows() -> tuple[WeightedRow, ...]:
    rows: list[WeightedRow] = []
    for key_index in range(1, 5):
        polynomial = unit_norm_polynomial(key_index)
        weight, terms, total_degree = polynomial_weight(polynomial, VARIABLES)
        rows.append(WeightedRow(f"N{key_index}", weight, terms, total_degree))
    return tuple(rows)


def weighted_homogeneity_summary() -> dict[str, int]:
    reciprocal = reciprocal_weight_rows()
    pairwise = pairwise_weight_rows()
    unit = unit_weight_rows()
    expected_reciprocal = {
        "P1": (9, 22, 9),
        "P2": (8, 18, 8),
        "P3": (7, 13, 7),
        "P4": (6, 10, 6),
    }
    expected_pairwise = {
        "C12": (7, 40, 10),
        "C13": (6, 35, 10),
        "C14": (5, 32, 10),
        "C15": (4, 23, 10),
        "C23": (5, 31, 9),
        "C24": (4, 28, 9),
        "C25": (3, 19, 9),
        "C34": (3, 23, 8),
        "C35": (2, 14, 8),
        "C45": (1, 11, 7),
    }
    expected_unit = {
        "N1": (0, 485, 18),
        "N2": (0, 325, 16),
        "N3": (0, 170, 14),
        "N4": (0, 101, 12),
    }
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
        "unit_weight": 0,
    }


def main() -> None:
    summary = weighted_homogeneity_summary()
    print("h=5 reciprocal weighted homogeneity")
    print("weights: l5..l9 = 5..1 and bar_l5..bar_l9 = -5..-1")
    for label, rows in (
        ("reciprocal high parts", reciprocal_weight_rows()),
        ("pairwise minors", pairwise_weight_rows()),
        ("unit rows", unit_weight_rows()),
    ):
        print(label + ":")
        for row in rows:
            print(
                f"  {row.name}: weight={row.weight} "
                f"terms={row.terms} degree={row.total_degree}"
            )
    print(
        "summary: "
        f"reciprocal_rows={summary['reciprocal_rows']} "
        f"pairwise_rows={summary['pairwise_rows']} "
        f"unit_rows={summary['unit_rows']} "
        f"pairwise_weight_range={summary['min_pairwise_weight']}.."
        f"{summary['max_pairwise_weight']} "
        f"unit_weight={summary['unit_weight']}"
    )
    print("H5_WEIGHTED_HOMOGENEITY_PASS")


if __name__ == "__main__":
    main()
