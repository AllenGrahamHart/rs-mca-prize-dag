#!/usr/bin/env python3
"""Abstract minor propagation for h=5 rank-one reciprocal charts."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

import sympy as sp


SLOTS = range(1, 6)
A = {index: sp.Symbol(f"A{index}") for index in SLOTS}
B = {index: sp.Symbol(f"B{index}") for index in SLOTS}


@dataclass(frozen=True)
class MinorPropagationSyzygy:
    chart: int
    target_minor: str
    incident_minor_a: str
    incident_minor_b: str
    saturation_multiplier: str


def oriented_minor(left: int, right: int) -> sp.Expr:
    return B[right] * A[left] - B[left] * A[right]


def minor_name(left: int, right: int) -> str:
    return f"C{left}{right}"


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


def minor_propagation_summary() -> dict[str, int]:
    rows = minor_propagation_syzygies()
    by_chart = {chart: 0 for chart in SLOTS}
    for row in rows:
        by_chart[row.chart] += 1
    expected = {chart: 6 for chart in SLOTS}
    if by_chart != expected:
        raise AssertionError(by_chart)
    return {
        "charts": len(tuple(SLOTS)),
        "ordered_chart_syzygies": len(rows),
        "nonincident_minors_per_chart": min(by_chart.values()),
        "incident_minors_per_chart": 4,
        "total_pairwise_minors": 10,
    }


def main() -> None:
    summary = minor_propagation_summary()
    print("h=5 rank-one minor propagation")
    print("identity: B_i*C_jk + B_k*C_ij - B_j*C_ik = 0")
    print(
        "summary: "
        f"charts={summary['charts']} "
        f"ordered_chart_syzygies={summary['ordered_chart_syzygies']} "
        f"incident_minors_per_chart={summary['incident_minors_per_chart']} "
        f"nonincident_minors_per_chart={summary['nonincident_minors_per_chart']} "
        f"total_pairwise_minors={summary['total_pairwise_minors']}"
    )
    print("H5_RANK_ONE_MINOR_PROPAGATION_PASS")


if __name__ == "__main__":
    main()
