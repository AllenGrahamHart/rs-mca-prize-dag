#!/usr/bin/env python3
"""Independent modular point replay of the polynomial certificates."""

from __future__ import annotations

import math


PRIMES = (998244353, 1000000007)


def rising_value(s: int, r: int, p: int) -> int:
    out = 1
    for j in range(r):
        out = out * (s + j) % p
    return out * pow(math.factorial(r), -1, p) % p


def trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def subtract(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] = (out[i] + value) % p
    for i, value in enumerate(b):
        out[i] = (out[i] - value) % p
    return trim(out)


def scalar(a: list[int], c: int, p: int) -> list[int]:
    return trim([c * value % p for value in a])


def shift(a: list[int], d: int) -> list[int]:
    return [0] * d + a


def divide_monic(a: list[int], b: list[int], p: int) -> list[int]:
    assert b[-1] == 1
    rem = a[:]
    while len(rem) >= len(b):
        d = len(rem) - len(b)
        rem = subtract(rem, shift(scalar(b, rem[-1], p), d), p)
    rem += [0] * (len(b) - 1 - len(rem))
    return rem


def reflection_value(m: int, s: int, p: int) -> int:
    h = m - 1
    locator = [0] * (h + 1)
    for r in range(h + 1):
        locator[h - r] = rising_value(s, r, p)
    dividend = [0] * (2 * m + 1)
    dividend[0] = p - 1
    for j in range(m + 1):
        dividend[m + j] = ((-1) ** j * math.comb(m, j)) % p
    return divide_monic(dividend, locator, p)[h - 1]


def expected_reflection_value(m: int, s: int, p: int) -> int:
    if m == 8:
        factors, numerator, denominator = list(range(8)) + [3, 4], 1, 22400
    else:
        factors, numerator, denominator = (
            list(range(16)) + [7, 8],
            17,
            188305108992000,
        )
    out = numerator * pow(denominator, -1, p) % p
    for j in factors:
        out = out * (s + j) % p
    return out


def pseudo_remainder(a: list[int], b: list[int], p: int) -> list[int]:
    rem = a[:]
    while len(rem) >= len(b):
        d = len(rem) - len(b)
        rem = subtract(
            scalar(rem, b[-1], p),
            shift(scalar(b, rem[-1], p), d),
            p,
        )
    return rem


def antipodal_y_value(s: int, p: int) -> int:
    b = [rising_value(s, r, p) for r in range(8)]
    odd = [b[6], b[4], b[2], b[0]]
    even = [b[7], b[5], b[3], b[1]]
    reduced = subtract(even, scalar(odd, s, p), p)
    rem = pseudo_remainder(odd, reduced, p)
    return rem[1] if len(rem) > 1 else 0


def expected_antipodal_value(s: int, p: int) -> int:
    out = -pow(4725, -1, p) % p
    for j in (0, 0, -3, -2, -1, -1, 1, 1, 2, 3):
        out = out * (s + j) % p
    return out


def main() -> None:
    reflection_checks = 0
    antipodal_checks = 0
    for p in PRIMES:
        for m in (8, 16):
            # Both sides have degree at most 2m, so 2m+1 points pin the
            # specialized identity independently of the symbolic checker.
            for s in range(2 * m + 1):
                assert reflection_value(m, s, p) == expected_reflection_value(m, s, p)
                reflection_checks += 1
        # Avoid s in {0,+/-1}, where the generic quadratic pseudo-divisor
        # drops degree; those are exactly prime-field cases excluded in the
        # theorem before pseudo-division.
        for s in range(10, 23):
            assert antipodal_y_value(s, p) == expected_antipodal_value(s, p)
            antipodal_checks += 1

    mutations = 0
    p = PRIMES[0]
    mutations += reflection_value(8, 11, p) != (-expected_reflection_value(8, 11, p)) % p
    mutations += antipodal_y_value(11, p) != (-expected_antipodal_value(11, p)) % p
    assert mutations == 2

    print(
        "L1_MERSENNE_HNF_ORDER_ZERO_QUADRATIC_COLLISION_ROUTER_AUDIT_PASS "
        f"primes={len(PRIMES)} reflection_points={reflection_checks} "
        f"antipodal_points={antipodal_checks} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
