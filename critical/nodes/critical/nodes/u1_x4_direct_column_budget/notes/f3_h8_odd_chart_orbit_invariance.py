#!/usr/bin/env python3
"""Orbit invariance of the h=8 odd-chart partition."""

from __future__ import annotations

from f3_h8_odd_chart_partition import odd_chart_partition_summary
from f3_h8_odd_chart_scaling_action import odd_chart_scaling_summary


def odd_chart_orbit_invariance_summary() -> dict[str, int]:
    partition = odd_chart_partition_summary()
    scaling = odd_chart_scaling_summary()
    if partition["priority_charts"] != scaling["rows"]:
        raise AssertionError((partition, scaling))
    if scaling["max_stabilizer_size"] != 1:
        raise AssertionError(scaling)
    return {
        "priority_charts": partition["priority_charts"],
        "first_chart": partition["first_chart"],
        "last_chart": partition["last_chart"],
        "first_s": scaling["first_s"],
        "last_s": scaling["last_s"],
        "max_stabilizer_size": scaling["max_stabilizer_size"],
        "high_odd_degrees": partition["high_odd_degrees"],
    }


def main() -> None:
    summary = odd_chart_orbit_invariance_summary()
    print("h=8 odd-chart orbit invariance")
    print(
        "official root scaling preserves the high-odd zero pattern, hence "
        "preserves the first-live odd chart"
    )
    print(
        f"charts={summary['first_chart']}..{summary['last_chart']} "
        f"priority_charts={summary['priority_charts']} "
        f"s_range={summary['first_s']}..{summary['last_s']} "
        f"max_stabilizer={summary['max_stabilizer_size']} "
        f"high_odd_degrees={summary['high_odd_degrees']}"
    )
    print("H8_ODD_CHART_ORBIT_INVARIANCE_PASS")


if __name__ == "__main__":
    main()
