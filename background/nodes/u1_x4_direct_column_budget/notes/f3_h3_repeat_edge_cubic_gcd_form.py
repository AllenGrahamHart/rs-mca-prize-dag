#!/usr/bin/env python3
"""Cubic common-root form for h=3 repeat-boundary edges."""

from __future__ import annotations

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_coordinate_hitting_ledger import active_coordinate_edges_from_triples
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS, common_intersection
from f3_h3_repeat_support_forced_point_reduction import active_ordered_triples


def eval_cubic(t: int, lam: int, prod: int, p: int) -> int:
    return (
        pow(t, 3, p)
        - ((lam + 2) % p) * ((t * t) % p)
        + ((2 * lam + 1) % p) * t
        - prod
    ) % p


def edge_cubic_data(p: int, n: int) -> dict[frozenset[int], tuple[int, int]]:
    data: dict[frozenset[int], tuple[int, int]] = {}
    for u, v, w, lam in active_ordered_triples(p, n):
        edge = frozenset((u, v, w))
        prod = (u * v * w) % p
        item = (lam, prod)
        if edge in data and data[edge] != item:
            raise AssertionError((p, n, edge, data[edge], item))
        data[edge] = item
    return data


def verify_row(p: int, n: int) -> dict[str, int | str]:
    h = root_table(p, n)
    hset = set(h)
    triples = active_ordered_triples(p, n)
    edges = active_coordinate_edges_from_triples(p, n, triples)
    data = edge_cubic_data(p, n)
    if set(data) != set(edges):
        raise AssertionError((p, n, len(data), len(edges)))

    common_roots: set[int] | None = None
    for edge, (lam, prod) in data.items():
        roots = {t for t in hset if eval_cubic(t, lam, prod, p) == 0}
        if roots != set(edge):
            raise AssertionError((p, n, edge, lam, prod, roots))
        common_roots = roots if common_roots is None else common_roots & roots

    common = common_intersection(edges)
    if (common_roots or set()) != common:
        raise AssertionError((p, n, common_roots, common))
    return {
        "b_line": len(triples),
        "active_edges": len(edges),
        "common_roots": ",".join(str(a) for a in sorted(common)) if common else "-",
        "gcd_positive": int(bool(common)),
    }


def main() -> None:
    print("h=3 repeat edge cubic gcd form")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} B_line={row['b_line']} active_edges={row['active_edges']} "
            f"common_roots={row['common_roots']} gcd_positive={row['gcd_positive']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["gcd_positive"]:
            raise AssertionError((p, n, "contrast row should have no common root"))
        print(
            f"contrast p={p} n={n} B_line={row['b_line']} "
            f"active_edges={row['active_edges']} common_roots={row['common_roots']} "
            f"gcd_positive={row['gcd_positive']}"
        )
    print("Singleton hitting is common-root positivity for the active edge cubics")
    print("H3_REPEAT_EDGE_CUBIC_GCD_FORM_PASS")


if __name__ == "__main__":
    main()
