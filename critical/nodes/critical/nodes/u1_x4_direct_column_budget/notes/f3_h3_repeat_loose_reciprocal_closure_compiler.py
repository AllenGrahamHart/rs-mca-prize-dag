#!/usr/bin/env python3
"""Reciprocal-closure compiler for h=3 repeat-boundary loose triangles."""

from __future__ import annotations

from itertools import combinations

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_coordinate_hitting_ledger import active_coordinate_edges_from_triples
from f3_h3_repeat_edge_cubic_gcd_form import edge_cubic_data
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_loose_triangle_shadow_compiler import shadow_triangle_counts
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS
from f3_h3_repeat_support_forced_point_reduction import active_ordered_triples


def reciprocal_coordinate(u: int, p: int) -> int:
    shifted = (u - 1) % p
    if shifted == 0:
        raise AssertionError((p, "coordinate 1 has no reciprocal chart"))
    return pow(shifted, -1, p)


def coordinate_from_reciprocal(r: int, p: int) -> int:
    if r == 0:
        raise AssertionError((p, "zero reciprocal coordinate"))
    return (1 + pow(r, -1, p)) % p


def reciprocal_image(p: int, n: int) -> dict[int, int]:
    image: dict[int, int] = {}
    for u in root_table(p, n):
        if u == 1:
            continue
        r = reciprocal_coordinate(u, p)
        if r in image:
            raise AssertionError((p, n, "reciprocal chart is not injective", r, image[r], u))
        image[r] = u
    return image


def third_reciprocal(r: int, s: int, p: int) -> int:
    total = (r + s) % p
    if total == 0:
        raise AssertionError((p, "vertical reciprocal pair", r, s))
    return (-total) % p


def lambda_from_reciprocal_pair(r: int, s: int, p: int) -> int:
    total = (r + s) % p
    if total == 0:
        raise AssertionError((p, "vertical reciprocal pair", r, s))
    return (1 + pow(r, -1, p) + pow(s, -1, p) - pow(total, -1, p)) % p


def reciprocal_pair_map(p: int, n: int) -> dict[tuple[int, int], tuple[int, int]]:
    image = reciprocal_image(p, n)
    recs = sorted(image)
    hset = set(root_table(p, n))
    pairs: dict[tuple[int, int], tuple[int, int]] = {}
    for r, s in combinations(recs, 2):
        total = (r + s) % p
        if total == 0:
            continue
        t = third_reciprocal(r, s, p)
        if t not in image or t in (r, s):
            continue
        lam = lambda_from_reciprocal_pair(r, s, p)
        if lam in hset:
            pairs[(r, s)] = (t, lam)
    return pairs


def active_pair_map_from_edges(p: int, n: int) -> dict[tuple[int, int], tuple[int, int]]:
    data = edge_cubic_data(p, n)
    triples = active_ordered_triples(p, n)
    edges = active_coordinate_edges_from_triples(p, n, triples)
    pairs: dict[tuple[int, int], tuple[int, int]] = {}
    for edge in edges:
        rec_edge = {reciprocal_coordinate(u, p) for u in edge}
        if sum(rec_edge) % p != 0:
            raise AssertionError((p, n, edge, "reciprocal edge is not zero-sum"))
        lam, _ = data[edge]
        for r, s in combinations(sorted(rec_edge), 2):
            t_set = rec_edge - {r, s}
            if len(t_set) != 1:
                raise AssertionError((p, n, edge, rec_edge))
            t = next(iter(t_set))
            pairs[(r, s)] = (t, lam)
    return pairs


def reciprocal_triangle_counts(
    pairs: dict[tuple[int, int], tuple[int, int]], p: int
) -> dict[str, int]:
    vertices = sorted({point for pair in pairs for point in pair})
    contained = 0
    loose = 0
    for a, b, c in combinations(vertices, 3):
        if (a, b) not in pairs or (a, c) not in pairs or (b, c) not in pairs:
            continue
        if (a + b + c) % p == 0:
            contained += 1
        else:
            loose += 1
    return {
        "shadow_edges": len(pairs),
        "contained_triangles": contained,
        "loose_triangles": loose,
    }


def check_models() -> None:
    p = 101
    contained_pairs = {
        (2, 3): (96, 7),
        (2, 96): (3, 7),
        (3, 96): (2, 7),
    }
    loose_pairs = {
        (2, 3): (96, 7),
        (2, 5): (94, 11),
        (3, 5): (93, 13),
    }
    if reciprocal_triangle_counts(contained_pairs, p)["contained_triangles"] != 1:
        raise AssertionError("zero-sum reciprocal triangle should be contained")
    row = reciprocal_triangle_counts(loose_pairs, p)
    if row["loose_triangles"] != 1 or row["contained_triangles"] != 0:
        raise AssertionError(("non-zero-sum reciprocal triangle should be loose", row))


def verify_row(p: int, n: int) -> dict[str, int]:
    triples = active_ordered_triples(p, n)
    edges = active_coordinate_edges_from_triples(p, n, triples)
    pair_from_reciprocal = reciprocal_pair_map(p, n)
    pair_from_edges = active_pair_map_from_edges(p, n)
    if pair_from_reciprocal != pair_from_edges:
        raise AssertionError(
            (
                p,
                n,
                "reciprocal active pairs differ from coordinate active pairs",
                len(pair_from_reciprocal),
                len(pair_from_edges),
            )
        )
    rec_counts = reciprocal_triangle_counts(pair_from_reciprocal, p)
    shadow_counts = shadow_triangle_counts(edges, p, validate_active=True)
    if rec_counts != shadow_counts:
        raise AssertionError((p, n, rec_counts, shadow_counts))
    return {
        "b_line": len(triples),
        "active_edges": len(edges),
        **rec_counts,
    }


def main() -> None:
    print("h=3 repeat loose reciprocal-closure compiler")
    check_models()
    print("active pair {r,s} has third reciprocal -(r+s)")
    print("shadow triangle is contained iff r+s+t=0")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} B_line={row['b_line']} active_edges={row['active_edges']} "
            f"active_pairs={row['shadow_edges']} contained_triangles={row['contained_triangles']} "
            f"loose_triangles={row['loose_triangles']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["loose_triangles"] == 0:
            raise AssertionError((p, n, "contrast row should have a loose closure violation"))
        print(
            f"contrast p={p} n={n} B_line={row['b_line']} "
            f"active_edges={row['active_edges']} active_pairs={row['shadow_edges']} "
            f"contained_triangles={row['contained_triangles']} "
            f"loose_triangles={row['loose_triangles']}"
        )
    print("H3-NO-LOOSE-TRIANGLE is reciprocal pair-closure to zero-sum")
    print("H3_REPEAT_LOOSE_RECIPROCAL_CLOSURE_COMPILER_PASS")


if __name__ == "__main__":
    main()
