#!/usr/bin/env python3
"""Audit the zero-weld capacity contradiction and its strict boundary."""

from __future__ import annotations


def main() -> None:
    checked = 0
    for e in range(2, 4097):
        exact_capacity = e
        omitted_lower_bound = 3 * (e - 1)
        assert omitted_lower_bound > exact_capacity
        checked += 1

    # Mutation fences: with only two omitted rows the inequality is not
    # uniformly strict, and at e=1 the actual three-row bound is too small.
    assert 2 * (2 - 1) == 2
    assert 3 * (1 - 1) < 1
    print(
        "AUDIT_RATE_HALF_CA_HANKEL_A1_CORE_ONE_ZERO_WELD_EXCLUSION_PASS "
        f"degrees={checked} mutations=2"
    )


if __name__ == "__main__":
    main()
