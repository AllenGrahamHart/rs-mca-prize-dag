#!/usr/bin/env python3
"""Compile chart-local recovery obligations for the h=5 reciprocal gate."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

from f3_h5_basefree_reciprocal_system import (
    ALL_BARS,
    basefree_summary,
    pairwise_polynomial,
    pairwise_rows,
    reciprocal_slots,
)
from f3_h5_reciprocal_compatibility_compiler import TOP
from f3_h5_reciprocal_open_cover import open_cover_summary
from f3_h5_unit_norm_reciprocal_gate import (
    unit_norm_polynomial,
    unit_norm_rows,
    unit_norm_summary,
)
from f3_h5_x83_triangular_norm_gate import LOCATOR


CONJUGATE = {
    **{TOP[index]: ALL_BARS[index] for index in range(len(TOP))},
    **{ALL_BARS[index]: TOP[index] for index in range(len(TOP))},
}


@dataclass(frozen=True)
class ChartRecoveryRow:
    chart: int
    denominator: str
    incident_minors: tuple[str, ...]
    unit_norm_row: str
    unit_terms: int
    unit_total_degree: int
    automatic_unit_norm: bool


@dataclass(frozen=True)
class CentralUnitSyzygy:
    key_index: int
    incident_minor: str
    conjugate_minor: str
    unit_norm_row: str
    saturation_multiplier: str


@dataclass(frozen=True)
class ChartSystemProfile:
    chart: int
    equations: int
    total_terms: int
    max_terms: int
    max_total_degree: int
    unit_norm_row: str


def conjugate(expr: sp.Expr) -> sp.Expr:
    return sp.expand(expr.xreplace(CONJUGATE))


def slot_numerator_denominator(
    slot: tuple[int, int, sp.Expr, sp.Symbol],
) -> tuple[sp.Expr, sp.Expr]:
    _, denominator, numerator, bar_var = slot
    return numerator, sp.Integer(denominator) * bar_var


def unit_norm_expression(slot: tuple[int, int, sp.Expr, sp.Symbol]) -> sp.Expr:
    numerator, denominator = slot_numerator_denominator(slot)
    return sp.factor(numerator * conjugate(numerator) - denominator * conjugate(denominator))


def incident_minor_names(chart: int) -> tuple[str, ...]:
    return tuple(f"C{min(chart, other)}{max(chart, other)}" for other in range(1, 6) if other != chart)


def chart_rows() -> tuple[ChartRecoveryRow, ...]:
    slots = reciprocal_slots()
    if tuple(slot[0] for slot in slots) != (1, 2, 3, 4, 5):
        raise AssertionError(slots)

    pairwise_names = {row.name for row in pairwise_rows()}
    unit_rows_by_name = {row.name: row for row in unit_norm_rows()}

    rows: list[ChartRecoveryRow] = []
    for slot in slots:
        chart, denominator_scalar, _, bar_var = slot
        minors = incident_minor_names(chart)
        if not set(minors).issubset(pairwise_names):
            raise AssertionError((chart, minors, pairwise_names))

        expression = unit_norm_expression(slot)
        if chart < 5:
            expected = unit_norm_polynomial(chart)
            if sp.factor(expression - expected) != 0:
                raise AssertionError((chart, expression, expected))
            unit_row = unit_rows_by_name[f"N{chart}"]
            rows.append(
                ChartRecoveryRow(
                    chart=chart,
                    denominator=f"{denominator_scalar}*{bar_var}",
                    incident_minors=minors,
                    unit_norm_row=unit_row.name,
                    unit_terms=unit_row.terms,
                    unit_total_degree=unit_row.total_degree,
                    automatic_unit_norm=False,
                )
            )
        else:
            if expression != 0:
                raise AssertionError((chart, expression))
            rows.append(
                ChartRecoveryRow(
                    chart=chart,
                    denominator=str(bar_var),
                    incident_minors=minors,
                    unit_norm_row="TAUTOLOGY",
                    unit_terms=0,
                    unit_total_degree=0,
                    automatic_unit_norm=True,
                )
            )

    return tuple(rows)


def central_unit_syzygies() -> tuple[CentralUnitSyzygy, ...]:
    slots = {slot[0]: slot for slot in reciprocal_slots()}
    rows: list[CentralUnitSyzygy] = []
    for key_index in range(1, 5):
        slot = slots[key_index]
        denominator, high_part = slot[1], slot[2]
        paired_top = LOCATOR[10 - key_index]
        incident_minor = pairwise_polynomial(slot, slots[5])
        conjugate_minor = conjugate(incident_minor)
        unit_norm = unit_norm_polynomial(key_index)

        lhs = sp.expand(LOCATOR[5] * unit_norm)
        rhs = sp.expand(high_part * conjugate_minor + denominator * paired_top * incident_minor)
        if sp.factor(lhs - rhs) != 0:
            raise AssertionError((key_index, sp.factor(lhs - rhs)))

        rows.append(
            CentralUnitSyzygy(
                key_index=key_index,
                incident_minor=f"C{key_index}5",
                conjugate_minor=f"conj(C{key_index}5)",
                unit_norm_row=f"N{key_index}",
                saturation_multiplier="l5",
            )
        )
    return tuple(rows)


def chart_system_profiles() -> tuple[ChartSystemProfile, ...]:
    pairwise = {row.name: row for row in pairwise_rows()}
    profiles = []
    for row in chart_rows():
        minor_terms = [pairwise[name].terms for name in row.incident_minors]
        minor_degrees = [pairwise[name].total_degree for name in row.incident_minors]
        equation_terms = minor_terms + ([] if row.automatic_unit_norm else [row.unit_terms])
        equation_degrees = minor_degrees + (
            [] if row.automatic_unit_norm else [row.unit_total_degree]
        )
        profiles.append(
            ChartSystemProfile(
                chart=row.chart,
                equations=len(row.incident_minors) + int(not row.automatic_unit_norm),
                total_terms=sum(equation_terms),
                max_terms=max(equation_terms),
                max_total_degree=max(equation_degrees),
                unit_norm_row=row.unit_norm_row,
            )
        )
    return tuple(profiles)


def chart_recovery_summary() -> dict[str, int]:
    basefree = basefree_summary()
    open_cover = open_cover_summary()
    unit_norm = unit_norm_summary()
    rows = chart_rows()
    syzygies = central_unit_syzygies()
    profiles = chart_system_profiles()

    expected = {
        1: ("16384*bar_l9", ("C12", "C13", "C14", "C15"), "N1", 485, 18, False),
        2: ("16384*bar_l8", ("C12", "C23", "C24", "C25"), "N2", 325, 16, False),
        3: ("256*bar_l7", ("C13", "C23", "C34", "C35"), "N3", 170, 14, False),
        4: ("512*bar_l6", ("C14", "C24", "C34", "C45"), "N4", 101, 12, False),
        5: ("bar_l5", ("C15", "C25", "C35", "C45"), "TAUTOLOGY", 0, 0, True),
    }
    actual = {
        row.chart: (
            row.denominator,
            row.incident_minors,
            row.unit_norm_row,
            row.unit_terms,
            row.unit_total_degree,
            row.automatic_unit_norm,
        )
        for row in rows
    }
    if actual != expected:
        raise AssertionError(actual)

    nontrivial = [row for row in rows if not row.automatic_unit_norm]
    tautological = [row for row in rows if row.automatic_unit_norm]
    if open_cover["charts"] != len(rows):
        raise AssertionError(open_cover)
    if unit_norm["equations"] != len(nontrivial):
        raise AssertionError(unit_norm)
    if len(syzygies) != len(nontrivial):
        raise AssertionError(syzygies)
    expected_profiles = {
        1: (5, 615, 485, 18, "N1"),
        2: (5, 443, 325, 16, "N2"),
        3: (5, 273, 170, 14, "N3"),
        4: (5, 195, 101, 12, "N4"),
        5: (4, 67, 23, 10, "TAUTOLOGY"),
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

    return {
        "charts": len(rows),
        "pairwise_equations": basefree["pairwise_equations"],
        "incident_minors_per_chart": len(rows[0].incident_minors),
        "nontrivial_unit_charts": len(nontrivial),
        "tautological_unit_charts": len(tautological),
        "central_unit_syzygies": len(syzygies),
        "min_chart_total_terms": min(row.total_terms for row in profiles),
        "max_chart_total_terms": max(row.total_terms for row in profiles),
        "min_chart_equations": min(row.equations for row in profiles),
        "max_chart_equations": max(row.equations for row in profiles),
        "central_chart_total_terms": profiles[-1].total_terms,
        "central_chart_max_degree": profiles[-1].max_total_degree,
        "max_chart_unit_degree": max(row.unit_total_degree for row in rows),
        "max_chart_unit_terms": max(row.unit_terms for row in rows),
        "official_max_x10_fiber": open_cover["official_max_x10_fiber"],
    }


def main() -> None:
    summary = chart_recovery_summary()
    print("h=5 chart-local reciprocal recovery")
    for row in chart_rows():
        print(
            f"  chart {row.chart}: denominator={row.denominator} "
            f"minors={','.join(row.incident_minors)} "
            f"unit_norm={row.unit_norm_row} "
            f"terms={row.unit_terms} degree={row.unit_total_degree}"
        )
    for row in central_unit_syzygies():
        print(
            f"  central syzygy {row.unit_norm_row}: "
            f"{row.saturation_multiplier}*{row.unit_norm_row} in "
            f"<{row.incident_minor},{row.conjugate_minor}>"
        )
    for row in chart_system_profiles():
        print(
            f"  chart profile {row.chart}: equations={row.equations} "
            f"total_terms={row.total_terms} max_terms={row.max_terms} "
            f"max_degree={row.max_total_degree} unit={row.unit_norm_row}"
        )
    print(
        "summary: "
        f"charts={summary['charts']} "
        f"pairwise_equations={summary['pairwise_equations']} "
        f"incident_minors_per_chart={summary['incident_minors_per_chart']} "
        f"nontrivial_unit_charts={summary['nontrivial_unit_charts']} "
        f"tautological_unit_charts={summary['tautological_unit_charts']} "
        f"central_unit_syzygies={summary['central_unit_syzygies']} "
        f"chart_terms={summary['min_chart_total_terms']}.."
        f"{summary['max_chart_total_terms']} "
        f"central_chart_terms={summary['central_chart_total_terms']} "
        f"central_chart_max_degree={summary['central_chart_max_degree']} "
        f"max_unit_degree={summary['max_chart_unit_degree']} "
        f"max_unit_terms={summary['max_chart_unit_terms']} "
        f"official_max_x10_fiber={summary['official_max_x10_fiber']}"
    )
    print("H5_CHART_RECOVERY_COMPILER_PASS")


if __name__ == "__main__":
    main()
