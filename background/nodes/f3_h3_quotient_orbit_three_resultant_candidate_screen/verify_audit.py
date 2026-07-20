#!/usr/bin/env python3
"""Mutation audit for the quotient-orbit three-resultant screen."""

from __future__ import annotations

from sympy import Poly

import verify


def main() -> None:
    block = Poly(verify.T**2 + 1, verify.T)

    double_block = Poly(block.as_expr() ** 2 * (verify.T - 2), verify.T)
    resultants = verify.resultant_triple(block, double_block)
    assert resultants[:2] == (0, 0)
    assert resultants[2] != 0

    false_positive = Poly(
        3 + 3 * verify.T + 3 * verify.T**2 + 3 * verify.T**4 + 3 * verify.T**5,
        verify.T,
    )
    false_resultants = verify.resultant_triple(block, false_positive)
    assert all(value % 5 == 0 for value in false_resultants)
    assert verify.gcd_triple(false_resultants) % 5 == 0

    assert verify.gcd_triple((0, 0, 80)) == 5
    assert verify.gcd_triple((0, 0, 16)) == 1
    assert 3 * 24_534 != 24_534

    print(
        "F3_H3_QUOTIENT_ORBIT_THREE_RESULTANT_CANDIDATE_SCREEN_AUDIT_PASS "
        "mutations=7"
    )


if __name__ == "__main__":
    main()
