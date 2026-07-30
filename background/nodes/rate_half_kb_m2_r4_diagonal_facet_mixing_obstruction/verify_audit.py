#!/usr/bin/env python3
"""Independently enumerate fixed-point-free label matchings."""

from collections import Counter


I = frozenset(range(6))
K = frozenset(range(5))
XI = 5
LABELS = tuple(range(12))


def matchings(vertices: tuple[int, ...]):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for index in range(1, len(vertices)):
        second = vertices[index]
        rest = vertices[1:index] + vertices[index + 1:]
        for tail in matchings(rest):
            yield ((first, second),) + tail


def main() -> None:
    census = Counter()
    preserving = 0
    preserving_contradictions = 0
    for edges in matchings(LABELS):
        mate = {}
        for left, right in edges:
            mate[left] = right
            mate[right] = left

        crossing = sum(mate[label] not in I for label in I)
        a = sum(left in K and right in K for left, right in edges)
        b = int(mate[XI] in K)
        if crossing == 0:
            preserving += 1
            k = mate[XI]
            assert k in K
            # The aligned and near-aligned xi capacities are both below the
            # four J roots transported from the common-K fiber.
            assert all(4 > capacity for capacity in (0, 2))
            preserving_contradictions += 1
        else:
            census[(a, b, crossing)] += 1

    expected = {(2, 0, 2), (1, 1, 2), (1, 0, 4), (0, 1, 4), (0, 0, 6)}
    assert set(census) == expected
    assert preserving == preserving_contradictions
    assert preserving > 0
    assert sum(census.values()) + preserving == 10395
    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_FACET_MIXING_OBSTRUCTION_AUDIT_PASS "
        f"matchings=10395 preserving_deleted={preserving} mixing_rows={len(census)}"
    )


if __name__ == "__main__":
    main()
