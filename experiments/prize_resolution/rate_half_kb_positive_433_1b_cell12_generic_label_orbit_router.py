#!/usr/bin/env python3
"""Quotient the 105 cell-12 outside labels by universal record symmetries."""

import hashlib
import itertools
import json


POSITIVE_DE_SWAP = (1, 0, 2, 3, 4, 5, 6)
OUTSIDE_DE_SWAP = (0, 1, 2, 4, 3, 5, 6)


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


MATCHINGS = tuple(pairings(range(6)))
MATCHING_INDEX = {
    tuple(sorted(tuple(sorted(edge)) for edge in matching)): index
    for index, matching in enumerate(MATCHINGS)
}


def act(label, permutation):
    xi_index, pairing_index = label
    old_residual = tuple(index for index in range(7) if index != xi_index)
    new_xi = permutation[xi_index]
    new_residual = tuple(index for index in range(7) if index != new_xi)
    compact = {value: index for index, value in enumerate(new_residual)}
    matching = tuple(sorted(
        tuple(sorted((
            compact[permutation[old_residual[left]]],
            compact[permutation[old_residual[right]]],
        )))
        for left, right in MATCHINGS[pairing_index]
    ))
    return new_xi, MATCHING_INDEX[matching]


def main():
    require(len(MATCHINGS) == 15 and len(MATCHING_INDEX) == 15,
            "matching census")
    labels = set(itertools.product(range(7), range(15)))
    orbits = []
    while labels:
        seed = min(labels)
        orbit = {seed}
        queue = [seed]
        while queue:
            label = queue.pop()
            for permutation in (POSITIVE_DE_SWAP, OUTSIDE_DE_SWAP):
                image = act(label, permutation)
                if image not in orbit:
                    orbit.add(image)
                    queue.append(image)
        labels -= orbit
        orbits.append(sorted(orbit))
    require(sum(map(len, orbits)) == 105 and len(orbits) == 36,
            "orbit cover")
    size_profile = {
        size: sum(len(orbit) == size for orbit in orbits)
        for size in (1, 2, 4)
    }
    require(size_profile == {1: 3, 2: 15, 4: 18}, "orbit sizes")
    canonical = json.dumps(orbits, separators=(",", ":"))
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_CELL12_LABEL_ORBIT_ROUTER_PASS "
        f"labels=105 orbits=36 sizes=1:3,2:15,4:18 "
        f"sha256={hashlib.sha256(canonical.encode()).hexdigest()}"
    )


if __name__ == "__main__":
    main()
