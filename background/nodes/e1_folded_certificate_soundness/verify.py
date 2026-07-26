#!/usr/bin/env python3
"""Toy replay of the folded E1 certificate examples at N'=16."""

from __future__ import annotations

import itertools


def factor_int(n: int) -> list[int]:
    out = []
    d = 2
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
    factors = factor_int(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise AssertionError("no primitive root")


def order_n_generator(p: int, n: int) -> int:
    z = pow(primitive_root(p), (p - 1) // n, p)
    assert pow(z, n, p) == 1 and pow(z, n // 2, p) != 1
    return z


def folded_zero_count(n: int, p: int) -> int:
    z = order_n_generator(p, n)
    powers = [pow(z, i, p) for i in range(n // 2)]
    count = 0
    for w in itertools.product(range(-2, 3), repeat=n // 2):
        if all(x == 0 for x in w):
            continue
        if sum(x * powers[i] for i, x in enumerate(w)) % p == 0:
            count += 1
    return count


def main() -> None:
    certified = folded_zero_count(16, 60161)
    bad = folded_zero_count(16, 10177)
    assert certified == 0, certified
    assert bad == 48, bad
    print("E1 folded certificate toy checks passed: N=16 p=60161 -> 0, p=10177 -> 48")


if __name__ == "__main__":
    main()
