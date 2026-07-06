#!/usr/bin/env python3
"""Sanity check for the n=32,h=16 over-ceiling algebraic certificate."""

from __future__ import annotations


def sig_general(exps: tuple[int, ...], powers: list[int], p: int, h: int) -> tuple[tuple[int, ...], int]:
    coef = [1] + [0] * h
    for a in exps:
        r = powers[a]
        for j in range(h, 0, -1):
            coef[j] = (coef[j] - r * coef[j - 1]) % p
    e = tuple(((-coef[j]) % p if (j & 1) else coef[j]) for j in range(1, h))
    e_h = (-coef[h]) % p if (h & 1) else coef[h]
    return e, e_h


def is_coset(exps: tuple[int, ...], h: int, n: int) -> bool:
    if n % h:
        return False
    step = n // h
    r0 = exps[0] % step
    return sorted(exps) == sorted((r0 + j * step) % n for j in range(h))


def mu_n_generator(p: int, n: int) -> int:
    assert (p - 1) % n == 0
    e = (p - 1) // n
    a = 2
    while True:
        z = pow(a, e, p)
        if pow(z, n // 2, p) != 1:
            return z
        a += 1


def check_cell(p: int) -> None:
    n = 32
    h = 16
    z = mu_n_generator(p, n)
    powers = [pow(z, a, p) for a in range(n)]
    even = tuple(range(0, n, 2))
    odd = tuple(range(1, n, 2))
    sig_even, top_even = sig_general(even, powers, p, h)
    sig_odd, top_odd = sig_general(odd, powers, p, h)
    assert sig_even == sig_odd == (0,) * (h - 1)
    assert top_even != top_odd
    assert is_coset(even, h, n)
    assert is_coset(odd, h, n)


def main() -> None:
    for p in (1153, 32801):
        check_cell(p)
        print(f"n=32 h=16 p={p}: only toral even/odd complement trade")
    print("M720 over-ceiling complete-window certificates PASS")


if __name__ == "__main__":
    main()
