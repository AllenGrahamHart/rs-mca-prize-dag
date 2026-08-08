#!/usr/bin/env python3
"""Verify the complete cell-4 parallel-DE pairing-3/6 composition."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
ORBIT_PARENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_de_pairing3_6_orbit_exclusion"
)
POSITIVE_PARENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_positive_de_pairing6_complete_exclusion"
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


def verify_ledger():
    matchings = tuple(pairings(range(6)))
    lookup = {canonical(matching): index
              for index, matching in enumerate(matchings)}

    def swap_matching(matching):
        def swap(index):
            return 1 if index == 0 else 0 if index == 1 else index
        return lookup[canonical((swap(left), swap(right))
                                for left, right in matching)]

    permutation = tuple(swap_matching(matching) for matching in matchings)

    def action(label):
        xi, pairing = label
        if xi == 0:
            return (1, pairing)
        if xi == 1:
            return (0, pairing)
        return (xi, permutation[pairing])

    labels = {(xi, pairing) for xi in range(7) for pairing in range(15)}
    orbits = {frozenset((label, action(label))) for label in labels}
    first_pair = {(xi, pairing)
                  for xi in (0, 1, 2) for pairing in (0, 1, 2)}
    block = {(xi, pairing)
             for xi in (0, 1, 2) for pairing in (3, 6)}
    block_orbits = {orbit for orbit in orbits if orbit <= block}
    require(block_orbits == {
        frozenset(((0, 3), (1, 3))),
        frozenset(((2, 3), (2, 6))),
        frozenset(((0, 6), (1, 6))),
    }, "three complete block orbits")
    require(len(block) == 6 and len(block_orbits) == 3 and
            len(block)*4*4 == 96, "block counts")
    paid = first_pair | block
    paid_orbits = {orbit for orbit in orbits if orbit <= paid}
    live_orbits = {orbit for orbit in orbits if orbit.isdisjoint(paid)}
    require(len(paid) == 15 and len(paid_orbits) == 9,
            "paid aggregate")
    require(len(live_orbits) == 51 and sum(map(len, live_orbits)) == 90,
            "live aggregate")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == nodes[ORBIT_PARENT]["status"] ==
            nodes[POSITIVE_PARENT]["status"] == "PROVED", "proved nodes")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require((ORBIT_PARENT, NODE_ID, "req") in edges and
            (POSITIVE_PARENT, NODE_ID, "req") in edges and
            (NODE_ID, "rate_half_band_closure", "ev") in edges,
            "DAG wiring")


def main():
    verify_ledger()
    verify_dag()
    statement = (NODE / "statement.md").read_text()
    require("`6*4*4=96` raw cases" in statement and
            "live orbits:  51" in statement, "printed ledger")
    print("cell=4 pairings=3,6 labels=6 raw_cases=96 live_labels=90 live_orbits=51")


if __name__ == "__main__":
    main()
