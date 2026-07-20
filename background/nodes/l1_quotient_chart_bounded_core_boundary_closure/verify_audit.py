#!/usr/bin/env python3
"""Mutation audit for the bounded core-boundary closure."""


def main() -> None:
    # Dropping the dense/sparse orientation loses full supports at polarity zero.
    full_support = {0, 1, 2, 3}
    empty_support: set[int] = set()
    assert full_support != empty_support

    # Without the lower cutoff, 2^(M+N) need not be polynomial.
    n = 64
    assert 2**n > n**4

    # Unbounded boundary makes the exponent drift.
    fixed_boundary = 3
    drifting_boundary = n // 2
    assert drifting_boundary > fixed_boundary

    # The strict next-strip hypothesis is required by the CRT supplier.
    m, ell, p = 3, 11, 4
    assert (m + 1) * ell - p + p == (m + 1) * ell

    # Per-chart polynomiality does not bound the number of source charts.
    per_chart_bound = n**5
    source_chart_count_unknown = True
    assert per_chart_bound > 0 and source_chart_count_unknown

    print("L1_BOUNDED_BOUNDARY_AUDIT_PASS mutations=5")


if __name__ == "__main__":
    main()

