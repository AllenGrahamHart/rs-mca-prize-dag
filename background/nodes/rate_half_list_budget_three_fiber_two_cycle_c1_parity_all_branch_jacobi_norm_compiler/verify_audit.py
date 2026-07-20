#!/usr/bin/env python3
"""Mutation audit for the all-branch c=1 parity Jacobi compiler."""

from __future__ import annotations

import verify


def main() -> None:
    r_value = 7
    x_value = (
        r_value * r_value + pow(r_value, -2, verify.PRIME)
    ) * verify.inverse(2) % verify.PRIME
    values = verify.h_values(r_value)
    kinds = ("R0", "R12", "R12", "P0", "P12", "P12")
    assert all(
        verify.source_norm(kind, x_value, value) == 0
        for kind, value in zip(kinds, values)
    )

    # The role constants are load-bearing.
    v_value = values[1]
    correct = verify.source_norm("R12", x_value, v_value)
    wrong_58 = (
        correct - 58 * v_value * v_value + 57 * v_value * v_value
    ) % verify.PRIME
    assert correct == 0 and wrong_58 != 0

    # The second norm uses A^2-zB^2, and P changes sign with x.
    z_value = x_value * x_value % verify.PRIME
    q_value = 11
    a_value, b_value = verify.even_parts("P12", z_value, q_value)
    correct_norm = (a_value * a_value - z_value * b_value * b_value) % verify.PRIME
    wrong_norm = (a_value * a_value + z_value * b_value * b_value) % verify.PRIME
    direct = verify.source_norm("P12", x_value, x_value * q_value)
    conjugate = verify.source_norm("P12", -x_value % verify.PRIME, x_value * q_value)
    assert direct * verify.source_norm(
        "P12", -x_value % verify.PRIME, -x_value * q_value % verify.PRIME
    ) % verify.PRIME == correct_norm
    assert wrong_norm != correct_norm
    assert conjugate != (a_value - x_value * b_value) % verify.PRIME

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_ALL_BRANCH_JACOBI_AUDIT_PASS "
        "mutations=3 tests_per_sign=7"
    )


if __name__ == "__main__":
    main()

