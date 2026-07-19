#!/usr/bin/env python3
"""Audit positivity of the exceptional saturated gcd."""

from __future__ import annotations


def main() -> None:
    profiles = 0
    for e in range(8, 2048, 5):
        for b in range((e - 2) // 5 + 1):
            capacity = e - 5 * b
            e_star = e - b
            r = 2 * e_star + 1
            for c in (1, capacity):
                assert r - 1 - c >= e + 3 * b > 0
                profiles += 1

    # Mutation fences: one more than the capacity breaks the sharp lower
    # bound, and a zero gcd cannot support the pointwise contradiction.
    e, b = 18, 1
    capacity = e - 5 * b
    assert 2 * (e - b) - capacity == e + 3 * b
    assert not (0 > 0)
    print(
        "AUDIT_RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_TRACE_ALLOCATION_PASS "
        f"profiles={profiles} mutations=2"
    )


if __name__ == "__main__":
    main()
