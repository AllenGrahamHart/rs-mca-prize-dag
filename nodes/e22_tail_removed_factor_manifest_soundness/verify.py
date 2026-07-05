#!/usr/bin/env python3
"""Tiny finite-field check for tail-removed factor-manifest soundness."""

from __future__ import annotations


def prime_factors(n: int) -> set[int]:
    out: set[int] = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.add(d)
            n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def primitive_root(p: int) -> int:
    factors = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise AssertionError(f"no primitive root found for {p}")


def poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = (out[i + j] + ai * bj) % p
    return out


def locator(roots: list[int], p: int) -> list[int]:
    poly = [1]
    for root in roots:
        poly = poly_mul(poly, [(-root) % p, 1], p)
    return poly


def xm_minus_z(m: int, z: int, p: int) -> list[int]:
    return [(-z) % p] + [0] * (m - 1) + [1]


def kernel(domain: list[int], m: int, p: int) -> list[int]:
    return [x for x in domain if pow(x, m, p) == 1]


def invariant_under_kernel(subset: set[int], domain: list[int], m: int, p: int) -> bool:
    ker = kernel(domain, m, p)
    return all((x * eta) % p in subset for x in subset for eta in ker)


def main() -> None:
    p = 17
    n = 16
    m = 4
    gen = primitive_root(p)
    h = pow(gen, (p - 1) // n, p)
    domain = [pow(h, j, p) for j in range(n)]
    values = sorted({pow(x, m, p) for x in domain})

    quotient_values = values[:2]
    non_tail = sorted(
        x for x in domain if pow(x, m, p) in set(quotient_values)
    )
    tail = [x for x in domain if x not in non_tail][:1]
    assert len(tail) < m

    product = [1]
    for z in quotient_values:
        product = poly_mul(product, xm_minus_z(m, z, p), p)
    assert locator(non_tail, p) == product
    assert invariant_under_kernel(set(non_tail), domain, m, p)
    print("PASS: tail-removed factor manifest implies kernel-invariant non-tail set")


if __name__ == "__main__":
    main()
