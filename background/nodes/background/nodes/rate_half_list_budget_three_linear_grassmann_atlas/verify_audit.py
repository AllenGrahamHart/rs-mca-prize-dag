#!/usr/bin/env python3
"""Independent degree-pattern audit of the linear Grassmann atlas."""

from __future__ import annotations

from itertools import combinations


EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
ROWS = (
    ((0, 0, 1, 1, 1, 2), (0, 0, 1, 1, 2, 1), (0, 0, 1, 1, 2, 2)),
    ((0, 1, 1, 1, 1, 0), (0, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 0), (1, 1, 1, 1, 1, 1)),
    ((0, 1, 1, 1, 1, 1), (0, 1, 1, 1, 1, 2)),
    ((1, 1, 1, 1, 1, 1),),
    ((0, 1, 0, 1, 0, 0), (0, 1, 0, 1, 0, 1)),
    ((1, 1, 0, 1, 0, 0),),
)


def triangle(row: tuple[int, ...], omitted: int) -> tuple[int, ...]:
    vertices = [value for value in range(4) if value != omitted]
    return tuple(row[EDGES.index(edge)] for edge in combinations(vertices, 2))


def zero_cofactor_allowed(pattern: tuple[int, ...]) -> bool:
    return pattern == (0, 0, 0) or pattern == (1, 1, 1)


def main() -> None:
    linear_rows = [row for family in ROWS for row in family if max(row) <= 1]
    quadratic_rows = [row for family in ROWS for row in family if max(row) == 2]
    assert (len(linear_rows), len(quadratic_rows)) == (9, 4)

    zero_candidates = []
    for family_index, family in enumerate(ROWS):
        for row in family:
            if max(row) > 1:
                continue
            for omitted in range(4):
                pattern = triangle(row, omitted)
                if zero_cofactor_allowed(pattern):
                    zero_candidates.append((family_index, omitted, pattern))

    constant_candidates = [item for item in zero_candidates if item[2] == (0, 0, 0)]
    assert constant_candidates == [(4, 2, (0, 0, 0)), (4, 2, (0, 0, 0))]
    assert all(item[0] in (1, 2, 3, 4, 5) for item in zero_candidates)
    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_LINEAR_GRASSMANN_ATLAS_PASS "
        "linear=9 quadratic=4 path_zero_support=2/2"
    )


if __name__ == "__main__":
    main()
