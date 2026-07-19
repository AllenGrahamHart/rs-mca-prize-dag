#!/usr/bin/env python3
"""Exact arithmetic and toy replay for the cyclic simple-pole MCA floor."""

from __future__ import annotations

from itertools import product
from math import comb


def evaluate(poly: tuple[int, ...], x: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % prime
    return value


def toy_simple_pole_replay() -> tuple[int, int, int]:
    prime = 17
    domain = tuple(range(9))
    n, k = len(domain), 2
    polynomials = ((0, 0, 0), (1, 0, 0), (0, 1, 0))
    supports = (domain[0:3], domain[3:6], domain[6:9])

    received = [0] * n
    for poly, support in zip(polynomials, supports, strict=True):
        for x in support:
            received[x] = evaluate(poly, x, prime)

    for poly in polynomials:
        agreements = sum(
            received[x] == evaluate(poly, x, prime) for x in domain
        )
        assert agreements >= k + 1

    codewords = tuple(product(range(prime), repeat=k))
    lower_numerator = len(polynomials) * (prime - n)
    lower_denominator = prime - n + k * len(polynomials)
    promised = (lower_numerator + lower_denominator - 1) // lower_denominator
    best_distinct = 0

    for alpha in range(prime):
        if alpha in domain:
            continue
        slopes = {evaluate(poly, alpha, prime) for poly in polynomials}
        best_distinct = max(best_distinct, len(slopes))
        assert len(slopes) >= promised

        inverse = [pow((x - alpha) % prime, -1, prime) for x in domain]
        f_values = [received[x] * inverse[x] % prime for x in domain]
        g_values = [(-inverse[x]) % prime for x in domain]

        max_g_agreement = max(
            sum(
                g_values[x] == evaluate(codeword, x, prime) for x in domain
            )
            for codeword in codewords
        )
        assert max_g_agreement <= k

        for slope in slopes:
            line_word = [
                (f_values[x] + slope * g_values[x]) % prime for x in domain
            ]
            max_agreement = max(
                sum(
                    line_word[x] == evaluate(codeword, x, prime)
                    for x in domain
                )
                for codeword in codewords
            )
            assert max_agreement >= k + 1

    return len(polynomials), promised, best_distinct


def cap_arithmetic() -> tuple[int, int, int]:
    n, k = 1 << 41, 1 << 40
    old_sigma = 8_592_912_738
    c = 1 << 22
    d, s = 2048, c - 1
    sigma = d * c + s
    quotient_size = n // c
    m = k // c + d
    cap = 1 << 256
    count = comb(quotient_size - 1, m)

    assert (sigma, quotient_size, m) == (8_594_128_895, 524_288, 264_192)
    assert 0 < s < c
    assert old_sigma + 1 <= sigma
    assert k + sigma < n
    assert quotient_size * cap**d < (1 << 53) * count
    assert not quotient_size * cap**d < (1 << 52) * count
    assert k * (n + 1) < 1 << 82
    assert not k * (n + 1) < 1 << 81
    assert (1 << 53) + (1 << 82) < 1 << 83

    denominator = quotient_size * cap ** (d - 1)
    cap_list = (count + denominator - 1) // denominator
    assert (1 << 128) * cap_list * (cap - n) > cap * (
        cap - n + k * cap_list
    )

    for q in (n + 1, 2 * n + 1, cap):
        list_denominator = quotient_size * q ** (d - 1)
        list_size = (count + list_denominator - 1) // list_denominator
        assert (1 << 83) * list_size * (q - n) > q * (
            q - n + k * list_size
        )

    return count.bit_length(), cap_list.bit_length(), 83


def main() -> None:
    toy = toy_simple_pole_replay()
    count_bits, list_bits, reciprocal_bits = cap_arithmetic()
    print(
        "RATE_HALF_CYCLIC_SIMPLE_POLE_MCA_FLOOR_PASS "
        f"toy={toy} cap_count_bits={count_bits} cap_list_bits={list_bits} "
        f"reciprocal_lt_2^{reciprocal_bits}"
    )


if __name__ == "__main__":
    main()
