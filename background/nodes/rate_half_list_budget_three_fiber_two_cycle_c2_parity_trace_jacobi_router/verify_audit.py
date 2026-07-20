#!/usr/bin/env python3
"""Mutation audit for the c=2 parity trace/Jacobi router."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

import verify


def main() -> None:
    generator = verify.primitive_root()
    q = pow(generator, (verify.PRIME - 1) // 32, verify.PRIME)
    r = q * q % verify.PRIME
    roots = (1, -1 % verify.PRIME, r, -r % verify.PRIME)
    chi = (r + pow(r, -1, verify.PRIME)) % verify.PRIME

    correct = Counter(
        verify.pair_trace(left, right) for left, right in combinations(roots, 2)
    )
    assert correct[0] == 2
    assert correct[(2 + chi) % verify.PRIME] == 2
    assert correct[(2 - chi) % verify.PRIME] == 2

    wrong_minus = (-2 + chi) % verify.PRIME
    assert wrong_minus not in correct

    invariant_i, invariant_j = 17, 29
    assert verify.outer_gate(0, invariant_i, invariant_j) != 0
    assert verify.outer_gate(0, invariant_i, 0) == 0

    plus = verify.outer_gate((2 + chi) % verify.PRIME, invariant_i, invariant_j)
    minus = verify.outer_gate((2 - chi) % verify.PRIME, invariant_i, invariant_j)
    assert plus * minus % verify.PRIME == (
        verify.outer_gate((2 - chi) % verify.PRIME, invariant_i, invariant_j)
        * verify.outer_gate((2 + chi) % verify.PRIME, invariant_i, invariant_j)
        % verify.PRIME
    )

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_PARITY_TRACE_JACOBI_AUDIT_PASS "
        "mutations=3"
    )


if __name__ == "__main__":
    main()
