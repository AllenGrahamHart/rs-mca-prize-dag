#!/usr/bin/env python3
"""Verify the one-loop 442 outside template-orbit classifier."""

import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_template_orbit_classifier"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first = items[0]
    for index in range(1, len(items)):
        second = items[index]
        rest = items[1:index]+items[index+1:]
        for tail in matchings(rest):
            yield tuple(sorted((tuple(sorted((first, second))),)+tail))


def templates(records, sign_dimension):
    return {
        (signs, forced, pairing)
        for signs in itertools.product((-1, 1), repeat=sign_dimension)
        for forced in records
        for pairing in matchings(tuple(record for record in records
                                       if record != forced))
    }


def transform(template, sign_multiplier=None, sign_permutation=None,
              record_map=None):
    signs, forced, pairing = template
    if sign_permutation is not None:
        signs = tuple(signs[index] for index in sign_permutation)
    if sign_multiplier is not None:
        signs = tuple(left*right for left, right in zip(
            signs, sign_multiplier
        ))
    record_map = record_map or {}

    def image(record):
        return record_map.get(record, record)

    return (
        signs,
        image(forced),
        tuple(sorted(tuple(sorted((image(left), image(right))))
                     for left, right in pairing)),
    )


def classify(records, sign_dimension, generators):
    universe = templates(records, sign_dimension)
    remaining = set(universe)
    orbits = []
    while remaining:
        current = {next(iter(remaining))}
        frontier = list(current)
        while frontier:
            template = frontier.pop()
            for generator in generators:
                image = transform(template, **generator)
                require(image in universe, "action closure")
                if image not in current:
                    current.add(image)
                    frontier.append(image)
        orbits.append(current)
        remaining -= current
    return universe, orbits


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("64 template orbits" in statement and "KB41TO-2" in statement,
            "claim")
    require("does not evaluate" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_edge_skeleton_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    s0_records = ("CE", "CF", "DE+", "DE-", "DF+", "DF-", "EF")
    s0_generators = (
        {"record_map": {"DE+": "DE-", "DE-": "DE+",
                        "DF+": "DF-", "DF-": "DF+"}},
        {"sign_multiplier": (-1, 1, -1),
         "record_map": {"DE+": "DE-", "DE-": "DE+"}},
        {"sign_multiplier": (1, -1, -1),
         "record_map": {"DF+": "DF-", "DF-": "DF+"}},
        {"sign_permutation": (1, 0, 2),
         "record_map": {"CE": "CF", "CF": "CE",
                        "DE+": "DF+", "DF+": "DE+",
                        "DE-": "DF-", "DF-": "DE-"}},
    )
    s0_universe, s0_orbits = classify(s0_records, 3, s0_generators)

    s1_records = ("CE", "CF", "DD", "DE", "DF", "EF+", "EF-")
    s1_generators = (
        {"sign_multiplier": (1, 1, -1, -1)},
        {"sign_multiplier": (-1, 1, -1, 1),
         "record_map": {"EF+": "EF-", "EF-": "EF+"}},
        {"sign_multiplier": (1, -1, 1, -1),
         "record_map": {"EF+": "EF-", "EF-": "EF+"}},
        {"sign_permutation": (1, 0, 3, 2),
         "record_map": {"CE": "CF", "CF": "CE",
                        "DE": "DF", "DF": "DE"}},
    )
    s1_universe, s1_orbits = classify(s1_records, 4, s1_generators)

    s2_records = ("CD+", "CD-", "EE", "DF+", "DF-", "EF+", "EF-")
    s2_generators = (
        {"record_map": {"CD+": "CD-", "CD-": "CD+",
                        "DF+": "DF-", "DF-": "DF+"}},
        {"record_map": {"EF+": "EF-", "EF-": "EF+"}},
        {"record_map": {"DF+": "DF-", "DF-": "DF+",
                        "EF+": "EF-", "EF-": "EF+"}},
    )
    s2_universe, s2_orbits = classify(s2_records, 0, s2_generators)

    require((len(s0_universe), len(s1_universe), len(s2_universe))
            == (840, 1680, 105), "raw counts")
    require((len(s0_orbits), len(s1_orbits), len(s2_orbits))
            == (64, 114, 23), "orbit counts")

    def distribution(orbits):
        return {size: sum(len(orbit) == size for orbit in orbits)
                for size in {len(orbit) for orbit in orbits}}

    require(distribution(s0_orbits) == {4: 6, 8: 14, 16: 44},
            "S0 distribution")
    require(distribution(s1_orbits) == {8: 18, 16: 96},
            "S1 distribution")
    require(distribution(s2_orbits) == {1: 1, 2: 6, 4: 9, 8: 7},
            "S2 distribution")
    require((len(s0_orbits)+len(s1_orbits)+len(s2_orbits))*4 == 804,
            "four-row cap")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_TEMPLATE_PASS "
        "orbits=64,114,23 per_common=201 four_rows=804"
    )


if __name__ == "__main__":
    main()
