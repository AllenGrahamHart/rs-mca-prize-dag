#!/usr/bin/env python3
"""Mutation audit for the c=1 parity R0 Jacobi-norm transfer."""

from __future__ import annotations

import verify


def main() -> None:
    r_value = pow(5, (verify.PRIME - 1) // 32, verify.PRIME)
    u_value = r_value * r_value % verify.PRIME
    t_value = u_value * u_value % verify.PRIME
    x_value = (u_value + pow(u_value, -1, verify.PRIME)) * pow(2, -1, verify.PRIME) % verify.PRIME
    epsilon = pow(r_value, 16, verify.PRIME)
    p_value = verify.legendre_p3(x_value)
    h_value = verify.h3(t_value)

    original = (
        4 * t_value * (1 + t_value * h_value * h_value) ** 2
        + (t_value - 1) ** 2
    ) % verify.PRIME
    correct = (
        (1 + epsilon * p_value * p_value) ** 2 + x_value * x_value - 1
    ) % verify.PRIME
    wrong_sign = (
        (1 - epsilon * p_value * p_value) ** 2 + x_value * x_value - 1
    ) % verify.PRIME
    wrong_tail = (
        (1 + epsilon * p_value * p_value) ** 2 - x_value * x_value + 1
    ) % verify.PRIME
    assert original == 4 * t_value * correct % verify.PRIME
    assert wrong_sign != correct
    assert wrong_tail != correct

    # First- and second-kind torsion factors must not be exchanged.
    assert verify.chebyshev_t(4, x_value) == 0
    assert verify.chebyshev_u(3, x_value) != 0

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_R0_JACOBI_AUDIT_PASS "
        "mutations=3 norm_reuse_scope=1"
    )


if __name__ == "__main__":
    main()
