#!/usr/bin/env python3
"""Dual-annihilator target for the h=3 conic codimension theorem."""

from __future__ import annotations

from dataclasses import dataclass

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


def conic_dual_annihilator_summary() -> dict[str, int]:
    deficit = rank_deficit_budget_summary()
    allowance = deficit["min_allowed_deficit"]
    if allowance != 1847:
        raise AssertionError(deficit)

    rows = tuple(dual_annihilator_row(row, allowance) for row in EXPECTED_ROWS)
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
    print("H3_CONIC_DUAL_ANNIHILATOR_TARGET_PASS")


if __name__ == "__main__":
    main()
