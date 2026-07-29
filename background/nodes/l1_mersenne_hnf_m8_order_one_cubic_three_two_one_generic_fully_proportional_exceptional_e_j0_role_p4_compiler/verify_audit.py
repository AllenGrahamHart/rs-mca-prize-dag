#!/usr/bin/env python3
"""Independent rational audit of the J-zero role/P4 compiler."""

from __future__ import annotations

from fractions import Fraction as Q


SAMPLES = (
    (Q(2), Q(7), Q(11), Q(1), Q(2), Q(3)),
    (Q(-1), Q(-4), Q(5), Q(2), Q(-1), Q(5)),
)


def main() -> None:
    for role_r, q, r0, c2, c1, c0 in SAMPLES:
        ad = Q(13, 2)
        delta = c1**2 - 4 * c2 * c0
        role_s = -c1 * role_r / (2 * c0) - q * ad / 18
        u1 = 9 * q * (c1 * role_r + 2 * c0 * role_s) + c0 * q**2 * ad
        u0 = 27 * (
            c2 * role_r**2 + c1 * role_r * role_s + c0 * role_s**2
        ) + 12 * c0 * q * r0
        linear = 18 * c0 * role_s + 9 * c1 * role_r + c0 * q * ad
        weld = c0**2 * (q**2 * ad**2 + 144 * q * r0) - 81 * delta * role_r**2
        assert u1 == q * linear
        assert u1 == 0
        assert 12 * c0 * u0 == weld

        d = Q(17, 3)
        p4 = -3 * q * d**2 + q * ad * d + 12 * r0
        s_d = role_s + q * d / 3
        phi = c2 * role_r**2 + c1 * role_r * s_d + c0 * s_d**2
        remainder = u1 * d + u0
        assert 27 * phi + c0 * q * p4 == remainder

    print(
        "AUDIT_L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_321_EXCEPTIONAL_E_J0_ROLE_P4_COMPILER_PASS "
        f"rational_samples={len(SAMPLES)}"
    )


if __name__ == "__main__":
    main()
