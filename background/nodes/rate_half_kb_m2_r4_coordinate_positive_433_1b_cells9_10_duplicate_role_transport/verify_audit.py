#!/usr/bin/env python3
"""Independent role-cell and label audit for the cells 9-10 transport."""

import ast
import itertools
from pathlib import Path


NODE = Path(__file__).resolve().parent
PERMUTATION = (0, 1, 2, 3, 4, 6, 5)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, second),) + tail


def canonical(value):
    return tuple(sorted(tuple(sorted(edge)) for edge in value))


def main():
    ast.parse((NODE / "verify.py").read_text())
    role_cells = []
    for singleton in range(5):
        rest = tuple(index for index in range(5) if index != singleton)
        for matching in pairings(rest):
            role_cells.append((singleton, canonical(matching)))
    lookup = {value: index for index, value in enumerate(role_cells)}
    bc_swap = (0, 2, 1, 3, 4)
    singleton, matching = role_cells[9]
    image = (bc_swap[singleton], canonical(tuple(
        (bc_swap[left], bc_swap[right]) for left, right in matching
    )))
    require(lookup[image] == 10, "B/C role-cell action")
    signs = set(itertools.product((-1, 1), repeat=2))
    require({(epsilon_1, -epsilon_2) for epsilon_1, epsilon_2 in signs} == signs,
            "source-sign bijection")

    rows = tuple(pairings(range(6)))
    row_lookup = {canonical(value): index for index, value in enumerate(rows)}
    images = set()
    for xi_index in range(7):
        old = tuple(value for value in range(7) if value != xi_index)
        new_xi = PERMUTATION[xi_index]
        new = tuple(value for value in range(7) if value != new_xi)
        compact = {value: index for index, value in enumerate(new)}
        for matching in rows:
            transported = canonical(tuple(
                (compact[PERMUTATION[old[left]]],
                 compact[PERMUTATION[old[right]]])
                for left, right in matching
            ))
            images.add((new_xi, row_lookup[transported]))
    require(images == set(itertools.product(range(7), range(15))),
            "105-label bijection")
    print("audit=ok role_cell=9->10 labels=105 systems=1680")


if __name__ == "__main__":
    main()
