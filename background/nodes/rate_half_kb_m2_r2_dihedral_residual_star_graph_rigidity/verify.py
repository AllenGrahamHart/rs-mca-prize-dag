#!/usr/bin/env python3
"""Verify the residual n=3,6 dihedral source-star graph rigidity."""

from __future__ import annotations

from collections import Counter, defaultdict


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def canonical_pair(left: tuple, right: tuple) -> tuple[tuple, tuple]:
    return tuple(sorted((left, right)))


def dihedral_incidence(n: int) -> list[tuple[int, int]]:
    # Regular D_n orbit: u(i,e)=(-i,1-e), v(i,e)=(1-i,1-e).
    points = [(i, e) for i in range(n) for e in (0, 1)]

    def u(point: tuple[int, int]) -> tuple[int, int]:
        i, e = point
        return ((-i) % n, 1 - e)

    def v(point: tuple[int, int]) -> tuple[int, int]:
        i, e = point
        return ((1 - i) % n, 1 - e)

    def orbit_pair(point: tuple[int, int], involution) -> frozenset:
        return frozenset((point, involution(point)))

    y_fibers = sorted({orbit_pair(point, u) for point in points}, key=repr)
    z_fibers = sorted({orbit_pair(point, v) for point in points}, key=repr)
    y_index = {fiber: index for index, fiber in enumerate(y_fibers)}
    neighborhoods = []
    for z_fiber in z_fibers:
        adjacent = sorted({y_index[orbit_pair(point, u)] for point in z_fiber})
        require(len(adjacent) == 2, "a Z fiber must meet two Y fibers")
        neighborhoods.append(tuple(adjacent))
    require(len(set(neighborhoods)) == n, "cycle neighborhoods must be distinct")

    degrees = Counter(vertex for edge in neighborhoods for vertex in edge)
    require(set(degrees.values()) == {2}, "Y incidence must be a cycle")
    return neighborhoods


def source_graph(n: int) -> tuple[Counter, Counter]:
    pole_count = 6 // n
    stars: Counter = Counter()
    label_degrees: Counter = Counter()
    for pole in range(pole_count):
        for left, right in dihedral_incidence(n):
            labels_left = [(pole, left, sign) for sign in (0, 1)]
            labels_right = [(pole, right, sign) for sign in (0, 1)]

            # One endpoint lift gives one orientation and its tau image.
            first = [
                canonical_pair(labels_left[0], labels_right[0]),
                canonical_pair(labels_left[1], labels_right[1]),
            ]
            # c eta c^-1=eta*a forces the complementary orientation.
            second = [
                canonical_pair(labels_left[0], labels_right[1]),
                canonical_pair(labels_left[1], labels_right[0]),
            ]
            for star in first + second:
                stars[star] += 1
                for label in star:
                    label_degrees[label] += 1
    return stars, label_degrees


def verify() -> None:
    for n in (3, 6):
        neighborhoods = dihedral_incidence(n)
        require(len(neighborhoods) == n, "wrong quotient-fiber count")
        stars, label_degrees = source_graph(n)
        require(sum(stars.values()) == 24, "complete source mass must be 24")
        require(len(stars) == 24, "every residual star must be distinct")
        require(set(stars.values()) == {1}, "all star weights must be one")
        require(len(label_degrees) == 12, "there must be twelve source labels")
        require(set(label_degrees.values()) == {4}, "every source row is quartic")
        defect = sum(weight * (weight - 1) // 2 for weight in stars.values())
        require(defect == 0, "residual graph must have zero defect")

        components: defaultdict[int, set[int]] = defaultdict(set)
        for pole in range(6 // n):
            for left, right in neighborhoods:
                components[pole].update((left, right))
        require(len(components) == 6 // n, "wrong number of pole components")
        require(all(len(vertices) == n for vertices in components.values()), "wrong component order")


if __name__ == "__main__":
    verify()
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_RESIDUAL_STAR_GRAPH_RIGIDITY_PASS")
