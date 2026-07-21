#!/usr/bin/env python3
"""Mutation audit for the c2 product/ratio trace compiler."""

from __future__ import annotations

import verify


def main() -> None:
    prime = 97
    omega = verify.subgroup_generator(prime, 16)

    # Independent product and ratio torsion can have incompatible half signs.
    product = 1
    ratio = omega
    trace = (ratio + pow(ratio, -1, prime)) % prime
    product_half, trace_half = verify.tower(product, trace, 4, prime)
    assert product_half * product_half % prime == 1
    assert (trace_half * trace_half - 4) % prime == 0
    assert trace_half != 2 * product_half % prime

    # The X identity needs Z+2, not Z-2.
    c, d = omega, pow(omega, 3, prime)
    product = c * d % prime
    ratio = c * pow(d, -1, prime) % prime
    trace = (ratio + pow(ratio, -1, prime)) % prime
    square_total = (c + d) ** 2 % prime
    assert square_total != product * (trace - 2) % prime

    # Stopping one level early does not certify the required half-order sign.
    assert verify.tower(product, trace, 3, prime) != verify.tower(
        product, trace, 4, prime
    )

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_ONE_ANTIPODAL_PRODUCT_TRACE_AUDIT_PASS "
        "mutations=3"
    )


if __name__ == "__main__":
    main()
