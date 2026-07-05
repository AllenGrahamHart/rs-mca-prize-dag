#!/usr/bin/env python3
"""Weighted finite inclusion-exclusion check."""

from __future__ import annotations

from itertools import combinations


def powerset(items):
    items = list(items)
    for r in range(len(items) + 1):
        for combo in combinations(items, r):
            yield combo


def weight(objects: set[int], weights: dict[int, int]) -> int:
    return sum(weights[obj] for obj in objects)


def inclusion_exclusion(
    universe: set[int], events: list[set[int]], weights: dict[int, int]
) -> int:
    total = 0
    for subset in powerset(range(len(events))):
        if subset:
            intersection = set.intersection(*(events[i] for i in subset))
        else:
            intersection = universe
        total += (-1) ** len(subset) * weight(intersection, weights)
    return total


def main() -> None:
    universe = set(range(9))
    weights = {i: (i * i + 3 * i + 1) % 7 + 1 for i in universe}
    event_families = [
        [{0, 1, 4, 7}, {2, 4, 6}, {1, 3, 5, 7}],
        [{0, 2, 8}, {0, 1, 2, 3}, {5, 6}, {2, 6, 7, 8}],
    ]

    for events in event_families:
        direct = weight(universe - set.union(*events), weights)
        assert inclusion_exclusion(universe, events, weights) == direct

    print("PASS: weighted lower-scale inclusion-exclusion")


if __name__ == "__main__":
    main()
