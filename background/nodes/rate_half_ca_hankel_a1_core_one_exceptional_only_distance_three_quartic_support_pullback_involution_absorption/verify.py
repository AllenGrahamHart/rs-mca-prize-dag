#!/usr/bin/env python3
"""Exact controls for quartic-pullback involution absorption."""

from __future__ import annotations


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def budgets(fixed_points: int) -> tuple[int, int, int]:
    proportional = 2
    bootstrap_pair = 1
    comparison_pair = 2
    comparison_quartic = 4
    bootstrap = (
        proportional
        + fixed_points
        + bootstrap_pair
        + comparison_pair
        + comparison_quartic
    )
    final = proportional + fixed_points + comparison_quartic
    antiweight = proportional + fixed_points
    return bootstrap, final, antiweight


def main() -> None:
    antipodal = budgets(0)
    reciprocal = budgets(2)
    need(antipodal == (9, 6, 2), "antipodal absorption budget drifted")
    need(reciprocal == (11, 8, 4), "reciprocal absorption budget drifted")
    official_e = 2**38 - 1
    need(official_e - 148 > reciprocal[0], "captured set need not contain a deck orbit")
    print(
        "RATE_HALF_DISTANCE_THREE_PULLBACK_INVOLUTION_ABSORPTION_PASS "
        f"antipodal={antipodal} reciprocal={reciprocal} captured={official_e-148}"
    )


if __name__ == "__main__":
    main()
