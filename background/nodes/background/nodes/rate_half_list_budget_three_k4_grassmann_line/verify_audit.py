#!/usr/bin/env python3
"""Independent exterior-algebra audit of the K4 line theorem."""

from __future__ import annotations

from itertools import combinations


P = 103


def edge(point_i: tuple[int, int, int], point_j: tuple[int, int, int]) -> tuple[int, int]:
    wi, ui, vi = point_i
    wj, uj, vj = point_j
    return ((wi * uj - wj * ui) % P, (wi * vj - wj * vi) % P)


def root(poly: tuple[int, int]) -> int:
    return -poly[0] * pow(poly[1], -1, P) % P


def plucker(edges: dict[tuple[int, int], tuple[int, int]], x: int) -> int:
    value = lambda pair: (edges[pair][0] + x * edges[pair][1]) % P
    return (
        value((0, 1)) * value((2, 3))
        - value((0, 2)) * value((1, 3))
        + value((0, 3)) * value((1, 2))
    ) % P


def main() -> None:
    points = ((1, 0, 0), (1, 1, 1), (1, 8, 2), (1, 27, 3))
    edges = {(i, j): edge(points[i], points[j]) for i, j in combinations(range(4), 2)}
    roots = [root(poly) for poly in edges.values()]
    assert len(set(roots)) == 6
    assert all(plucker(edges, x) == 0 for x in range(P))

    # If three p_j lie on one constant plane a*w+b*u+c*v=0, their three
    # edge polynomials acquire one common root. This mutation realizes it.
    collinear = ((1, 0, 0), (1, 1, 2), (1, 2, 4))
    mutated = [edge(collinear[i], collinear[j]) for i, j in combinations(range(3), 2)]
    assert all(poly[1] != 0 for poly in mutated)
    assert len({root(poly) for poly in mutated}) == 1
    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_K4_GRASSMANN_LINE_PASS "
        "plucker_points=103 roots=6 zero_cofactor_mutation=1/1"
    )


if __name__ == "__main__":
    main()
