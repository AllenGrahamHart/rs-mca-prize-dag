#!/usr/bin/env python3
"""Deterministic odd-chart router for h=8 non-antipodal x83 supports."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os

from f3_h8_n64_x83_obstruction_interface import (
    is_antipodal_support,
    locator_from_exponents,
    root_table,
)
from f3_h8_x83_orbit_certifier_skeleton import (
    N,
    anchored_support_from_rank,
    is_rotation_canonical,
)
from f3_h8_x83_parity_reduction import has_high_odd_locator_term


CHART_PRIORITY = (
    (7, 9),
    (5, 11),
    (3, 13),
    (1, 15),
)
DEFAULT_SAMPLE_SUPPORTS = 2048


@dataclass(frozen=True)
class ChartRoute:
    chart: int
    locator_degree: int


def odd_chart_for_locator(locator: list[int]) -> ChartRoute | None:
    for chart, degree in CHART_PRIORITY:
        if locator[degree] != 0:
            return ChartRoute(chart=chart, locator_degree=degree)
    return None


def route_support(support: tuple[int, ...], vals: list[int], p: int) -> ChartRoute | None:
    locator = locator_from_exponents(support, vals, p)
    route = odd_chart_for_locator(locator)
    if (route is not None) != has_high_odd_locator_term(locator):
        raise AssertionError((support, locator, route))
    return route


def sample_routes() -> dict[str, int]:
    p = int(os.environ.get("F3_H8_ROUTER_P", "4289"))
    start_rank = int(os.environ.get("F3_H8_ROUTER_START_RANK", "0"))
    max_supports = int(os.environ.get("F3_H8_ROUTER_MAX_SUPPORTS", str(DEFAULT_SAMPLE_SUPPORTS)))
    stop_rank = start_rank + max_supports
    vals = root_table(p, N)

    processed = 0
    nonantipodal = 0
    canonical = 0
    routed = 0
    unrouted_high_odd_zero = 0
    chart_counts = {chart: 0 for chart, _ in CHART_PRIORITY}

    for rank in range(start_rank, stop_rank):
        support = anchored_support_from_rank(rank)
        processed += 1
        if is_antipodal_support(support, N):
            continue
        nonantipodal += 1
        if not is_rotation_canonical(support):
            continue
        canonical += 1
        route = route_support(support, vals, p)
        if route is None:
            unrouted_high_odd_zero += 1
            continue
        chart_counts[route.chart] += 1
        routed += 1

    return {
        "p": p,
        "start_rank": start_rank,
        "stop_rank": stop_rank,
        "processed": processed,
        "nonantipodal": nonantipodal,
        "canonical": canonical,
        "routed": routed,
        "unrouted_high_odd_zero": unrouted_high_odd_zero,
        "chart_7": chart_counts[7],
        "chart_5": chart_counts[5],
        "chart_3": chart_counts[3],
        "chart_1": chart_counts[1],
    }


def router_summary() -> dict[str, int]:
    priority_charts = tuple(chart for chart, _ in CHART_PRIORITY)
    priority_degrees = tuple(degree for _, degree in CHART_PRIORITY)
    if priority_charts != (7, 5, 3, 1):
        raise AssertionError(priority_charts)
    if priority_degrees != (9, 11, 13, 15):
        raise AssertionError(priority_degrees)
    sample = sample_routes()
    if sample["routed"] != (
        sample["chart_7"] + sample["chart_5"] + sample["chart_3"] + sample["chart_1"]
    ):
        raise AssertionError(sample)
    if sample["canonical"] != sample["routed"] + sample["unrouted_high_odd_zero"]:
        raise AssertionError(sample)
    return {
        "priority_charts": len(priority_charts),
        "first_chart": priority_charts[0],
        "last_chart": priority_charts[-1],
        "first_degree": priority_degrees[0],
        "last_degree": priority_degrees[-1],
        **sample,
    }


def main() -> None:
    summary = router_summary()
    print("h=8 odd-chart router")
    print("priority: c9 -> chart 7, c11 -> chart 5, c13 -> chart 3, c15 -> chart 1")
    print(
        f"sample p={summary['p']} ranks={summary['start_rank']}.."
        f"{summary['stop_rank']}"
    )
    print(
        "sample counts: "
        f"processed={summary['processed']} "
        f"nonantipodal={summary['nonantipodal']} "
        f"canonical={summary['canonical']} "
        f"routed={summary['routed']} "
        f"unrouted_high_odd_zero={summary['unrouted_high_odd_zero']} "
        f"chart7={summary['chart_7']} "
        f"chart5={summary['chart_5']} "
        f"chart3={summary['chart_3']} "
        f"chart1={summary['chart_1']}"
    )
    print("ROUTER_RECORD " + json.dumps(summary, sort_keys=True))
    print("H8_ODD_CHART_ROUTER_PASS")


if __name__ == "__main__":
    main()
