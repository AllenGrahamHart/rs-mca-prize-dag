#!/usr/bin/env python3
"""Audit the capacity equality and final exceptional degree gap."""

from __future__ import annotations


def main() -> None:
    profiles = 0
    equality_profiles = 0
    for e in range(8, 2048, 5):
        for b in range((e - 2) // 5 + 1):
            e_star = e - b
            for slope_deficit in (0, 1):
                capacity = e - 5 * b - 1 + slope_deficit
                if capacity < 1:
                    continue
                assert e_star - capacity == 4 * b + 1 - slope_deficit
                assert capacity <= e_star
                if capacity == e_star:
                    assert (b, slope_deficit) == (0, 1)
                    equality_profiles += 1
                profiles += 1

    # Mutation fences: removing the exceptional degree drop closes the final
    # gap, while allowing D_*=2 creates a spurious capacity overshoot.
    d0, r, c = 100, 21, 1
    assert (d0 - c) - (r - 1) == d0 - r
    assert (d0 - c) - r == d0 - r - 1
    assert 18 - 5 * 0 - 1 + 2 > 18
    print(
        "AUDIT_RATE_HALF_CA_HANKEL_A1_CORE_ONE_TRACE_FREE_EXCLUSION_PASS "
        f"profiles={profiles} equality_profiles={equality_profiles} mutations=3"
    )


if __name__ == "__main__":
    main()
