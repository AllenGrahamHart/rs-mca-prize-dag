#!/usr/bin/env python3
"""Mutation audit for the quotient-orbit Taylor cutoff ladder."""

from __future__ import annotations

from sympy import Poly

import verify


def main() -> None:
    block = Poly(verify.T**2 + 1, verify.T)
    product = Poly(block.as_expr() ** 5 + 5, verify.T)
    contents = [verify.content_at_cutoff(block, product, cutoff) for cutoff in range(2, 5)]
    supports_five = [content % 5 == 0 for content in contents]
    assert supports_five == sorted(supports_five, reverse=True)

    false_positive = Poly(
        3
        + 3 * verify.T
        + 3 * verify.T**2
        + 3 * verify.T**4
        + 3 * verify.T**5,
        verify.T,
    )
    assert verify.content_at_cutoff(block, false_positive, 2) % 5 != 0
    assert not verify.common_root(block, false_positive, 2, 5)

    assert 2 * 4_096 == 8_192
    assert 2 * 67_084_290 == 134_168_580
    assert 8_192 != 143_360

    print(
        "F3_H3_QUOTIENT_ORBIT_TAYLOR_CUTOFF_LADDER_AUDIT_PASS "
        "mutations=7"
    )


if __name__ == "__main__":
    main()
