#!/usr/bin/env python3
"""Mutation audit for the gap-only parity counterexample."""

from __future__ import annotations

import verify


def main() -> None:
    original = verify.coefficients()
    changed = verify.coefficients((1, 1, 11, 35, 43))
    assert (original[14], original[15], original[16]) == (0, 0, 2)
    assert (changed[14], changed[15], changed[16]) != (0, 0, 2)

    correct_square = verify.multiply_truncated(
        list(verify.EXPECTED_C), list(verify.EXPECTED_C)
    )
    mutated_c = list(verify.EXPECTED_C)
    mutated_c[4] += 1
    assert verify.multiply_truncated(mutated_c, mutated_c) != correct_square

    roots = verify.EXPECTED_ROOTS
    assert all((-root) % verify.PRIME not in roots for root in roots)
    assert tuple(verify.order(root) for root in roots) != (56, 56, 56, 56)

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_GAP_ONLY_PARITY_COUNTEREXAMPLE_AUDIT_PASS "
        "mutations=3"
    )


if __name__ == "__main__":
    main()
