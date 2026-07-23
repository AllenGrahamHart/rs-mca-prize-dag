#!/usr/bin/env python3
"""Constructive checks for the order-one HNF Frobenius gate."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def nonsquare(p):
    return next(d for d in range(2, p) if pow(d, (p - 1) // 2, p) == p - 1)


def add(x, y, p):
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def neg(x, p):
    return (-x[0] % p, -x[1] % p)


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


def inverse(x, p, d):
    assert x != (0, 0)
    return power(x, p * p - 2, p, d)


def divide_by_int(x, value, p):
    return (x[0] * pow(value, -1, p) % p,
            x[1] * pow(value, -1, p) % p)


def falling_binom(x, r, p, d):
    out = (1, 0)
    for j in range(r):
        out = mul(out, add(x, (-j % p, 0), p), p, d)
        out = divide_by_int(out, j + 1, p)
    return out


def rising_binom(x, r, p, d):
    out = (1, 0)
    for j in range(r):
        out = mul(out, add(x, (j, 0), p), p, d)
        out = divide_by_int(out, j + 1, p)
    return out


def u_coefficient(rho, c, r, p, d):
    c_rho = mul(c, rho, p, d)
    out = (0, 0)
    for j in range(r + 1):
        left = falling_binom(c_rho, j, p, d)
        if j % 2:
            left = neg(left, p)
        right = mul(power(c, r - j, p, d),
                    rising_binom(rho, r - j, p, d), p, d)
        out = add(out, mul(left, right, p, d), p)
    return out


def polynomial_from_roots(roots, p, d):
    coefficients = [(1, 0)]
    for root in roots:
        updated = [(0, 0)] * (len(coefficients) + 1)
        for j, value in enumerate(coefficients):
            updated[j] = add(updated[j], neg(mul(value, root, p, d), p), p)
            updated[j + 1] = add(updated[j + 1], value, p)
        coefficients = updated
    return coefficients


checks = 0
for p, m in ((23, 8), (31, 16)):
    h = m - 1
    dquad = nonsquare(p)
    norm_one = [
        (a, b)
        for a in range(p)
        for b in range(p)
        if (a, b) != (0, 0) and power((a, b), p + 1, p, dquad) == (1, 0)
    ]
    d = next(value for value in norm_one if value not in ((1, 0), (p - 1, 0)))
    c = add((1, 0), d, p)
    zeta = power(d, p + 1, p, dquad)
    c_star = add((1, 0), mul(zeta, inverse(d, p, dquad), p, dquad), p)
    assert power(zeta, m, p, dquad) == (1, 0)
    assert power(c, p, p, dquad) == c_star
    checks += 1

    rho = (3, 1)
    rho_star = power(rho, p, p, dquad)
    for r in range(h + 1):
        assert power(u_coefficient(rho, c, r, p, dquad), p, p, dquad) == \
            u_coefficient(rho_star, c_star, r, p, dquad)
    checks += 1

    y_zero = power(d, -m % (p * p - 1), p, dquad)
    assert power(y_zero, p, p, dquad) == inverse(y_zero, p, dquad)
    remaining_roots = [value for value in norm_one if value != y_zero][:h - 1]
    assert len(remaining_roots) == h - 1

    q_tilde = polynomial_from_roots(remaining_roots, p, dquad)
    q_tilde_frobenius = [power(value, p, p, dquad) for value in q_tilde]
    constant_tilde = q_tilde[0]
    assert [mul(constant_tilde, value, p, dquad)
            for value in q_tilde_frobenius] == list(reversed(q_tilde))
    checks += 1

    roots = [y_zero] + remaining_roots
    q = polynomial_from_roots(roots, p, dquad)
    q_frobenius = [power(value, p, p, dquad) for value in q]
    constant = q[0]
    assert [mul(constant, value, p, dquad) for value in q_frobenius] == list(reversed(q))
    checks += 1

statement = (ROOT / "statement.md").read_text()
proof = (ROOT / "proof.md").read_text()
for anchor in (
    "(OFG1)",
    "(OFG2)",
    "(OFG3)",
    "(OFG4)",
    "(OFG5)",
    "(OFG5a)",
    "(OFG6)",
    "(OFG7)",
    "(OFG8)",
    "retained component",
):
    assert anchor in statement
    checks += 1
for anchor in (
    "c^p=(1+d)^p",
    "automatic zero-value factor",
    "The reverse implication is not claimed",
    "setwise Frobenius inversion",
):
    assert anchor in proof
    checks += 1

print(f"L1_MERSENNE_HNF_ORDER_ONE_FROBENIUS_GATE_PASS checks={checks}")
