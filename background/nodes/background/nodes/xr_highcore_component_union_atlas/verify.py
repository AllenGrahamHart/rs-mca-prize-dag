#!/usr/bin/env python3
"""Replay the canonical component atlas and its integer GRK ledger."""

from __future__ import annotations

from collections import deque
from itertools import combinations, product
from math import comb


ErrorSet = tuple[int, ...]
RaySystem = dict[int, tuple[ErrorSet, ...]]


def witnesses(
    rays: RaySystem, left: int, right: int, redundancy: int
) -> tuple[tuple[ErrorSet, ErrorSet], ...]:
    return tuple(
        sorted(
            (a, b)
            for a in rays[left]
            for b in rays[right]
            if len(set(a) | set(b)) == redundancy
        )
    )


def component_atlas(
    rays: RaySystem, redundancy: int
) -> tuple[dict[str, object], ...]:
    slopes = sorted(rays)
    adjacency = {slope: set() for slope in slopes}
    for index, left in enumerate(slopes):
        for right in slopes[index + 1 :]:
            if witnesses(rays, left, right, redundancy):
                adjacency[left].add(right)
                adjacency[right].add(left)

    high = {slope for slope in slopes if adjacency[slope]}
    unseen = set(high)
    atlas: list[dict[str, object]] = []
    while unseen:
        root = min(unseen)
        parent: dict[int, int | None] = {root: None}
        queue = deque([root])
        tree_edges: list[tuple[int, int]] = []
        while queue:
            left = queue.popleft()
            for right in sorted(adjacency[left]):
                if right in parent:
                    continue
                parent[right] = left
                tree_edges.append((left, right))
                queue.append(right)

        component = tuple(sorted(parent))
        unseen.difference_update(component)
        if not tree_edges:
            raise AssertionError("a high-core component must contain an edge")

        selected: dict[int, ErrorSet] = {}
        first_left, first_right = tree_edges[0]
        first_pair = witnesses(rays, first_left, first_right, redundancy)[0]
        selected[first_left], selected[first_right] = first_pair
        for left, right in tree_edges[1:]:
            selected[right] = witnesses(rays, left, right, redundancy)[0][1]

        if set(selected) != set(component):
            raise AssertionError((component, selected))
        union = tuple(sorted(set().union(*(set(error) for error in selected.values()))))
        if len(union) < redundancy:
            raise AssertionError((component, union))
        for slope, error in selected.items():
            if error not in rays[slope] or not set(error) <= set(union):
                raise AssertionError((slope, error, union))
        atlas.append(
            {
                "slopes": component,
                "selected": selected,
                "union": union,
                "excess": len(union) - redundancy,
            }
        )

    covered = [slope for chart in atlas for slope in chart["slopes"]]
    if len(covered) != len(set(covered)) or set(covered) != high:
        raise AssertionError((covered, high))
    return tuple(atlas)


def structural_replay() -> int:
    # Exhaust every one-ray-per-slope system on a small domain.
    domain = range(6)
    errors = ((),) + tuple((x,) for x in domain) + tuple(combinations(domain, 2))
    checked = 0
    for selected in product(errors, repeat=3):
        rays = {slope: (error,) for slope, error in enumerate(selected)}
        atlas = component_atlas(rays, redundancy=3)
        high = {
            slope
            for slope in rays
            if any(
                other != slope
                and len(set(rays[slope][0]) | set(rays[other][0])) == 3
                for other in rays
            )
        }
        if sum(len(chart["slopes"]) for chart in atlas) != len(high):
            raise AssertionError((selected, atlas, high))
        checked += 1
    return checked


def multiray_and_ledger_replay() -> tuple[int, int]:
    rays: RaySystem = {
        0: ((0, 1, 2),),
        1: ((1, 2, 3), (30, 31, 32)),
        2: ((2, 3, 4),),
        3: ((10, 11, 12),),
        4: ((10, 11, 13),),
        5: ((20, 21, 22),),
    }
    redundancy, reserve = 4, 1
    atlas = component_atlas(rays, redundancy)
    profiles = tuple((chart["slopes"], chart["excess"]) for chart in atlas)
    if profiles != (((0, 1, 2), 1), ((3, 4), 0)):
        raise AssertionError(profiles)

    bound_sum = 0
    for chart in atlas:
        excess = int(chart["excess"])
        bound = comb(redundancy + excess, excess) * redundancy // comb(
            excess + reserve, excess
        )
        if len(chart["slopes"]) > bound:
            raise AssertionError((chart, bound))
        bound_sum += bound

    # The tempting edge atlas is not a partition: slope 1 is paid twice.
    edge_charts = ((0, 1), (1, 2), (3, 4))
    edge_cover = [slope for chart in edge_charts for slope in chart]
    if len(edge_cover) == len(set(edge_cover)):
        raise AssertionError("edge-atlas deduplication mutation survived")
    return len(atlas), bound_sum


def main() -> None:
    checked = structural_replay()
    components, bound_sum = multiray_and_ledger_replay()
    print(
        "XR_HIGHCORE_COMPONENT_UNION_ATLAS_PASS "
        f"systems={checked} components={components} grk_sum={bound_sum}"
    )


if __name__ == "__main__":
    main()
