#!/usr/bin/env python3
"""Concrete full-rank minor certificate for an h=3 same-fiber conic chart."""

from __future__ import annotations

import hashlib
from itertools import product

from f3_h3_rich_curve_rank_sample import (
    A,
    B,
    H,
    P,
    conic_chart_curve,
    column_for_curve,
    precompute,
)


ROW_MIN = 261
ROW_MAX = 580
EXPECTED_DETERMINANT = 514
EXPECTED_CERTIFICATE_DIGEST = "c8ed933836ad696533f73b13a86e71eabce164927a50fc2f8bfd5ce207f92060"


def monomial_labels() -> tuple[tuple[int, int, int, int], ...]:
    return tuple((a, *bs) for a, bs in product(range(A), product(range(B), repeat=3)))


def row_window() -> tuple[int, ...]:
    return tuple(range(ROW_MIN, ROW_MAX + 1))


def certificate_digest(rows: tuple[int, ...], labels: tuple[tuple[int, int, int, int], ...]) -> str:
    blob = (
        "rows="
        + ",".join(map(str, rows))
        + "|cols="
        + ",".join(":".join(map(str, label)) for label in labels)
    )
    return hashlib.sha256(blob.encode()).hexdigest()


def det_mod(matrix: list[list[int]], p: int) -> int:
    size = len(matrix)
    work = [row[:] for row in matrix]
    determinant = 1
    for index in range(size):
        pivot = None
        for row in range(index, size):
            if work[row][index] % p:
                pivot = row
                break
        if pivot is None:
            return 0
        if pivot != index:
            work[index], work[pivot] = work[pivot], work[index]
            determinant = (-determinant) % p
        pivot_value = work[index][index] % p
        determinant = determinant * pivot_value % p
        pivot_inverse = pow(pivot_value, -1, p)
        for row in range(index + 1, size):
            factor = work[row][index] * pivot_inverse % p
            if not factor:
                continue
            for column in range(index, size):
                work[row][column] = (work[row][column] - factor * work[index][column]) % p
    return determinant % p


def conic_chart_columns() -> tuple[list[int], ...]:
    curve, _ = conic_chart_curve()
    degree_cap = (A - 1) + 6 * H * (B - 1)
    powers = precompute(curve)
    return tuple(
        column_for_curve(*powers, a, bs, degree_cap)
        for a, bs in product(range(A), product(range(B), repeat=3))
    )


def minor_matrix() -> list[list[int]]:
    rows = row_window()
    columns = conic_chart_columns()
    if len(rows) != A * B**3 or len(columns) != A * B**3:
        raise AssertionError((len(rows), len(columns), A * B**3))
    return [[columns[column][row] for column in range(len(columns))] for row in rows]


def minor_certificate_summary() -> dict[str, int | str]:
    curve, conic_b = conic_chart_curve()
    labels = monomial_labels()
    rows = row_window()
    digest = certificate_digest(rows, labels)
    if digest != EXPECTED_CERTIFICATE_DIGEST:
        raise AssertionError((digest, EXPECTED_CERTIFICATE_DIGEST))
    determinant = det_mod(minor_matrix(), P)
    if determinant != EXPECTED_DETERMINANT:
        raise AssertionError((determinant, EXPECTED_DETERMINANT))
    if determinant == 0:
        raise AssertionError("minor determinant vanished")
    return {
        "p": P,
        "h": H,
        "a": A,
        "b": B,
        "conic_b": conic_b,
        "rows": len(rows),
        "columns": len(labels),
        "row_min": rows[0],
        "row_max": rows[-1],
        "determinant": determinant,
        "digest": digest,
        "rank_lower_bound": len(labels),
        "coefficient_dimension": A * B**3,
        "curve_slots": len(curve.ps),
    }


def main() -> None:
    summary = minor_certificate_summary()
    print("h=3 conic-chart full-rank minor certificate")
    print(
        f"p={summary['p']} H={summary['h']} A={summary['a']} B={summary['b']} "
        f"conic_b={summary['conic_b']}"
    )
    print(
        f"minor rows={summary['row_min']}..{summary['row_max']} "
        f"columns={summary['columns']} all monomials"
    )
    print(
        f"determinant mod {summary['p']} = {summary['determinant']} "
        f"digest={summary['digest']}"
    )
    print(
        f"rank_lower_bound={summary['rank_lower_bound']} "
        f"coefficient_dimension={summary['coefficient_dimension']}"
    )
    print("This is a toy finite-field minor certificate, not uniform RC-RANK.")
    print("H3_CONIC_CHART_RANK_MINOR_CERTIFICATE_PASS")


if __name__ == "__main__":
    main()
