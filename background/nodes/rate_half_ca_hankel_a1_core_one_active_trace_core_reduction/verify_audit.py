#!/usr/bin/env python3
"""Audit zero-trace capacity at bounded core-one analogues."""

from __future__ import annotations


def main() -> None:
    profiles = 0
    boundaries = 0
    for e in range(8, 2048, 5):
        for b in range((e - 2) // 5 + 1):
            e_star = e - b
            for slope_deficit in (0, 1):
                capacity = e - 5 * b - 1 + slope_deficit
                if capacity < 1:
                    continue
                if not slope_deficit:
                    assert capacity < e_star
                else:
                    assert 2 * (e_star - 1) > capacity
                    if capacity >= e_star - 1:
                        assert b == 0
                        assert capacity == e_star
                        boundaries += 1
                profiles += 1

    # Mutation fences: D_*=2 permits two exceptional roots, and e=1 erases
    # the strict two-row inequality.
    e, b = 18, 0
    assert e - 1 + 2 > e - b
    assert 2 * (1 - 1) == 0
    print(
        "AUDIT_RATE_HALF_CA_HANKEL_A1_CORE_ONE_ACTIVE_TRACE_CORE_REDUCTION_PASS "
        f"profiles={profiles} boundaries={boundaries} mutations=2"
    )


if __name__ == "__main__":
    main()
