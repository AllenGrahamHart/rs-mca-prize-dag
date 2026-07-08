#!/usr/bin/env python3
"""Finite exception scan for the h=3 repeat-boundary hitting route."""

from __future__ import annotations

from f3_h3_repeat_coordinate_hitting_ledger import (
    active_coordinate_edges_from_triples,
    minimum_hitting_set,
)
from f3_h3_repeat_support_forced_point_reduction import active_ordered_triples


WITNESS_ROWS = (
    (337, 16),
    (2017, 32),
    (4801, 64),
    (7937, 64),
    (65537, 256),
    (91393, 256),
)


def verify_row(p: int, n: int) -> dict[str, int | str]:
    triples = active_ordered_triples(p, n)
    edges = active_coordinate_edges_from_triples(p, n, triples)
    non_two_edges = [edge for edge in edges if 2 % p not in edge]
    tau, hitting = minimum_hitting_set(edges)
    tau_non_two, hitting_non_two = minimum_hitting_set(non_two_edges)
    if edges and tau != 1:
        raise AssertionError((p, n, "expected singleton hitting certificate", tau))
    if non_two_edges and tau_non_two != 1:
        raise AssertionError((p, n, "expected singleton non-2 exception hitter", tau_non_two))
    return {
        "b_line": len(triples),
        "active_edges": len(edges),
        "non_two_edges": len(non_two_edges),
        "tau_coord": tau,
        "hitting_set": ",".join(str(a) for a in hitting) if hitting else "-",
        "tau_non_two": tau_non_two,
        "hitting_non_two": ",".join(str(a) for a in hitting_non_two)
        if hitting_non_two
        else "-",
    }


def main() -> None:
    print("h=3 repeat hitting exception scan")
    false_two_cover_rows = 0
    for p, n in WITNESS_ROWS:
        row = verify_row(p, n)
        if row["non_two_edges"]:
            false_two_cover_rows += 1
        print(
            f"p={p} n={n} B_line={row['b_line']} active_edges={row['active_edges']} "
            f"non_two_edges={row['non_two_edges']} tau_coord={row['tau_coord']} "
            f"hitting_set={row['hitting_set']} tau_non_two={row['tau_non_two']} "
            f"hitting_non_two={row['hitting_non_two']}"
        )
    if false_two_cover_rows < 2:
        raise AssertionError(("expected multiple finite counterexamples", false_two_cover_rows))
    print("Pure forced-2 cover is false on boundary-style rows")
    print("H3_REPEAT_HITTING_EXCEPTION_SCAN_PASS")


if __name__ == "__main__":
    main()
