#!/usr/bin/env python3
"""Constructive checks for the HNF Frobenius reciprocal gate."""

from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def nonsquare(p):
    return next(d for d in range(2, p) if pow(d, (p - 1) // 2, p) == p - 1)


def mul(x, y, p, d):
    return ((x[0] * y[0] + d * x[1] * y[1]) % p,
            (x[0] * y[1] + x[1] * y[0]) % p)


def power(x, exponent, p, d):
    out = (1, 0)
    while exponent:
        if exponent & 1:
            out = mul(out, x, p, d)
        x = mul(x, x, p, d)
        exponent >>= 1
    return out


def add(x, y, p):
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def scale(x, scalar, p):
    return (x[0] * scalar % p, x[1] * scalar % p)


def polynomial_from_roots(roots, p, d):
    coefficients = [(1, 0)]
    for root in roots:
        updated = [(0, 0)] * (len(coefficients) + 1)
        for j, value in enumerate(coefficients):
            updated[j] = add(updated[j], scale(mul(value, root, p, d), -1, p), p)
            updated[j + 1] = add(updated[j + 1], value, p)
        coefficients = updated
    return coefficients


checks = 0
for p, m in ((23, 8), (31, 16)):
    h = m - 1
    d = nonsquare(p)
    norm_one = [
        (a, b)
        for a in range(p)
        for b in range(p)
        if (a, b) != (0, 0) and power((a, b), p + 1, p, d) == (1, 0)
    ]
    assert len(norm_one) == p + 1
    roots = norm_one[1:h + 1]
    q = polynomial_from_roots(roots, p, d)
    q_frobenius = [power(value, p, p, d) for value in q]
    constant = q[0]
    lhs = [mul(constant, value, p, d) for value in q_frobenius]
    rhs = list(reversed(q))
    assert lhs == rhs
    checks += 1

    for j in range(h + 1):
        # q is stored in increasing powers; this is FRG5 with t=s^p.
        assert mul(q[0], q_frobenius[h - j], p, d) == q[j]
    checks += 1

    # The diagonal hypergeometric solution s=1 has P=(W^m-1)/(W-1)
    # and hence Q=(Z-1)^h with constant -1.
    diagonal_q = [(-1) ** (h - k) * comb(h, k) % p for k in range(h + 1)]
    assert diagonal_q[0] == p - 1 and diagonal_q[-1] == 1
    assert [diagonal_q[0] * value % p for value in diagonal_q] == list(reversed(diagonal_q))
    checks += 1

    for s in (1, 2, 5):
        a0 = 1
        for r in range(h):
            a0 = a0 * (s + r) * pow(r + 1, -1, p) % p
        assert a0 == comb(s + h - 1, h) % p
        if s == 1:
            assert (-pow(a0, m, p)) % p == diagonal_q[0]
        checks += 1

statement = (ROOT / "statement.md").read_text()
proof = (ROOT / "proof.md").read_text()
for anchor in (
    "(FRG1)",
    "(FRG2)",
    "(FRG3)",
    "(FRG4)",
    "(FRG5)",
    "(FRG6)",
    "t!=s",
    "necessary candidates",
):
    assert anchor in statement
    checks += 1
for anchor in (
    "y_i^p=y_i^(-1)",
    "The reverse implication is deliberately not claimed",
    "need not identify every root pointwise",
):
    assert anchor in proof
    checks += 1

print(f"L1_MERSENNE_HNF_FROBENIUS_RECIPROCAL_GATE_PASS checks={checks}")
