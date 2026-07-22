#!/usr/bin/env python3
"""Independent finite-field audit of the hypergeometric recurrence."""

from math import comb


def inv(x, p):
    return pow(x % p, p - 2, p)


def recurrence(h, A, c, p):
    g = [0] * (h + 1)
    g[h] = 1
    g[h - 2] = A
    for k in range(h, 1, -1):
        g[k - 2] = (
            (2 * A - c * (h - k)) * g[k]
            + (1 + c) * (h - k + 1) * g[k - 1]
        ) * inv(h - k + 2, p) % p
    ell = (
        (2 * A - c * (h - 1)) * g[1] + (1 + c) * h * g[0]
    ) * inv(2 * A, p) % p
    return g, ell


def rising_binom(s, r, p):
    value = 1
    for j in range(r):
        value = value * (s + j) * inv(j + 1, p) % p
    return value


def falling_binom(s, r, p):
    value = 1
    for j in range(r):
        value = value * (s - j) * inv(j + 1, p) % p
    return value


def generating_coefficient(rho, c, r, p):
    return sum(
        (-1) ** j
        * falling_binom(c * rho, j, p)
        * pow(c, r - j, p)
        * rising_binom(rho, r - j, p)
        for j in range(r + 1)
    ) % p


checks = 0
for p in (101, 103):
    for h in (7, 15):
        for c in (2, 3, 7, 19):
            A = c * h * inv(2, p) % p
            g, ell = recurrence(h, A, c, p)
            for k in range(h + 3):
                gk = g[k] if 0 <= k <= h else 0
                gk1 = g[k - 1] if 0 <= k - 1 <= h else 0
                gk2 = g[k - 2] if 0 <= k - 2 <= h else 0
                lhs = 2 * A * (gk - (ell if k == 1 else 0))
                rhs = (
                    (h - k + 2) * gk2
                    - (1 + c) * (h - k + 1) * gk1
                    + c * (h - k) * gk
                )
                assert (lhs - rhs) % p == 0
            checks += 1

            d = (c - 1) % p
            s = h * inv(d, p) % p
            for k in range(h + 1):
                shifted_k = sum(
                    g[j] * comb(j, k) for j in range(k, h + 1)
                ) * pow(inv(d, p), h - k) % p
                assert shifted_k == rising_binom(s, h - k, p)
            checks += 1

            x0 = -inv(d, p) % p
            for n in (32, 64, 128):
                assert (pow(x0, n, p) == 1) == (pow(d, n, p) == 1)
                checks += 1

        for A, c in ((2, 3), (5, 4), (7, 6)):
            g, _ = recurrence(h, A, c, p)
            rho = 2 * A * inv(c * (c - 1), p) % p
            assert [g[h - r] for r in range(h + 1)] == [
                generating_coefficient(rho, c, r, p) for r in range(h + 1)
            ]
            checks += 1

print(
    "L1_MERSENNE_NEXT_TO_MAXIMAL_HYPERGEOMETRIC_NORMAL_FORM_AUDIT_PASS "
    f"checks={checks}"
)
