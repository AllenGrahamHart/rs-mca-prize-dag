#!/usr/bin/env python3
"""Official root-scaling action on all h=8 odd charts."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from math import gcd

from f3_h8_odd_chart_partition import odd_chart_partition_summary
from f3_h8_odd_chart_router import CHART_PRIORITY
from f3_h8_weighted_homogeneity import WEIGHTS, ALL_BARS, weighted_homogeneity_summary


OFFICIAL_EXPONENTS = tuple(range(13, 42))


@dataclass(frozen=True)
class OddChartScalingRow:
    chart: int
    locator_degree: int
    denominator_weight: int
    max_gcd: int
    max_stabilizer_size: int


def bar_variable_for_degree(locator_degree: int):
    return ALL_BARS[locator_degree - 8]


@lru_cache(maxsize=1)
def odd_chart_scaling_rows() -> tuple[OddChartScalingRow, ...]:
    rows: list[OddChartScalingRow] = []
    for chart, locator_degree in CHART_PRIORITY:
        denominator_weight = WEIGHTS[bar_variable_for_degree(locator_degree)]
        stabilizers = [
            gcd(abs(denominator_weight), 2**exponent)
            for exponent in OFFICIAL_EXPONENTS
        ]
        rows.append(
            OddChartScalingRow(
                chart=chart,
                locator_degree=locator_degree,
                denominator_weight=denominator_weight,
                max_gcd=max(stabilizers),
                max_stabilizer_size=max(stabilizers),
            )
        )
    return tuple(rows)


@lru_cache(maxsize=1)
def odd_chart_scaling_summary() -> dict[str, int]:
    weighted = weighted_homogeneity_summary()
    partition = odd_chart_partition_summary()
    rows = odd_chart_scaling_rows()
    if weighted["pairwise_rows"] != 28 or weighted["unit_rows"] != 7:
        raise AssertionError(weighted)
    if partition["priority_charts"] != len(rows):
        raise AssertionError(partition)
    if tuple(row.chart for row in rows) != (7, 5, 3, 1):
        raise AssertionError(rows)
    if any(row.denominator_weight != -row.chart for row in rows):
        raise AssertionError(rows)
    if any(row.max_stabilizer_size != 1 for row in rows):
        raise AssertionError(rows)
    return {
        "rows": len(rows),
        "first_s": OFFICIAL_EXPONENTS[0],
        "last_s": OFFICIAL_EXPONENTS[-1],
        "first_chart": rows[0].chart,
        "last_chart": rows[-1].chart,
        "max_gcd": max(row.max_gcd for row in rows),
        "max_stabilizer_size": max(row.max_stabilizer_size for row in rows),
        "weighted_pairwise_rows": weighted["pairwise_rows"],
        "weighted_unit_rows": weighted["unit_rows"],
    }


def main() -> None:
    summary = odd_chart_scaling_summary()
    print("h=8 odd-chart official scaling action")
    print("support scaling by gamma in mu_n sends c_i -> gamma^(16-i)c_i")
    for row in odd_chart_scaling_rows():
        print(
            f"  chart={row.chart}: bar_c{row.locator_degree} "
            f"weight={row.denominator_weight} "
            f"max_gcd={row.max_gcd} "
            f"max_stabilizer={row.max_stabilizer_size}"
        )
    print(
        "summary: "
        f"rows={summary['rows']} "
        f"s_range={summary['first_s']}..{summary['last_s']} "
        f"charts={summary['first_chart']}..{summary['last_chart']} "
        f"max_gcd={summary['max_gcd']} "
        f"max_stabilizer_size={summary['max_stabilizer_size']}"
    )
    print("H8_ODD_CHART_SCALING_ACTION_PASS")


if __name__ == "__main__":
    main()
