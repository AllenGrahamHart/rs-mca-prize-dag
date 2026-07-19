#!/usr/bin/env python3
"""Verify the h=3 local fiber-count bridge on finite subgroup rows."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations


def prime_factors(n: int) -> list[int]:
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
    factors = prime_factors(p - 1)
    g = 2
    while any(pow(g, (p - 1) // r, p) == 1 for r in factors):
        g += 1
    return g


def root_table(p: int, n: int) -> list[int]:
    z = pow(primitive_root(p), (p - 1) // n, p)
    if pow(z, n, p) != 1 or pow(z, n // 2, p) == 1:
        raise AssertionError((p, n, z))
    return [pow(z, i, p) for i in range(n)]


def elementary_key(values: tuple[int, int, int], p: int) -> tuple[int, int]:
    x, y, z = values
    s1 = (x + y + z) % p
    s2 = (x * y + x * z + y * z) % p
    return s1, s2


def conic_value(u: int, v: int, s1: int, s2: int, p: int) -> int:
    a = (-s1) % p
    b = s2
    return (u * u + u * v + v * v + a * (u + v) + b) % p


def verify_row(p: int, n: int) -> dict[str, int]:
    vals = root_table(p, n)
    triple_counts: Counter[tuple[int, int]] = Counter()
    for exps in combinations(range(n), 3):
        triple_counts[elementary_key(tuple(vals[i] for i in exps), p)] += 1

    ordered_counts: Counter[tuple[int, int]] = Counter()
    for exps in permutations(range(n), 3):
        ordered = tuple(vals[i] for i in exps)
        key = elementary_key(ordered, p)
        s1, s2 = key
        u, v, w = ordered
        if len({u, v, w}) != 3:
            raise AssertionError(("permutation repeated value", p, n, exps))
        if conic_value(u, v, s1, s2, p) != 0:
            raise AssertionError(("ordered triple not on conic", p, n, exps, key))
        if w != (s1 - u - v) % p:
            raise AssertionError(("bad third coordinate", p, n, exps, key))
        ordered_counts[key] += 1

    if set(triple_counts) != set(ordered_counts):
        raise AssertionError(("key mismatch", p, n))

    active_local_pairs = 0
    max_triples = 0
    max_ordered = 0
    rich_keys = 0
    for key, count in triple_counts.items():
        ordered = ordered_counts[key]
        if ordered != 6 * count:
            raise AssertionError(("factor-six failure", p, n, key, count, ordered))
        local_pairs = count * (count - 1) // 2
        ordered_formula = ordered * (ordered - 6) // 72
        if local_pairs != ordered_formula:
            raise AssertionError(("pair formula failure", p, n, key, local_pairs, ordered_formula))
        active_local_pairs += local_pairs
        max_triples = max(max_triples, count)
        max_ordered = max(max_ordered, ordered)
        rich_keys += int(count >= 2)

    return {
        "keys": len(triple_counts),
        "triples": sum(triple_counts.values()),
        "ordered": sum(ordered_counts.values()),
        "rich_keys": rich_keys,
        "local_pairs": active_local_pairs,
        "max_triples": max_triples,
        "max_ordered": max_ordered,
    }


def main() -> None:
    rows = (
        (97, 16),
        (97, 32),
        (193, 64),
    )
    print("h=3 local fiber-count bridge")
    for p, n in rows:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} keys={row['keys']} triples={row['triples']} "
            f"ordered={row['ordered']} rich_keys={row['rich_keys']} "
            f"local_pairs={row['local_pairs']} max_triples={row['max_triples']} "
            f"max_ordered={row['max_ordered']}"
        )
    print("factor-six and local pair formulas verified")
    print("H3_LOCAL_FIBER_COUNT_BRIDGE_PASS")


if __name__ == "__main__":
    main()
