#!/usr/bin/env python3
"""Independent prime-field audit of the exceptional leading chart."""

from __future__ import annotations


PRIMES = (8191, 131071, 524287, 2147483647)
EXPECTED = (6740, 100974, 284891, 1825899718)


def decimal_chunk_mod(value: int, prime: int) -> int:
    digits = str(value)
    first = len(digits) % 3 or 3
    chunks = [int(digits[:first])]
    chunks.extend(int(digits[index : index + 3]) for index in range(first, len(digits), 3))
    residue = 0
    for chunk in chunks:
        residue = (1000 * residue + chunk) % prime
    return residue


def inv(value: int, prime: int) -> int:
    assert value % prime
    return pow(value, -1, prime)


def main() -> None:
    numerator = 115275930
    denominator = 45228187
    obstruction = 60466872820654125

    for prime, expected in zip(PRIMES, EXPECTED, strict=True):
        z = 1575 * inv(247, prime) % prime
        q = -10 * (z + 27) * inv(231, prime) % prime
        c_b = (-720 * q * q - 1902 * q - 40 * (z + 27)) % prime
        c_0 = (240 * z * q + 240 * z - 630 * q) % prime
        assert c_b

        forced_b = -c_0 * inv(c_b, prime) % prime
        assert denominator % prime
        assert forced_b == numerator * inv(denominator, prime) % prime
        assert (c_b * forced_b + c_0) % prime == 0
        assert (forced_b * forced_b - z) % prime

        assert decimal_chunk_mod(obstruction, prime) == expected
        assert (247 * numerator * numerator - 1575 * denominator * denominator) % prime == expected
        assert expected

    print(
        "AUDIT_L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_321_EXCEPTIONAL_E_LEADING_CHART_EXCLUSION_PASS "
        "prime_field_routes=4 independent_reduction=decimal_chunks"
    )


if __name__ == "__main__":
    main()
