#!/usr/bin/env python3
"""Classifier for the h=3 hyperbola-line degeneracy cell."""

from __future__ import annotations

import random

import sympy as sp


u, v, a, b, w = sp.symbols("u v a b w")


def reduce_omega(expr):
    """Reduce a polynomial expression modulo w^2 + w + 1."""

    poly = sp.Poly(sp.expand(expr), w, u, v, a, b, domain=sp.QQ)
    mod = sp.Poly(w**2 + w + 1, w, u, v, a, b, domain=sp.QQ)
    return sp.expand(poly.rem(mod).as_expr())


def symbolic_check() -> None:
    omega2 = -w - 1
    alpha = (w + 2) / 3
    beta = (1 - w) / 3

    if reduce_omega(alpha * beta - sp.Rational(1, 3)) != 0:
        raise AssertionError("alpha beta != 1/3")

    A = u - w * v
    B = u - omega2 * v
    X = A + a * beta
    Y = B + a * alpha
    G = u**2 + u * v + v**2 + a * (u + v) + b
    delta = a**2 * alpha * beta - b

    if reduce_omega(delta - (a**2 / 3 - b)) != 0:
        raise AssertionError("Delta classifier failed")
    if reduce_omega(X * Y - delta - G) != 0:
        raise AssertionError("hyperbola identity failed")
    if reduce_omega((X * Y - G).subs(b, a**2 / 3)) != 0:
        raise AssertionError("line-cell factorization failed")


def primitive_cube_root(p: int) -> int:
    if (p - 1) % 3:
        raise ValueError(p)
    for cand in range(2, p):
        root = pow(cand, (p - 1) // 3, p)
        if root != 1 and (root * root + root + 1) % p == 0:
            return root
    raise AssertionError(f"no primitive cube root modulo {p}")


def g_value(p: int, aa: int, bb: int, uu: int, vv: int) -> int:
    return (uu * uu + uu * vv + vv * vv + aa * (uu + vv) + bb) % p


def count_zeros(p: int, aa: int, bb: int) -> int:
    total = 0
    for uu in range(p):
        for vv in range(p):
            if g_value(p, aa, bb, uu, vv) == 0:
                total += 1
    return total


def finite_field_check() -> None:
    rng = random.Random(20260708)
    for p in (7, 13, 19, 31, 37, 43, 61, 73, 97, 109):
        omega = primitive_cube_root(p)
        omega2 = omega * omega % p
        alpha = (omega + 2) * pow(3, -1, p) % p
        beta = (1 - omega) * pow(3, -1, p) % p
        inv3 = pow(3, -1, p)

        if alpha * beta % p != inv3:
            raise AssertionError(("alpha beta", p, omega, alpha, beta))

        for _ in range(40):
            aa = rng.randrange(p)
            bb = aa * aa * inv3 % p
            vv = rng.randrange(p)

            # X=0 line.
            uu = (omega * vv - aa * beta) % p
            if g_value(p, aa, bb, uu, vv) != 0:
                raise AssertionError(("X-line", p, aa, bb, uu, vv))

            # Y=0 line.
            uu = (omega2 * vv - aa * alpha) % p
            if g_value(p, aa, bb, uu, vv) != 0:
                raise AssertionError(("Y-line", p, aa, bb, uu, vv))

    for p in (7, 13, 19, 31):
        inv3 = pow(3, -1, p)
        for aa in range(p):
            line_b = aa * aa * inv3 % p
            if count_zeros(p, aa, line_b) != 2 * p - 1:
                raise AssertionError(("line count", p, aa, line_b))
            if count_zeros(p, aa, (line_b + 1) % p) != p - 1:
                raise AssertionError(("hyperbola count", p, aa, line_b + 1))


def main() -> None:
    symbolic_check()
    finite_field_check()
    print("symbolic classifier: Delta = a^2/3 - b")
    print("finite-field checks: line cell has 2p-1 points, nonzero Delta has p-1")
    print("H3_HYPERBOLA_LINE_DEGENERACY_PASS")


if __name__ == "__main__":
    main()
