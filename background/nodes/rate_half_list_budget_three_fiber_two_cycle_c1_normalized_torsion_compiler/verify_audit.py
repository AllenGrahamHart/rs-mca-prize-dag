#!/usr/bin/env python3
"""Mutation audit for the c=1 normalized torsion compiler."""

from __future__ import annotations

import verify


def main() -> None:
    # An order-eight element needs all three small-analogue doubling levels.
    modulus = 17
    first, second, unused = 2, 8, 9
    total = (first + second) % modulus
    product = first * second % modulus
    assert verify.torsion_recurrence(
        total, product, unused, levels=3, modulus=modulus
    ) == (2, 1, 1)
    assert verify.torsion_recurrence(
        total, product, unused, levels=2, modulus=modulus
    ) != (2, 1, 1)
    assert verify.torsion_recurrence(
        total,
        product,
        unused,
        levels=3,
        modulus=modulus,
        product_coefficient=1,
    ) != (2, 1, 1)

    repeated, first_square, second_square = 7, 11, 13
    alpha, beta, gamma = 5, 9, 17
    invariant_i, invariant_j = verify.outer_invariants(alpha, beta, gamma)
    old_norm = verify.algebra.c1_components(
        repeated,
        first_square,
        second_square,
        invariant_i,
        invariant_j,
    )[2]
    scale = pow(repeated, -1, verify.PRIME)
    normalized_first = first_square * scale % verify.PRIME
    normalized_second = second_square * scale % verify.PRIME
    wrong_alpha, wrong_beta, wrong_gamma = verify.scale_outer(
        repeated, alpha, beta, gamma, h_value=verify.OFFICIAL_H + 1
    )
    wrong_i, wrong_j = verify.outer_invariants(
        wrong_alpha, wrong_beta, wrong_gamma
    )
    wrong_norm = verify.normalized_norm(
        (normalized_first + normalized_second) % verify.PRIME,
        normalized_first * normalized_second % verify.PRIME,
        wrong_i,
        wrong_j,
    )
    expected = old_norm * pow(
        repeated, -(24 * verify.OFFICIAL_H + 12), verify.PRIME
    ) % verify.PRIME
    assert wrong_norm != expected

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_NORMALIZED_TORSION_AUDIT_PASS "
        "mutations=3"
    )


if __name__ == "__main__":
    main()

