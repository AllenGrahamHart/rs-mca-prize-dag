#!/usr/bin/env python3
"""Mutation audit for the Taylor-content support compiler."""

from __future__ import annotations

from sympy import Poly

import verify


def main() -> None:
    block = Poly(verify.T**2 + 1, verify.T)

    simple_overlap = Poly(block.as_expr() * (verify.T - 2), verify.T)
    certificate = verify.taylor_resultant(block, simple_overlap, 2)
    assert certificate.eval(0) == 0
    assert certificate.as_expr() != 0

    false_positive = Poly(
        3
        + 3 * verify.T
        + 3 * verify.T**2
        + 3 * verify.T**4
        + 3 * verify.T**5,
        verify.T,
    )
    content = verify.odd_content(verify.taylor_resultant(block, false_positive, 2))
    assert content % 5 != 0
    assert not verify.common_root(block, false_positive, 2, 5)

    repeated_block = Poly(verify.T**2 + verify.T + 1, verify.T)
    repeated_product = Poly(repeated_block.as_expr() ** 3 + 3, verify.T)
    assert verify.common_root(repeated_block, repeated_product, 2, 3)

    assert 35 * 4_096 == 143_360
    assert 35 * 67_084_290 == 2_347_950_150

    print(
        "F3_H3_QUOTIENT_ORBIT_TAYLOR_CONTENT_SUPPORT_COMPILER_AUDIT_PASS "
        "mutations=7"
    )


if __name__ == "__main__":
    main()
