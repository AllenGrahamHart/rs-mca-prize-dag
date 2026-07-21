#!/usr/bin/env python3
"""Mutation audit for the c2 one-antipodal reducer."""

from __future__ import annotations

import verify


def main() -> None:
    prime = 97
    omega = verify.subgroup_generator(prime, 16)
    c, d = omega, pow(omega, 3, prime)
    total = (c + d) % prime
    product = c * d % prime
    square_total = total * total % prime

    assert verify.sign_free_torsion(square_total, product, 4, prime) == (2, 1)
    assert verify.sign_free_torsion(square_total, product, 3, prime) != (2, 1)
    assert verify.sign_free_torsion(
        square_total, product, 4, prime, initial_shift=1
    ) != (2, 1)

    # Product torsion without the trace equation is insufficient.
    assert verify.sign_free_torsion(1, 1, 4, prime)[1] == 1
    assert verify.sign_free_torsion(1, 1, 4, prime)[0] != 2

    # One antipodal pair alone does not make the complementary pair antipodal.
    assert square_total != 0

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_ONE_ANTIPODAL_REDUCER_AUDIT_PASS "
        "mutations=4"
    )


if __name__ == "__main__":
    main()
