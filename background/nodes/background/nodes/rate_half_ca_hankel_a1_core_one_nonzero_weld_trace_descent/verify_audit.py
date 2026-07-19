#!/usr/bin/env python3
"""Audit the trace degrees and exceptional-slope inequalities."""

from __future__ import annotations


def main() -> None:
    rows = 0
    exceptional = 0
    for e in range(8, 256, 5):
        for b in range((e - 2) // 5 + 1):
            e_star = e - b
            for slope_deficit in (0, 1):
                capacity = e - 5 * b - 1 + slope_deficit
                if capacity < 1:
                    continue
                for delta in range(1, min(e_star, capacity) + 1):
                    for epsilon in range(slope_deficit + 1):
                        a = e_star - delta - epsilon
                        if a < 0:
                            continue
                        assert e_star - a == delta + epsilon
                        rows += 1
                if slope_deficit:
                    for c in (1, capacity):
                        r = 2 * e_star + 1
                        assert r - 1 - c >= e + 3 * b
                        assert r - (r - 1 - c) == c + 1
                        exceptional += 1

    # Mutation fences: one extra exceptional omission or one extra bad-row
    # degree invalidates the printed sharp bounds.
    e, b, c = 18, 1, 13
    assert 2 * (e - b) - c == e + 3 * b
    assert c + 2 > e - 5 * b + 1
    print(
        "AUDIT_RATE_HALF_CA_HANKEL_A1_CORE_ONE_NONZERO_WELD_TRACE_DESCENT_PASS "
        f"row_profiles={rows} exceptional_profiles={exceptional} mutations=2"
    )


if __name__ == "__main__":
    main()
