#!/usr/bin/env python3
"""Finite replay for the PMA quotient-closure scope theorem."""

from fractions import Fraction


CHECKS = 0


def check(label, condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def stabilizer_size(mask):
    n = len(mask)
    return sum(
        all(mask[(i + shift) % n] == mask[i] for i in range(n))
        for shift in range(n)
    )


def folded(values, d):
    n = len(values)
    quotient = n // d
    return all(values[i] == values[i % quotient] for i in range(n))


# Folded receiver + folded codeword force periodic agreement.
for n in (8, 12, 16, 24, 32):
    for d in range(2, n + 1):
        if n % d:
            continue
        quotient = n // d
        u = [((i % quotient) ** 2 + 3 * (i % quotient) + 1) % 17 for i in range(n)]
        p = [((i % quotient) ** 3 + 2) % 17 for i in range(n)]
        agreement = [u[i] == p[i] for i in range(n)]
        check("receiver folded", folded(u, d))
        check("codeword folded", folded(p, d))
        check("folded agreement invariant", stabilizer_size(agreement) >= d)


# A folded codeword alone does not force periodic agreement.
n = 8
d = 2
p = [0] * n
u = [0] + [1] * (n - 1)
agreement = [u[i] == p[i] for i in range(n)]
check("codeword-only folded", folded(p, d))
check("nonfolded receiver", not folded(u, d))
check("codeword-only agreement can be primitive", stabilizer_size(agreement) == 1)


# Official first-shell identities and the raw-route cut use only O(log n)-bit
# integer arithmetic; no giant binomial coefficient is materialized.
rates = (Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), Fraction(1, 16))
rows = 0
for s in range(13, 45):
    n = 1 << s
    for rho in rates:
        rows += 1
        k = n * rho.numerator // rho.denominator
        j = n - k - 1
        N = n // 2
        h = k // 2 + 1
        check("first shell odd", j % 2 == 1)
        check("periodic core integral", (j - 1) % 2 == 0)
        check("complement index", (j - 1) // 2 == N - h)
        check("nondegenerate Q2", 0 < h < N)
        check("raw route exceeds 719 line", n * N > 719 * (N - h))
        check("boundary factor is load-bearing", N <= 719 * (N - h))


# Small set-level boundary stripping sanity checks. Exponents model the cyclic
# group Z/nZ; K_d-cosets are residue classes modulo n/d.
for n, d in ((8, 2), (12, 3), (16, 4), (24, 3)):
    quotient = n // d
    full_cosets = {1 % quotient, 3 % quotient}
    full = {x for x in range(n) if x % quotient in full_cosets}
    boundary = {0}
    error = full | boundary
    recovered_full = {
        x
        for x in range(n)
        if all(((x % quotient) + t * quotient) % n in error for t in range(d))
    }
    recovered_boundary = error - recovered_full
    check("full core recovered", recovered_full == full)
    check("boundary recovered", recovered_boundary == boundary)
    check("one-defect support primitive", stabilizer_size([i in error for i in range(n)]) == 1)
    D = len(error) + 3
    check("reserve preserved", (D - 1) - len(full) == D - len(error))


print(f"PMA quotient-closure scope: PASS ({CHECKS} checks, {rows} official rows)")
