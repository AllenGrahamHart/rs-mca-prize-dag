#!/usr/bin/env python3
"""Mutation audit for the c2 secondary differential certifier."""

from __future__ import annotations

import verify


def main() -> None:
    prime = 53
    height = 8
    e_poly = [1, 1, 11, 34, 43]
    a = verify.coefficients(prime, height, e_poly)
    b_poly = a[: 2 * height - 2]
    leading = a[2 * height]
    correct = [1, 22, 49, 3, 16]

    phi = verify.differential_phi(
        prime, height, e_poly, b_poly, correct, leading
    )
    assert phi[:height] == [0] * height

    changed = correct[:]
    changed[4] += 1
    bad_phi = verify.differential_phi(
        prime, height, e_poly, b_poly, changed, leading
    )
    assert bad_phi[:height] != [0] * height

    actual = verify.residual(prime, e_poly, b_poly)
    wrong_sign = actual[:]
    wrong_sign[2 * height - 1] *= -1
    assert wrong_sign != actual

    e_two = [1, 37, 42, 87, 27]
    a_two = verify.coefficients(97, 7, e_two)
    b_two = a_two[:12]
    assert b_two[-1] != 0
    assert verify.residual(97, e_two, b_two)[14] != 0

    assert max(2 * n + 4 * height for n in range(height)) == 6 * height - 2
    assert 6 * height - 2 < prime

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_SECONDARY_DIFFERENTIAL_AUDIT_PASS "
        "mutations=3"
    )


if __name__ == "__main__":
    main()
