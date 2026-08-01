#!/usr/bin/env python3
"""Exact outside-edge census for the negative zero-loop 433 skeleton."""

import itertools


def permute(solution, permutation):
    colored, loops, multiplicities = solution
    colored_out = tuple(colored[permutation[index]] for index in range(3))
    loops_out = tuple(loops[permutation[index]] for index in range(3))
    edge_values = {
        (0, 1): multiplicities[0],
        (0, 2): multiplicities[1],
        (1, 2): multiplicities[2],
    }
    multiplicities_out = []
    for left, right in ((0, 1), (0, 2), (1, 2)):
        old_edge = tuple(sorted((permutation[left], permutation[right])))
        multiplicities_out.append(edge_values[old_edge])
    return colored_out, loops_out, tuple(multiplicities_out)


def census():
    solutions = []
    for colored in itertools.product(range(3), repeat=3):
        if sum(colored) != 2:
            continue
        for loops in itertools.product(range(2), repeat=3):
            if sum(loops) > 2:
                continue
            for multiplicities in itertools.product(range(3), repeat=3):
                de, df, ef = multiplicities
                if sum(loops) + sum(multiplicities) != 5:
                    continue
                degrees = (
                    2 * loops[0] + de + df,
                    2 * loops[1] + de + ef,
                    2 * loops[2] + df + ef,
                )
                if any(
                    degrees[index] != 4 - colored[index]
                    for index in range(3)
                ):
                    continue
                solutions.append((colored, loops, multiplicities))

    solution_set = set(solutions)
    unseen = set(solutions)
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = {
            permute(representative, permutation)
            for permutation in itertools.permutations(range(3))
        }
        if not orbit <= solution_set:
            raise RuntimeError("permutation closure")
        unseen -= orbit
        orbits.append((representative, len(orbit)))
    return solutions, sorted(orbits)


def verify():
    solutions, orbits = census()
    expected = (
        (((0, 0, 2), (0, 1, 0), (2, 2, 0)), 6),
        (((0, 0, 2), (1, 1, 0), (1, 1, 1)), 3),
        (((0, 1, 1), (0, 0, 0), (2, 2, 1)), 3),
        (((0, 1, 1), (1, 0, 0), (1, 1, 2)), 3),
        (((0, 1, 1), (1, 0, 1), (2, 0, 1)), 6),
    )
    if len(solutions) != 21:
        raise RuntimeError("labeled solution count")
    if tuple(orbits) != expected:
        raise RuntimeError(f"orbit census {orbits}")
    return solutions, orbits


def main():
    _, orbits = verify()
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_OUTSIDE_SKELETON_PASS "
        f"labeled=21 orbits={len(orbits)} sizes="
        + ",".join(str(size) for _, size in orbits)
    )


if __name__ == "__main__":
    main()
