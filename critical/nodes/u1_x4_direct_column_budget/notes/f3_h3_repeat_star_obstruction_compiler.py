#!/usr/bin/env python3
"""Combinatorial obstruction compiler for singleton h=3 hitting."""

from __future__ import annotations

from f3_h3_repeat_coordinate_hitting_ledger import (
    active_coordinate_edges_from_triples,
    minimum_hitting_set,
)
from f3_h3_repeat_hitting_exception_scan import WITNESS_ROWS
from f3_h3_repeat_support_forced_point_reduction import active_ordered_triples


def common_intersection(edges: list[frozenset[int]]) -> set[int]:
    if not edges:
        return set()
    common = set(edges[0])
    for edge in edges[1:]:
        common &= edge
    return common


def star_obstruction(edges: list[frozenset[int]]) -> tuple[frozenset[int], ...] | None:
    if not edges or common_intersection(edges):
        return None
    base = edges[0]
    witness = [base]
    for point in sorted(base):
        for edge in edges[1:]:
            if point not in edge:
                witness.append(edge)
                break
        else:
            raise AssertionError(("empty intersection but base point is global", point))
    obstruction = tuple(witness)
    if common_intersection(list(obstruction)):
        raise AssertionError(("constructed obstruction still has common point", obstruction))
    return obstruction


def check_combinatorial_model() -> None:
    star = [frozenset((1, 2, 3)), frozenset((1, 3, 4)), frozenset((1, 5, 6))]
    if star_obstruction(star) is not None:
        raise AssertionError("star family should have no obstruction")
    nonstar = [
        frozenset((1, 2, 3)),
        frozenset((2, 3, 4)),
        frozenset((1, 3, 5)),
        frozenset((1, 2, 6)),
    ]
    obstruction = star_obstruction(nonstar)
    if obstruction is None or len(obstruction) != 4:
        raise AssertionError(("nonstar family should have a four-edge obstruction", obstruction))


def verify_row(p: int, n: int) -> dict[str, int | str]:
    triples = active_ordered_triples(p, n)
    edges = active_coordinate_edges_from_triples(p, n, triples)
    tau, hitting = minimum_hitting_set(edges)
    obstruction = star_obstruction(edges)
    if (tau <= 1) != (obstruction is None):
        raise AssertionError((p, n, tau, hitting, obstruction))
    return {
        "b_line": len(triples),
        "active_edges": len(edges),
        "tau_coord": tau,
        "hitting_set": ",".join(str(a) for a in hitting) if hitting else "-",
        "obstruction_edges": len(obstruction or ()),
    }


def main() -> None:
    print("h=3 repeat star-obstruction compiler")
    check_combinatorial_model()
    print("tau_coord > 1 iff an empty-intersection obstruction of <=4 edges exists")
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} B_line={row['b_line']} active_edges={row['active_edges']} "
            f"tau_coord={row['tau_coord']} hitting_set={row['hitting_set']} "
            f"obstruction_edges={row['obstruction_edges']}"
        )
    print("H3_REPEAT_STAR_OBSTRUCTION_COMPILER_PASS")


if __name__ == "__main__":
    main()
