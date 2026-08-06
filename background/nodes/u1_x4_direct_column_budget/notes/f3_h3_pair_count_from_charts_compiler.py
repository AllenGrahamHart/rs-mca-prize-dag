#!/usr/bin/env python3
"""Verify the h=3 local chart-count to pair-count compiler."""

from __future__ import annotations

from collections import defaultdict
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
    return (x + y + z) % p, (x * y + x * z + y * z) % p


def q_value(t: int, p: int) -> int:
    return (t * t + t + 1) % p


def chart_point(
    p: int, a: int, u0: int, v0: int, t: int
) -> tuple[int, int, int] | None:
    q = q_value(t, p)
    if q == 0:
        return None
    a0 = (2 * u0 + v0 + a) % p
    b0 = (u0 + 2 * v0 + a) % p
    s = (-(a0 + b0 * t) * pow(q, -1, p)) % p
    u = (u0 + s) % p
    v = (v0 + t * s) % p
    w = (-a - u - v) % p
    return u, v, w


def vertical_point(p: int, a: int, u0: int, v0: int) -> tuple[int, int, int]:
    v_inf = (-a - u0 - v0) % p
    return u0 % p, v_inf, v0 % p


def ordered_fibers(p: int, n: int) -> dict[tuple[int, int], set[tuple[int, int, int]]]:
    vals = root_table(p, n)
    fibers: dict[tuple[int, int], set[tuple[int, int, int]]] = defaultdict(set)
    for exps in combinations(range(n), 3):
        values = tuple(vals[e] for e in exps)
        key = elementary_key(values, p)
        for ordered in permutations(values, 3):
            fibers[key].add(ordered)
    return fibers


def chart_count_for_fiber(
    p: int, hset: set[int], key: tuple[int, int], ordered: set[tuple[int, int, int]]
) -> tuple[int, int, int]:
    s1, s2 = key
    a = (-s1) % p
    b = s2
    if (a * a - 3 * b) % p == 0:
        return 0, 0, 1

    u0, v0, _ = min(ordered)
    chart = set()
    for t in range(p):
        point = chart_point(p, a, u0, v0, t)
        if point is not None and len(set(point)) == 3 and all(x in hset for x in point):
            chart.add(point)

    vertical = vertical_point(p, a, u0, v0)
    epsilon = int(
        len(set(vertical)) == 3 and all(x in hset for x in vertical) and vertical not in chart
    )
    if len(ordered) != len(chart) + epsilon:
        raise AssertionError((p, key, len(ordered), len(chart), epsilon))
    return len(chart), epsilon, 0


def verify_row(p: int, n: int, max_fibers: int = 32) -> dict[str, int]:
    hset = set(root_table(p, n))
    fibers = ordered_fibers(p, n)
    selected = sorted(
        ((len(ordered), key, ordered) for key, ordered in fibers.items()),
        reverse=True,
    )[:max_fibers]

    t_values: list[int] = []
    r_values: list[int] = []
    pair_total = 0
    skipped_degenerate = 0

    for _, key, ordered in selected:
        t_count, epsilon, skipped = chart_count_for_fiber(p, hset, key, ordered)
        skipped_degenerate += skipped
        if skipped:
            continue
        r_count = t_count + epsilon
        if r_count != len(ordered) or r_count % 6:
            raise AssertionError((p, n, key, t_count, epsilon, len(ordered)))
        n_triples = r_count // 6
        local_pairs = n_triples * (n_triples - 1) // 2
        formula_pairs = r_count * (r_count - 6) // 72
        if local_pairs != formula_pairs:
            raise AssertionError((p, n, key, local_pairs, formula_pairs))
        t_values.append(t_count)
        r_values.append(r_count)
        pair_total += local_pairs

    if not t_values:
        raise AssertionError((p, n, "no nondegenerate selected fibers"))

    z = len(t_values)
    total_t = sum(t_values)
    total_r = sum(r_values)
    max_t = max(t_values)
    max_r = max(r_values)
    exact_numer = max_r * total_r
    chart_numer = (max_t + 1) * (total_t + z)
    if 72 * pair_total > exact_numer or 72 * pair_total > chart_numer:
        raise AssertionError((p, n, pair_total, exact_numer, chart_numer))

    return {
        "fibers": z,
        "total_t": total_t,
        "total_r": total_r,
        "max_t": max_t,
        "max_r": max_r,
        "pairs": pair_total,
        "exact_bound": (exact_numer + 71) // 72,
        "chart_bound": (chart_numer + 71) // 72,
        "exact_numer": exact_numer,
        "chart_numer": chart_numer,
        "skipped_degenerate": skipped_degenerate,
    }


def main() -> None:
    rows = (
        (97, 16),
        (97, 32),
        (193, 64),
    )
    print("h=3 pair-count from charts compiler")
    for p, n in rows:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} fibers={row['fibers']} total_T={row['total_t']} "
            f"max_T={row['max_t']} pairs={row['pairs']} "
            f"exact_bound={row['exact_bound']} chart_bound={row['chart_bound']} "
            f"exact_numer={row['exact_numer']} chart_numer={row['chart_numer']} "
            f"skipped_degenerate={row['skipped_degenerate']}"
        )
    print("pair count requires total chart mass plus a max/level-set bound")
    print("H3_PAIR_COUNT_FROM_CHARTS_COMPILER_PASS")


if __name__ == "__main__":
    main()
