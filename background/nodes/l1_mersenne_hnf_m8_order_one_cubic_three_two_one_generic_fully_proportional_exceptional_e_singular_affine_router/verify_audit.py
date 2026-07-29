#!/usr/bin/env python3
"""Independent sample audit for the exceptional singular-affine router."""

from __future__ import annotations


PRIMES = (8191, 131071, 524287, 2147483647)
SAMPLES = (1, 2, 5, 17, 101)


def main() -> None:
    checked = 0
    for prime in PRIMES:
        for b in SAMPLES:
            z = b * b % prime
            a = (1575 - 247 * z) % prime
            a2 = 63 * a % prime
            a1 = 9240 * z * (9 - z) % prime
            a0 = 400 * z * (9 - z) * (z + 27) % prime
            e2 = -720 * b % prime
            e1 = 240 * z - 1902 * b - 630
            e0 = -40 * b * (z - 6 * b + 27)
            s1 = (a2 * e1 - e2 * a1) % prime
            s0 = (a2 * e0 - e2 * a0) % prime

            c = -800 * z * z + 8929 * z - 11025
            n = 40 * z * z + 51 * z - 2835
            e_0 = (42 * a * b + (z + 27) * c) % prime
            e_1 = (
                15 * a * (8 * z - 21)
                + b * (-52800 * z * z + 710097 * z - 1497825)
            ) % prime
            r = (163 * b * (z + 27) - n) % prime

            assert s0 == 360 * b * e_0 % prime
            assert s1 == 126 * e_1 % prime
            assert ((z + 27) * e_1 - 66 * b * e_0) % prime == -3 * a * r % prime
            checked += 1

    assert tuple(24948 % prime for prime in PRIMES) == (375, 24948, 24948, 24948)
    print(
        "AUDIT_L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_321_EXCEPTIONAL_E_SINGULAR_AFFINE_ROUTER_PASS "
        f"prime_field_samples={checked}"
    )


if __name__ == "__main__":
    main()
