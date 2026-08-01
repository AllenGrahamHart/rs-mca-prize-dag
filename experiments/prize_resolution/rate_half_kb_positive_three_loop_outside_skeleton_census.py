#!/usr/bin/env python3
"""Outside-edge census for positive coordinate three-loop packets."""

import itertools
import math


def permute(solution, permutation):
    colored, multiplicities = solution
    edge_values = {
        (0, 1): multiplicities[0],
        (0, 2): multiplicities[1],
        (1, 2): multiplicities[2],
    }
    return (
        tuple(colored[permutation[index]] for index in range(3)),
        tuple(
            edge_values[tuple(sorted((permutation[left], permutation[right])))]
            for left, right in ((0, 1), (0, 2), (1, 2))
        ),
    )


def minimum_cross_defect(multiplicity):
    """Two signed deck-orbit types each repeat two target edges."""
    return min(
        2 * math.comb(positive, 2) + 2 * math.comb(multiplicity - positive, 2)
        for positive in range(multiplicity + 1)
    )


def census():
    solutions = []
    for colored in itertools.product(range(3), repeat=3):
        if sum(colored) != 2:
            continue
        for multiplicities in itertools.product(range(6), repeat=3):
            de, df, ef = multiplicities
            if sum(multiplicities) != 5:
                continue
            degrees = (
                colored[0] + de + df,
                colored[1] + de + ef,
                colored[2] + df + ef,
            )
            if degrees == (4, 4, 4):
                solutions.append((colored, multiplicities))

    unseen = set(solutions)
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = {
            permute(representative, permutation)
            for permutation in itertools.permutations(range(3))
        }
        if not orbit <= set(solutions):
            raise RuntimeError("permutation closure")
        unseen -= orbit
        orbits.append((representative, len(orbit)))
    return tuple(solutions), tuple(sorted(orbits))


def verify():
    solutions, orbits = census()
    expected = (
        (((0, 0, 2), (3, 1, 1)), 3),
        (((0, 1, 1), (2, 2, 1)), 3),
    )
    if len(solutions) != 6 or orbits != expected:
        raise RuntimeError(f"outside census {orbits}")
    costs = tuple(
        sum(minimum_cross_defect(value) for value in multiplicities)
        for (_, multiplicities), _ in orbits
    )
    if costs != (2, 0):
        raise RuntimeError(f"defect costs {costs}")
    return solutions, orbits, costs


def main():
    _, orbits, costs = verify()
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_OUTSIDE_CENSUS_PASS "
        f"raw=6 orbits={len(orbits)} sizes="
        f"{','.join(str(size) for _, size in orbits)} "
        f"extra_defect={','.join(map(str, costs))} survivors=1"
    )


if __name__ == "__main__":
    main()
