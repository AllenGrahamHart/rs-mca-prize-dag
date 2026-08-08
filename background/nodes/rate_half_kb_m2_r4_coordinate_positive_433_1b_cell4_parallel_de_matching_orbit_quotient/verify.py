#!/usr/bin/env python3
"""Verify the cell-4 parallel-DE matching-orbit quotient."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
ATLAS = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas"
FIRST_PAIR = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_de_firstpair_complete_exclusion"
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


def verify_action():
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
    require(all(permutation[permutation[index]] == index
                for index in range(15)), "involution law")

    records = (
        ("DE", "S_DE_PLUS"),
        ("DE", "S_DE_PLUS"),
        ("-DE", "S_DE_MINUS"),
        ("DF", "S_DF"),
        ("soEF", "S_soEF"),
        ("BF", "S_BF"),
        ("scCF", "S_scCF"),
    )

    def residual(xi):
        return records[:xi] + records[xi + 1:]

    def signature(xi, matching_index):
        values = residual(xi)
        return tuple(sorted((values[left], values[right])
                            for left, right in matchings[matching_index]))

    require(residual(0) == residual(1), "positive missing-role transport")
    for pairing in range(15):
        require(signature(0, pairing) == signature(1, pairing),
                "xi0-xi1 system signature")
    for xi in range(2, 7):
        for pairing in range(15):
            require(signature(xi, pairing) ==
                    signature(xi, permutation[pairing]),
                    "fixed-xi matching signature")

    def action(label):
        xi, pairing = label
        if xi == 0:
            return (1, pairing)
        if xi == 1:
            return (0, pairing)
        return (xi, permutation[pairing])

    labels = {(xi, pairing) for xi in range(7) for pairing in range(15)}
    orbits = set()
    for label in labels:
        orbits.add(frozenset((label, action(label))))
    require(len(labels) == 105 and len(orbits) == 60, "105-to-60 quotient")
    sizes = {size: sum(len(orbit) == size for orbit in orbits)
             for size in (1, 2)}
    require(sizes == {1: 15, 2: 45}, "orbit size profile")
    paid = {(xi, pairing) for xi in (0, 1, 2) for pairing in (0, 1, 2)}
    paid_orbits = {orbit for orbit in orbits if orbit <= paid}
    live_orbits = {orbit for orbit in orbits if orbit.isdisjoint(paid)}
    require(len(paid) == 9 and len(paid_orbits) == 6 and
            len(live_orbits) == 54 and
            sum(map(len, live_orbits)) == 96, "live quotient ledger")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == nodes[ATLAS]["status"] ==
            nodes[FIRST_PAIR]["status"] == "PROVED", "proved DAG nodes")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require((ATLAS, NODE_ID, "req") in edges and
            (FIRST_PAIR, NODE_ID, "req") in edges and
            (NODE_ID, "rate_half_band_closure", "ev") in edges,
            "DAG wiring")


def verify_documents():
    atlas = (ROOT / "background/nodes" / ATLAS / "statement.md").read_text()
    statement = (NODE / "statement.md").read_text()
    audit = (NODE / "audit.md").read_text()
    require("outside: de,de,-de; df, sigma_o ef" in atlas,
            "atlas record custody")
    require("15 + 5*9 = 60" in statement and "`54` orbit representatives" in
            statement, "orbit statement")
    require("products and identical\n  squared sums" in audit and
            "No target-lane" in audit, "scope discipline")


def main():
    verify_action()
    verify_dag()
    verify_documents()
    print("cell=4 labels=105 orbits=60 paid_orbits=6 "
          "live_labels=96 live_orbits=54")


if __name__ == "__main__":
    main()
