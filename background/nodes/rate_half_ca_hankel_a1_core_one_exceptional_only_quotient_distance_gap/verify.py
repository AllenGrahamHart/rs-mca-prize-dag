#!/usr/bin/env python3
"""Verify the exact exceptional-only quotient-distance gap arithmetic."""

from __future__ import annotations


E = 2**38 - 1
R = 2 * E + 1
K = 2 * E // 3


def incidence_gap(distance: int) -> tuple[int, int]:
    internal = (2 * E) // (distance - 1)
    lower = 2 * E * E + E * distance - 3 * E
    upper = 4 * E * (distance - 3) + internal * (R - distance + 3)
    return lower - upper, internal


def concave_numerator(distance: int) -> int:
    return -3 * distance * distance + (2 * E + 14) * distance - 6 * E - 17


def main() -> None:
    assert E == 3 * 174763 * 524287
    assert K == 183251937962
    assert concave_numerator(4) == 2 * E - 9 > 0
    assert concave_numerator(K + 1) == 4 * E // 3 - 6 > 0

    gap_at_last_killed, internal = incidence_gap(K + 2)
    assert internal == 2
    assert gap_at_last_killed == E // 3 - 4 > 0

    first_survivor = K + 3
    next_gap, next_internal = incidence_gap(first_survivor)
    assert first_survivor == 183251937965
    assert next_internal == 2
    assert next_gap < 0

    # Exact spot checks across every floor regime reached before the boundary.
    for distance in (4, 5, 10, E // 4, E // 2, K, K + 1, K + 2):
        gap, _ = incidence_gap(distance)
        assert gap > 0

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_"
        "QUOTIENT_DISTANCE_GAP_PASS "
        f"e={E} killed_max={K+2} survivor_min={first_survivor} "
        f"boundary_gap={gap_at_last_killed}"
    )


if __name__ == "__main__":
    main()
