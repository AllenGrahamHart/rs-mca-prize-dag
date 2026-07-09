#!/usr/bin/env python3
"""Shadow-graph compiler for h=3 repeat-boundary loose triangles."""

from __future__ import annotations

from itertools import combinations

from f3_h3_repeat_coordinate_hitting_ledger import active_coordinate_edges_from_triples
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_linear_hypergraph_compiler import verify_linearity
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS, common_intersection
from f3_h3_repeat_support_forced_point_reduction import active_ordered_triples


def pair_owner_map(
    edges: list[frozenset[int]], p: int, *, validate_active: bool
) -> dict[tuple[int, int], frozenset[int]]:
    if validate_active:
        verify_linearity(edges, p)
    owners: dict[tuple[int, int], frozenset[int]] = {}
    for edge in edges:
        for pair in combinations(sorted(edge), 2):
            if pair in owners and owners[pair] != edge:
                raise AssertionError((p, pair, owners[pair], edge))
            owners[pair] = edge
    return owners


def shadow_triangle_counts(
    edges: list[frozenset[int]], p: int, *, validate_active: bool
) -> dict[str, int]:
    owners = pair_owner_map(edges, p, validate_active=validate_active)
    vertices = sorted({point for pair in owners for point in pair})
    contained = 0
    loose = 0
    for a, b, c in combinations(vertices, 3):
        pairs = ((a, b), (a, c), (b, c))
        if not all(pair in owners for pair in pairs):
            continue
        owner_set = {owners[pair] for pair in pairs}
        if len(owner_set) == 1:
            contained += 1
            continue
        if len(owner_set) != 3:
            raise AssertionError(("linearity should prevent two-owner shadow triangle", pairs, owner_set))
        if common_intersection(list(owner_set)):
            raise AssertionError(("three-owner shadow triangle should be coreless", pairs, owner_set))
        loose += 1
    return {
        "shadow_edges": len(owners),
        "contained_triangles": contained,
        "loose_triangles": loose,
    }


def check_models() -> None:
    single_edge = [frozenset((1, 2, 3))]
    loose = [
        frozenset((1, 2, 7)),
        frozenset((1, 3, 8)),
        frozenset((2, 3, 9)),
    ]
    if shadow_triangle_counts(single_edge, 101, validate_active=False)["contained_triangles"] != 1:
        raise AssertionError("single active edge should give one contained triangle")
    row = shadow_triangle_counts(loose, 101, validate_active=False)
    if row["loose_triangles"] != 1 or row["contained_triangles"] != 3:
        raise AssertionError(("loose model miscounted", row))


def verify_row(p: int, n: int) -> dict[str, int]:
    triples = active_ordered_triples(p, n)
    edges = active_coordinate_edges_from_triples(p, n, triples)
    return {
        "b_line": len(triples),
        "active_edges": len(edges),
        **shadow_triangle_counts(edges, p, validate_active=True),
    }


def main() -> None:
    print("h=3 repeat loose-triangle shadow compiler")
    check_models()
    print("loose triangle = shadow triangle supported by three active edges")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} B_line={row['b_line']} active_edges={row['active_edges']} "
            f"shadow_edges={row['shadow_edges']} contained_triangles={row['contained_triangles']} "
            f"loose_triangles={row['loose_triangles']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        print(
            f"contrast p={p} n={n} B_line={row['b_line']} "
            f"active_edges={row['active_edges']} shadow_edges={row['shadow_edges']} "
            f"contained_triangles={row['contained_triangles']} "
            f"loose_triangles={row['loose_triangles']}"
        )
    print("H3_REPEAT_LOOSE_TRIANGLE_SHADOW_COMPILER_PASS")


if __name__ == "__main__":
    main()
