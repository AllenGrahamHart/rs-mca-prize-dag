#!/usr/bin/env python3
"""Exact positive-coordinate common-loop skeleton census."""

import itertools


PROFILES = {
    (4, 4, 2): (1, 0, 2),
    (4, 3, 3): (0, 2, 1),
}


def permute(solution, permutation):
    loops, multiplicities = solution
    edge_values = {
        (0, 1): multiplicities[0],
        (0, 2): multiplicities[1],
        (1, 2): multiplicities[2],
    }
    return (
        tuple(loops[permutation[index]] for index in range(3)),
        tuple(
            edge_values[tuple(sorted((permutation[left], permutation[right])))]
            for left, right in ((0, 1), (0, 2), (1, 2))
        ),
    )


def profile_solutions(degrees):
    solutions = []
    for loops in itertools.product(range(2), repeat=3):
        for multiplicities in itertools.product(range(5), repeat=3):
            de, df, ef = multiplicities
            if sum(loops) + sum(multiplicities) != 5:
                continue
            observed = (
                2 * loops[0] + de + df,
                2 * loops[1] + de + ef,
                2 * loops[2] + df + ef,
            )
            if observed == degrees:
                solutions.append((loops, multiplicities))
    return tuple(solutions)


def orbit_census(degrees):
    permutation = PROFILES[degrees]
    solutions = set(profile_solutions(degrees))
    unseen = set(solutions)
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = {representative, permute(representative, permutation)}
        if not orbit <= solutions:
            raise RuntimeError("equal-degree swap closure")
        unseen -= orbit
        orbits.append((representative, len(orbit)))
    return tuple(sorted(orbits))


def verify():
    expected = {
        (4, 4, 2): (
            (((0, 0, 0), (3, 1, 1)), 1),
            (((0, 0, 1), (4, 0, 0)), 1),
            (((0, 1, 0), (2, 2, 0)), 2),
            (((1, 1, 0), (1, 1, 1)), 1),
            (((1, 1, 1), (2, 0, 0)), 1),
        ),
        (4, 3, 3): (
            (((0, 0, 0), (2, 2, 1)), 1),
            (((0, 0, 1), (3, 1, 0)), 2),
            (((1, 0, 0), (1, 1, 2)), 1),
            (((1, 0, 1), (2, 0, 1)), 2),
            (((1, 1, 1), (1, 1, 0)), 1),
        ),
    }
    for profile, expected_orbits in expected.items():
        observed = orbit_census(profile)
        if observed != expected_orbits:
            raise RuntimeError(f"{profile} orbit census {observed}")
    return expected


def main():
    result = verify()
    print(
        "RATE_HALF_KB_POSITIVE_LOOP_SKELETON_CENSUS_PASS "
        f"profiles={len(result)} labeled="
        f"{sum(sum(size for _, size in rows) for rows in result.values())} "
        f"orbits={sum(len(rows) for rows in result.values())}"
    )


if __name__ == "__main__":
    main()
