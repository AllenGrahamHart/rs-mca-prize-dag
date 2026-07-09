#!/usr/bin/env python3
"""Pair-membership compiler for h=3 repeat-boundary loose triangles."""

from __future__ import annotations

from itertools import combinations

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_loose_reciprocal_closure_compiler import (
    coordinate_from_reciprocal,
    lambda_from_reciprocal_pair,
    reciprocal_image,
    reciprocal_pair_map,
    reciprocal_triangle_counts,
    third_reciprocal,
)
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS


def pair_membership_values(r: int, s: int, p: int) -> tuple[int, int, int, int] | None:
    total = (r + s) % p
    if r == 0 or s == 0 or total == 0:
        return None
    u = coordinate_from_reciprocal(r, p)
    v = coordinate_from_reciprocal(s, p)
    w = coordinate_from_reciprocal((-total) % p, p)
    lam = lambda_from_reciprocal_pair(r, s, p)
    return (u, v, w, lam)


def membership_pair_map(p: int, n: int) -> tuple[dict[tuple[int, int], tuple[int, int]], dict[str, int]]:
    hset = set(root_table(p, n))
    image = reciprocal_image(p, n)
    pairs: dict[tuple[int, int], tuple[int, int]] = {}
    stats = {
        "candidate_pairs": 0,
        "vertical_pairs": 0,
        "third_not_in_s": 0,
        "repeated_third": 0,
        "lambda_not_in_h": 0,
        "active_pairs": 0,
    }
    for r, s in combinations(sorted(image), 2):
        stats["candidate_pairs"] += 1
        values = pair_membership_values(r, s, p)
        if values is None:
            stats["vertical_pairs"] += 1
            continue
        u, v, w, lam = values
        t = third_reciprocal(r, s, p)
        if t not in image:
            stats["third_not_in_s"] += 1
            continue
        if t in (r, s) or len({u, v, w}) != 3:
            stats["repeated_third"] += 1
            continue
        if lam not in hset:
            stats["lambda_not_in_h"] += 1
            continue
        pairs[(r, s)] = (t, lam)
        stats["active_pairs"] += 1
    return pairs, stats


def verify_row(p: int, n: int) -> dict[str, int]:
    pairs, stats = membership_pair_map(p, n)
    existing = reciprocal_pair_map(p, n)
    if pairs != existing:
        raise AssertionError((p, n, len(pairs), len(existing)))
    tri = reciprocal_triangle_counts(pairs, p)
    return {**stats, **tri}


def main() -> None:
    print("h=3 repeat loose pair-membership compiler")
    print("active pair iff W(r,s), Lambda(r,s) are in H")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} candidate_pairs={row['candidate_pairs']} "
            f"active_pairs={row['active_pairs']} third_not_in_S={row['third_not_in_s']} "
            f"lambda_not_in_H={row['lambda_not_in_h']} "
            f"contained_triangles={row['contained_triangles']} "
            f"loose_triangles={row['loose_triangles']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        if row["loose_triangles"] == 0:
            raise AssertionError((p, n, "contrast row should have loose triangles"))
        print(
            f"contrast p={p} n={n} candidate_pairs={row['candidate_pairs']} "
            f"active_pairs={row['active_pairs']} third_not_in_S={row['third_not_in_s']} "
            f"lambda_not_in_H={row['lambda_not_in_h']} "
            f"contained_triangles={row['contained_triangles']} "
            f"loose_triangles={row['loose_triangles']}"
        )
    print("H3-NO-LOOSE-TRIANGLE is a four-membership pair-graph triangle theorem")
    print("H3_REPEAT_LOOSE_PAIR_MEMBERSHIP_COMPILER_PASS")


if __name__ == "__main__":
    main()
