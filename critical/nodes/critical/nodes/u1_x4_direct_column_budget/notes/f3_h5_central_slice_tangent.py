#!/usr/bin/env python3
"""Tangent compiler for the h=5 central weighted slice."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

import sympy as sp

from f3_h5_basefree_reciprocal_system import ALL_BARS, reciprocal_slots
from f3_h5_central_weighted_slice import CENTRAL_SUBS, central_slice_summary
from f3_h5_reciprocal_compatibility_compiler import TOP


SLICE_TOP = TOP[1:]
NONCENTRAL_BARS = ALL_BARS[1:]
HALF = Fraction(1, 2)
QUARTER = Fraction(1, 4)
THREE_QUARTERS = Fraction(3, 4)


@dataclass(frozen=True)
class SliceTangentRow:
    key_index: int
    solved_bar: str
    denominator: int
    constant_numerator: int
    linear_coefficients: tuple[Fraction, ...]


def _fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _linear_part_text(row: SliceTangentRow) -> str:
    pieces = [
        f"{_fraction_text(coeff)}*{var}"
        for coeff, var in zip(row.linear_coefficients, SLICE_TOP)
        if coeff
    ]
    return " + ".join(pieces) if pieces else "0"


def _identity_matrix(size: int, diagonal: Fraction) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(diagonal if row == col else Fraction(0) for col in range(size))
        for row in range(size)
    )


def _matrix_multiply(
    left: tuple[tuple[Fraction, ...], ...],
    right: tuple[tuple[Fraction, ...], ...],
) -> tuple[tuple[Fraction, ...], ...]:
    size = len(left)
    return tuple(
        tuple(sum(left[row][k] * right[k][col] for k in range(size)) for col in range(size))
        for row in range(size)
    )


def slice_tangent_rows() -> tuple[SliceTangentRow, ...]:
    central_slice_summary()
    slots = {slot[0]: slot for slot in reciprocal_slots()}
    rows: list[SliceTangentRow] = []
    for key_index in range(1, 5):
        _, denominator, high_part, solved_bar = slots[key_index]
        poly = sp.Poly(high_part.subs(CENTRAL_SUBS), *SLICE_TOP, domain=sp.ZZ)
        constant = int(poly.coeff_monomial((0,) * len(SLICE_TOP)))
        coefficients: list[Fraction] = []
        for position in range(len(SLICE_TOP)):
            monomial = [0] * len(SLICE_TOP)
            monomial[position] = 1
            coefficient = int(poly.coeff_monomial(tuple(monomial)))
            coefficients.append(Fraction(coefficient, denominator))
        rows.append(
            SliceTangentRow(
                key_index=key_index,
                solved_bar=str(solved_bar),
                denominator=denominator,
                constant_numerator=constant,
                linear_coefficients=tuple(coefficients),
            )
        )
    return tuple(rows)


def graph_tangent_matrix() -> tuple[tuple[Fraction, ...], ...]:
    bar_index = {str(bar): index for index, bar in enumerate(NONCENTRAL_BARS)}
    matrix = [[Fraction(0) for _ in SLICE_TOP] for _ in NONCENTRAL_BARS]
    for row in slice_tangent_rows():
        matrix[bar_index[row.solved_bar]] = list(row.linear_coefficients)
    return tuple(tuple(row) for row in matrix)


def fixed_map_tangent_matrix() -> tuple[tuple[Fraction, ...], ...]:
    graph = graph_tangent_matrix()
    return _matrix_multiply(graph, graph)


def fixed_equation_linear_matrix() -> tuple[tuple[Fraction, ...], ...]:
    fixed_map = fixed_map_tangent_matrix()
    identity = _identity_matrix(len(SLICE_TOP), Fraction(1))
    return tuple(
        tuple(identity[row][col] - fixed_map[row][col] for col in range(len(SLICE_TOP)))
        for row in range(len(SLICE_TOP))
    )


def slice_tangent_summary() -> dict[str, int]:
    rows = slice_tangent_rows()
    expected_rows = {
        1: ("bar_l9", 16384, 0, (HALF, Fraction(0), Fraction(0), Fraction(0))),
        2: ("bar_l8", 16384, 0, (Fraction(0), HALF, Fraction(0), Fraction(0))),
        3: ("bar_l7", 256, 0, (Fraction(0), Fraction(0), HALF, Fraction(0))),
        4: ("bar_l6", 512, 0, (Fraction(0), Fraction(0), Fraction(0), HALF)),
    }
    actual_rows = {
        row.key_index: (
            row.solved_bar,
            row.denominator,
            row.constant_numerator,
            row.linear_coefficients,
        )
        for row in rows
    }
    if actual_rows != expected_rows:
        raise AssertionError(actual_rows)

    expected_graph = (
        (Fraction(0), Fraction(0), Fraction(0), HALF),
        (Fraction(0), Fraction(0), HALF, Fraction(0)),
        (Fraction(0), HALF, Fraction(0), Fraction(0)),
        (HALF, Fraction(0), Fraction(0), Fraction(0)),
    )
    graph = graph_tangent_matrix()
    if graph != expected_graph:
        raise AssertionError(graph)

    fixed_map = fixed_map_tangent_matrix()
    expected_fixed_map = _identity_matrix(len(SLICE_TOP), QUARTER)
    if fixed_map != expected_fixed_map:
        raise AssertionError(fixed_map)

    fixed_equation = fixed_equation_linear_matrix()
    expected_fixed_equation = _identity_matrix(len(SLICE_TOP), THREE_QUARTERS)
    if fixed_equation != expected_fixed_equation:
        raise AssertionError(fixed_equation)

    determinant = THREE_QUARTERS**len(SLICE_TOP)
    return {
        "slice_tangent_rows": len(rows),
        "zero_constant_rows": sum(row.constant_numerator == 0 for row in rows),
        "graph_tangent_nonzero_entries": sum(
            1 for row in graph for coefficient in row if coefficient
        ),
        "graph_tangent_denominator": HALF.denominator,
        "fixed_map_denominator": QUARTER.denominator,
        "fixed_equation_diagonal_numerator": THREE_QUARTERS.numerator,
        "fixed_equation_diagonal_denominator": THREE_QUARTERS.denominator,
        "fixed_equation_det_numerator": determinant.numerator,
        "fixed_equation_det_denominator": determinant.denominator,
    }


def main() -> None:
    summary = slice_tangent_summary()
    print("h=5 central slice tangent compiler")
    print("slice variables: l6,l7,l8,l9")
    print("bar variables: bar_l6,bar_l7,bar_l8,bar_l9")
    for row in slice_tangent_rows():
        print(
            f"  C{row.key_index}5: solves={row.solved_bar} "
            f"constant_numerator={row.constant_numerator} "
            f"linear={_linear_part_text(row)}"
        )
    print("graph tangent matrix is the anti-diagonal matrix with coefficient 1/2")
    print("fixed-map tangent is 1/4 times the identity")
    print(
        "fixed-equation linearization is 3/4 times the identity, "
        f"det={summary['fixed_equation_det_numerator']}/"
        f"{summary['fixed_equation_det_denominator']}"
    )
    print("This is a local algebraic slice fact, not an official-row closure.")
    print("H5_CENTRAL_SLICE_TANGENT_PASS")


if __name__ == "__main__":
    main()
