#!/usr/bin/env python3
"""Verify the saturated (1,1,2) defect classifier."""

import json
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_112_saturated_defect_classifier"
PARENTS = {
    "rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction",
    "rate_half_kb_m2_v4_outer_recurrence_router",
    "rate_half_kb_m2_r4_diagonal_source_subfield_dichotomy",
}
PURE = list(combinations(range(4), 2))
MIXED = [(i, j) for i in range(4) for j in range(2)]
PURE_INDEX = {edge: index for index, edge in enumerate(PURE)}
MIXED_INDEX = {edge: index for index, edge in enumerate(MIXED)}
TAU = {0: 1, 1: 0, 2: 3, 3: 2}
TAU_PURE = {
    index: PURE_INDEX[tuple(sorted((TAU[left], TAU[right])))]
    for index, (left, right) in enumerate(PURE)
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def defect(weights: Counter[int]) -> int:
    return sum(value * (value - 1) // 2 for value in weights.values())


def valid(pure_packet, mixed_packet, source_line=False):
    pure_weights = Counter(pure_packet)
    mixed_weights = Counter(mixed_packet)
    pure_defect = defect(pure_weights)
    mixed_defect = defect(mixed_weights)
    if pure_defect + mixed_defect > 1:
        return False
    j0_degree = [0] * 4
    j1_degree = [0] * 2
    for edge, weight in pure_weights.items():
        left, right = PURE[edge]
        j0_degree[left] += weight
        j0_degree[right] += weight
    for edge, weight in mixed_weights.items():
        left, right = MIXED[edge]
        j0_degree[left] += weight
        j1_degree[right] += weight
    if j1_degree != [2, 2] or not all(2 <= degree <= 4 for degree in j0_degree):
        return False
    if source_line:
        if mixed_defect:
            return False
        if any(pure_weights[index] != pure_weights[TAU_PURE[index]]
               for index in range(len(PURE))):
            return False
        if any(TAU_PURE[index] == index and pure_weights[index] % 2
               for index in range(len(PURE))):
            return False
    return True


GROUP_J0 = [
    perm for perm in permutations(range(4))
    if {frozenset((perm[0], perm[1])), frozenset((perm[2], perm[3]))}
    == {frozenset((0, 1)), frozenset((2, 3))}
]


def canonical(packet):
    pure_packet, mixed_packet = packet
    images = []
    for perm in GROUP_J0:
        for swap in (0, 1):
            pure_image = tuple(sorted(
                PURE_INDEX[tuple(sorted((perm[PURE[edge][0]], perm[PURE[edge][1]])))]
                for edge in pure_packet
            ))
            mixed_image = tuple(sorted(
                MIXED_INDEX[(perm[MIXED[edge][0]], MIXED[edge][1] ^ swap)]
                for edge in mixed_packet
            ))
            images.append((pure_image, mixed_image))
    return min(images)


def packets(source_line=False):
    return [
        (pure_packet, mixed_packet)
        for pure_packet in combinations_with_replacement(range(6), 4)
        for mixed_packet in combinations_with_replacement(range(8), 4)
        if valid(pure_packet, mixed_packet, source_line)
    ]


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("1,560" in statement and "96 labeled" in statement, "counts")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
            "dependencies")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    universal = packets()
    source_line = packets(source_line=True)
    universal_orbits = {canonical(packet) for packet in universal}
    source_line_orbits = {canonical(packet) for packet in source_line}
    require(len(GROUP_J0) == 8, "matching centralizer")
    require((len(universal), len(universal_orbits)) == (1560, 123),
            "universal packet census")
    require((len(source_line), len(source_line_orbits)) == (96, 12),
            "source-line packet census")

    profiles = set()
    for pure_packet, mixed_packet in universal:
        degree = [0] * 4
        for edge in pure_packet:
            left, right = PURE[edge]
            degree[left] += 1
            degree[right] += 1
        for edge in mixed_packet:
            degree[MIXED[edge][0]] += 1
        profiles.add(tuple(sorted(degree)))
    require(profiles == {(2, 2, 4, 4), (2, 3, 3, 4), (3, 3, 3, 3)},
            "J0 degree profiles")

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_SATURATED_DEFECT_CLASSIFIER_PASS "
        "universal=1560/123 source_line=96/12 profiles=3 residual_defect=1"
    )


if __name__ == "__main__":
    main()
