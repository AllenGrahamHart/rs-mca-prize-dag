#!/usr/bin/env python3
"""Verify the h=3 dilation lift bound on small finite subgroup rows."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations


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


def signatures(exps: tuple[int, int, int], vals: list[int], p: int) -> tuple[int, int, int]:
    x, y, z = (vals[e] for e in exps)
    e1 = (x + y + z) % p
    e2 = (x * y + x * z + y * z) % p
    e3 = (x * y * z) % p
    return e1, e2, e3


def side_normal(pair: tuple[tuple[int, ...], tuple[int, ...]]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    a, b = pair
    return (a, b) if a <= b else (b, a)


def shift_side(side: tuple[int, ...], shift: int, n: int) -> tuple[int, ...]:
    return tuple(sorted((x + shift) % n for x in side))


def shift_pair(
    pair: tuple[tuple[int, ...], tuple[int, ...]], shift: int, n: int
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return side_normal((shift_side(pair[0], shift, n), shift_side(pair[1], shift, n)))


def orbit(pair: tuple[tuple[int, ...], tuple[int, ...]], n: int) -> set[tuple[tuple[int, ...], tuple[int, ...]]]:
    return {shift_pair(pair, shift, n) for shift in range(n)}


def canonical(pair: tuple[tuple[int, ...], tuple[int, ...]], n: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return min(orbit(pair, n))


def activated_pairs(p: int, n: int) -> set[tuple[tuple[int, ...], tuple[int, ...]]]:
    vals = root_table(p, n)
    buckets: dict[tuple[int, int], list[tuple[tuple[int, ...], int]]] = defaultdict(list)
    for exps in combinations(range(n), 3):
        e1, e2, e3 = signatures(exps, vals, p)
        buckets[(e1, e2)].append((exps, e3))

    out: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    for triples in buckets.values():
        if len(triples) < 2:
            continue
        for i, (left, left_e3) in enumerate(triples):
            left_set = set(left)
            for right, right_e3 in triples[i + 1 :]:
                if left_e3 == right_e3 or left_set.intersection(right):
                    continue
                out.add(side_normal((left, right)))
    return out


def verify_row(p: int, n: int) -> dict[str, int]:
    raw = activated_pairs(p, n)
    orbit_buckets: dict[tuple[tuple[int, ...], tuple[int, ...]], set[tuple[tuple[int, ...], tuple[int, ...]]]] = {}
    for pair in raw:
        key = canonical(pair, n)
        orbit_buckets.setdefault(key, set()).add(pair)

    orbit_sizes = [len(bucket) for bucket in orbit_buckets.values()]
    if any(size > n for size in orbit_sizes):
        raise AssertionError((p, n, max(orbit_sizes), n))
    if len(raw) > n * len(orbit_buckets):
        raise AssertionError((p, n, len(raw), len(orbit_buckets), n))

    stabilizer_hist: Counter[int] = Counter()
    for key in orbit_buckets:
        full_orbit = orbit(key, n)
        stabilizer = n // len(full_orbit)
        stabilizer_hist[stabilizer] += 1
        if not orbit_buckets[key].issubset(full_orbit):
            raise AssertionError((p, n, key))

    return {
        "raw": len(raw),
        "normalized": len(orbit_buckets),
        "max_orbit": max(orbit_sizes, default=0),
        "slack": n * len(orbit_buckets) - len(raw),
        "nontrivial_stabilizer_orbits": sum(
            count for stabilizer, count in stabilizer_hist.items() if stabilizer > 1
        ),
    }


def main() -> None:
    rows = (
        (97, 16),
        (97, 32),
        (193, 64),
    )
    print("h=3 dilation lift bound")
    for p, n in rows:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} raw={row['raw']} normalized={row['normalized']} "
            f"n*normalized={n * row['normalized']} max_orbit={row['max_orbit']} "
            f"slack={row['slack']} nontrivial_stabilizer_orbits={row['nontrivial_stabilizer_orbits']}"
        )
    print("dilation-normalized orbits lift to at most n raw shape pairs")
    print("H3_DILATION_LIFT_BOUND_PASS")


if __name__ == "__main__":
    main()
