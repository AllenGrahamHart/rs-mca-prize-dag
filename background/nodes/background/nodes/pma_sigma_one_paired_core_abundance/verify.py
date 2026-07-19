#!/usr/bin/env python3
"""Exact verifier for the paired-core first moment and route obstruction."""

from collections import Counter
from itertools import combinations, product
from math import comb, factorial, isqrt


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def first_prime_one_mod(n, lower):
    q = lower + ((1 - lower) % n)
    while not is_prime(q):
        q += n
    return q


def falling(q, length):
    out = 1
    for j in range(length):
        out *= q - j
    return out


def pairing_count(m):
    return factorial(2 * m + 1) // (2**m * factorial(m))


def exact_total_formula(q, n, k):
    m = (n - k) // 2
    return comb(n, k - 1) * q ** (k - 1) * pairing_count(m) * falling(q, m + 1)


def exhaustive_k2(q, n):
    k = 2
    domain = tuple(range(1, n + 1))
    assert n < q and (n - k) % 2 == 0
    m = (n - k) // 2
    total = 0
    for values in product(range(q), repeat=n):
        word = dict(zip(domain, values))
        for (c,) in combinations(domain, 1):
            fibers = Counter()
            for x in domain:
                if x == c:
                    continue
                phi = (word[x] - word[c]) * pow(x - c, q - 2, q) % q
                fibers[phi] += 1
            if sorted(fibers.values()) == [1] + [2] * m:
                total += 1
    return total


def small_exact_checks():
    rows = [(5, 4), (7, 6)]
    for q, n in rows:
        observed = exhaustive_k2(q, n)
        expected = exact_total_formula(q, n, 2)
        assert observed == expected
        wrong_without_singleton = expected // (n - 1)
        assert observed != wrong_without_singleton
    return len(rows)


def official_route_cut():
    n = 65536
    k = 32768
    m = (n - k) // 2
    q = first_prime_one_mod(n, n + 1)
    assert q == 65537 and q % n == 1 and is_prime(q)

    numerator = comb(n, k - 1) * pairing_count(m) * falling(q, m + 1)
    denominator = q ** (2 * m + 1)
    target = n**6 * denominator
    assert numerator > target

    mean_floor = numerator // denominator
    margin_floor = numerator // target
    assert mean_floor > n**6 and margin_floor > 1
    return {
        "q": q,
        "mean_floor_bits": mean_floor.bit_length(),
        "n6_bits": (n**6).bit_length(),
        "margin_floor_bits": margin_floor.bit_length(),
    }


def mutation_checks():
    assert 12289 % 8192 != 1
    assert 65537 % 65536 == 1
    n, k, q = 6, 2, 7
    observed = exhaustive_k2(q, n)
    m = (n - k) // 2
    wrong_repeated_values = comb(n, k - 1) * q ** (k - 1) * pairing_count(m) * q ** (m + 1)
    assert observed != wrong_repeated_values
    return 2


def main():
    small = small_exact_checks()
    row = official_route_cut()
    mutations = mutation_checks()
    print(
        "PMA_PAIRED_CORE_ABUNDANCE_PASS "
        f"small_rows={small} q={row['q']} "
        f"mean_floor_bits={row['mean_floor_bits']} n6_bits={row['n6_bits']} "
        f"margin_floor_bits={row['margin_floor_bits']} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
