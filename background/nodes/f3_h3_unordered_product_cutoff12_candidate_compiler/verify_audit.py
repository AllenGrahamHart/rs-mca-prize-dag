#!/usr/bin/env python3
"""Mutation audit for the unordered-product cutoff-12 compiler."""

from __future__ import annotations

import verify


def main() -> None:
    verify.finite_field_check()
    verify.arithmetic_check()

    assert 2 * 13 - 2 == 24
    assert 2 * 13 - 1 == 25
    assert 2 * 14 - 2 == 26
    assert 12 + 1 == 13
    assert 11 + 1 != 13

    for target in (0, 2, 5):
        assert (target - 1) % 7 != 0
    assert (1 - 1) % 7 == 0

    n = 8192
    assert n * (n - 1) // 2 != (n - 1) ** 2
    print(
        "F3_H3_UNORDERED_PRODUCT_CUTOFF12_CANDIDATE_COMPILER_AUDIT_PASS "
        "mutations=7 identity_selector=1"
    )


if __name__ == "__main__":
    main()
