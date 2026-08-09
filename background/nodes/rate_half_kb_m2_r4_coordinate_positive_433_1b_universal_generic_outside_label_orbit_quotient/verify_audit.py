#!/usr/bin/env python3
"""Independently reconstruct the universal label orbits."""

import itertools
from pathlib import Path


NODE = Path(__file__).resolve().parent
PERMUTATIONS = ((1, 0, 2, 3, 4, 5, 6), (0, 1, 2, 4, 3, 5, 6))


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for partner in values[1:]:
        rest = tuple(value for value in values if value not in (first, partner))
        for tail in pairings(rest):
            yield ((first, partner),) + tail


def canonical(value):
    return tuple(sorted(tuple(sorted(edge)) for edge in value))


def main():
    rows = tuple(pairings(range(6)))
    lookup = {canonical(value): index for index, value in enumerate(rows)}

    def image(label, permutation):
        xi_index, pairing_index = label
        old = tuple(value for value in range(7) if value != xi_index)
        new_xi = permutation[xi_index]
        new = tuple(value for value in range(7) if value != new_xi)
        positions = {value: index for index, value in enumerate(new)}
        transported = canonical(
            (positions[permutation[old[left]]],
             positions[permutation[old[right]]])
            for left, right in rows[pairing_index]
        )
        return new_xi, lookup[transported]

    labels = set(itertools.product(range(7), range(15)))
    orbits = []
    while labels:
        orbit = {min(labels)}
        frontier = list(orbit)
        while frontier:
            label = frontier.pop()
            for permutation in PERMUTATIONS:
                transported = image(label, permutation)
                if transported not in orbit:
                    orbit.add(transported)
                    frontier.append(transported)
        labels -= orbit
        orbits.append(orbit)
    endpoint = [orbit for orbit in orbits if next(iter(orbit))[0] in (5, 6)]
    active = [orbit for orbit in orbits if next(iter(orbit))[0] not in (5, 6)]
    profiles = lambda values: [sum(len(orbit) == size for orbit in values)
                               for size in (1, 2, 4)]
    if (len(orbits), profiles(orbits), len(endpoint), profiles(endpoint),
            len(active), profiles(active)) != (36, [3, 15, 18], 12,
                                                [2, 6, 4], 24, [1, 9, 14]):
        raise RuntimeError("orbit profile")
    if "No representative is excluded" not in (NODE / "statement.md").read_text():
        raise RuntimeError("scope marker")
    print("audit=ok full=105/36 endpoint=30/12 active=75/24")


if __name__ == "__main__":
    main()
