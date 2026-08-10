#!/usr/bin/env python3
"""Quotient repeated-BC cell-3 outside labels by the target D-sign action."""

from collections import Counter
import hashlib
import itertools
import json

import sympy as sp


RECORDS = ("BE", "CF", "DE+", "DE-", "DF+", "DF-", "EF")
D_SIGN_FLIP = (0, 1, 3, 2, 5, 4, 6)


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
    tuple(sorted(tuple(sorted(pair)) for pair in matching)): index
    for index, matching in enumerate(MATCHINGS)
}


def canonical_matching(matching):
    return tuple(sorted(tuple(sorted(pair)) for pair in matching))


def act(label, permutation=D_SIGN_FLIP):
    xi_index, pairing_index = label
    old_residual = tuple(index for index in range(7) if index != xi_index)
    new_xi = permutation[xi_index]
    new_residual = tuple(index for index in range(7) if index != new_xi)
    compact = {record: index for index, record in enumerate(new_residual)}
    image = canonical_matching(tuple(
        (
            compact[permutation[old_residual[left]]],
            compact[permutation[old_residual[right]]],
        )
        for left, right in MATCHINGS[pairing_index]
    ))
    return new_xi, MATCHING_INDEX[image]


def compile_orbits():
    labels = set(itertools.product(range(7), range(15)))
    orbits = []
    while labels:
        seed = min(labels)
        orbit = tuple(sorted({seed, act(seed)}))
        require(all(act(act(label)) == label for label in orbit), "involution")
        labels -= set(orbit)
        orbits.append(orbit)
    return tuple(orbits)


def profile(orbits):
    counts = Counter(map(len, orbits))
    return {size: counts[size] for size in (1, 2, 4)}


def digest(orbits):
    canonical = json.dumps(orbits, separators=(",", ":"))
    return hashlib.sha256(canonical.encode()).hexdigest()


def main():
    require(len(MATCHINGS) == len(MATCHING_INDEX) == 15, "matching census")
    require(tuple(RECORDS[index] for index in D_SIGN_FLIP) ==
            ("BE", "CF", "DE-", "DE+", "DF-", "DF+", "EF"),
            "record action")
    b, c, d, e, f, sigma = sp.symbols("b c d e f sigma")
    products = (b*e, c*f, d*e, -d*e, d*f, -d*f, sigma*e*f)
    sums = ((b+e)**2, (c+f)**2, (d+e)**2, (d-e)**2,
            (d+f)**2, (d-f)**2, (e+sigma*f)**2)
    transformed_products = tuple(sp.expand(value.subs(d, -d, simultaneous=True))
                                 for value in products)
    transformed_sums = tuple(sp.expand(value.subs(d, -d, simultaneous=True))
                             for value in sums)
    require(all(sp.expand(transformed_products[index]
                          - products[D_SIGN_FLIP[index]]) == 0
                for index in range(7)), "product action")
    require(all(sp.expand(transformed_sums[index]
                          - sums[D_SIGN_FLIP[index]]) == 0
                for index in range(7)), "squared-sum action")
    orbits = compile_orbits()
    require(sum(map(len, orbits)) == 105, "label cover")
    orbit_profile = profile(orbits)
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL3_OUTSIDE_ROUTER_PASS "
        f"labels=105 orbits={len(orbits)} profile={orbit_profile} "
        f"sha256={digest(orbits)}"
    )


if __name__ == "__main__":
    main()
