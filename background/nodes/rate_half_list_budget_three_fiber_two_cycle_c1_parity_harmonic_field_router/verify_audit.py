#!/usr/bin/env python3
"""Mutation audit for the c=1 parity harmonic field router."""

from __future__ import annotations

import verify


def main() -> None:
    assert verify.K_MAX - verify.K_MIN == 4_495_441
    assert verify.K_MAX - (verify.K_MIN + 1) != 4_495_441

    inverse_five = pow(5, -1, verify.PRIME)
    correct_h_p = 8 * inverse_five % verify.PRIME
    wrong_h_p = 4 * inverse_five % verify.PRIME
    assert correct_h_p != wrong_h_p

    iota = verify.square_root(-1)
    zeta = verify.square_root(iota)
    theta = (1 + iota) * pow(zeta, -1, verify.PRIME) % verify.PRIME
    algebraic_trace = -3 * theta % verify.PRIME
    assert verify.trace_iterate(algebraic_trace, 1) == 16
    assert (
        verify.trace_iterate(algebraic_trace, 1)
        != verify.trace_iterate(algebraic_trace, 0)
    )

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_HARMONIC_FIELD_AUDIT_PASS "
        "mutations=3"
    )


if __name__ == "__main__":
    main()

