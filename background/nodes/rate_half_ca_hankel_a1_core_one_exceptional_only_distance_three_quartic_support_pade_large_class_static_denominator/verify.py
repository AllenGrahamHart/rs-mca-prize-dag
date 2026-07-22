#!/usr/bin/env python3
"""Exact controls for large-class Pade denominator rigidity."""

from __future__ import annotations


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def resultant_threshold(tail: int) -> tuple[int, int, int]:
    kernel_u_degree = 2 * (tail + 1)
    resultant_degree = 2 * kernel_u_degree * tail
    static_threshold = resultant_degree + tail
    return kernel_u_degree, resultant_degree, static_threshold


def main() -> None:
    antipodal = resultant_threshold(6)
    reciprocal = resultant_threshold(8)
    need(antipodal == (14, 168, 174), "antipodal threshold drifted")
    need(reciprocal == (18, 288, 296), "reciprocal threshold drifted")
    need(172410 > antipodal[2], "antipodal class does not force staticity")
    need(2128 > reciprocal[2], "reciprocal class does not force staticity")
    print(
        "RATE_HALF_DISTANCE_THREE_PADE_STATIC_DENOMINATOR_PASS "
        f"antipodal={antipodal} reciprocal={reciprocal} "
        "class_bounds=(172410,2128)"
    )


if __name__ == "__main__":
    main()
