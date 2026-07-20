#!/usr/bin/env python3
"""Mutation audit for the c=1 parity nonharmonic scalar compiler."""

from __future__ import annotations

import verify


def is_fourth(value: int, prime: int) -> bool:
    return any(pow(root, 4, prime) == value % prime for root in range(prime))


def trace_from_cross_ratio(value: int, prime: int) -> int:
    return (
        4 * (value + 1) ** 2 * pow((value - 1) ** 2, -1, prime) - 2
    ) % prime


def main() -> None:
    # The omitted +2 mutation fails on an exact scalar model.
    q_out = pow(5, 12, verify.PRIME)
    y_value = (q_out + pow(q_out, -1, verify.PRIME)) % verify.PRIME
    z_value = 7
    s_value = (1 + q_out) * z_value % verify.PRIME
    t_value = q_out * z_value * z_value % verify.PRIME
    assert s_value * s_value % verify.PRIME == (y_value + 2) * t_value % verify.PRIME
    assert s_value * s_value % verify.PRIME != y_value * t_value % verify.PRIME

    # In the nonsplit congruence shard, T/q is the invariant criterion and
    # the old unscaled T test has genuine false rejections.
    prime = 17
    l_order = 8
    ratios = [
        value for value in range(1, prime)
        if pow(value, l_order, prime) == 1
        and pow(value, l_order // 2, prime) != 1
    ]
    false_rejections = 0
    for ratio in ratios:
        for w_value in range(1, prime):
            t_value = ratio * pow(w_value, 4, prime) % prime
            assert is_fourth(t_value * pow(ratio, -1, prime), prime)
            assert is_fourth(t_value * ratio, prime)
            if not is_fourth(t_value, prime):
                false_rejections += 1
    assert false_rejections > 0

    # The terminal depth is exactly log2(L) in a toy exact-order case.
    ratio = ratios[0]
    trace = (ratio + pow(ratio, -1, prime)) % prime
    for _ in range(2):
        trace = (trace * trace - 2) % prime
    assert trace != 2
    trace = (trace * trace - 2) % prime
    assert trace == 2

    # R0's trace is invariant under r -> -r, so source descent must not be
    # inferred from the unordered trace equation.
    prime = 1009
    iota = next(value for value in range(prime) if value * value % prime == prime - 1)
    r_value = 7
    def r0_cross_ratio(value: int) -> int:
        return (
            (value - 1)
            * (value - iota)
            * pow((value + 1) * (value + iota) % prime, -1, prime)
        ) % prime

    assert trace_from_cross_ratio(r0_cross_ratio(r_value), prime) == trace_from_cross_ratio(
        r0_cross_ratio(-r_value % prime), prime
    )

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_NONHARMONIC_SCALAR_AUDIT_PASS "
        f"mutations=4 old_gate_false_rejections={false_rejections}"
    )


if __name__ == "__main__":
    main()

