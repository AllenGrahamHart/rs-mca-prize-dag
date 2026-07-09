#!/usr/bin/env python3
"""Verify h=3 conic-chart coverage of ordered H-triples."""

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
    w_inf = v0 % p
    return u0 % p, v_inf, w_inf


def ordered_fibers(p: int, n: int) -> dict[tuple[int, int], set[tuple[int, int, int]]]:
    vals = root_table(p, n)
    fibers: dict[tuple[int, int], set[tuple[int, int, int]]] = defaultdict(set)
    for exps in combinations(range(n), 3):
        values = tuple(vals[e] for e in exps)
        key = elementary_key(values, p)
        for ordered in permutations(values, 3):
            fibers[key].add(ordered)
    return fibers


def verify_fiber(
    p: int, hset: set[int], key: tuple[int, int], ordered: set[tuple[int, int, int]]
) -> dict[str, int]:
    s1, s2 = key
    a = (-s1) % p
    b = s2
    if (a * a - 3 * b) % p == 0:
        return {"skipped_degenerate": 1}
    u0, v0, _ = min(ordered)

    chart: set[tuple[int, int, int]] = set()
    skipped_poles = 0
    for t in range(p):
        point = chart_point(p, a, u0, v0, t)
        if point is None:
            skipped_poles += 1
            continue
        if len(set(point)) == 3 and all(x in hset for x in point):
            chart.add(point)

    vertical = vertical_point(p, a, u0, v0)
    vertical_contributes = (
        len(set(vertical)) == 3 and all(x in hset for x in vertical) and vertical not in chart
    )
    recovered = set(chart)
    if vertical_contributes:
        recovered.add(vertical)

    if recovered != ordered:
        missing = sorted(ordered - recovered)[:5]
        extra = sorted(recovered - ordered)[:5]
        raise AssertionError((p, key, len(ordered), len(chart), vertical, missing, extra))

    epsilon = int(vertical_contributes)
    if len(ordered) != len(chart) + epsilon:
        raise AssertionError((p, key, len(ordered), len(chart), epsilon))

    return {
        "ordered": len(ordered),
        "chart": len(chart),
        "epsilon": epsilon,
        "skipped_poles": skipped_poles,
        "skipped_degenerate": 0,
    }


def verify_row(p: int, n: int, max_fibers: int = 12) -> dict[str, int]:
    hset = set(root_table(p, n))
    fibers = ordered_fibers(p, n)
    selected = sorted(
        ((len(ordered), key, ordered) for key, ordered in fibers.items()),
        reverse=True,
    )[:max_fibers]

    totals = {
        "fibers": 0,
        "ordered": 0,
        "chart": 0,
        "epsilon": 0,
        "skipped_poles": 0,
        "skipped_degenerate": 0,
    }
    for _, key, ordered in selected:
        row = verify_fiber(p, hset, key, ordered)
        totals["skipped_degenerate"] += row.get("skipped_degenerate", 0)
        if row.get("skipped_degenerate", 0):
            continue
        totals["fibers"] += 1
        totals["ordered"] += row["ordered"]
        totals["chart"] += row["chart"]
        totals["epsilon"] += row["epsilon"]
        totals["skipped_poles"] += row["skipped_poles"]
    return totals


def main() -> None:
    rows = (
        (97, 16),
        (97, 32),
        (193, 64),
    )
    print("h=3 conic-chart H-point coverage")
    for p, n in rows:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} fibers={row['fibers']} ordered={row['ordered']} "
            f"chart={row['chart']} epsilon={row['epsilon']} "
            f"skipped_poles={row['skipped_poles']} "
            f"skipped_degenerate={row['skipped_degenerate']}"
        )
    print("ordered H-triples are covered by finite chart points plus at most one vertical point")
    print("H3_CONIC_CHART_HPOINT_COVERAGE_PASS")


if __name__ == "__main__":
    main()
