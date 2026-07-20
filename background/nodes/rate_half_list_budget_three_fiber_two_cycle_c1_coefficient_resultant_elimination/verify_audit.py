#!/usr/bin/env python3
"""Mutation audit for the c=1 coefficient-resultant elimination."""

from __future__ import annotations

import verify


def main() -> None:
    omega = (1, 4, 9, 16)

    positive_i, positive_j = verify.outer_invariants(
        (1, -1 % verify.PRIME, 2, 3)
    )
    assert verify.product(
        verify.ordered_packet(omega, positive_i, positive_j)
    ) == 0
    assert verify.product(
        verify.ordered_packet(
            omega,
            positive_i,
            positive_j,
            wrong_sum_sign=True,
        )
    ) != 0
    assert verify.product(
        verify.ordered_packet(
            omega,
            positive_i,
            positive_j,
            omit_product_in_norm=True,
        )
    ) != 0

    reverse_i, reverse_j = verify.outer_invariants(
        (4, -4 % verify.PRIME, 2, 3)
    )
    assert verify.product(
        verify.ordered_packet(omega, reverse_i, reverse_j)
    ) == 0
    assert verify.product(
        verify.ordered_packet(
            omega,
            reverse_i,
            reverse_j,
            increasing_only=True,
        )
    ) != 0

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_COEFFICIENT_RESULTANT_AUDIT_PASS "
        "mutations=3"
    )


if __name__ == "__main__":
    main()

