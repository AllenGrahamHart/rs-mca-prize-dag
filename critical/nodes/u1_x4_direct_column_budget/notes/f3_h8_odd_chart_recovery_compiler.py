#!/usr/bin/env python3
"""Compile odd-chart reciprocal recovery targets for h=8 x83."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h8_basefree_reciprocal_system import (
    basefree_summary,
    pairwise_rows,
    reciprocal_slots,
)
from f3_h8_unit_norm_reciprocal_gate import unit_norm_rows, unit_norm_summary
from f3_h8_x83_parity_reduction import parity_reduction_summary


ODD_CHARTS = (1, 3, 5, 7)


@dataclass(frozen=True)
class OddChartRow:
    chart: int
    high_locator_degree: int
    denominator: str
    incident_minors: tuple[str, ...]
    unit_norm_row: str
    unit_terms: int
    unit_total_degree: int


@dataclass(frozen=True)
class ChartSystemProfile:
    chart: int
    equations: int
    total_terms: int
    max_terms: int
    max_total_degree: int
    unit_norm_row: str


def incident_minor_names(chart: int) -> tuple[str, ...]:
    return tuple(f"C{min(chart, other)}{max(chart, other)}" for other in range(1, 9) if other != chart)


def odd_chart_rows() -> tuple[OddChartRow, ...]:
    slots = {slot[0]: slot for slot in reciprocal_slots()}
    pairwise_names = {row.name for row in pairwise_rows()}
    unit_rows_by_name = {row.name: row for row in unit_norm_rows()}
    rows: list[OddChartRow] = []

    for chart in ODD_CHARTS:
        _, denominator_scalar, _, bar_var = slots[chart]
        minors = incident_minor_names(chart)
        if not set(minors).issubset(pairwise_names):
            raise AssertionError((chart, minors, pairwise_names))
        unit = unit_rows_by_name[f"N{chart}"]
        rows.append(
            OddChartRow(
                chart=chart,
                high_locator_degree=16 - chart,
                denominator=f"{denominator_scalar}*{bar_var}",
                incident_minors=minors,
                unit_norm_row=unit.name,
                unit_terms=unit.terms,
                unit_total_degree=unit.total_degree,
            )
        )
    return tuple(rows)


def chart_system_profiles() -> tuple[ChartSystemProfile, ...]:
    pairwise = {row.name: row for row in pairwise_rows()}
    profiles = []
    for row in odd_chart_rows():
        minor_terms = [pairwise[name].terms for name in row.incident_minors]
        minor_degrees = [pairwise[name].total_degree for name in row.incident_minors]
        equation_terms = minor_terms + [row.unit_terms]
        equation_degrees = minor_degrees + [row.unit_total_degree]
        profiles.append(
            ChartSystemProfile(
                chart=row.chart,
                equations=len(row.incident_minors) + 1,
                total_terms=sum(equation_terms),
                max_terms=max(equation_terms),
                max_total_degree=max(equation_degrees),
                unit_norm_row=row.unit_norm_row,
            )
        )
    return tuple(profiles)


def odd_chart_recovery_summary() -> dict[str, int]:
    parity = parity_reduction_summary()
    basefree = basefree_summary()
    unit_norm = unit_norm_summary()
    rows = odd_chart_rows()
    profiles = chart_system_profiles()

    expected_rows = {
        1: (
            15,
            "33554432*bar_c15",
            ("C12", "C13", "C14", "C15", "C16", "C17", "C18"),
            "N1",
            19601,
            30,
        ),
        3: (
            13,
            "4194304*bar_c13",
            ("C13", "C23", "C34", "C35", "C36", "C37", "C38"),
            "N3",
            7922,
            26,
        ),
        5: (
            11,
            "262144*bar_c11",
            ("C15", "C25", "C35", "C45", "C56", "C57", "C58"),
            "N5",
            2705,
            22,
        ),
        7: (
            9,
            "32768*bar_c9",
            ("C17", "C27", "C37", "C47", "C57", "C67", "C78"),
            "N7",
            842,
            18,
        ),
    }
    actual_rows = {
        row.chart: (
            row.high_locator_degree,
            row.denominator,
            row.incident_minors,
            row.unit_norm_row,
            row.unit_terms,
            row.unit_total_degree,
        )
        for row in rows
    }
    if actual_rows != expected_rows:
        raise AssertionError(actual_rows)

    expected_profiles = {
        1: (8, 20977, 19601, 30, "N1"),
        3: (8, 8992, 7922, 26, "N3"),
        5: (8, 3553, 2705, 22, "N5"),
        7: (8, 1552, 842, 18, "N7"),
    }
    actual_profiles = {
        row.chart: (
            row.equations,
            row.total_terms,
            row.max_terms,
            row.max_total_degree,
            row.unit_norm_row,
        )
        for row in profiles
    }
    if actual_profiles != expected_profiles:
        raise AssertionError(actual_profiles)
    if parity["high_odd_degrees"] != len(ODD_CHARTS):
        raise AssertionError(parity)
    if basefree["pairwise_equations"] != 28 or unit_norm["equations"] != 7:
        raise AssertionError((basefree, unit_norm))

    return {
        "odd_charts": len(rows),
        "incident_minors_per_chart": len(rows[0].incident_minors),
        "equations_per_chart": min(row.equations for row in profiles),
        "min_chart_total_terms": min(row.total_terms for row in profiles),
        "max_chart_total_terms": max(row.total_terms for row in profiles),
        "min_chart_max_degree": min(row.max_total_degree for row in profiles),
        "max_chart_max_degree": max(row.max_total_degree for row in profiles),
        "max_unit_terms": max(row.unit_terms for row in rows),
        "max_unit_degree": max(row.unit_total_degree for row in rows),
        "basefree_pairwise_equations": basefree["pairwise_equations"],
        "parity_high_odd_degrees": parity["high_odd_degrees"],
    }


def main() -> None:
    summary = odd_chart_recovery_summary()
    print("h=8 odd-chart reciprocal recovery")
    print("open cover: non-antipodal x83 survivor has one high odd coefficient")
    for row in odd_chart_rows():
        print(
            f"  chart {row.chart}: high_c={row.high_locator_degree} "
            f"denominator={row.denominator} "
            f"minors={','.join(row.incident_minors)} "
            f"unit_norm={row.unit_norm_row} "
            f"terms={row.unit_terms} degree={row.unit_total_degree}"
        )
    for row in chart_system_profiles():
        print(
            f"  chart profile {row.chart}: equations={row.equations} "
            f"total_terms={row.total_terms} max_terms={row.max_terms} "
            f"max_degree={row.max_total_degree} unit={row.unit_norm_row}"
        )
    print(
        "summary: "
        f"odd_charts={summary['odd_charts']} "
        f"incident_minors_per_chart={summary['incident_minors_per_chart']} "
        f"equations_per_chart={summary['equations_per_chart']} "
        f"chart_terms={summary['min_chart_total_terms']}.."
        f"{summary['max_chart_total_terms']} "
        f"chart_max_degrees={summary['min_chart_max_degree']}.."
        f"{summary['max_chart_max_degree']} "
        f"max_unit_terms={summary['max_unit_terms']} "
        f"basefree_pairwise_equations={summary['basefree_pairwise_equations']} "
        f"parity_high_odd_degrees={summary['parity_high_odd_degrees']}"
    )
    print("H8_ODD_CHART_RECOVERY_COMPILER_PASS")


if __name__ == "__main__":
    main()
