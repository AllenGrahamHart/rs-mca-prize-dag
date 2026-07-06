#!/usr/bin/env python3
"""Finite-field checks for quotient-fiber locator saturation."""


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
    for r in roots:
        poly = poly_mul(poly, [(-r) % p, 1], p)
    return poly


def xm_minus_z(m: int, z: int, p: int) -> list[int]:
    return [(-z) % p] + [0] * (m - 1) + [1]


def eval_poly(poly: list[int], x: int, p: int) -> int:
    acc = 0
    for coeff in reversed(poly):
        acc = (acc * x + coeff) % p
    return acc


def main() -> None:
    cases = [(17, 16), (97, 32), (193, 64)]
    for p, n in cases:
        gen = primitive_root(p)
        step = (p - 1) // n
        h = pow(gen, step, p)
        domain = [pow(h, j, p) for j in range(n)]
        for m in [2**i for i in range(1, n.bit_length()) if 2**i <= n]:
            values = sorted({pow(x, m, p) for x in domain})
            for z in values:
                fib = [x for x in domain if pow(x, m, p) == z]
                assert len(fib) == m, (p, n, m, z, fib)
                assert locator(fib, p) == xm_minus_z(m, z, p), (p, n, m, z)

                # Missing one fiber point prevents divisibility.
                missing_support = [x for x in domain if x != fib[0]]
                miss_loc = locator(missing_support, p)
                assert eval_poly(miss_loc, fib[0], p) != 0

    print("PASS: quotient-fiber locator factors are exactly full fibers")


if __name__ == "__main__":
    main()
