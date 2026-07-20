#!/usr/bin/env python3
"""Exact checks for the WCL (1,6) even-norm divisor descent."""

from itertools import combinations

import sympy as sp


NODE = "dli_wcl_ell1_weight6_even_norm_divisor_descent"


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = (out[i + j] + ai * bj) % p
    return out


def polynomial_from_roots(roots, p):
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % p, 1], p)
    return out


def build_g(E, B, p):
    G = mul(E, E, p)
    B2 = mul(B, B, p)
    for j, value in enumerate(B2):
        G[j + 1] = (G[j + 1] - value) % p
    return G


def rem(f, g, p):
    f = [x % p for x in f]
    while len(f) >= len(g):
        lead = f[-1]
        shift = len(f) - len(g)
        for j, gj in enumerate(g):
            f[shift + j] = (f[shift + j] - lead * gj) % p
        while f and f[-1] == 0:
            f.pop()
    return f


def pow_y(exponent, modulus, p):
    acc, base = [1], [0, 1]
    while exponent:
        if exponent & 1:
            acc = rem(mul(acc, base, p), modulus, p) or [0]
        base = rem(mul(base, base, p), modulus, p) or [0]
        exponent >>= 1
    return acc


def symbolic_check():
    x, y = sp.symbols("x y")
    e0, e1, e2, b0, b1 = sp.symbols("e0 e1 e2 b0 b1")
    E = y**3 + e2 * y**2 + e1 * y + e0
    B = b1 * y + b0
    F = E.subs(y, x**2) - x * B.subs(y, x**2)
    G = E**2 - y * B**2
    assert sp.expand(F * F.subs(x, -x) - G.subs(y, x**2)) == 0
    assert sp.Poly(F, x).coeff_monomial(x**5) == 0


def positive_control():
    p, omega = 97, 28  # omega has exact order 32.
    exponents = (0, 1, 2, 3, 4, 8)
    signs = (1, -1, 1, 1, 1, 1)
    roots = [sign * pow(omega, exponent, p) % p
             for exponent, sign in zip(exponents, signs)]
    assert sum(roots) % p == 0
    assert len({r * r % p for r in roots}) == 6

    F = polynomial_from_roots(roots, p)
    assert F == [8, 58, 62, 77, 85, 0, 1]
    E = [F[0], F[2], F[4], F[6]]
    B = [(-F[1]) % p, (-F[3]) % p]
    G = build_g(E, B, p)
    assert E == [8, 62, 85, 1]
    assert B == [39, 20]
    assert G == [64, 53, 55, 68, 74, 73, 1]
    H = [p - 1] + [0] * 15 + [1]
    assert rem(H, G, p) == []

    reconstructed = []
    for y in {r * r % p for r in roots}:
        Ey = sum(value * pow(y, j, p) for j, value in enumerate(E)) % p
        By = sum(value * pow(y, j, p) for j, value in enumerate(B)) % p
        rho = Ey * pow(By, -1, p) % p
        assert rho * rho % p == y
        reconstructed.append(rho)
    assert set(reconstructed) == set(roots)


def complete_toy_relation_census():
    p, omega = 97, 28
    base = [pow(omega, exponent, p) for exponent in range(16)]
    hits = 0
    for indices in combinations(range(16), 6):
        values = [base[i] for i in indices]
        for mask in range(64):
            roots = [(-value if (mask >> j) & 1 else value) % p
                     for j, value in enumerate(values)]
            if sum(roots) % p:
                continue
            hits += 1
            F = polynomial_from_roots(roots, p)
            assert F[5] == 0
            E = [F[0], F[2], F[4], F[6]]
            B = [(-F[1]) % p, (-F[3]) % p]
            G = build_g(E, B, p)
            assert rem([p - 1] + [0] * 15 + [1], G, p) == []
    assert hits == 5408


def official_shape_quotients():
    p = 65537
    signatures = []
    for E, B in [
        ([3, 5, 7, 1], [11, 13]),
        ([p - 1, 0, 4, 1], [2, 9]),
        ([17, p - 3, 1, 1], [0, 5]),
    ]:
        G = build_g(E, B, p)
        residue = pow_y(256, G, p)
        residue[0] = (residue[0] - 1) % p
        assert len(residue) <= 6
        signatures.append(tuple(residue))
    assert len(set(signatures)) == 3


def main():
    symbolic_check()
    positive_control()
    complete_toy_relation_census()
    official_shape_quotients()
    print("DLI_WCL_ELL1_WEIGHT6_EVEN_NORM_DIVISOR_DESCENT_PASS "
          "symbolic=1 positive=1 toy_relations=5408 quotient=3")


if __name__ == "__main__":
    main()
