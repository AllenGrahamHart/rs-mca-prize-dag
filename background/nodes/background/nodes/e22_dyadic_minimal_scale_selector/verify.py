#!/usr/bin/env python3
"""Tiny check for the dyadic minimal-scale selector."""

from __future__ import annotations

from itertools import combinations


def fibers(n: int, m: int) -> list[frozenset[int]]:
    assert n % m == 0
    step = n // m
    return [frozenset(range(r, n, step)) for r in range(step)]


def recover_tail(n: int, m: int, support: set[int]) -> set[int]:
    full = [f for f in fibers(n, m) if f <= support]
    full_union = set().union(*full) if full else set()
    return set(support) - full_union


def admissible_moduli(n: int, t: int, support: set[int]) -> list[int]:
    out = []
    m = 1
    while m <= n:
        if m > t and len(recover_tail(n, m, support)) < m:
            out.append(m)
        m *= 2
    return out


def main() -> None:
    n = 16
    t = 2
    universe = range(n)

    checked = 0
    selected: dict[frozenset[int], int] = {}
    for r in range(n + 1):
        for combo in combinations(universe, r):
            support = set(combo)
            mods = admissible_moduli(n, t, support)
            if not mods:
                continue
            checked += 1
            assert mods == sorted(mods)
            assert mods[0] == min(mods)
            selected[frozenset(support)] = mods[0]

    assert checked
    assert len(selected) == checked
    sample = {0, 1, 4, 5, 8}
    mods = admissible_moduli(n, t, sample)
    assert mods[0] == min(mods)

    print(
        "e22 dyadic minimal-scale selector checks passed:",
        {"supports_with_selector": checked, "sample_moduli": mods},
    )


if __name__ == "__main__":
    main()
