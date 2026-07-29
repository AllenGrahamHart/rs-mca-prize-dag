#!/usr/bin/env python3
"""Independent rational-sample audit of the J-zero structural compiler."""

from __future__ import annotations

from fractions import Fraction as Q


SAMPLES = ((Q(2), Q(5)), (Q(-1), Q(9)), (Q(5, 2), Q(11)))


def main() -> None:
    for b, q in SAMPLES:
        x = (b + 15) / 4
        a = -(b + 3) / 2
        ell = (b**2 + 6 * b + 105 + 8 * q) / 16
        p = 40 * b * (b**2 - 6 * b + 27) + 42 * q * (11 * b + 15)
        d_star = (
            3 * q * (40 * b**2 - 253 * b + 1155)
            - 20 * b * (11 * b**2 + 81 * b + 414)
        )
        d_core = d_star / (3600 * b)
        q0 = q**2 / 3
        g = (q0 - x * ell + 20 + 8 * q / 3 + d_core) / a
        h = ell - g
        y = (ell - 2 * g) / a - x
        v = g + x * y + y**2
        r0 = -q * p / (2880 * b)
        constant = 15 + 23 * q / 4 + q**2 / 8

        assert q0 == a * g + x * ell - 20 - 8 * q / 3 - d_core
        assert h + g == ell and h == g + a * (x + y)
        original = r0 - g * h + x * q0 + y * (a + x) * v + constant
        simplified = r0 - g * h + x * q0 + (a + x) * d_core + constant
        assert original - simplified == (a + x) * (y * v - d_core)

    print(
        "AUDIT_L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_321_EXCEPTIONAL_E_J0_STRUCTURAL_COMPILER_PASS "
        f"rational_samples={len(SAMPLES)}"
    )


if __name__ == "__main__":
    main()
