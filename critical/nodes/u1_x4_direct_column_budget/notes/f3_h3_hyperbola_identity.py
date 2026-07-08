#!/usr/bin/env python3
"""Symbolic and finite-field checks for the h=3 hyperbola normal form."""

from __future__ import annotations

import random

import sympy as sp


u, v, a, b, w = sp.symbols("u v a b w")


def reduce_omega(expr):
    """Reduce a polynomial expression modulo w^2 + w + 1."""

    poly = sp.Poly(sp.expand(expr), w, u, v, a, b, domain=sp.QQ)
    mod = sp.Poly(w**2 + w + 1, w, u, v, a, b, domain=sp.QQ)
    rem = poly.rem(mod)
    return sp.expand(rem.as_expr())


def symbolic_check() -> None:
    omega2 = -w - 1
    # (1 + omega^2)/(omega^2 - omega) reduced modulo omega^2+omega+1.
    # Since (2*omega+1)^2 = -3, this equals (omega+2)/3.
    alpha = (w + 2) / 3
    beta = (1 - w) / 3

    A = u - w * v
    B = u - omega2 * v
    if reduce_omega(alpha + beta - 1) != 0:
        raise AssertionError("alpha + beta != 1")
    if reduce_omega(alpha * A + beta * B - (u + v)) != 0:
        raise AssertionError("linear coordinate inverse failed")
    if reduce_omega(A * B - (u**2 + u * v + v**2)) != 0:
        raise AssertionError("quadratic factorization failed")

    X = A + a * beta
    Y = B + a * alpha
    delta = a**2 * alpha * beta - b
    G = u**2 + u * v + v**2 + a * (u + v) + b
    if reduce_omega(X * Y - delta - G) != 0:
        raise AssertionError("XY-Delta identity failed")


def primitive_cube_root(p: int) -> int:
    if (p - 1) % 3:
        raise ValueError(p)
    for cand in range(2, p):
        root = pow(cand, (p - 1) // 3, p)
        if root != 1 and (root * root + root + 1) % p == 0:
            return root
    raise AssertionError(f"no primitive cube root modulo {p}")


def finite_field_check() -> None:
    rng = random.Random(20260708)
    for p in (7, 13, 19, 31, 37, 43, 61, 73, 97, 109):
        omega = primitive_cube_root(p)
        omega2 = omega * omega % p
        det = (omega2 - omega) % p
        alpha = (1 + omega2) * pow(det, -1, p) % p
        beta = (1 - alpha) % p
        for _ in range(200):
            uu = rng.randrange(p)
            vv = rng.randrange(p)
            aa = rng.randrange(p)
            bb = rng.randrange(p)
            A = (uu - omega * vv) % p
            B = (uu - omega2 * vv) % p
            X = (A + aa * beta) % p
            Y = (B + aa * alpha) % p
            delta = (aa * aa % p * alpha % p * beta - bb) % p
            G = (uu * uu + uu * vv + vv * vv + aa * (uu + vv) + bb) % p
            if (X * Y - delta - G) % p:
                raise AssertionError((p, uu, vv, aa, bb, omega, alpha, beta))


def main() -> None:
    symbolic_check()
    finite_field_check()
    print("symbolic identity: XY - Delta = G_F")
    print("finite-field checks: 10 primes, 200 rows each")
    print("H3_HYPERBOLA_IDENTITY_PASS")


if __name__ == "__main__":
    main()
