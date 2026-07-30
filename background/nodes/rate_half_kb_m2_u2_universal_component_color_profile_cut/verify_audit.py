#!/usr/bin/env python3
"""Independently replay four-edge color profiles on every pole-cycle type."""

from itertools import combinations


CYCLE_PARTITIONS = ((6,), (4, 2), (3, 3), (2, 2, 2))
EXPECTED = {
    (0, 0, 0, 0, 2, 2),
    (0, 0, 0, 1, 1, 2),
    (0, 0, 1, 1, 1, 1),
}


def cycle_graph(partition: tuple[int, ...]) -> list[tuple[int, int]]:
    edges = []
    offset = 0
    for size in partition:
        for index in range(size):
            left = offset + index
            edges.append((left, offset + index))
            edges.append((left, offset + (index - 1) % size))
        offset += size
    return edges


def main() -> None:
    seen = set()
    for partition in CYCLE_PARTITIONS:
        edges = cycle_graph(partition)
        assert len(edges) == 12
        assert all(sum(left == vertex for left, _ in edges) == 2
                   for vertex in range(6))
        assert all(sum(right == vertex for _, right in edges) == 2
                   for vertex in range(6))
        for chosen in combinations(edges, 4):
            degrees = tuple(sorted(
                sum(left == vertex for left, _ in chosen)
                for vertex in range(6)
            ))
            assert max(degrees) <= 2
            assert sum(degrees) == 4
            seen.add(degrees)
    assert seen == EXPECTED
    print(
        "RATE_HALF_KB_M2_U2_UNIVERSAL_COMPONENT_COLOR_PROFILE_CUT_AUDIT_PASS "
        f"cycle_types={len(CYCLE_PARTITIONS)} profiles={len(seen)}"
    )


if __name__ == "__main__":
    main()
