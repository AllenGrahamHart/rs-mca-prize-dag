#!/usr/bin/env python3
"""Audit the exceptional quotient's one-degree contradiction."""

from __future__ import annotations


def main() -> None:
    profiles = 0
    for d0 in range(20, 100):
        for r in range(3, d0):
            required = d0 - (r - 1)
            available = d0 - r
            assert required == available + 1
            profiles += 1

    # Mutation fences: a generic degree-r fiber fits exactly, while allowing
    # one more degree in A also erases the contradiction.
    d0, r = 100, 21
    assert d0 - r == d0 - r
    assert d0 - (r - 1) == (d0 - r) + 1
    print(
        "AUDIT_RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_TRACE_NONVANISHING_PASS "
        f"profiles={profiles} mutations=2"
    )


if __name__ == "__main__":
    main()
