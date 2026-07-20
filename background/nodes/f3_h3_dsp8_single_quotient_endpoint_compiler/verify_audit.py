#!/usr/bin/env python3
"""Mutation audit for the C36' single-quotient endpoint."""

from __future__ import annotations

from fractions import Fraction

import verify


def main() -> None:
    order = 8192
    exact = verify.budget(order)
    assert exact == 300 * order * order - 17 * 17 * (order - 1) * (order - 2)
    assert exact != 300 * order * order - 17 * 17 * (order - 2) ** 2

    assert Fraction(18, verify.free_floor(16)) == Fraction(9, 29)
    assert Fraction(18, verify.antipodal_floor(16)) == Fraction(9, 22)
    assert Fraction(17, verify.free_floor(16)) != Fraction(9, 29)

    fibers = verify.zero_center_fibers(32)
    maximum = max(map(len, fibers.values()))
    assert maximum == 2
    assert maximum > 1
    assert 1 + 6 > maximum

    print(
        "F3_H3_DSP8_SINGLE_QUOTIENT_ENDPOINT_COMPILER_AUDIT_PASS "
        "mutations=5"
    )


if __name__ == "__main__":
    main()
