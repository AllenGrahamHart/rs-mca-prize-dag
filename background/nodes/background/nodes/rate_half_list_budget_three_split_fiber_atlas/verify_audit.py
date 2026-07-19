#!/usr/bin/env python3
"""Independent valuation audit of the B*=3 split-fiber atlas."""

from __future__ import annotations

from itertools import combinations, product


EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
TYPES = (
    ((2, 1, 1, 0), (0, 0, 1, 1, 1, 1), (0, 0, 0, 0, 1, 1)),
    ((1, 1, 1, 1), (0, 1, 1, 1, 1, 0), (1, 0, 0, 0, 0, 1)),
    ((2, 2, 1, 1), (0, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 1)),
    ((2, 2, 2, 2), (1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0)),
    ((1, 1, 0, 1), (0, 1, 0, 1, 0, 0), (0, 0, 0, 0, 0, 1)),
    ((1, 1, 1, 2), (1, 1, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0)),
)


def edge_value(values: tuple[int, ...], i: int, j: int) -> int:
    return values[EDGES.index(tuple(sorted((i, j))))]


def repeated_maximum(values: tuple[int, ...]) -> bool:
    return values.count(max(values)) >= 2


def main() -> None:
    chamber_counts = []
    pencil_counts = []
    for deficits, p_degrees, delta in TYPES:
        chambers = []
        for degrees in product(
            *(range(p, p + slack + 1) for p, slack in zip(p_degrees, delta, strict=True))
        ):
            triangle_orders = []
            for i, j, k in combinations(range(4), 3):
                triangle_orders.append(
                    (
                        -deficits[k] + edge_value(degrees, i, j),
                        -deficits[i] + edge_value(degrees, j, k),
                        -deficits[j] + edge_value(degrees, i, k),
                    )
                )
            if all(repeated_maximum(row) for row in triangle_orders):
                chambers.append(degrees)
        chamber_counts.append(len(chambers))

        pencils = 0
        for i, j, k in combinations(range(4), 3):
            pairs = ((i, j), (j, k), (i, k))
            if any(edge_value(delta, *edge) for edge in pairs):
                continue
            orders = (
                -deficits[k] + edge_value(p_degrees, i, j),
                -deficits[i] + edge_value(p_degrees, j, k),
                -deficits[j] + edge_value(p_degrees, i, k),
            )
            pencils += len(set(orders)) == 1
        pencil_counts.append(pencils)

    assert chamber_counts == [3, 4, 2, 1, 2, 1]
    assert pencil_counts == [1, 0, 2, 4, 2, 4]
    assert sum(chamber_counts) == sum(pencil_counts) == 13
    # The removed pendant chamber has both slack edges at their lower degree.
    removed = (0, 0, 1, 1, 1, 1)
    assert not all(
        repeated_maximum(
            (
                -TYPES[0][0][k] + edge_value(removed, i, j),
                -TYPES[0][0][i] + edge_value(removed, j, k),
                -TYPES[0][0][j] + edge_value(removed, i, k),
            )
        )
        for i, j, k in combinations(range(4), 3)
    )
    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_SPLIT_FIBER_ATLAS_PASS "
        "chambers=3+4+2+1+2+1 pencils=1+0+2+4+2+4 mutation=1/1"
    )


if __name__ == "__main__":
    main()
