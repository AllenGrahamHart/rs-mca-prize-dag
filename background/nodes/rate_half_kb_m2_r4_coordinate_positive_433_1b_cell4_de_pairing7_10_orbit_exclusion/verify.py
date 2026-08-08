#!/usr/bin/env python3
"""Verify the cell-4 pairing-7/10 DE orbit composition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PAIRING7 = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_de_pairing7_complete_exclusion"
)
QUOTIENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_parallel_de_matching_orbit_quotient"
)
PREVIOUS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_de_pairing5_12_complete_exclusion"
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

    previous = {
        (xi, pairing)
        for xi in (0, 1, 2)
        for pairing in (0, 1, 2, 3, 4, 5, 6, 9, 12)
    }
    previous_orbits = {orbit for orbit in orbits if orbit <= previous}
    require(len(previous) == 27 and len(previous_orbits) == 15,
            "previous complete ledger")

    direct = {(0, 7), (1, 7), (2, 7)}
    new_orbits = {orbit for orbit in orbits if orbit & direct}
    new_labels = set().union(*new_orbits)
    require(new_orbits == {
        frozenset(((0, 7), (1, 7))),
        frozenset(((2, 7), (2, 10))),
    } and new_labels == {(0, 7), (1, 7), (2, 7), (2, 10)},
            "honest pairing-7/10 orbit closure")
    require((0, 10) not in new_labels and (1, 10) not in new_labels,
            "positive pairing-10 scope fence")

    paid = previous | new_labels
    paid_orbits = {orbit for orbit in orbits if orbit <= paid}
    live_orbits = {orbit for orbit in orbits if orbit.isdisjoint(paid)}
    require(len(paid) == 31 and len(paid_orbits) == 17 and
            sum(map(len, paid_orbits)) == 31,
            "aggregate paid ledger")
    require(len(live_orbits) == 43 and sum(map(len, live_orbits)) == 74,
            "aggregate live ledger")
    require(len(new_labels)*4*4 == 64, "raw sign-lane count")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    for node in (NODE_ID, PAIRING7, QUOTIENT, PREVIOUS):
        require(nodes[node]["status"] == "PROVED", f"proved node {node}")
    edges = {(row["from"], row["to"], row["kind"])
             for row in dag["edges"]}
    for parent in (PAIRING7, QUOTIENT, PREVIOUS):
        require((parent, NODE_ID, "req") in edges, f"parent edge {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")


def verify_documents():
    statement = (NODE / "statement.md").read_text()
    compact_statement = " ".join(statement.split())
    proof = (NODE / "proof.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("= 64 raw cases" in compact_statement and
            "74 labels in 43 quotient orbits" in compact_statement,
            "printed aggregate")
    require("105-31 = 74" in proof and "60-17 = 43" in proof,
            "ledger subtraction")
    require("`(0,10)` and `(1,10)`" in frontier and
            "remain open" in frontier, "scope fence")


def main():
    verify_composition()
    verify_dag()
    verify_documents()
    print(
        "cell=4 new_labels=4 new_orbits=2 raw_cases=64 "
        "paid_labels=31 live_labels=74 live_orbits=43"
    )


if __name__ == "__main__":
    main()
