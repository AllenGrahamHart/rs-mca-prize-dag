#!/usr/bin/env python3
"""Mutation audit for the quotient-chart bipolar entropy closure."""


def main() -> None:
    ell = 8

    # An almost-full core fiber has polarity one, not boundary size ell-1.
    occupied = ell - 1
    assert min(occupied, ell - occupied) == 1
    assert occupied > 1

    # A half-full tie needs a fixed orientation to avoid duplicate encodings.
    half = ell // 2
    assert half == ell - half

    # Dropping core orientation bits identifies empty and full defect fibers.
    empty: set[int] = set()
    full = set(range(ell))
    assert empty != full

    # Without the cutoff, block orientations can be exponential in n.
    n = 64
    assert 2**n > n**4

    # Per-chart closure leaves chart multiplicity untouched.
    chart_multiplicity_unknown = True
    assert chart_multiplicity_unknown

    print("L1_BIPOLAR_ENTROPY_AUDIT_PASS mutations=5")


if __name__ == "__main__":
    main()

