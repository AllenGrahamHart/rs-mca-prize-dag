#!/usr/bin/env python3
"""Mutation audit for the c=2 normalized pair-torsion compiler."""

from __future__ import annotations

import verify


def main() -> None:
    generator = verify.primitive_root()
    subgroup = [
        pow(generator, (verify.PRIME - 1) // 8 * index, verify.PRIME)
        for index in range(8)
    ]
    a, b, c, d = subgroup[0], subgroup[1], subgroup[2], subgroup[4]
    t, total, product = verify.normalized_coordinates(a, b, c, d)

    assert verify.torsion_recurrence(t, total, product, 3) == (1, 2, 1)
    assert verify.torsion_recurrence(
        t, total, product, 3, recurrence_constant=1
    ) != (1, 2, 1)

    correct_reverse = verify.orientation_reverse(t, total, product)
    wrong_reverse = (
        pow(t, -1, verify.PRIME),
        total * pow(t, -1, verify.PRIME) % verify.PRIME,
        product * pow(t, -1, verify.PRIME) % verify.PRIME,
    )
    assert correct_reverse == verify.normalized_coordinates(b, a, c, d)
    assert wrong_reverse != correct_reverse

    colliding_total = (1 + c * pow(a, -1, verify.PRIME)) % verify.PRIME
    colliding_product = c * pow(a, -1, verify.PRIME) % verify.PRIME
    assert verify.distinctness_product(t, colliding_total, colliding_product) == 0

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_NORMALIZED_PAIR_TORSION_AUDIT_PASS "
        "mutations=3"
    )


if __name__ == "__main__":
    main()
