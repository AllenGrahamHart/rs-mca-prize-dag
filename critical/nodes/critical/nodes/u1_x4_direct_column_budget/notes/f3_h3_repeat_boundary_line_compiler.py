#!/usr/bin/env python3
"""Verify the h=3 repeat-boundary line-pencil compiler."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations_with_replacement, product

from f3_h3_pair_count_from_charts_compiler import root_table


def signature(values: tuple[int, int, int], p: int) -> tuple[int, int]:
    return sum(values) % p, sum((x * x) % p for x in values) % p


def perm_count(multiset: tuple[int, int, int]) -> int:
    distinct = len(set(multiset))
    if distinct == 3:
        return 6
    if distinct == 2:
        return 3
    return 1


def boundary_ledger(p: int, n: int) -> dict[str, int]:
    vals = root_table(p, n)
    multiset_buckets: dict[tuple[int, int], list[tuple[tuple[int, int, int], int]]] = (
        defaultdict(list)
    )
    for idxs in combinations_with_replacement(range(n), 3):
        key = signature(tuple(vals[i] for i in idxs), p)
        multiset_buckets[key].append((idxs, perm_count(idxs)))

    d_boundary = 0
    z_repeat = 0
    for entries in multiset_buckets.values():
        d_sigma = 0
        r_sigma = 0
        for idxs, weight in entries:
            if len(set(idxs)) == 3:
                d_sigma += weight
            else:
                r_sigma += weight
        if r_sigma:
            d_boundary += d_sigma
            z_repeat += 1
    return {"d_boundary": d_boundary, "z_repeat": z_repeat}


def normalized_boundary_triples(p: int, n: int) -> dict[str, int]:
    h = root_table(p, n)
    hset = set(h)
    count = 0
    triple_cell = 0
    for u, v, w in product(h, repeat=3):
        if len({u, v, w}) != 3:
            continue
        lam = (u + v + w - 2) % p
        if lam not in hset:
            continue
        e2 = (u * v + u * w + v * w) % p
        if e2 != (1 + 2 * lam) % p:
            continue
        count += 1
        if lam == 1:
            triple_cell += 1
    return {"count": count, "triple_cell": triple_cell}


def pair_chart_count(p: int, n: int) -> dict[str, int]:
    h = root_table(p, n)
    hset = set(h)
    count = 0
    triple_cell = 0
    for u in h:
        if u == 1:
            continue
        for v in h:
            if v in (1, u):
                continue
            denom = (u + v - 2) % p
            if denom == 0:
                continue
            w = (1 - ((u - 1) * (v - 1) % p) * pow(denom, -1, p)) % p
            lam = (u + v + w - 2) % p
            if w not in hset or lam not in hset or len({u, v, w}) != 3:
                continue
            e2 = (u * v + u * w + v * w) % p
            if e2 != (1 + 2 * lam) % p:
                raise AssertionError((p, n, u, v, w, lam))
            count += 1
            if lam == 1:
                triple_cell += 1
    return {"count": count, "triple_cell": triple_cell}


def line_pencil_count(p: int, n: int) -> dict[str, int]:
    hset = set(root_table(p, n))
    count = 0
    triple_cell = 0
    support = Counter()
    for r in range(p):
        if r in (0, p - 1):
            continue
        inv_r1 = pow((r + 1) % p, -1, p)
        c3 = (-r * inv_r1) % p
        c4 = ((r * r + r + 1) * inv_r1) % p
        for t in range(1, p):
            v = (1 + t) % p
            u = (1 + r * t) % p
            w = (1 + c3 * t) % p
            lam = (1 + c4 * t) % p
            if v not in hset or u not in hset or w not in hset or lam not in hset:
                continue
            if len({u, v, w}) != 3:
                continue
            count += 1
            support[r] += 1
            if lam == 1:
                triple_cell += 1

    return {
        "count": count,
        "triple_cell": triple_cell,
        "r_support": len(support),
        "max_r_fiber": max(support.values(), default=0),
        "q0_count": sum(v for r, v in support.items() if (r * r + r + 1) % p == 0),
    }


def verify_coefficient_degeneracies(p: int) -> dict[str, int]:
    if p in (2, 3):
        raise AssertionError("characteristic 2 or 3 is excluded")
    inv2 = pow(2, -1, p)
    expected_bad = {0, p - 1, 1, (-inv2) % p, (-2) % p}
    observed_bad: set[int] = set()
    q0 = 0
    for r in range(p):
        if r == p - 1:
            observed_bad.add(r)
            continue
        inv_r1 = pow((r + 1) % p, -1, p)
        coeffs = (1, r, (-r * inv_r1) % p)
        if len(set(coeffs)) != 3:
            observed_bad.add(r)
        if (r * r + r + 1) % p == 0:
            q0 += 1
    if observed_bad != expected_bad:
        raise AssertionError((p, observed_bad, expected_bad))
    return {"bad_coefficients": len(observed_bad), "q0_roots": q0}


def verify_row(p: int, n: int) -> dict[str, int]:
    ledger = boundary_ledger(p, n)
    triples = normalized_boundary_triples(p, n)
    pairs = pair_chart_count(p, n)
    lines = line_pencil_count(p, n)
    if triples != pairs:
        raise AssertionError((p, n, triples, pairs))
    for key in ("count", "triple_cell"):
        if triples[key] != lines[key]:
            raise AssertionError((p, n, key, triples, lines))
    if ledger["d_boundary"] > n * lines["count"]:
        raise AssertionError((p, n, ledger, lines))
    if ledger["z_repeat"] > n * n:
        raise AssertionError((p, n, ledger))
    return {
        **ledger,
        "b_line": lines["count"],
        "triple_cell": lines["triple_cell"],
        "r_support": lines["r_support"],
        "max_r_fiber": lines["max_r_fiber"],
        "q0_count": lines["q0_count"],
        "d_bound": n * lines["count"],
        "z_bound": n * n,
    }


def main() -> None:
    print("h=3 repeat-boundary line-pencil compiler")
    for p in (17, 97):
        row = verify_coefficient_degeneracies(p)
        print(
            f"p={p} bad_coefficients={row['bad_coefficients']} "
            f"q0_roots={row['q0_roots']}"
        )
    for p, n in ((97, 16), (97, 32), (193, 64)):
        row = verify_row(p, n)
        print(
            f"p={p} n={n} D_boundary={row['d_boundary']} "
            f"nB_line={row['d_bound']} B_line={row['b_line']} "
            f"Z_repeat={row['z_repeat']} n^2={row['z_bound']} "
            f"triple_cell={row['triple_cell']} r_support={row['r_support']} "
            f"max_r_fiber={row['max_r_fiber']} q0_count={row['q0_count']}"
        )
    print("D_boundary <= n*B_line and Z_repeat <= n^2")
    print("H3_REPEAT_BOUNDARY_LINE_COMPILER_PASS")


if __name__ == "__main__":
    main()
