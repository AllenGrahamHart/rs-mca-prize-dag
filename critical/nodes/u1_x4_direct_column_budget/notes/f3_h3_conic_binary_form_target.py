#!/usr/bin/env python3
"""Binary-form reduction target for the h=3 same-fiber conic rank route."""

from __future__ import annotations

from fractions import Fraction

from f3_h3_conic_degree2_chart import numerator_coefficients
from f3_h3_exact_profile_4096_budget_floor import EXPECTED_ROWS as ROWS_4096
from f3_h3_exact_profile_4096_rank_deficit_budget import retarget_deficit_summary
from f3_h3_exact_profile_bridge_budget import EXPECTED_ROWS
from f3_h3_exact_profile_rank_deficit_budget import rank_deficit_budget_summary


P = 769
CONIC_A = 37
BASE_U = 101
BASE_V = 333
Q_COEFFS = (1, 1, 1)


def rank_mod_p(rows: list[tuple[int, ...]], p: int) -> int:
    width = max(len(row) for row in rows)
    matrix = [list(row) + [0] * (width - len(row)) for row in rows]
    rank = 0
    for col in range(width):
        pivot = None
        for row in range(rank, len(matrix)):
            if matrix[row][col] % p:
                pivot = row
                break
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inv = pow(matrix[rank][col] % p, -1, p)
        matrix[rank] = [(value * inv) % p for value in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank or matrix[row][col] % p == 0:
                continue
            factor = matrix[row][col] % p
            matrix[row] = [
                (value - factor * pivot_value) % p
                for value, pivot_value in zip(matrix[row], matrix[rank])
            ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def official_gap_summary(rows=EXPECTED_ROWS) -> dict[str, int]:
    gaps = []
    for row in rows:
        h_order = 2**row.s
        gaps.append((Fraction(h_order, row.a), row.s, h_order, row.a, row.b))
    gap, s, h_order, a_count, b_count = min(gaps)
    return {
        "rows": len(rows),
        "min_gap_s": s,
        "min_gap_num": gap.numerator,
        "min_gap_den": gap.denominator,
        "min_gap_ppm": gap.numerator * 1_000_000 // gap.denominator,
        "min_gap_h": h_order,
        "min_gap_a": a_count,
        "min_gap_b": b_count,
        "min_b": min(row.b for row in rows),
        "max_b": max(row.b for row in rows),
    }


def conic_binary_form_summary() -> dict[str, int]:
    coeffs = numerator_coefficients(P, CONIC_A, BASE_U, BASE_V)
    quadratics = [coeffs["U"], coeffs["V"], coeffs["W"], Q_COEFFS]
    relation = tuple(
        (
            coeffs["U"][index]
            + coeffs["V"][index]
            + coeffs["W"][index]
            + CONIC_A * Q_COEFFS[index]
        )
        % P
        for index in range(3)
    )
    if any(relation):
        raise AssertionError(relation)

    span_rank = rank_mod_p(quadratics, P)
    if span_rank != 3:
        raise AssertionError((span_rank, quadratics))

    deficit = rank_deficit_budget_summary()
    deficit_4096 = retarget_deficit_summary()
    official = official_gap_summary()
    official_4096 = official_gap_summary(ROWS_4096)
    if deficit["min_allowed_deficit"] != 1847:
        raise AssertionError(deficit)
    if deficit_4096["min_allowed_deficit"] != 2899:
        raise AssertionError(deficit_4096)
    if (official["min_gap_num"], official["min_gap_den"]) != (4096, 681):
        raise AssertionError(official)
    if (official_4096["min_gap_num"], official_4096["min_gap_den"]) != (
        8192,
        2953,
    ):
        raise AssertionError(official_4096)
    if (official_4096["min_b"], official_4096["max_b"]) != (187, 119_920):
        raise AssertionError(official_4096)

    return {
        "p": P,
        "conic_a": CONIC_A,
        "quadratics": len(quadratics),
        "quadratic_span_rank": span_rank,
        "linear_relations": len(quadratics) - span_rank,
        "quadratic_degree": 2,
        "quadratic_total_exponent_factor": 3,
        "pullback_degree_factor": 6,
        "official_rows": official["rows"],
        "official_min_gap_ppm": official["min_gap_ppm"],
        "official_min_gap_s": official["min_gap_s"],
        "official_min_gap_h": official["min_gap_h"],
        "official_min_gap_a": official["min_gap_a"],
        "official_min_gap_b": official["min_gap_b"],
        "official_min_b": official["min_b"],
        "official_max_b": official["max_b"],
        "allowed_codimension": deficit["min_allowed_deficit"],
        "tight_deficit_s": deficit["first_s"],
        "official_4096_min_gap_ppm": official_4096["min_gap_ppm"],
        "official_4096_min_gap_s": official_4096["min_gap_s"],
        "official_4096_min_gap_h": official_4096["min_gap_h"],
        "official_4096_min_gap_a": official_4096["min_gap_a"],
        "official_4096_min_gap_b": official_4096["min_gap_b"],
        "official_4096_min_b": official_4096["min_b"],
        "official_4096_max_b": official_4096["max_b"],
        "allowed_4096_codimension": deficit_4096["min_allowed_deficit"],
        "tight_4096_deficit_s": deficit_4096["tight_s"],
    }


def main() -> None:
    summary = conic_binary_form_summary()
    print("h=3 conic binary-form rank target")
    print(
        f"p={summary['p']} conic_a={summary['conic_a']} "
        f"quadratics={summary['quadratics']} "
        f"span_rank={summary['quadratic_span_rank']} "
        f"linear_relations={summary['linear_relations']}"
    )
    print(
        "cleared conic columns live in binary forms of degree "
        "(A-1)+6H(B-1)"
    )
    print(
        "official exact-profile boxes: "
        f"rows={summary['official_rows']} "
        f"B={summary['official_min_b']}..{summary['official_max_b']} "
        f"min_H/A_ppm={summary['official_min_gap_ppm']} "
        f"at_s={summary['official_min_gap_s']}"
    )
    print(
        "sufficient theorem target: "
        f"binary-form span codimension <= {summary['allowed_codimension']} "
        f"(tight_s={summary['tight_deficit_s']})"
    )
    print(
        "retuned H3-ACT(4096) target: "
        f"codimension <= {summary['allowed_4096_codimension']} "
        f"B={summary['official_4096_min_b']}.."
        f"{summary['official_4096_max_b']} "
        f"min_H/A_ppm={summary['official_4096_min_gap_ppm']} "
        f"at_s={summary['official_4096_min_gap_s']}"
    )
    print("H3_CONIC_BINARY_FORM_TARGET_PASS")


if __name__ == "__main__":
    main()
