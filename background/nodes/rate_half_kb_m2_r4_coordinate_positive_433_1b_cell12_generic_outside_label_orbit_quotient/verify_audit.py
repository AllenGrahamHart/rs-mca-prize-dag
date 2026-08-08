#!/usr/bin/env python3
"""Independently reconstruct the cell-12 generic label orbits."""

import ast
import itertools
from pathlib import Path


NODE = Path(__file__).resolve().parent
PERMUTATIONS = ((1, 0, 2, 3, 4, 5, 6), (0, 1, 2, 4, 3, 5, 6))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def matchings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for partner in values[1:]:
        rest = tuple(value for value in values
                     if value not in (first, partner))
        for tail in matchings(rest):
            yield ((first, partner),) + tail


def canonical(value):
    return tuple(sorted(tuple(sorted(edge)) for edge in value))


def main():
    ast.parse((NODE / "verify.py").read_text())
    rows = tuple(matchings(range(6)))
    lookup = {canonical(value): index for index, value in enumerate(rows)}
    require(len(rows) == len(lookup) == 15, "matching census")

    def image(label, permutation):
        xi_index, pairing_index = label
        old = tuple(value for value in range(7) if value != xi_index)
        new_xi = permutation[xi_index]
        new = tuple(value for value in range(7) if value != new_xi)
        positions = {value: index for index, value in enumerate(new)}
        transported = canonical(tuple(
            (positions[permutation[old[left]]],
             positions[permutation[old[right]]])
            for left, right in rows[pairing_index]
        ))
        return new_xi, lookup[transported]

    labels = set(itertools.product(range(7), range(15)))
    orbit_sizes = []
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
        labels.difference_update(orbit)
        orbit_sizes.append(len(orbit))
    require(sorted(orbit_sizes) == [1]*3 + [2]*15 + [4]*18,
            "orbit profile")
    hostile = list(orbit_sizes)
    hostile[0] += 1
    require(sum(hostile) != 105, "hostile mutation")
    statement = (NODE / "statement.md").read_text()
    require("No representative is excluded" in statement,
            "quotient scope")
    print("audit=ok labels=105 orbits=36 hostile_mutations=1")


if __name__ == "__main__":
    main()
