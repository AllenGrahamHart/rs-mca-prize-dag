#!/usr/bin/env python3
"""Verify the honest cell-4 pairing-3/6 DE orbit composition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PAIRING3 = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_de_pairing3_complete_exclusion"
)
QUOTIENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_parallel_de_matching_orbit_quotient"
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

    first_pair = {(xi, pairing)
                  for xi in (0, 1, 2) for pairing in (0, 1, 2)}
    first_orbits = {orbit for orbit in orbits if orbit <= first_pair}
    require(len(first_pair) == 9 and len(first_orbits) == 6,
            "first-pair paid ledger")

    direct = {(0, 3), (1, 3), (2, 3)}
    new_orbits = {orbit for orbit in orbits if orbit & direct}
    new_labels = set().union(*new_orbits)
    require(new_orbits == {
        frozenset(((0, 3), (1, 3))),
        frozenset(((2, 3), (2, 6))),
    } and new_labels == {(0, 3), (1, 3), (2, 3), (2, 6)},
            "honest pairing-3 orbit closure")
    require((0, 6) not in new_labels and (1, 6) not in new_labels,
            "positive pairing-6 scope fence")

    paid = first_pair | new_labels
    paid_orbits = {orbit for orbit in orbits if orbit <= paid}
    live_orbits = {orbit for orbit in orbits if orbit.isdisjoint(paid)}
    require(len(paid) == 13 and len(paid_orbits) == 8 and
            sum(map(len, paid_orbits)) == 13,
            "aggregate paid ledger")
    require(len(live_orbits) == 52 and sum(map(len, live_orbits)) == 92,
            "aggregate live ledger")
    require(len(new_labels)*4*4 == 64, "raw sign-lane count")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == nodes[PAIRING3]["status"] ==
            nodes[QUOTIENT]["status"] == "PROVED", "proved DAG nodes")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require((PAIRING3, NODE_ID, "req") in edges and
            (QUOTIENT, NODE_ID, "req") in edges and
            (NODE_ID, "rate_half_band_closure", "ev") in edges,
            "DAG wiring")


def verify_documents():
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("= 64 raw cases" in statement and
            "92 labels in 52 live orbits" in statement,
            "printed aggregate")
    require("96 - 4 = 92" in proof and "54 - 2 = 52" in proof,
            "ledger subtraction")
    require("`(0,6)` and `(1,6)`" in frontier and
            "remain" in frontier, "scope fence")


def main():
    verify_composition()
    verify_dag()
    verify_documents()
    print(
        "cell=4 new_labels=4 new_orbits=2 raw_cases=64 "
        "paid_labels=13 live_labels=92 live_orbits=52"
    )


if __name__ == "__main__":
    main()
