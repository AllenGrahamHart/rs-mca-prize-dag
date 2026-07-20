#!/usr/bin/env python3
"""Mutation audit for the c=1 parity R0 lift-free compiler."""

from __future__ import annotations

import verify


def main() -> None:
    u_value = 7
    t_value = u_value * u_value % verify.PRIME
    y_value = verify.trace_pair(t_value, u_value)[0]
    assert verify.k_value(t_value, y_value) == 0

    wrong_center = (
        t_value * y_value * y_value + 4 * (t_value - 1) ** 2
    ) % verify.PRIME
    wrong_lead = (
        (y_value - 2) ** 2 + 4 * (t_value - 1) ** 2
    ) % verify.PRIME
    assert wrong_center != 0
    assert wrong_lead != 0

    t_poly_value = 11
    s_squared = (y_value + 2) * t_poly_value % verify.PRIME
    correct = (
        t_value * (s_squared - 4 * t_poly_value) ** 2
        + 4 * (t_value - 1) ** 2 * t_poly_value * t_poly_value
    ) % verify.PRIME
    wrong_scalar = (
        t_value * (s_squared - 2 * t_poly_value) ** 2
        + 4 * (t_value - 1) ** 2 * t_poly_value * t_poly_value
    ) % verify.PRIME
    assert correct == 0
    assert wrong_scalar != 0

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_R0_LIFT_FREE_AUDIT_PASS "
        "mutations=3 selector_warning=1"
    )


if __name__ == "__main__":
    main()

