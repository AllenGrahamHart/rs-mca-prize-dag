#!/usr/bin/env python3
"""Independently enumerate internal edge assignments per pure multiset."""

from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement


EDGES = list(combinations(range(4), 2))
EDGE_INDEX = {edge: index for index, edge in enumerate(EDGES)}
TAU = {0: 1, 1: 0, 2: 3, 3: 2}
TAU_EDGE = {
    index: EDGE_INDEX[tuple(sorted((TAU[left], TAU[right])))]
    for index, (left, right) in enumerate(EDGES)
}


def defect(packet):
    return sum(weight * (weight - 1) // 2 for weight in packet.values())


def main() -> None:
    assignments = defaultdict(list)
    for first, second in combinations_with_replacement(range(6), 2):
        packet = Counter((first, second, TAU_EDGE[first], TAU_EDGE[second]))
        if defect(packet) <= 1:
            key = tuple(sorted(packet.elements()))
            assignments[key].append((first, second))

    counts = sorted(len(values) for values in assignments.values())
    assert len(assignments) == 5
    assert counts == [2, 2, 2, 2, 4]
    assert max(counts) * 2 == 8
    assert all(len(set(EDGES[first]) & set(EDGES[second])) == 1
               for values in assignments.values() for first, second in values)

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_SOURCE_LINE_INTERNAL_STAR_RECONSTRUCTION_AUDIT_PASS "
        "pure_multisets=5 assignment_counts=2,2,2,2,4 signs=2 max_candidates=8"
    )


if __name__ == "__main__":
    main()
