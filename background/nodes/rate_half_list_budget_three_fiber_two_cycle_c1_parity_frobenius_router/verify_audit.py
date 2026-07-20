#!/usr/bin/env python3
"""Mutation audit for the c=1 parity Frobenius router."""

from __future__ import annotations

import verify


def trace_terminal(value: int, levels: int, modulus: int) -> int:
    for _ in range(levels):
        value = (value * value - 2) % modulus
    return value


def main() -> None:
    r_value = 7
    r_traces = [
        verify.tau(value)
        for role in ("R", "P")
        for value in verify.cross_ratios(role, r_value)
    ]
    negative_traces = [
        verify.tau(value)
        for role in ("R", "P")
        for value in verify.cross_ratios(role, -r_value % verify.PRIME)
    ]
    assert r_traces[0] == negative_traces[0]
    assert any(
        r_traces[index] != negative_traces[index]
        for index in range(1, 6)
    )

    # The exceptional traces are not interchangeable.
    modulus = 97
    assert trace_terminal(-8 % modulus, 3, modulus) != trace_terminal(
        6 * pow(5, -1, modulus) % modulus, 3, modulus
    )

    # An exact order-eight control needs three, not two, updates.
    q_value = pow(5, 12, modulus)
    trace = (q_value + pow(q_value, -1, modulus)) % modulus
    assert trace_terminal(trace, 3, modulus) == 2
    assert trace_terminal(trace, 2, modulus) != 2

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_FROBENIUS_AUDIT_PASS "
        "mutations=3 residual_preserved=R0"
    )


if __name__ == "__main__":
    main()

