#!/usr/bin/env python3
"""Independently enumerate V4 subgroups and transpose orbits."""


def add(x, y):
    return (x[0] ^ y[0], x[1] ^ y[1])


def main():
    identity = (0, 0)
    elements = ((0, 0), (1, 0), (0, 1), (1, 1))
    nonzero = [x for x in elements if x != identity]
    subgroups = [{identity, x} for x in nonzero]
    assert len({frozenset(group) for group in subgroups}) == 3
    assert all(add(x, x) == identity for x in nonzero)

    transpose = lambda x: (x[1], x[0])
    coordinate = {(1, 0), (0, 1)}
    diagonal = (1, 1)
    assert {transpose(x) for x in coordinate} == coordinate
    assert transpose(diagonal) == diagonal
    print("audit=ok subgroups=3 coordinate_orbit=2 diagonal_fixed=1")


if __name__ == "__main__":
    main()
