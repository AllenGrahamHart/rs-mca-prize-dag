#!/usr/bin/env python3
"""Independent official-prime sample audit of the J-zero affine router."""

from __future__ import annotations


PRIMES = (8191, 131071, 524287, 2147483647)
SAMPLES = ((1, 2), (2, 5), (5, 17), (17, 101), (101, 257))


def main() -> None:
    checked = 0
    for prime in PRIMES:
        for b, q in SAMPLES:
            b %= prime
            q %= prime
            p = 40 * b * (b * b - 6 * b + 27) + 42 * q * (11 * b + 15)
            d_star = (
                3 * q * (40 * b * b - 253 * b + 1155)
                - 20 * b * (11 * b * b + 81 * b + 414)
            )
            q_star = (
                720 * b * (360 + 1098 * q + 191 * q * q - 10 * q**3)
                + (12 * q - 44 * b - 294) * q * p
            )
            k_star = 240 * b * q * (b - 6) - p
            e_g = k_star - 720 * b * q * q
            l_star = 135 * b * (b * b + 6 * b + 105 + 8 * q) - 6 * p
            x_star = q_star - 24 * d_star * q * q
            j_star = 150 * b * q_star - 3 * d_star * d_star - 5 * p * d_star
            b_poly = 96 * q * q + (216 - 32 * b) * q + 3 * b * b + 18 * b + 315
            t = -280 * b * b + 2241 * b + 3465
            m = 29 * b * b + 234 * b + 81
            r_j = 3 * d_star + 5 * p - 3600 * b * q * q

            assert (l_star - 45 * b * b_poly - 6 * e_g) % prime == 0
            assert (r_j + 5 * e_g + 75 * b * b_poly - 3 * (t * q - 5 * b * m)) % prime == 0
            assert (j_star + d_star * r_j - 150 * b * x_star) % prime == 0
            checked += 1

    obstruction = -23972710684
    assert tuple(obstruction % prime for prime in PRIMES) == (
        3690,
        44145,
        312391,
        1797093080,
    )
    print(
        "AUDIT_L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_321_EXCEPTIONAL_E_J0_AFFINE_ROUTER_PASS "
        f"prime_field_samples={checked}"
    )


if __name__ == "__main__":
    main()
