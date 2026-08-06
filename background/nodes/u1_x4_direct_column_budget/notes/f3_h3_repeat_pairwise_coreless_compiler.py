#!/usr/bin/env python3
"""Pairwise-coreless obstruction compiler for h=3 repeat-boundary edges."""

from __future__ import annotations

from itertools import combinations

from f3_h3_repeat_coordinate_hitting_ledger import active_coordinate_edges_from_triples
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS, common_intersection
from f3_h3_repeat_star_obstruction_taxonomy import obstruction_kind
from f3_h3_repeat_support_forced_point_reduction import active_ordered_triples


def pairwise_intersecting(edges: tuple[frozenset[int], ...]) -> bool:
    return all(left & right for left, right in combinations(edges, 2))


def coreless_subtype(edges: tuple[frozenset[int], ...]) -> str:
    if not edges or common_intersection(list(edges)):
        return "star"
    if not pairwise_intersecting(edges):
        return "has_disjoint_pair"
    for triple in combinations(edges, 3):
        if not common_intersection(list(triple)):
            return "three_edge_coreless"
    if len(edges) != 4:
        raise AssertionError(("pairwise coreless family with no 3-core must have 4 edges", edges))
    universe = set().union(*edges)
    if len(universe) != 4:
        raise AssertionError(("tetrahedron universe should have four points", edges, universe))
    expected = {frozenset(universe - {point}) for point in universe}
    if set(edges) != expected:
        raise AssertionError(("four-edge coreless family is not tetrahedral", edges, expected))
    return "tetrahedron"


def check_models() -> None:
    three_edge = (
        frozenset((1, 2, 5)),
        frozenset((1, 3, 6)),
        frozenset((2, 3, 7)),
    )
    tetrahedron = (
        frozenset((2, 3, 4)),
        frozenset((1, 3, 4)),
        frozenset((1, 2, 4)),
        frozenset((1, 2, 3)),
    )
    if coreless_subtype(three_edge) != "three_edge_coreless":
        raise AssertionError("three-edge model misclassified")
    if coreless_subtype(tetrahedron) != "tetrahedron":
        raise AssertionError("tetrahedron model misclassified")


def row_summary(p: int, n: int) -> dict[str, int | str]:
    triples = active_ordered_triples(p, n)
    edges = tuple(active_coordinate_edges_from_triples(p, n, triples))
    kind = obstruction_kind(edges)
    subtype = coreless_subtype(edges)
    if kind == "star" and subtype != "star":
        raise AssertionError((p, n, kind, subtype))
    if kind == "disjoint_pair" and subtype != "has_disjoint_pair":
        raise AssertionError((p, n, kind, subtype))
    return {
        "b_line": len(triples),
        "active_edges": len(edges),
        "kind": kind,
        "subtype": subtype,
    }


def main() -> None:
    print("h=3 repeat pairwise-coreless compiler")
    check_models()
    print("pairwise-coreless obstruction = three_edge_coreless or tetrahedron")
    for p, n in WITNESS_ROWS:
        row = row_summary(p, n)
        if row["kind"] != "star":
            raise AssertionError((p, n, row))
        print(
            f"p={p} n={n} B_line={row['b_line']} active_edges={row['active_edges']} "
            f"kind={row['kind']} subtype={row['subtype']}"
        )
    for p, n in CONTRAST_ROWS:
        row = row_summary(p, n)
        if row["kind"] != "disjoint_pair":
            raise AssertionError((p, n, row))
        print(
            f"contrast p={p} n={n} B_line={row['b_line']} "
            f"active_edges={row['active_edges']} kind={row['kind']} subtype={row['subtype']}"
        )
    print("H3_REPEAT_PAIRWISE_CORELESS_COMPILER_PASS")


if __name__ == "__main__":
    main()
