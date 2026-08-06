#!/usr/bin/env python3
"""Pattern compiler for pairwise-coreless h=3 repeat-boundary obstructions."""

from __future__ import annotations

from itertools import combinations

from f3_h3_repeat_coordinate_hitting_ledger import active_coordinate_edges_from_triples
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_pairwise_coreless_compiler import (
    coreless_subtype,
    pairwise_intersecting,
)
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS, common_intersection
from f3_h3_repeat_star_obstruction_taxonomy import obstruction_kind
from f3_h3_repeat_support_forced_point_reduction import active_ordered_triples


def three_edge_pattern(edges: tuple[frozenset[int], frozenset[int], frozenset[int]]) -> str:
    if not pairwise_intersecting(edges):
        return "has_disjoint_pair"
    if common_intersection(list(edges)):
        return "star"
    sizes = sorted(
        (
            len(edges[0] & edges[1]),
            len(edges[0] & edges[2]),
            len(edges[1] & edges[2]),
        )
    )
    if sizes == [1, 1, 1]:
        return "loose_triangle"
    if sizes == [1, 1, 2]:
        return "pinched_triangle"
    raise AssertionError(("unexpected 3-edge coreless pattern", edges, sizes))


def coreless_pattern(edges: tuple[frozenset[int], ...]) -> str:
    subtype = coreless_subtype(edges)
    if subtype != "three_edge_coreless":
        return subtype
    for triple in combinations(edges, 3):
        pattern = three_edge_pattern(triple)  # type: ignore[arg-type]
        if pattern in ("loose_triangle", "pinched_triangle"):
            return pattern
    raise AssertionError(("three-edge coreless subtype without triangle pattern", edges))


def check_models() -> None:
    loose = (
        frozenset((1, 2, 7)),
        frozenset((1, 3, 8)),
        frozenset((2, 3, 9)),
    )
    pinched = (
        frozenset((1, 2, 3)),
        frozenset((1, 2, 4)),
        frozenset((3, 4, 5)),
    )
    tetrahedron = (
        frozenset((2, 3, 4)),
        frozenset((1, 3, 4)),
        frozenset((1, 2, 4)),
        frozenset((1, 2, 3)),
    )
    if coreless_pattern(loose) != "loose_triangle":
        raise AssertionError("loose triangle model misclassified")
    if coreless_pattern(pinched) != "pinched_triangle":
        raise AssertionError("pinched triangle model misclassified")
    if coreless_pattern(tetrahedron) != "tetrahedron":
        raise AssertionError("tetrahedron model misclassified")


def row_summary(p: int, n: int) -> dict[str, int | str]:
    triples = active_ordered_triples(p, n)
    edges = tuple(active_coordinate_edges_from_triples(p, n, triples))
    return {
        "b_line": len(triples),
        "active_edges": len(edges),
        "kind": obstruction_kind(edges),
        "pattern": coreless_pattern(edges),
    }


def main() -> None:
    print("h=3 repeat coreless-pattern compiler")
    check_models()
    print("three-edge coreless = loose_triangle or pinched_triangle")
    print("four-edge no-three-core case = tetrahedron")
    for p, n in WITNESS_ROWS:
        row = row_summary(p, n)
        if row["kind"] != "star":
            raise AssertionError((p, n, row))
        print(
            f"p={p} n={n} B_line={row['b_line']} active_edges={row['active_edges']} "
            f"kind={row['kind']} pattern={row['pattern']}"
        )
    for p, n in CONTRAST_ROWS:
        row = row_summary(p, n)
        if row["kind"] != "disjoint_pair":
            raise AssertionError((p, n, row))
        print(
            f"contrast p={p} n={n} B_line={row['b_line']} "
            f"active_edges={row['active_edges']} kind={row['kind']} "
            f"pattern={row['pattern']}"
        )
    print("H3_REPEAT_CORELESS_PATTERN_COMPILER_PASS")


if __name__ == "__main__":
    main()
