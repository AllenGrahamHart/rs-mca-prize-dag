#!/usr/bin/env python3
"""Exact arithmetic and toy construction replay for the fixed-tail floor."""

from __future__ import annotations

from itertools import combinations
from math import ceil, comb, log2


def mul(left: list[int], right: list[int], prime: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % prime
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def product_linear(roots: tuple[int, ...], prime: int) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % prime, 1], prime)
    return out


def find_root(prime: int, order: int) -> int:
    cofactor = (prime - 1) // order
    for seed in range(2, prime):
        root = pow(seed, cofactor, prime)
        if pow(root, order // 2, prime) != 1:
            return root
    raise AssertionError("no root")


def toy_replay() -> tuple[int, int, int]:
    prime, n, k, c, d, s = 193, 64, 32, 4, 1, 2
    quotient_size = n // c
    m = k // c + d
    root = find_root(prime, n)
    domain = tuple(pow(root, i, prime) for i in range(n))
    quotient = tuple(dict.fromkeys(pow(x, c, prime) for x in domain))
    assert len(quotient) == quotient_size

    distinguished = quotient[0]
    fiber = tuple(x for x in domain if pow(x, c, prime) == distinguished)
    tail = fiber[:s]
    tail_locator = product_linear(tail, prime)

    buckets: dict[int, list[tuple[tuple[int, ...], list[int]]]] = {}
    for chosen in combinations(quotient[1:], m):
        quotient_locator = [1]
        for value in chosen:
            factor = [(-value) % prime] + [0] * (c - 1) + [1]
            quotient_locator = mul(quotient_locator, factor, prime)
        alpha_1 = quotient_locator[-c - 1]
        locator = mul(tail_locator, quotient_locator, prime)
        buckets.setdefault(alpha_1, []).append((chosen, locator))

    total = comb(quotient_size - 1, m)
    bucket = max(buckets.values(), key=len)
    lower = ceil(total / prime**d)
    assert len(bucket) >= lower

    degree = k + d * c + s
    high = [0] * (degree + 1)
    for index in range(k, degree + 1):
        high[index] = bucket[0][1][index]
    words = set()
    for chosen, locator in bucket:
        assert all(locator[index] == high[index] for index in range(k, degree + 1))
        remainder = [(locator[i] - high[i]) % prime for i in range(k)]
        assert all(locator[i] == remainder[i] for i in range(k))
        codeword = tuple((-value) % prime for value in remainder)
        words.add(codeword)
        roots = set(tail)
        roots.update(x for x in domain if pow(x, c, prime) in chosen)
        assert len(roots) == degree
        for x in domain:
            value = 0
            for coefficient in reversed(locator):
                value = (value * x + coefficient) % prime
            assert (value == 0) == (x in roots)
    assert len(words) == len(bucket)

    # Removing the alpha_1 prefix condition is not sound: some locator then
    # differs from this high part in degree at least k.
    all_locators = [item for values in buckets.values() for item in values]
    assert any(
        any(locator[index] != high[index] for index in range(k, degree + 1))
        for _, locator in all_locators
    )
    return total, lower, len(bucket)


def log2_bigint(value: int) -> float:
    bits = value.bit_length()
    if bits <= 200:
        return log2(value)
    return bits - 200 + log2(value >> (bits - 200))


def cap_arithmetic() -> tuple[int, float, float]:
    n, k = 1 << 41, 1 << 40
    sigma = 8_592_912_738
    c = 1 << 22
    d, s = divmod(sigma, c)
    quotient_size = n // c
    m = k // c + d
    assert (d, s, quotient_size, m) == (2048, 2_978_146, 524_288, 264_192)

    count = comb(quotient_size - 1, m)
    boundary = (128 + log2_bigint(count)) / (d + 1)
    assert 255.9209 < boundary < 255.9210

    exact_left = count << 128
    assert exact_left > (1 << 255) ** (d + 1)
    assert exact_left < (1 << 256) ** (d + 1)

    qcore = comb(127, 64)
    qcore_gap = 128 - log2_bigint(qcore)
    assert 4.8285 < qcore_gap < 4.8286
    return count.bit_length(), boundary, qcore_gap


def main() -> None:
    total, lower, bucket = toy_replay()
    count_bits, boundary, qcore_gap = cap_arithmetic()
    print(
        "RATE_HALF_FIXED_TAIL_PREFIX_FLOOR_PASS "
        f"toy_total={total} toy_pigeonhole={lower} toy_bucket={bucket} "
        f"cap_count_bits={count_bits} q_boundary_bits={boundary:.13f} "
        f"cap_qcore_gap_bits={qcore_gap:.7f}"
    )


if __name__ == "__main__":
    main()
