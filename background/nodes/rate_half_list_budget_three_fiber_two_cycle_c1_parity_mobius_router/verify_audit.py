#!/usr/bin/env python3
"""Mutation audit for the c=1 parity Mobius router."""

from __future__ import annotations

import verify


def main() -> None:
    r_value = 7
    for role in ("R", "P"):
        direct = verify.direct_cross_ratios(role, r_value)
        formula = verify.formula_cross_ratios(role, r_value)
        assert direct == formula

    value = verify.formula_cross_ratios("R", r_value)[0]
    ratio = 11
    correct_trace = verify.trace_from_cross_ratio(value)
    wrong_trace = (
        4
        * (value - 1) ** 2
        * verify.inverse((value + 1) ** 2)
        - 2
    ) % verify.PRIME
    assert correct_trace != wrong_trace
    assert verify.matching_polynomial(value, ratio) == (
        ratio
        * (value - 1) ** 2
        * (ratio + verify.inverse(ratio) - correct_trace)
    ) % verify.PRIME
    assert verify.matching_polynomial(value, ratio) != (
        ratio
        * (value - 1) ** 2
        * (ratio + verify.inverse(ratio) - wrong_trace)
    ) % verify.PRIME

    p_source = verify.role_points("P", r_value)
    r_sources = verify.role_points("R", r_value)
    assert set(p_source) != set(r_sources)

    ratio = pow(verify.IOTA, 1, verify.PRIME)
    trace = (ratio + verify.inverse(ratio)) % verify.PRIME
    assert verify.trace_iterate(trace, levels=2) == 2
    assert verify.trace_iterate(trace, levels=1) != 2

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_MOBIUS_AUDIT_PASS "
        "mutations=3"
    )


if __name__ == "__main__":
    main()

