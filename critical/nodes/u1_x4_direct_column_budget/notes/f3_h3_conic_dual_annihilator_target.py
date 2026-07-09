#!/usr/bin/env python3
"""Dual-annihilator target for the h=3 conic codimension theorem."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_exact_profile_4096_budget_floor import EXPECTED_ROWS as ROWS_4096
from f3_h3_exact_profile_4096_rank_deficit_budget import retarget_deficit_summary
from f3_h3_exact_profile_bridge_budget import EXPECTED_ROWS
from f3_h3_exact_profile_rank_deficit_budget import rank_deficit_budget_summary


@dataclass(frozen=True)
class DualAnnihilatorRow:
    s: int
    a_count: int
    b_count: int
    h_order: int
    m_total: int
    base_products: int
    shift_window: int
    dual_constraints: int
    base_degree: int
    ambient_dimension: int
    column_surplus: int
    annihilator_allowance: int


def dual_annihilator_row(row, allowance: int) -> DualAnnihilatorRow:
    h_order = 2**row.s
    m_total = 3 * (row.b - 1)
    base_products = row.b**3
    shift_window = row.a
    dual_constraints = shift_window * base_products
    base_degree = 2 * h_order * m_total
    ambient_dimension = row.a + base_degree
    return DualAnnihilatorRow(
        s=row.s,
        a_count=row.a,
        b_count=row.b,
        h_order=h_order,
        m_total=m_total,
        base_products=base_products,
        shift_window=shift_window,
        dual_constraints=dual_constraints,
        base_degree=base_degree,
        ambient_dimension=ambient_dimension,
        column_surplus=dual_constraints - ambient_dimension,
        annihilator_allowance=allowance,
    )


def dual_summary_for_rows(rows_source, allowance: int) -> dict[str, int]:
    rows = tuple(dual_annihilator_row(row, allowance) for row in rows_source)
    if any(row.column_surplus <= allowance for row in rows):
        raise AssertionError(rows)
    if any(row.base_products <= allowance for row in rows):
        raise AssertionError(rows)
    tight_surplus = min(rows, key=lambda row: row.column_surplus)
    tight_base = min(rows, key=lambda row: row.base_products)
    tight_ambient = min(rows, key=lambda row: row.ambient_dimension)
    return {
        "rows": len(rows),
        "first_s": rows[0].s,
        "last_s": rows[-1].s,
        "allowance": allowance,
        "min_base_products": tight_base.base_products,
        "min_base_products_s": tight_base.s,
        "min_shift_window": min(row.shift_window for row in rows),
        "max_shift_window": max(row.shift_window for row in rows),
        "min_ambient_dimension": tight_ambient.ambient_dimension,
        "min_ambient_s": tight_ambient.s,
        "max_ambient_dimension": max(row.ambient_dimension for row in rows),
        "min_column_surplus": tight_surplus.column_surplus,
        "min_column_surplus_s": tight_surplus.s,
        "min_m_total": min(row.m_total for row in rows),
        "max_m_total": max(row.m_total for row in rows),
    }


def conic_dual_annihilator_summary() -> dict[str, int]:
    deficit = rank_deficit_budget_summary()
    allowance = deficit["min_allowed_deficit"]
    if allowance != 1847:
        raise AssertionError(deficit)
    deficit_4096 = retarget_deficit_summary()
    allowance_4096 = deficit_4096["min_allowed_deficit"]
    if allowance_4096 != 2899:
        raise AssertionError(deficit_4096)

    old = dual_summary_for_rows(EXPECTED_ROWS, allowance)
    retuned = dual_summary_for_rows(ROWS_4096, allowance_4096)
    return {
        **old,
        "allowance_4096": retuned["allowance"],
        "min_4096_base_products": retuned["min_base_products"],
        "min_4096_base_products_s": retuned["min_base_products_s"],
        "min_4096_shift_window": retuned["min_shift_window"],
        "max_4096_shift_window": retuned["max_shift_window"],
        "min_4096_ambient_dimension": retuned["min_ambient_dimension"],
        "max_4096_ambient_dimension": retuned["max_ambient_dimension"],
        "min_4096_column_surplus": retuned["min_column_surplus"],
        "min_4096_column_surplus_s": retuned["min_column_surplus_s"],
        "min_4096_m_total": retuned["min_m_total"],
        "max_4096_m_total": retuned["max_m_total"],
    }


def main() -> None:
    summary = conic_dual_annihilator_summary()
    print("h=3 conic dual-annihilator target")
    print(
        "dual condition: sequences ell_0..ell_L killed by B^3 "
        "length-A shifted product windows"
    )
    print(
        "official rows: "
        f"s={summary['first_s']}..{summary['last_s']} "
        f"M={summary['min_m_total']}..{summary['max_m_total']} "
        f"A={summary['min_shift_window']}..{summary['max_shift_window']}"
    )
    print(
        "dual target: "
        f"annihilator_dimension <= {summary['allowance']} "
        f"inside ambient dimension {summary['min_ambient_dimension']}.."
        f"{summary['max_ambient_dimension']}"
    )
    print(
        "supply checks: "
        f"base_products >= {summary['min_base_products']} "
        f"(s={summary['min_base_products_s']}), "
        f"constraints-ambient >= {summary['min_column_surplus']} "
        f"(s={summary['min_column_surplus_s']})"
    )
    print(
        "retuned H3-ACT(4096) dual target: "
        f"annihilator_dimension <= {summary['allowance_4096']} "
        f"M={summary['min_4096_m_total']}..{summary['max_4096_m_total']} "
        f"A={summary['min_4096_shift_window']}.."
        f"{summary['max_4096_shift_window']}"
    )
    print(
        "retuned supply checks: "
        f"base_products >= {summary['min_4096_base_products']} "
        f"(s={summary['min_4096_base_products_s']}), "
        f"constraints-ambient >= {summary['min_4096_column_surplus']} "
        f"(s={summary['min_4096_column_surplus_s']})"
    )
    print("H3_CONIC_DUAL_ANNIHILATOR_TARGET_PASS")


if __name__ == "__main__":
    main()
