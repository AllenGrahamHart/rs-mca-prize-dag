#!/usr/bin/env python3
"""Rational-curve multiplication interface for the h=3 conic rank target."""

from __future__ import annotations

from dataclasses import dataclass
from math import comb

from f3_h3_exact_profile_4096_budget_floor import EXPECTED_ROWS as ROWS_4096
from f3_h3_exact_profile_4096_rank_deficit_budget import retarget_deficit_summary
from f3_h3_exact_profile_bridge_budget import EXPECTED_ROWS
from f3_h3_exact_profile_rank_deficit_budget import rank_deficit_budget_summary


@dataclass(frozen=True)
class MultiplicationRow:
    s: int
    a_count: int
    b_count: int
    h_order: int
    m_total: int
    generator_degree: int
    target_dimension: int
    box_columns: int
    simplex_columns: int
    box_column_margin: int
    simplex_column_margin: int
    linear_normality_defect: int


def multiplication_row(row) -> MultiplicationRow:
    h_order = 2**row.s
    m_total = 3 * (row.b - 1)
    generator_degree = 2 * h_order
    target_dimension = row.a + generator_degree * m_total
    box_columns = row.a * row.b**3
    simplex_columns = row.a * comb(m_total + 3, 3)
    return MultiplicationRow(
        s=row.s,
        a_count=row.a,
        b_count=row.b,
        h_order=h_order,
        m_total=m_total,
        generator_degree=generator_degree,
        target_dimension=target_dimension,
        box_columns=box_columns,
        simplex_columns=simplex_columns,
        box_column_margin=box_columns - target_dimension,
        simplex_column_margin=simplex_columns - target_dimension,
        linear_normality_defect=generator_degree + 1 - 4,
    )


def conic_rational_curve_summary() -> dict[str, int]:
    rows = tuple(multiplication_row(row) for row in EXPECTED_ROWS)
    rows_4096 = tuple(multiplication_row(row) for row in ROWS_4096)
    deficit = rank_deficit_budget_summary()
    deficit_4096 = retarget_deficit_summary()
    if deficit["min_allowed_deficit"] != 1847:
        raise AssertionError(deficit)
    if deficit_4096["min_allowed_deficit"] != 2899:
        raise AssertionError(deficit_4096)
    for row_set in (rows, rows_4096):
        if any(row.box_column_margin <= 0 for row in row_set):
            raise AssertionError(row_set)
        if any(row.simplex_column_margin <= 0 for row in row_set):
            raise AssertionError(row_set)
        if any(row.linear_normality_defect <= 0 for row in row_set):
            raise AssertionError(row_set)
    tight_box = min(rows, key=lambda row: row.box_column_margin)
    tight_simplex = min(rows, key=lambda row: row.simplex_column_margin)
    tight_linear = min(rows, key=lambda row: row.linear_normality_defect)
    tight_4096_box = min(rows_4096, key=lambda row: row.box_column_margin)
    tight_4096_simplex = min(rows_4096, key=lambda row: row.simplex_column_margin)
    tight_4096_linear = min(rows_4096, key=lambda row: row.linear_normality_defect)
    if (
        tight_4096_box.box_column_margin,
        tight_4096_simplex.simplex_column_margin,
        tight_4096_linear.linear_normality_defect,
    ) != (19_301_121_234, 86_422_920_495, 16_381):
        raise AssertionError((tight_4096_box, tight_4096_simplex, tight_4096_linear))
    return {
        "rows": len(rows),
        "first_s": rows[0].s,
        "last_s": rows[-1].s,
        "min_box_column_margin": tight_box.box_column_margin,
        "min_box_margin_s": tight_box.s,
        "min_simplex_column_margin": tight_simplex.simplex_column_margin,
        "min_simplex_margin_s": tight_simplex.s,
        "min_linear_normality_defect": tight_linear.linear_normality_defect,
        "min_linear_defect_s": tight_linear.s,
        "min_m_total": min(row.m_total for row in rows),
        "max_m_total": max(row.m_total for row in rows),
        "min_generator_degree": min(row.generator_degree for row in rows),
        "max_generator_degree": max(row.generator_degree for row in rows),
        "allowed_codimension": deficit["min_allowed_deficit"],
        "allowed_4096_codimension": deficit_4096["min_allowed_deficit"],
        "min_4096_box_column_margin": tight_4096_box.box_column_margin,
        "min_4096_box_margin_s": tight_4096_box.s,
        "min_4096_simplex_column_margin": tight_4096_simplex.simplex_column_margin,
        "min_4096_simplex_margin_s": tight_4096_simplex.s,
        "min_4096_linear_normality_defect": tight_4096_linear.linear_normality_defect,
        "min_4096_linear_defect_s": tight_4096_linear.s,
        "min_4096_m_total": min(row.m_total for row in rows_4096),
        "max_4096_m_total": max(row.m_total for row in rows_4096),
        "min_4096_generator_degree": min(row.generator_degree for row in rows_4096),
        "max_4096_generator_degree": max(row.generator_degree for row in rows_4096),
    }


def main() -> None:
    summary = conic_rational_curve_summary()
    print("h=3 conic rational-curve multiplication interface")
    print(
        "rank map: H0(O(A-1)) times boxed degree-M monomials in "
        "four sections of O(2H)"
    )
    print(
        "official rows: "
        f"s={summary['first_s']}..{summary['last_s']} "
        f"M={summary['min_m_total']}..{summary['max_m_total']} "
        f"generator_degree={summary['min_generator_degree']}.."
        f"{summary['max_generator_degree']}"
    )
    print(
        "dimension margins: "
        f"box_columns-target >= {summary['min_box_column_margin']} "
        f"(s={summary['min_box_margin_s']}), "
        f"simplex_columns-target >= {summary['min_simplex_column_margin']} "
        f"(s={summary['min_simplex_margin_s']})"
    )
    print(
        "four generators are not a complete linear series: "
        f"min linear-normality defect={summary['min_linear_normality_defect']} "
        f"(s={summary['min_linear_defect_s']})"
    )
    print(f"official codimension allowance={summary['allowed_codimension']}")
    print(
        "retuned H3-ACT(4096) rows: "
        f"M={summary['min_4096_m_total']}..{summary['max_4096_m_total']} "
        f"generator_degree={summary['min_4096_generator_degree']}.."
        f"{summary['max_4096_generator_degree']}"
    )
    print(
        "retuned dimension margins: "
        f"box_columns-target >= {summary['min_4096_box_column_margin']} "
        f"(s={summary['min_4096_box_margin_s']}), "
        f"simplex_columns-target >= {summary['min_4096_simplex_column_margin']} "
        f"(s={summary['min_4096_simplex_margin_s']})"
    )
    print(
        "retuned four-generator linear-normality defect: "
        f"{summary['min_4096_linear_normality_defect']} "
        f"(s={summary['min_4096_linear_defect_s']})"
    )
    print(f"retuned codimension allowance={summary['allowed_4096_codimension']}")
    print("H3_CONIC_RATIONAL_CURVE_INTERFACE_PASS")


if __name__ == "__main__":
    main()
