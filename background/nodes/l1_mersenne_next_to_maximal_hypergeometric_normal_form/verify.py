#!/usr/bin/env python3
"""Constructive checks for the next-to-maximal hypergeometric normal form."""

from fractions import Fraction
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def coeff(poly, k):
    return poly[k] if 0 <= k < len(poly) else Fraction(0)


def recurrence(h, A, c):
    g = [Fraction(0) for _ in range(h + 1)]
    g[h] = Fraction(1)
    g[h - 1] = Fraction(0)
    g[h - 2] = A
    for k in range(h, 1, -1):
        g[k - 2] = (
            (2 * A - c * (h - k)) * g[k]
            + (1 + c) * (h - k + 1) * g[k - 1]
        ) / (h - k + 2)
    ell = (
        (2 * A - c * (h - 1)) * g[1] + (1 + c) * h * g[0]
    ) / (2 * A)
    return g, ell


def shifted(g, c):
    h = len(g) - 1
    d = c - 1
    return [
        sum(g[j] * comb(j, k) for j in range(k, h + 1)) * d ** (k - h)
        for k in range(h + 1)
    ]


def rising_binom(s, r):
    out = Fraction(1)
    for j in range(r):
        out *= s + j
        out /= j + 1
    return out


def falling_binom(s, r):
    out = Fraction(1)
    for j in range(r):
        out *= s - j
        out /= j + 1
    return out


def generating_coefficient(rho, c, r):
    return sum(
        (-1) ** j
        * falling_binom(c * rho, j)
        * c ** (r - j)
        * rising_binom(rho, r - j)
        for j in range(r + 1)
    )


checks = 0
for h in (7, 15):
    for c in (Fraction(2), Fraction(3), Fraction(5, 2)):
        A = c * h / 2
        g, ell = recurrence(h, A, c)

        for k in range(h + 3):
            lhs = 2 * A * (coeff(g, k) - (ell if k == 1 else 0))
            rhs = (
                (h - k + 2) * coeff(g, k - 2)
                - (1 + c) * (h - k + 1) * coeff(g, k - 1)
                + c * (h - k) * coeff(g, k)
            )
            assert lhs == rhs
        checks += 1

        assert (2 * A - c * h) * g[0] == 0
        checks += 1

        p = shifted(g, c)
        s = Fraction(h, 1) / (c - 1)
        expected = [rising_binom(s, h - k) for k in range(h + 1)]
        assert p == expected
        checks += 1

        b = -h - s
        K = (h + s) * p[0]
        for k in range(h + 2):
            lhs = (k - 1) * coeff(p, k - 1) - k * coeff(p, k)
            if k == 0:
                lhs -= K
            rhs = h * coeff(p, k - 1) + b * coeff(p, k)
            assert lhs == rhs
        checks += 1

for h in (7, 15):
    for A, c in (
        (Fraction(2), Fraction(3)),
        (Fraction(5, 2), Fraction(4)),
        (Fraction(7, 3), Fraction(5, 2)),
    ):
        g, _ = recurrence(h, A, c)
        rho = 2 * A / (c * (c - 1))
        assert [g[h - r] for r in range(h + 1)] == [
            generating_coefficient(rho, c, r) for r in range(h + 1)
        ]
        checks += 1

rows = (
    (8, 7, 8191),
    (8, 7, 131071),
    (8, 7, 524287),
    (8, 7, 2147483647),
    (16, 15, 8191),
)
for m, h, pchar in rows:
    assert h == m - 1 and pchar > h
    n = m * (pchar + 1)
    assert n % 2 == 0 and n & (n - 1) == 0
    checks += 1

statement = (ROOT / "statement.md").read_text()
proof = (ROOT / "proof.md").read_text()
for anchor in (
    "(HNF2)",
    "(HNF3)",
    "(HNF4)",
    "(HNF4a)",
    "(HNF5)",
    "(HNF7)",
    "(HNF7a)",
    "(HNF8)",
    "s notin F_p",
    "does not prove either intersection empty",
):
    assert anchor in statement
    checks += 1
for anchor in (
    "top-down recurrence",
    "unique unit-constant solution",
    "b=-h-s",
    "x_0^n=1",
    "without asserting that",
):
    assert anchor in proof
    checks += 1

print(f"L1_MERSENNE_NEXT_TO_MAXIMAL_HYPERGEOMETRIC_NORMAL_FORM_PASS checks={checks}")
