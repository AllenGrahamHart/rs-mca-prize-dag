#!/usr/bin/env python3
"""Linearity compiler for h=3 repeat-boundary active edges."""

from __future__ import annotations

from itertools import combinations

from f3_h3_repeat_coordinate_hitting_ledger import active_coordinate_edges_from_triples
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_star_obstruction_compiler import CONTRAST_ROWS
from f3_h3_repeat_support_forced_point_reduction import active_ordered_triples


def forced_third(a: int, b: int, p: int) -> int:
    x = (a - 1) % p
    y = (b - 1) % p
    if x == 0 or y == 0:
        raise AssertionError((p, "active shifted coordinate is zero", a, b))
    denom = (x + y) % p
    if denom == 0:
        raise AssertionError((p, "active pair has zero shifted sum", a, b))
    return (1 - x * y * pow(denom, -1, p)) % p


def verify_edge(edge: frozenset[int], p: int) -> None:
    for a, b in combinations(sorted(edge), 2):
        c = forced_third(a, b, p)
        remaining = set(edge) - {a, b}
        if remaining != {c}:
            raise AssertionError((p, edge, (a, b), c, remaining))


def verify_linearity(edges: list[frozenset[int]], p: int) -> dict[str, int]:
    pair_owner: dict[tuple[int, int], frozenset[int]] = {}
    for edge in edges:
        verify_edge(edge, p)
        for pair in combinations(sorted(edge), 2):
            if pair in pair_owner and pair_owner[pair] != edge:
                raise AssertionError((p, pair, pair_owner[pair], edge))
            pair_owner[pair] = edge
    return {
        "active_edges": len(edges),
        "pair_slots": 3 * len(edges),
        "distinct_pairs": len(pair_owner),
        "repeated_pairs": 3 * len(edges) - len(pair_owner),
    }


def check_models() -> None:
    loose = [
        frozenset((1, 2, 7)),
        frozenset((1, 3, 8)),
        frozenset((2, 3, 9)),
    ]
    pinched = [
        frozenset((1, 2, 3)),
        frozenset((1, 2, 4)),
        frozenset((3, 4, 5)),
    ]
    tetrahedron = [
        frozenset((2, 3, 4)),
        frozenset((1, 3, 4)),
        frozenset((1, 2, 4)),
        frozenset((1, 2, 3)),
    ]

    def repeated_pairs(edges: list[frozenset[int]]) -> int:
        pairs = [pair for edge in edges for pair in combinations(sorted(edge), 2)]
        return len(pairs) - len(set(pairs))

    if repeated_pairs(loose) != 0:
        raise AssertionError("loose triangle should be linear")
    if repeated_pairs(pinched) == 0:
        raise AssertionError("pinched triangle should repeat a pair")
    if repeated_pairs(tetrahedron) == 0:
        raise AssertionError("tetrahedron should repeat pairs")


def verify_row(p: int, n: int) -> dict[str, int]:
    triples = active_ordered_triples(p, n)
    edges = active_coordinate_edges_from_triples(p, n, triples)
    return {"b_line": len(triples), **verify_linearity(edges, p)}


def main() -> None:
    print("h=3 repeat linear-hypergraph compiler")
    check_models()
    print("any coordinate pair determines at most one active edge")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} B_line={row['b_line']} active_edges={row['active_edges']} "
            f"pair_slots={row['pair_slots']} distinct_pairs={row['distinct_pairs']} "
            f"repeated_pairs={row['repeated_pairs']}"
        )
    for p, n in CONTRAST_ROWS:
        row = verify_row(p, n)
        print(
            f"contrast p={p} n={n} B_line={row['b_line']} "
            f"active_edges={row['active_edges']} pair_slots={row['pair_slots']} "
            f"distinct_pairs={row['distinct_pairs']} repeated_pairs={row['repeated_pairs']}"
        )
    print("pinched and tetrahedral coreless patterns are impossible for active edges")
    print("H3_REPEAT_LINEAR_HYPERGRAPH_COMPILER_PASS")


if __name__ == "__main__":
    main()
