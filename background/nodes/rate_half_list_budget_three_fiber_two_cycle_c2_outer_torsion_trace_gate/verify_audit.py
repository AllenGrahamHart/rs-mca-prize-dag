#!/usr/bin/env python3
"""Mutation audit for the c=2 outer torsion-trace gate."""

from __future__ import annotations

import verify


def main() -> None:
    generator = verify.primitive_root()
    t = pow(generator, (verify.PRIME - 1) // 8, verify.PRIME)
    cubic, _ = verify.positive_packet(t)

    correct = verify.terminal_polynomial(cubic)
    assert verify.gcd_degree(cubic, correct) >= 1

    wrong_recurrence = verify.terminal_polynomial(
        cubic, recurrence_constant=1
    )
    assert verify.gcd_degree(cubic, wrong_recurrence) == 0

    wrong_shift = verify.terminal_polynomial(cubic, trace_shift=1)
    assert verify.gcd_degree(cubic, wrong_shift) == 0

    wrong_terminal = verify.terminal_polynomial(cubic, terminal_value=3)
    assert verify.gcd_degree(cubic, wrong_terminal) == 0

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_OUTER_TORSION_TRACE_AUDIT_PASS "
        "mutations=3"
    )


if __name__ == "__main__":
    main()

