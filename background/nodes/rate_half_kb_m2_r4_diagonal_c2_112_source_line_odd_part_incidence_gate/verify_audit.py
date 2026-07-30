#!/usr/bin/env python3
"""Independently exhaust internal-orbit pure-edge possibilities."""

from collections import Counter
from itertools import combinations, combinations_with_replacement


EDGES = list(combinations(range(4), 2))
EDGE_INDEX = {edge: index for index, edge in enumerate(EDGES)}
TAU = {0: 1, 1: 0, 2: 3, 3: 2}
TAU_EDGE = {
    index: EDGE_INDEX[tuple(sorted((TAU[left], TAU[right])))]
    for index, (left, right) in enumerate(EDGES)
}


def defect(weights):
    return sum(weight * (weight - 1) // 2 for weight in weights.values())


def main() -> None:
    admissible = []
    for first, second in combinations_with_replacement(range(6), 2):
        packet = Counter((first, second, TAU_EDGE[first], TAU_EDGE[second]))
        if defect(packet) <= 1:
            common = set(EDGES[first]) & set(EDGES[second])
            assert first != second
            assert len(common) == 1
            admissible.append((first, second))
    assert len(admissible) == 12

    ramified_costs = []
    for edge in range(6):
        packet = Counter((edge, edge, TAU_EDGE[edge], TAU_EDGE[edge]))
        ramified_costs.append(defect(packet))
    assert min(ramified_costs) == 2

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_SOURCE_LINE_ODD_PART_INCIDENCE_GATE_AUDIT_PASS "
        "admissible_internal_pairs=12 all_adjacent=true ramified_defect_floor=2"
    )


if __name__ == "__main__":
    main()
