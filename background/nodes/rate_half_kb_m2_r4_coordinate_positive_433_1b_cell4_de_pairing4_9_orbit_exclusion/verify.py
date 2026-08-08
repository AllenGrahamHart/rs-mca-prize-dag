#!/usr/bin/env python3
"""Verify the cell-4 pairing-4/9 DE orbit composition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PAIRING4 = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_de_pairing4_complete_exclusion"
)
QUOTIENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_parallel_de_matching_orbit_quotient"
)
PREVIOUS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_de_pairing3_6_complete_exclusion"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    for index in range(1, len(values)):
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((values[0], values[index]),) + tail


def canonical(edges):
    return tuple(sorted((min(left, right), max(left, right))
                        for left, right in edges))


def verify_composition():
    matchings = tuple(pairings(range(6)))
    lookup = {canonical(matching): index
              for index, matching in enumerate(matchings)}
    require(len(matchings) == len(lookup) == 15, "matching census")

    def swap_matching(matching):
        def swap(index):
            return 1 if index == 0 else 0 if index == 1 else index
        return lookup[canonical((swap(left), swap(right))
                                for left, right in matching)]

    permutation = tuple(swap_matching(matching) for matching in matchings)
    require(permutation == (0, 1, 2, 6, 9, 12, 3, 10, 13,
                            4, 7, 14, 5, 8, 11),
            "matching involution")

    def action(label):
        xi, pairing = label
        if xi == 0:
            return (1, pairing)
        if xi == 1:
            return (0, pairing)
        return (xi, permutation[pairing])

    labels = {(xi, pairing) for xi in range(7) for pairing in range(15)}
    orbits = {frozenset((label, action(label))) for label in labels}
    require(len(labels) == 105 and len(orbits) == 60, "105-to-60 quotient")

    previous = (
        {(xi, pairing) for xi in (0, 1, 2) for pairing in (0, 1, 2)} |
        {(xi, pairing) for xi in (0, 1, 2) for pairing in (3, 6)}
    )
    previous_orbits = {orbit for orbit in orbits if orbit <= previous}
    require(len(previous) == 15 and len(previous_orbits) == 9,
            "previous complete ledger")

    direct = {(0, 4), (1, 4), (2, 4)}
    new_orbits = {orbit for orbit in orbits if orbit & direct}
    new_labels = set().union(*new_orbits)
    require(new_orbits == {
        frozenset(((0, 4), (1, 4))),
        frozenset(((2, 4), (2, 9))),
    } and new_labels == {(0, 4), (1, 4), (2, 4), (2, 9)},
            "honest pairing-4/9 orbit closure")
    require((0, 9) not in new_labels and (1, 9) not in new_labels,
            "positive pairing-9 scope fence")

    paid = previous | new_labels
    paid_orbits = {orbit for orbit in orbits if orbit <= paid}
    live_orbits = {orbit for orbit in orbits if orbit.isdisjoint(paid)}
    require(len(paid) == 19 and len(paid_orbits) == 11 and
            sum(map(len, paid_orbits)) == 19,
            "aggregate paid ledger")
    require(len(live_orbits) == 49 and sum(map(len, live_orbits)) == 86,
            "aggregate live ledger")
    require(len(new_labels)*4*4 == 64, "raw sign-lane count")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    for node in (NODE_ID, PAIRING4, QUOTIENT, PREVIOUS):
        require(nodes[node]["status"] == "PROVED", f"proved node {node}")
    edges = {(row["from"], row["to"], row["kind"])
             for row in dag["edges"]}
    for parent in (PAIRING4, QUOTIENT, PREVIOUS):
        require((parent, NODE_ID, "req") in edges, f"parent edge {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")


def verify_documents():
    statement = (NODE / "statement.md").read_text()
    compact_statement = " ".join(statement.split())
    proof = (NODE / "proof.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("= 64 raw cases" in compact_statement and
            "86 labels in 49 quotient orbits" in compact_statement,
            "printed aggregate")
    require("105-19 = 86" in proof and "60-11 = 49" in proof,
            "ledger subtraction")
    require("`(0,9)` and `(1,9)`" in frontier and
            "remain open" in frontier, "scope fence")


def main():
    verify_composition()
    verify_dag()
    verify_documents()
    print(
        "cell=4 new_labels=4 new_orbits=2 raw_cases=64 "
        "paid_labels=19 live_labels=86 live_orbits=49"
    )


if __name__ == "__main__":
    main()
