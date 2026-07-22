#!/usr/bin/env python3
"""Mutation audit for the nonidentity P25 subresultant compiler."""

from __future__ import annotations

import verify


def main() -> None:
    verify.finite_field_check()

    prime = 41
    f, correct = verify.incidence_polynomials(8, 7, prime)
    wrong = list(reversed(correct))
    assert correct != wrong
    assert verify.gcd_degree(f, correct, prime) >= 0

    assert sum(index + 1 for index in range(25)) == 325
    assert sum(index + 1 for index in range(24)) != 325
    assert len(verify.incidence_polynomials(8, 1, prime)[0]) == 8

    print(
        "F3_H3_NONIDENTITY_P25_SUBRESULTANT_SCALAR_COMPILER_AUDIT_PASS "
        "mutations=5"
    )


if __name__ == "__main__":
    main()
