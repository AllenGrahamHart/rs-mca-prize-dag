#!/usr/bin/env python3
"""Forced-coordinate 2 normal form for h=3 repeat-boundary support."""

from __future__ import annotations

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_coordinate_hitting_ledger import active_coordinate_edges_from_triples
from f3_h3_repeat_support_forced_point_reduction import (
    active_ordered_triples,
    fixed_first_count,
)


ROWS = (
    (257, 16),
    (1153, 32),
    (4289, 64),
    (17921, 128),
    (65537, 256),
    (262657, 512),
    (1051649, 1024),
)


def trace_two_count(p: int, n: int) -> tuple[int, int]:
    h = root_table(p, n)
    hset = set(h)
    two = 2 % p
    if two not in hset:
        return 0, 0

    count = 0
    edges: set[frozenset[int]] = set()
    for v in h:
        w = pow(v, -1, p)
        lam = (v + w) % p
        if lam in hset and len({two, v, w}) == 3:
            count += 1
            edges.add(frozenset((two, v, w)))
    if count != 2 * len(edges):
        raise AssertionError((p, n, count, len(edges)))
    return count, len(edges)


def verify_row(p: int, n: int) -> dict[str, int]:
    hset = set(root_table(p, n))
    two = 2 % p
    triples = active_ordered_triples(p, n)
    edges = active_coordinate_edges_from_triples(p, n, triples)
    first_two = [triple for triple in triples if triple[0] == two]
    for _, v, w, lam in first_two:
        inv_v = pow(v, -1, p)
        if w != inv_v or lam != (v + inv_v) % p:
            raise AssertionError((p, n, v, w, lam, inv_v))

    trace_count, trace_edges = trace_two_count(p, n)
    if two in hset:
        fixed_count = fixed_first_count(p, n, two)
        if fixed_count != trace_count or fixed_count != len(first_two):
            raise AssertionError((p, n, fixed_count, trace_count, len(first_two)))
    elif trace_count or first_two:
        raise AssertionError((p, n, "2 not in H but trace/first-two is nonzero"))

    hit_two_edges = sum(1 for edge in edges if two in edge)
    if hit_two_edges != trace_edges:
        raise AssertionError((p, n, hit_two_edges, trace_edges))
    return {
        "b_line": len(triples),
        "active_edges": len(edges),
        "first_two": len(first_two),
        "trace_edges": trace_edges,
        "all_edges_hit_by_two": int(bool(edges) and hit_two_edges == len(edges)),
    }


def main() -> None:
    print("h=3 repeat forced-coordinate-2 normal form")
    for p, n in ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} B_line={row['b_line']} active_edges={row['active_edges']} "
            f"N_2={row['first_two']} trace_edges={row['trace_edges']} "
            f"all_edges_hit_by_two={row['all_edges_hit_by_two']}"
        )
    print("For first coordinate 2: w(v)=v^{-1} and lambda(v)=v+v^{-1}")
    print("H3_REPEAT_FORCED_TWO_NORMAL_FORM_PASS")


if __name__ == "__main__":
    main()
