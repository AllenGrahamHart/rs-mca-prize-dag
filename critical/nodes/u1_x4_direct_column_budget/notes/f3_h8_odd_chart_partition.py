#!/usr/bin/env python3
"""Structural odd-chart partition for h=8 non-antipodal x83 supports."""

from __future__ import annotations

from f3_h8_odd_chart_router import CHART_PRIORITY
from f3_h8_x83_parity_reduction import HIGH_ODD_DEGREES, parity_reduction_summary


def odd_chart_partition_summary() -> dict[str, int]:
    parity = parity_reduction_summary()
    priority_charts = tuple(chart for chart, _ in CHART_PRIORITY)
    priority_degrees = tuple(degree for _, degree in CHART_PRIORITY)
    if priority_charts != (7, 5, 3, 1):
        raise AssertionError(priority_charts)
    if priority_degrees != (9, 11, 13, 15):
        raise AssertionError(priority_degrees)
    if tuple(sorted(priority_degrees)) != HIGH_ODD_DEGREES:
        raise AssertionError((priority_degrees, HIGH_ODD_DEGREES))
    if parity["high_odd_degrees"] != len(priority_degrees):
        raise AssertionError(parity)
    return {
        "priority_charts": len(priority_charts),
        "first_chart": priority_charts[0],
        "last_chart": priority_charts[-1],
        "first_degree": priority_degrees[0],
        "last_degree": priority_degrees[-1],
        "high_odd_degrees": parity["high_odd_degrees"],
        "low_odd_degrees": parity["low_odd_degrees"],
        "max_denominator_prime": parity["max_denominator_prime"],
    }


def main() -> None:
    summary = odd_chart_partition_summary()
    print("h=8 odd-chart structural partition")
    print(
        "non-antipodal x83 full-zero support -> first nonzero high odd "
        "coefficient routes to a unique chart"
    )
    print(
        f"priority_charts={summary['priority_charts']} "
        f"priority={summary['first_chart']}..{summary['last_chart']} "
        f"degrees={summary['first_degree']}..{summary['last_degree']} "
        f"high_odd_degrees={summary['high_odd_degrees']} "
        f"low_odd_degrees={summary['low_odd_degrees']} "
        f"denom_prime={summary['max_denominator_prime']}"
    )
    print("H8_ODD_CHART_PARTITION_PASS")


if __name__ == "__main__":
    main()
