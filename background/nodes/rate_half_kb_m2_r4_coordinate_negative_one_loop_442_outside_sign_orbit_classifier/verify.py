#!/usr/bin/env python3
"""Verify the one-loop 442 outside sign-orbit classifier."""

import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_outside_sign_orbit_classifier"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def orbit(seed, generators):
    found = {seed}
    frontier = [seed]
    while frontier:
        value = frontier.pop()
        for generator in generators:
            image = tuple(value[index]*generator[index]
                          for index in range(len(value)))
            if image not in found:
                found.add(image)
                frontier.append(image)
    return found


def partition(dimension, generators):
    remaining = set(itertools.product((-1, 1), repeat=dimension))
    output = []
    while remaining:
        current = orbit(next(iter(remaining)), generators)
        output.append(current)
        remaining -= current
    return output


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("2+2+1=5" in statement and "KB41SG-1" in statement, "claim")
    require("does not quotient" in statement and "nonclaim" in contract,
            "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    parent = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_edge_skeleton_classifier"
    require((parent, NODE_ID, "req") in edges, "dependency")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    s0_generators = ((-1, 1, -1), (1, -1, -1))
    s0_orbits = partition(3, s0_generators)
    require(sorted(len(value) for value in s0_orbits) == [4, 4],
            "S0 orbit sizes")
    require({next(iter({a*b*c for a, b, c in value}))
             for value in s0_orbits} == {-1, 1}, "S0 parity")
    require(all(len({a*b*c for a, b, c in value}) == 1
                for value in s0_orbits), "S0 invariant")

    s1_generators = (
        (1, 1, -1, -1),
        (-1, 1, -1, 1),
        (1, -1, 1, -1),
    )
    s1_orbits = partition(4, s1_generators)
    require(sorted(len(value) for value in s1_orbits) == [8, 8],
            "S1 orbit sizes")
    require({next(iter({a*b*c*d for a, b, c, d in value}))
             for value in s1_orbits} == {-1, 1}, "S1 parity")
    require(all(len({a*b*c*d for a, b, c, d in value}) == 1
                for value in s1_orbits), "S1 invariant")

    require((len(s0_orbits)+len(s1_orbits)+1)*105 == 525,
            "template cap")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_SIGN_PASS "
        "S0_orbits=2 S1_orbits=2 S2_orbits=1 templates_per_common=525"
    )


if __name__ == "__main__":
    main()
