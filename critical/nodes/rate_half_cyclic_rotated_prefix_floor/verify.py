#!/usr/bin/env python3
"""Exact toy and cap-row replay for the cyclically rotated prefix floor."""

from __future__ import annotations

from itertools import combinations
from math import comb, log2


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    return trim(out)


def evaluate(poly: list[int], value: int, prime: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * value + coefficient) % prime
    return out


def product_linear(roots: tuple[int, ...], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % prime, 1], prime)
    return out


def find_power_two_root(prime: int, order: int) -> int:
    assert order > 1 and order & (order - 1) == 0
    assert (prime - 1) % order == 0
    cofactor = (prime - 1) // order
    for seed in range(2, prime):
        root = pow(seed, cofactor, prime)
        if pow(root, order, prime) == 1 and pow(root, order // 2, prime) != 1:
            return root
    raise AssertionError("no root of requested order")


def cyclic_rotation(
    quotient_locator: list[int], quotient_size: int, d: int, delta: int, prime: int
) -> list[int]:
    out = [0] * quotient_size
    for j, coefficient in enumerate(quotient_locator):
        exponent = quotient_size - d + j
        if exponent >= quotient_size:
            exponent -= quotient_size
            coefficient = coefficient * delta
        assert 0 <= exponent < quotient_size
        out[exponent] = (out[exponent] + coefficient) % prime
    return trim(out)


def substitute_power(poly: list[int], c: int) -> list[int]:
    out = [0] * ((len(poly) - 1) * c + 1)
    for i, coefficient in enumerate(poly):
        out[i * c] = coefficient
    return trim(out)


def padded(poly: list[int], length: int) -> tuple[int, ...]:
    return tuple(poly) + (0,) * (length - len(poly))


def toy_replay(prime: int, n: int, c: int, d: int, s: int) -> tuple[int, int, int]:
    k = n // 2
    quotient_size = n // c
    m = quotient_size // 2 + d
    assert 0 < s < c and 1 <= d <= quotient_size // 2 - 1

    root = find_power_two_root(prime, n)
    domain = tuple(pow(root, i, prime) for i in range(n))
    quotient = tuple(dict.fromkeys(pow(x, c, prime) for x in domain))
    assert len(quotient) == quotient_size
    delta_values = {pow(y, quotient_size, prime) for y in quotient}
    assert len(delta_values) == 1
    delta = next(iter(delta_values))

    distinguished = quotient[0]
    fiber = tuple(x for x in domain if pow(x, c, prime) == distinguished)
    tail = fiber[:s]
    tail_locator = product_linear(tail, prime)

    buckets: dict[
        tuple[int, ...], list[tuple[tuple[int, ...], list[int], list[int]]]
    ] = {}
    constant_terms: set[int] = set()
    omitted_constant_high: dict[tuple[int, ...], tuple[int, ...]] = {}
    constant_is_necessary = False

    for chosen in combinations(quotient[1:], m):
        quotient_locator = product_linear(chosen, prime)
        assert len(quotient_locator) == m + 1 and quotient_locator[-1] == 1
        constant_terms.add(quotient_locator[0])
        rotated = cyclic_rotation(quotient_locator, quotient_size, d, delta, prime)
        locator = mul(tail_locator, substitute_power(rotated, c), prime)
        locator_pad = padded(locator, n)

        for x in domain:
            y = pow(x, c, prime)
            left = evaluate(rotated, y, prime)
            right = pow(y, quotient_size - d, prime) * evaluate(
                quotient_locator, y, prime
            )
            assert left == right % prime

        key = tuple(quotient_locator[:d])
        buckets.setdefault(key, []).append((chosen, quotient_locator, locator))

        reduced_key = tuple(quotient_locator[1:d])
        high = locator_pad[k:]
        previous = omitted_constant_high.get(reduced_key)
        if previous is not None and previous != high:
            constant_is_necessary = True
        omitted_constant_high.setdefault(reduced_key, high)

    total = comb(quotient_size - 1, m)
    assert sum(map(len, buckets.values())) == total
    assert len(constant_terms) <= quotient_size
    assert len(buckets) <= quotient_size * prime ** (d - 1)
    assert constant_is_necessary

    bucket = max(buckets.values(), key=len)
    denominator = quotient_size * prime ** (d - 1)
    lower = (total + denominator - 1) // denominator
    assert len(bucket) >= lower

    common_high = padded(bucket[0][2], n)[k:]
    words: set[tuple[int, ...]] = set()
    for chosen, quotient_locator, locator in bucket:
        locator_pad = padded(locator, n)
        assert locator_pad[k:] == common_high
        codeword = tuple((-locator_pad[i]) % prime for i in range(k))
        words.add(codeword)

        expected_roots = set(tail)
        expected_roots.update(x for x in domain if pow(x, c, prime) in chosen)
        assert len(expected_roots) == k + d * c + s
        actual_roots = {x for x in domain if evaluate(locator, x, prime) == 0}
        assert actual_roots == expected_roots

        received = (0,) * k + common_high
        agreements = 0
        for x in domain:
            received_value = evaluate(list(received), x, prime)
            codeword_value = evaluate(list(codeword), x, prime)
            agreements += received_value == codeword_value
        assert agreements == len(expected_roots)

        assert tuple(quotient_locator[:d]) == tuple(bucket[0][1][:d])

    assert len(words) == len(bucket)
    return total, lower, len(bucket)


def log2_bigint(value: int) -> float:
    bits = value.bit_length()
    if bits <= 200:
        return log2(value)
    return bits - 200 + log2(value >> (bits - 200))


def cap_arithmetic() -> tuple[int, int, float, float, float]:
    n, k = 1 << 41, 1 << 40
    old_sigma = 8_592_912_738
    c = 1 << 22
    d, s = 2048, c - 1
    sigma = d * c + s
    quotient_size = n // c
    m = k // c + d
    assert (sigma, quotient_size, m) == (8_594_128_895, 524_288, 264_192)
    assert old_sigma + 1 <= sigma

    count = comb(quotient_size - 1, m)
    left = count << 128
    cap_right = quotient_size << (256 * d)
    assert left > cap_right

    cap_denominator = quotient_size << (256 * (d - 1))
    cap_list = (count + cap_denominator - 1) // cap_denominator
    assert cap_list > 1 << 128

    count_log = log2_bigint(count)
    boundary = (128 + count_log - log2(quotient_size)) / d
    margin = 128 + count_log - log2(quotient_size) - 256 * d
    list_log = log2_bigint(cap_list)
    assert boundary > 256
    assert margin > 0
    assert list_log > 128
    return count.bit_length(), cap_list.bit_length(), boundary, margin, list_log


def main() -> None:
    toy_one = toy_replay(prime=193, n=64, c=4, d=1, s=2)
    toy_two = toy_replay(prime=97, n=32, c=2, d=2, s=1)
    count_bits, list_bits, boundary, margin, list_log = cap_arithmetic()
    print(
        "RATE_HALF_CYCLIC_ROTATED_PREFIX_FLOOR_PASS "
        f"toy_d1={toy_one} toy_d2={toy_two} "
        f"cap_count_bits={count_bits} cap_list_bits={list_bits} "
        f"q_boundary_bits={boundary:.12f} "
        f"cap_margin_bits={margin:.9f} cap_list_log2={list_log:.9f}"
    )


if __name__ == "__main__":
    main()
