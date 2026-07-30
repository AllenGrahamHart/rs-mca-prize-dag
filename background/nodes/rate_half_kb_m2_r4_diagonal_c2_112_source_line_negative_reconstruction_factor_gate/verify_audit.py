#!/usr/bin/env python3
"""Independently classify negative internal-edge templates."""

from collections import Counter
from itertools import combinations, combinations_with_replacement


def main() -> None:
    edges = list(combinations(range(4), 2))
    index = {edge: i for i, edge in enumerate(edges)}
    tau = {0: 1, 1: 0, 2: 3, 3: 2}
    tau_edge = {
        i: index[tuple(sorted((tau[left], tau[right])))]
        for i, (left, right) in enumerate(edges)
    }
    templates = Counter()
    for first, second in combinations_with_replacement(range(6), 2):
        packet = Counter((first, second, tau_edge[first], tau_edge[second]))
        defect = sum(weight * (weight - 1) // 2
                     for weight in packet.values())
        if defect > 1:
            continue
        assert len(set(edges[first]) & set(edges[second])) == 1
        fixed = sum(tau_edge[edge] == edge for edge in (first, second))
        assert fixed in (0, 1)
        templates["fixed-moving" if fixed else "moving-moving"] += 1

    assert templates == {"fixed-moving": 8, "moving-moving": 4}
    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_SOURCE_LINE_NEGATIVE_RECONSTRUCTION_FACTOR_GATE_AUDIT_PASS "
        "assignments=12 fixed_moving=8 moving_moving=4"
    )


if __name__ == "__main__":
    main()
