#!/usr/bin/env python3
"""Mutation audit for the c=2 joint pair-torsion selector."""

from __future__ import annotations

import verify


def main() -> None:
    levels = 3
    generator = verify.primitive_root()
    t = pow(generator, (verify.PRIME - 1) // 8, verify.PRIME)
    roots = verify.completion_roots(t)
    cubic = verify.source_cubic(t)

    correct = verify.joint_selector(roots, cubic, levels)
    assert len(correct) > 1

    wrong_recurrence = verify.joint_selector(
        roots, cubic, levels, recurrence_constant=1
    )
    assert wrong_recurrence == [1]

    wrong_shift = verify.joint_selector(
        roots, cubic, levels, trace_shift=1
    )
    assert wrong_shift == [1]

    wrong_terminal = verify.joint_selector(
        roots, cubic, levels, terminal_value=3
    )
    assert wrong_terminal == [1]

    false_positive_roots = verify.find_outer_only_false_positive(cubic, levels)
    terminal = verify.terminal_polynomial(cubic, levels)
    assert len(verify.algebra.poly_gcd(cubic, terminal)) > 1
    assert verify.joint_selector(false_positive_roots, cubic, levels) == [1]

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_JOINT_PAIR_TORSION_AUDIT_PASS "
        "mutations=4"
    )


if __name__ == "__main__":
    main()
