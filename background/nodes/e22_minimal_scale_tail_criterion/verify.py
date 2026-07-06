#!/usr/bin/env python3
"""Tiny check for the E22 dyadic tail-minimality criterion."""

from __future__ import annotations

from itertools import combinations


def fibers(n: int, m: int) -> list[frozenset[int]]:
    assert n % m == 0
    step = n // m
    return [frozenset(range(r, n, step)) for r in range(step)]


def tail(n: int, m: int, support: set[int]) -> set[int]:
    full = [f for f in fibers(n, m) if f <= support]
    full_union = set().union(*full) if full else set()
    return set(support) - full_union


def dyadic_moduli(n: int, t: int) -> list[int]:
    out = []
    m = 1
    while m <= n:
        if m > t:
            out.append(m)
        m *= 2
    return out


def candidates(n: int, t: int, support: set[int]) -> list[int]:
    return [m for m in dyadic_moduli(n, t) if len(tail(n, m, support)) < m]


def criterion(n: int, t: int, support: set[int], m: int) -> bool:
    return len(tail(n, m, support)) < m and all(
        len(tail(n, mp, support)) >= mp
        for mp in dyadic_moduli(n, t)
        if mp < m
    )


def main() -> None:
    n = 16
    t = 2
    checked = 0
    for r in range(n + 1):
        for combo in combinations(range(n), r):
            support = set(combo)
            cand = candidates(n, t, support)
            if not cand:
                continue
            selected = min(cand)
            checked += 1
            for m in dyadic_moduli(n, t):
                assert criterion(n, t, support, m) == (m == selected)

    assert checked
    print("e22 minimal-scale tail criterion check passed:", {"supports": checked})


if __name__ == "__main__":
    main()
