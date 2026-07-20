#!/usr/bin/env python3
"""Mutation audit for the mismatch trace-resolvent verifier."""

from __future__ import annotations

import verify


def main() -> None:
    roots = (1, 4, 9, 16)
    direct = verify.resolvent_direct(roots)
    mutated = verify.resolvent_formula(roots)
    mutated[3] = (mutated[3] + 1) % verify.PRIME
    assert direct != mutated

    source = verify.centered((1, -1 % verify.PRIME, 2, 3))
    invariant_i, invariant_j = verify.invariants_from_roots(source)
    k0, k1, norm = verify.c1_components(
        1, 4, 9, invariant_i, invariant_j
    )
    assert norm == 0
    wrong_norm = (k0 * k0 + 4 * 9 * k1 * k1) % verify.PRIME
    assert wrong_norm != 0

    c2_source = (
        1,
        -1 % verify.PRIME,
        2,
        -2 % verify.PRIME,
    )
    c2_i, c2_j = verify.invariants_from_roots(c2_source)
    z = (1 + 4) ** 2 * pow(4, -1, verify.PRIME) % verify.PRIME
    correct = verify.eval_poly(verify.outer_cubic(c2_i, c2_j), z)
    assert correct == 0
    wrong = (
        4 * c2_i**3 * z * (z - 35) ** 2
        - c2_j**2 * (z + 12) ** 3
    ) % verify.PRIME
    assert wrong != 0

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_MISMATCH_TRACE_RESOLVENT_AUDIT_PASS "
        "mutations=3"
    )


if __name__ == "__main__":
    main()

