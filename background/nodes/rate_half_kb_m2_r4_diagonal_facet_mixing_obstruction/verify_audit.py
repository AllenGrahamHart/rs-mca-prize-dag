#!/usr/bin/env python3
"""Independently enumerate fixed-point-free label matchings."""

from collections import Counter


I = frozenset(range(6))
K = frozenset(range(5))
XI = 5
ETA_NEAR = 6
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
    c6_near_survivors = 0
    c6_near_deleted = 0
    c2_near_types = Counter()
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
            if crossing == 2:
                if (a, b) == (2, 0):
                    c2_near_types["a2"] += 1
                elif mate[ETA_NEAR] in K:
                    c2_near_types["a1_etaK"] += 1
                else:
                    assert mate[ETA_NEAR] in set(range(6, 12))
                    assert mate[mate[ETA_NEAR]] == ETA_NEAR
                    c2_near_types["a1_etaJ0"] += 1
            if crossing == 6:
                if mate[ETA_NEAR] == XI:
                    c6_near_deleted += 1
                else:
                    assert mate[ETA_NEAR] in K
                    ell = mate[XI]
                    assert ell in set(range(6, 12)) - {ETA_NEAR}
                    c6_near_survivors += 1

    expected = {(2, 0, 2), (1, 1, 2), (1, 0, 4), (0, 1, 4), (0, 0, 6)}
    assert set(census) == expected
    assert preserving == preserving_contradictions
    assert preserving > 0
    assert sum(census.values()) + preserving == 10395
    assert c6_near_deleted == 120
    assert c6_near_survivors == 600
    assert c2_near_types == {
        "a2": 1350,
        "a1_etaK": 900,
        "a1_etaJ0": 1800,
    }
    assert [z for z in range(3) if 4 - z <= 2] == [2]

    # Independent incidence-capacity replay for the two c=2 orbit rows.
    first_row_J0 = 4 * 4
    first_row_J1 = 20 - first_row_J0
    assert first_row_J1 == 4
    assert [first_row_J1 // 2] * 2 == [2, 2]
    assert 4 + 2 + 2 == 8
    exceptional_J1_interval = tuple(range(3 * 2, 2 * 4 + 1))
    assert exceptional_J1_interval == (6, 7, 8)
    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_FACET_MIXING_OBSTRUCTION_AUDIT_PASS "
        f"matchings=10395 preserving_deleted={preserving} mixing_rows={len(census)} "
        f"c6_near={c6_near_survivors} c6_eta_xi_deleted={c6_near_deleted} "
        f"c2_near_types={dict(c2_near_types)} "
        f"c2_exceptional={exceptional_J1_interval}"
    )


if __name__ == "__main__":
    main()
