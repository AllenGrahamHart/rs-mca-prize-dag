#!/usr/bin/env python3
"""Abstract rank-one propagation identities for h=8 reciprocal charts."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

import sympy as sp


SLOTS = range(1, 9)
A = {index: sp.Symbol(f"A{index}") for index in SLOTS}
B = {index: sp.Symbol(f"B{index}") for index in SLOTS}
ABAR = {index: sp.Symbol(f"bar_A{index}") for index in SLOTS}
BBAR = {index: sp.Symbol(f"bar_B{index}") for index in SLOTS}


@dataclass(frozen=True)
class MinorPropagationSyzygy:
    chart: int
    target_minor: str
    incident_minor_a: str
    incident_minor_b: str
    saturation_multiplier: str


@dataclass(frozen=True)
class UnitPropagationSyzygy:
    source_chart: int
    target_slot: int
    source_unit: str
    target_unit: str
    oriented_minor: str
    conjugate_minor: str


def oriented_minor(left: int, right: int) -> sp.Expr:
    return B[right] * A[left] - B[left] * A[right]


def conjugate_minor(left: int, right: int) -> sp.Expr:
    return BBAR[right] * ABAR[left] - BBAR[left] * ABAR[right]


def minor_name(left: int, right: int) -> str:
    return f"C{min(left, right)}{max(left, right)}"


def unit_row(index: int) -> sp.Expr:
    return A[index] * ABAR[index] - B[index] * BBAR[index]


def minor_propagation_syzygies() -> tuple[MinorPropagationSyzygy, ...]:
    rows: list[MinorPropagationSyzygy] = []
    for chart in SLOTS:
        others = [slot for slot in SLOTS if slot != chart]
        for left, right in combinations(others, 2):
            identity = sp.expand(
                B[chart] * oriented_minor(left, right)
                + B[right] * oriented_minor(chart, left)
                - B[left] * oriented_minor(chart, right)
            )
            if identity != 0:
                raise AssertionError((chart, left, right, sp.factor(identity)))
            rows.append(
                MinorPropagationSyzygy(
                    chart=chart,
                    target_minor=minor_name(left, right),
                    incident_minor_a=minor_name(chart, left),
                    incident_minor_b=minor_name(chart, right),
                    saturation_multiplier=f"B{chart}",
                )
            )
    return tuple(rows)


def unit_propagation_syzygies() -> tuple[UnitPropagationSyzygy, ...]:
    rows: list[UnitPropagationSyzygy] = []
    for source in SLOTS:
        for target in SLOTS:
            if source == target:
                continue
            c_st = oriented_minor(source, target)
            cbar_st = conjugate_minor(source, target)
            identity = sp.expand(
                B[source] * BBAR[source] * unit_row(target)
                - B[target] * BBAR[target] * unit_row(source)
                + BBAR[source] * ABAR[target] * c_st
                + B[target] * A[source] * cbar_st
            )
            if identity != 0:
                raise AssertionError((source, target, sp.factor(identity)))
            rows.append(
                UnitPropagationSyzygy(
                    source_chart=source,
                    target_slot=target,
                    source_unit=f"N{source}",
                    target_unit=f"N{target}",
                    oriented_minor=f"C{source}->{target}",
                    conjugate_minor=f"conj(C{source}->{target})",
                )
            )
    return tuple(rows)


def chart_propagation_summary() -> dict[str, int]:
    minor_rows = minor_propagation_syzygies()
    unit_rows = unit_propagation_syzygies()
    minor_by_chart = {chart: 0 for chart in SLOTS}
    unit_by_chart = {chart: 0 for chart in SLOTS}
    for row in minor_rows:
        minor_by_chart[row.chart] += 1
    for row in unit_rows:
        unit_by_chart[row.source_chart] += 1

    expected_minor = {chart: 21 for chart in SLOTS}
    expected_unit = {chart: 7 for chart in SLOTS}
    if minor_by_chart != expected_minor:
        raise AssertionError(minor_by_chart)
    if unit_by_chart != expected_unit:
        raise AssertionError(unit_by_chart)

    return {
        "charts": len(tuple(SLOTS)),
        "incident_minors_per_chart": 7,
        "nonincident_minors_per_chart": min(minor_by_chart.values()),
        "minor_syzygies": len(minor_rows),
        "unit_targets_per_chart": min(unit_by_chart.values()),
        "unit_syzygies": len(unit_rows),
        "total_pairwise_minors": 28,
    }


def main() -> None:
    summary = chart_propagation_summary()
    print("h=8 rank-one chart propagation")
    print("minor identity: B_i*C_jk + B_k*C_ij - B_j*C_ik = 0")
    print(
        "unit identity: B_i*bar_B_i*N_j - B_j*bar_B_j*N_i "
        "in <C_ij,conj(C_ij)>"
    )
    print(
        "summary: "
        f"charts={summary['charts']} "
        f"incident_minors_per_chart={summary['incident_minors_per_chart']} "
        f"nonincident_minors_per_chart={summary['nonincident_minors_per_chart']} "
        f"minor_syzygies={summary['minor_syzygies']} "
        f"unit_targets_per_chart={summary['unit_targets_per_chart']} "
        f"unit_syzygies={summary['unit_syzygies']} "
        f"total_pairwise_minors={summary['total_pairwise_minors']}"
    )
    print("H8_RANK_ONE_CHART_PROPAGATION_PASS")


if __name__ == "__main__":
    main()
