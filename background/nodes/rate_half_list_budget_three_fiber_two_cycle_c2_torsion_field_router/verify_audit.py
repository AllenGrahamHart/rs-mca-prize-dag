#!/usr/bin/env python3
"""Mutation audit for the c2 torsion-field router."""

from __future__ import annotations

import verify


def main() -> None:
    generator = verify.primitive_element()
    field_order = verify.PRIME * verify.PRIME - 1
    omega = verify.power(generator, field_order // 16)
    roots = (verify.ONE, omega, verify.power(omega, 3), verify.power(omega, 6))

    # The unitary packet is not pointwise prime-field fixed.
    assert verify.power(omega, verify.PRIME) != omega
    assert verify.power(omega, verify.PRIME) == verify.inverse(omega)

    e_poly = verify.denominator(roots)
    unscaled_reverse = list(reversed(e_poly))
    frobenius = [verify.power(coefficient, verify.PRIME) for coefficient in e_poly]
    assert frobenius != unscaled_reverse

    t, c, d = roots[1:]
    total = verify.add(c, d)
    product = verify.multiply(c, d)
    assert verify.torsion_recurrence(t, total, product, 4) == (
        verify.ONE,
        verify.TWO,
        verify.ONE,
    )
    assert verify.torsion_recurrence(
        t, total, product, 4, recurrence_constant=1
    ) != (verify.ONE, verify.TWO, verify.ONE)

    # N | q-1 alone does not put mu_N inside the squares.
    prime = 17
    primitive = 3
    assert pow(primitive, 16, prime) == 1
    assert pow(primitive, 8, prime) == prime - 1

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_TORSION_FIELD_ROUTER_AUDIT_PASS "
        "mutations=4"
    )


if __name__ == "__main__":
    main()
