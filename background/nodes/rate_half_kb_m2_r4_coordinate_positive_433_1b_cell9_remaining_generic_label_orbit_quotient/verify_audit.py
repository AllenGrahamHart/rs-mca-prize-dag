#!/usr/bin/env python3
"""Independent active-subset audit for the cell-9 quotient."""

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
    for index in range(1, len(values)):
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, values[index]),) + tail


def canonical(value):
    return tuple(sorted(tuple(sorted(edge)) for edge in value))


def main():
    matchings = tuple(pairings(range(6)))
    lookup = {canonical(value): index for index, value in enumerate(matchings)}

    def image(label, permutation):
        xi, pairing = label
        old = tuple(value for value in range(7) if value != xi)
        new_xi = permutation[xi]
        new = tuple(value for value in range(7) if value != new_xi)
        positions = {value: index for index, value in enumerate(new)}
        edges = canonical(
            (positions[permutation[old[left]]],
             positions[permutation[old[right]]])
            for left, right in matchings[pairing]
        )
        return new_xi, lookup[edges]

    labels = set(itertools.product(range(5), range(15)))
    sizes = []
    while labels:
        orbit = {min(labels)}
        queue = list(orbit)
        while queue:
            label = queue.pop()
            for permutation in PERMUTATIONS:
                value = image(label, permutation)
                if value not in orbit:
                    if value[0] >= 5:
                        raise RuntimeError("active subset not invariant")
                    orbit.add(value)
                    queue.append(value)
        labels -= orbit
        sizes.append(len(orbit))
    if sorted(sizes) != [1] + [2] * 9 + [4] * 14:
        raise RuntimeError("active orbit profile")
    if "No one of the 24 representatives is excluded" not in (NODE / "statement.md").read_text():
        raise RuntimeError("scope marker")
    print("audit=ok active_labels=75 active_orbits=24")


if __name__ == "__main__":
    main()
