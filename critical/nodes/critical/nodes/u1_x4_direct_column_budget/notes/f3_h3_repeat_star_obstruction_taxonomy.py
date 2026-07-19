#!/usr/bin/env python3
"""Taxonomy for h=3 repeat-boundary star obstructions."""

from __future__ import annotations

from f3_h3_repeat_coordinate_hitting_ledger import active_coordinate_edges_from_triples
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS, common_intersection
from f3_h3_repeat_support_forced_point_reduction import active_ordered_triples


def obstruction_kind(edges: tuple[frozenset[int], ...]) -> str:
    if not edges or common_intersection(list(edges)):
        return "star"
    for i, left in enumerate(edges):
        for right in edges[i + 1 :]:
            if left.isdisjoint(right):
                return "disjoint_pair"
    return "pairwise_coreless"


def check_models() -> None:
    star = (
        frozenset((1, 2, 3)),
        frozenset((1, 4, 5)),
        frozenset((1, 6, 7)),
    )
    disjoint = (
        frozenset((1, 2, 3)),
        frozenset((4, 5, 6)),
    )
    pairwise_coreless = (
        frozenset((1, 2, 3)),
        frozenset((1, 4, 5)),
        frozenset((2, 4, 6)),
    )
    if obstruction_kind(star) != "star":
        raise AssertionError("star model misclassified")
    if obstruction_kind(disjoint) != "disjoint_pair":
        raise AssertionError("disjoint model misclassified")
    if obstruction_kind(pairwise_coreless) != "pairwise_coreless":
        raise AssertionError("pairwise-coreless model misclassified")


def row_kind(p: int, n: int) -> dict[str, int | str]:
    triples = active_ordered_triples(p, n)
    edges = tuple(active_coordinate_edges_from_triples(p, n, triples))
    return {
        "b_line": len(triples),
        "active_edges": len(edges),
        "kind": obstruction_kind(edges),
    }


def main() -> None:
    print("h=3 repeat star-obstruction taxonomy")
    check_models()
    print("non-star obstruction = disjoint_pair or pairwise_coreless")
    for p, n in WITNESS_ROWS:
        row = row_kind(p, n)
        if row["kind"] != "star":
            raise AssertionError((p, n, row))
        print(
            f"p={p} n={n} B_line={row['b_line']} "
            f"active_edges={row['active_edges']} kind={row['kind']}"
        )
    for p, n in CONTRAST_ROWS:
        row = row_kind(p, n)
        if row["kind"] == "star":
            raise AssertionError((p, n, row))
        print(
            f"contrast p={p} n={n} B_line={row['b_line']} "
            f"active_edges={row['active_edges']} kind={row['kind']}"
        )
    print("H3_REPEAT_STAR_OBSTRUCTION_TAXONOMY_PASS")


if __name__ == "__main__":
    main()
