#!/usr/bin/env python3
"""Verify complete cell-4 pairing-8/13 composition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
ORBIT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_de_pairing8_13_orbit_exclusion"
)
POSITIVE = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_positive_de_pairing13_complete_exclusion"
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
    return tuple(sorted((min(a, b), max(a, b)) for a, b in edges))


def verify_labels():
    matchings = tuple(pairings(range(6)))
    lookup = {canonical(matching): index
              for index, matching in enumerate(matchings)}

    def swapped(matching):
        def swap(index):
            return 1 if index == 0 else 0 if index == 1 else index
        return lookup[canonical((swap(a), swap(b)) for a, b in matching)]

    permutation = tuple(swapped(matching) for matching in matchings)

    def action(label):
        xi, pairing = label
        if xi == 0:
            return (1, pairing)
        if xi == 1:
            return (0, pairing)
        return (xi, permutation[pairing])

    labels = {(xi, pairing) for xi in range(7) for pairing in range(15)}
    orbits = {frozenset((label, action(label))) for label in labels}
    orbit_parent = {(0, 8), (1, 8), (2, 8), (2, 13)}
    positive = {(0, 13), (1, 13)}
    complete = orbit_parent | positive
    require(complete == {(xi, pairing)
                         for xi in (0, 1, 2) for pairing in (8, 13)},
            "six-label Cartesian block")
    complete_orbits = {orbit for orbit in orbits if orbit <= complete}
    require(len(complete) == 6 and len(complete_orbits) == 3 and
            sum(map(len, complete_orbits)) == 6,
            "three complete quotient orbits")

    previous = {
        (xi, pairing)
        for xi in (0, 1, 2)
        for pairing in (0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 12)
    }
    paid = previous | complete
    paid_orbits = {orbit for orbit in orbits if orbit <= paid}
    live_orbits = {orbit for orbit in orbits if orbit.isdisjoint(paid)}
    require(len(paid) == 39 and len(paid_orbits) == 21,
            "cumulative paid ledger")
    require(sum(map(len, live_orbits)) == 66 and len(live_orbits) == 39,
            "cumulative live ledger")
    require(len(complete)*4*4 == 96, "raw-case count")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    for node in (NODE_ID, ORBIT, POSITIVE):
        require(nodes[node]["status"] == "PROVED", f"proved node {node}")
    edges = {(row["from"], row["to"], row["kind"])
             for row in dag["edges"]}
    require((ORBIT, NODE_ID, "req") in edges and
            (POSITIVE, NODE_ID, "req") in edges and
            (NODE_ID, "rate_half_band_closure", "ev") in edges,
            "DAG composition wiring")


def verify_documents():
    statement = " ".join((NODE / "statement.md").read_text().split())
    proof = (NODE / "proof.md").read_text()
    require("= 96 raw cases" in statement and
            "66 labels in 39 quotient orbits" in statement,
            "printed statement ledger")
    require("105-39=66" in proof and "60-21=39" in proof,
            "printed subtraction")


def main():
    verify_labels()
    verify_dag()
    verify_documents()
    print("cell=4 pairings=8,13 labels=6 raw_cases=96 live_labels=66 live_orbits=39")


if __name__ == "__main__":
    main()
