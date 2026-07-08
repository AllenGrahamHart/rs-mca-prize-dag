#!/usr/bin/env python3
"""Minimum coordinate-hitting ledger for h=3 repeat-boundary support."""

from __future__ import annotations

from itertools import combinations

from f3_h3_repeat_support_forced_point_reduction import (
    active_ordered_triples,
    fixed_first_count,
)


ROWS = (
    (257, 16),
    (1153, 32),
    (4289, 64),
    (17921, 128),
    (65537, 256),
    (262657, 512),
    (1051649, 1024),
)


def active_coordinate_edges_from_triples(
    p: int, n: int, triples: list[tuple[int, int, int, int]]
) -> list[frozenset[int]]:
    edges = {frozenset(triple[:3]) for triple in triples}
    for edge in edges:
        if len(edge) != 3:
            raise AssertionError((p, n, edge))
    return sorted(edges, key=lambda edge: tuple(sorted(edge)))


def active_coordinate_edges(p: int, n: int) -> list[frozenset[int]]:
    return active_coordinate_edges_from_triples(p, n, active_ordered_triples(p, n))


def minimum_hitting_set(edges: list[frozenset[int]]) -> tuple[int, tuple[int, ...]]:
    if not edges:
        return 0, ()
    universe = sorted(set().union(*edges))
    edge_list = list(edges)
    for size in range(1, len(universe) + 1):
        for candidate in combinations(universe, size):
            chosen = set(candidate)
            if all(edge & chosen for edge in edge_list):
                return size, candidate
    raise AssertionError("finite hypergraph has no hitting set")


def verify_row(p: int, n: int) -> dict[str, int | str]:
    triples = active_ordered_triples(p, n)
    edges = active_coordinate_edges_from_triples(p, n, triples)
    tau, hitting = minimum_hitting_set(edges)
    if triples and tau == 0:
        raise AssertionError((p, n, "empty hitting set for nonempty row"))
    if any(not ({u, v, w} & set(hitting)) for u, v, w, _ in triples):
        raise AssertionError((p, n, "hitting set misses an ordered triple"))

    first_count_sum = sum(fixed_first_count(p, n, a) for a in hitting)
    three_first_sum = 3 * first_count_sum
    if three_first_sum < len(triples):
        raise AssertionError((p, n, hitting, three_first_sum, len(triples)))

    residue_bound = (72 * tau + 18) * n * n
    return {
        "b_line": len(triples),
        "unique_edges": len(edges),
        "tau_coord": tau,
        "hitting_set": ",".join(str(a) for a in hitting) if hitting else "-",
        "three_sum_Na": three_first_sum,
        "residue_bound": residue_bound,
        "n3": n**3,
        "paid_by_bound": int(residue_bound < n**3),
    }


def main() -> None:
    print("h=3 repeat coordinate-hitting ledger")
    nonzero_tau_rows = 0
    for p, n in ROWS:
        row = verify_row(p, n)
        if row["tau_coord"]:
            nonzero_tau_rows += 1
        print(
            f"p={p} n={n} B_line={row['b_line']} unique_edges={row['unique_edges']} "
            f"tau_coord={row['tau_coord']} hitting_set={row['hitting_set']} "
            f"three_sum_Na={row['three_sum_Na']} residue_bound={row['residue_bound']} "
            f"n^3={row['n3']} paid_by_bound={row['paid_by_bound']}"
        )
    if nonzero_tau_rows != 1:
        raise AssertionError(("expected one nonzero hitting row", nonzero_tau_rows))
    print("Minimum hitting number tau_coord gives B_line <= 6*tau_coord*n")
    print("H3_REPEAT_COORDINATE_HITTING_LEDGER_PASS")


if __name__ == "__main__":
    main()
