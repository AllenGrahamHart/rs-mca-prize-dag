#!/usr/bin/env python3
"""Mutation audit for the c=2 pure fourth-root exclusion."""

from __future__ import annotations

import verify


def main() -> None:
    odd_height = 9
    odd_index = 2 * odd_height - 2
    assert odd_index % 4 == 0
    assert verify.pure_coefficient(odd_index) != 0

    even_height = 8
    even_first = 2 * even_height - 2
    even_second = 2 * even_height - 1
    even_leading = 2 * even_height
    assert verify.pure_coefficient(even_first) == 0
    assert verify.pure_coefficient(even_second) == 0
    assert verify.pure_coefficient(even_leading) != 0

    prime = 257
    correct = verify.coefficient_mod_prime(odd_index, prime)
    assert correct != 0
    assert verify.coefficient_mod_prime(odd_index + 1, prime) == 0

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_PURE_FOURTH_ROOT_EXCLUSION_AUDIT_PASS "
        "mutations=3"
    )


if __name__ == "__main__":
    main()
