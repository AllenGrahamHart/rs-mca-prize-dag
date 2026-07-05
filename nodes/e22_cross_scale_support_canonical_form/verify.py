#!/usr/bin/env python3
"""Tiny check for E22 cross-scale support canonicalization."""

from __future__ import annotations


def fibers(n: int, m: int) -> list[frozenset[int]]:
    # Model the cyclic domain by exponents mod n. The quotient x -> x^m has
    # fibers that are residue classes modulo n/m when m divides n.
    assert n % m == 0
    step = n // m
    return [frozenset(range(r, n, step)) for r in range(step)]


def recover(n: int, m: int, support: set[int]) -> tuple[set[int], list[frozenset[int]]]:
    full = [f for f in fibers(n, m) if f <= support]
    full_union = set().union(*full) if full else set()
    tail = set(support) - full_union
    return tail, full


def main() -> None:
    n = 24
    # A support with representations at multiple scales: full 4-fibers plus a
    # small tail; the canonical rule should recover each candidate scale from
    # the support alone. Larger tail-only candidate scales are allowed here and
    # are filtered by the pricing/nondegeneracy node.
    full_4 = fibers(n, 4)[1] | fibers(n, 4)[3]
    tail = {2, 4}
    support = set(full_4) | tail

    tail4, selected4 = recover(n, 4, support)
    assert tail4 == tail
    assert len(selected4) == 2
    assert len(tail4) < 4

    canonical = {
        m: (tuple(sorted(recover(n, m, support)[0])), len(recover(n, m, support)[1]))
        for m in (2, 3, 4, 6, 8, 12)
        if len(recover(n, m, support)[0]) < m
    }
    assert canonical[4][0] == tuple(sorted(tail))
    assert canonical == {
        m: (tuple(sorted(recover(n, m, set(support))[0])), len(recover(n, m, set(support))[1]))
        for m in (2, 3, 4, 6, 8, 12)
        if len(recover(n, m, set(support))[0]) < m
    }

    print("e22_cross_scale_support_canonical_form checks passed:", canonical)


if __name__ == "__main__":
    main()
