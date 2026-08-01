#!/usr/bin/env python3
"""Exact verifier for dli_c1_doubling_coboundary_identity.

All checks are exact (integers / rationals); no floating point.
  1. q=257, |H|=32 (2 in H): the polynomial coboundary identity
     prod(1+X^h) * prod(1-X^h) == prod(1-X^(2h))  mod (X^q - 1)
     in integer arithmetic, for a nontrivial coset.
  2. Small-orbit router: 257 | 2^16 - 1 (r=1 instance).
  3. Exact flatness: the subset-sum DP gives
     Z - 2^16/257 == 256/(257*2^16) exactly, matching (DB-3) with A == 1.
  4. q=7681, |H|=512 (official L=1 shape): the polynomial identity for
     the coset of 1, exact integer coefficients mod (X^q - 1).
"""
from __future__ import annotations
from fractions import Fraction


def require(c: bool, m: str) -> None:
    if not c:
        raise AssertionError(m)


def prime_factors(n: int) -> list[int]:
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p: int) -> int:
    fs = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in fs):
            return g
    raise AssertionError("no primitive root")


def sparse_product(exponents: list[int], sign: int, q: int) -> list[int]:
    """prod (1 + sign*X^e) as integer coefficient vector mod X^q - 1."""
    poly = [0] * q
    poly[0] = 1
    for e in exponents:
        new = poly[:]
        for i, c in enumerate(poly):
            if c:
                new[(i + e) % q] += sign * c
        poly = new
    return poly


def check_identity(q: int, order: int, coset_rep: int) -> None:
    g = primitive_root(q)
    hgen = pow(g, (q - 1) // order, q)
    H = [pow(hgen, i, q) for i in range(order)]
    require(len(set(H)) == order, "subgroup size")
    require((q - 1) % order == 0, "subgroup divides")
    require(q - 1 in H or (q - 1) in H, "-1 in H")

    ch = [coset_rep * h % q for h in H]
    ch2 = [2 * x % q for x in ch]
    lhs_a = sparse_product(ch, +1, q)
    lhs_d = sparse_product(ch, -1, q)
    prod = [0] * q
    for i, a in enumerate(lhs_a):
        if a:
            for j, b in enumerate(lhs_d):
                if b:
                    prod[(i + j) % q] += a * b
    rhs = sparse_product(ch2, -1, q)
    require(prod == rhs, f"coboundary polynomial identity q={q}")


def main() -> None:
    # 1-2: q=257, order 32, r=1.
    q, order, n = 257, 32, 16
    check_identity(q, order, 3)
    require(pow(2, 16, q) == 1, "2 has order dividing 16 mod 257")
    g = primitive_root(q)
    hgen = pow(g, (q - 1) // order, q)
    H = {pow(hgen, i, q) for i in range(order)}
    require(2 in H, "2 in H at q=257")
    require((2 ** (order * 1) - 1) % q == 0, "small-orbit router r=1")

    # 3: exact flatness via subset-sum DP.
    omega = pow(g, (q - 1) // (2 * n), q)
    coeffs = [pow(omega, i, q) for i in range(n)]
    counts = [0] * q
    counts[0] = 1
    for a in coeffs:
        new = counts[:]
        for s, c in enumerate(counts):
            if c:
                new[(s + a) % q] += c
        counts = new
    z = Fraction(sum(c * c for c in counts), 2 ** n)
    x = z - Fraction(2 ** n, q)
    require(x == Fraction(q - 1, q * 2 ** n), "exact flat-row excess (DB-3)")

    # 4: official L=1 shape, q=7681, order 512.
    check_identity(7681, 512, 1)

    print("DLI_C1_DOUBLING_COBOUNDARY_IDENTITY_PASS",
          f"flat_row_excess={x}")


if __name__ == "__main__":
    main()
