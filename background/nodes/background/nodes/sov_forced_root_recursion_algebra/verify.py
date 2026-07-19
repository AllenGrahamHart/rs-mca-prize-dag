#!/usr/bin/env python3
"""Local verifier for sov_forced_root_recursion_algebra.

Replays the algebraic gate from the SOV Modal helper without importing Modal
or launching the value-set scan.
"""

from __future__ import annotations

import random


def poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return out


def locator_from_roots(roots: list[int], p: int) -> list[int]:
    coeffs = [1]
    for root in roots:
        nxt = [0] * (len(coeffs) + 1)
        for i, coeff in enumerate(coeffs):
            nxt[i] = (nxt[i] - coeff * root) % p
            nxt[i + 1] = (nxt[i + 1] + coeff) % p
        coeffs = nxt
    return coeffs


def square_shift_root(L: list[int], p: int, h: int) -> list[int]:
    inv2 = pow(2, -1, p)
    s = [0] * (h + 1)
    s[h] = 1
    for degree in range(2 * h - 1, h - 1, -1):
        unknown = degree - h
        known = 0
        lo = max(0, degree - h)
        hi = min(h, degree)
        for i in range(lo, hi + 1):
            j = degree - i
            if not (0 <= j <= h):
                continue
            if i == unknown or j == unknown:
                continue
            known = (known + s[i] * s[j]) % p
        s[unknown] = ((L[degree] - known) * inv2) % p
    return s


def forced_obstructions(L: list[int], p: int, h: int) -> tuple[list[int], list[int], int]:
    S = square_shift_root(L, p, h)
    S2 = poly_mul(S, S, p)
    obs = [(S2[i] - L[i]) % p for i in range(1, h)]
    lam = (S2[0] - L[0]) % p
    return S, obs, lam


def is_square_mod(a: int, p: int) -> bool:
    return a % p == 0 or pow(a, (p - 1) // 2, p) == 1


def main() -> None:
    checks = 0
    primes = {5: 101, 6: 65537, 10: 65537, 21: 65537, 40: 65537}
    for h, p in primes.items():
        rng = random.Random(17 * h)
        roots = rng.sample(range(2, p - 1), h)
        A = locator_from_roots(roots, p)
        delta = 13 + h
        B = list(A)
        B[0] = (B[0] + delta) % p
        L = poly_mul(A, B, p)
        S, obs, lam = forced_obstructions(L, p, h)
        midpoint = [((a + b) * pow(2, -1, p)) % p for a, b in zip(A, B)]
        assert S == midpoint, h
        assert all(v == 0 for v in obs), h
        assert lam == (delta * delta * pow(4, -1, p)) % p, h
        assert lam != 0 and is_square_mod(lam, p), h
        checks += 1

    h = 10
    p = 65537
    roots = random.Random(99).sample(range(2, p - 1), h)
    A = locator_from_roots(roots, p)
    B = list(A)
    B[0] = (B[0] + 17) % p
    L = poly_mul(A, B, p)
    _, obs0, _ = forced_obstructions(L, p, h)
    Lp = list(L)
    Lp[h - 1] = (Lp[h - 1] + 1) % p
    _, obs1, _ = forced_obstructions(Lp, p, h)
    assert (obs1[-1] - obs0[-1]) % p == (-1) % p
    assert obs0[:-1] == obs1[:-1]
    checks += 1
    print(f"forced-root recursion checks passed: {checks}")


if __name__ == "__main__":
    main()
