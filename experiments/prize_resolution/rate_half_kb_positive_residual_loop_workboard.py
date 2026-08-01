#!/usr/bin/env python3
"""Exact residual loop workboard for positive coordinate packets."""

import itertools
import math


COMMON_ORBITS = (
    ("442-0a", "442", (0, 0, 0), (3, 1, 1), 1),
    ("442-1a", "442", (0, 0, 1), (4, 0, 0), 1),
    ("442-1b", "442", (0, 1, 0), (2, 2, 0), 2),
    ("442-2", "442", (1, 1, 0), (1, 1, 1), 1),
    ("442-3", "442", (1, 1, 1), (2, 0, 0), 1),
    ("433-0", "433", (0, 0, 0), (2, 2, 1), 1),
    ("433-1a", "433", (0, 0, 1), (3, 1, 0), 2),
    ("433-1b", "433", (1, 0, 0), (1, 1, 2), 1),
    ("433-2", "433", (1, 0, 1), (2, 0, 1), 2),
    ("433-3", "433", (1, 1, 1), (1, 1, 0), 1),
)


def minimum_cross_defect(multiplicity):
    """Minimum defect after splitting an orbit count between two signs."""
    return min(
        2 * math.comb(positive, 2)
        + 2 * math.comb(multiplicity - positive, 2)
        for positive in range(multiplicity + 1)
    )


def common_defect(loops, multiplicities):
    return sum(loops) + sum(
        minimum_cross_defect(value) for value in multiplicities
    )


def permute_outside(solution, permutation):
    colored, loops, multiplicities = solution
    edge_values = {
        (0, 1): multiplicities[0],
        (0, 2): multiplicities[1],
        (1, 2): multiplicities[2],
    }
    return (
        tuple(colored[permutation[index]] for index in range(3)),
        tuple(loops[permutation[index]] for index in range(3)),
        tuple(
            edge_values[tuple(sorted((permutation[left], permutation[right])))]
            for left, right in ((0, 1), (0, 2), (1, 2))
        ),
    )


def outside_census(loop_count):
    solutions = []
    for colored in itertools.product(range(3), repeat=3):
        if sum(colored) != 2:
            continue
        for loops in itertools.product(range(2), repeat=3):
            if sum(loops) != loop_count:
                continue
            for multiplicities in itertools.product(range(6), repeat=3):
                de, df, ef = multiplicities
                if sum(multiplicities) + loop_count != 5:
                    continue
                degrees = (
                    colored[0] + 2 * loops[0] + de + df,
                    colored[1] + 2 * loops[1] + de + ef,
                    colored[2] + 2 * loops[2] + df + ef,
                )
                if degrees == (4, 4, 4):
                    solutions.append((colored, loops, multiplicities))

    solution_set = set(solutions)
    unseen = set(solutions)
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = {
            permute_outside(representative, permutation)
            for permutation in itertools.permutations(range(3))
        }
        if not orbit <= solution_set:
            raise RuntimeError("outside permutation closure")
        unseen -= orbit
        defect = sum(representative[1]) + sum(
            minimum_cross_defect(value) for value in representative[2]
        )
        orbits.append((representative, len(orbit), defect))
    return tuple(solutions), tuple(sorted(orbits))


def residual_workboard():
    common_rows = []
    for name, profile, loops, multiplicities, orbit_size in COMMON_ORBITS:
        loop_count = sum(loops)
        defect = common_defect(loops, multiplicities)
        reason = "live"
        if loop_count > 1:
            reason = "global-loop-cap"
        elif defect > 3:
            reason = "common-defect-budget"
        common_rows.append(
            {
                "name": name,
                "profile": profile,
                "loops": loops,
                "multiplicities": multiplicities,
                "orbit_size": orbit_size,
                "loop_count": loop_count,
                "common_defect": defect,
                "reason": reason,
            }
        )

    outside = {count: outside_census(count) for count in (0, 1)}
    routed = []
    for row in common_rows:
        if row["reason"] != "live":
            continue
        allowance = 1 - row["loop_count"]
        admissible = []
        for outside_loops in range(allowance + 1):
            for representative, orbit_size, defect in outside[outside_loops][1]:
                if row["common_defect"] + defect <= 3:
                    admissible.append(
                        (outside_loops, representative, orbit_size, defect)
                    )
        if not admissible:
            raise RuntimeError(f"live common row has no outside route: {row['name']}")
        routed.append((row["name"], tuple(admissible)))
    return tuple(common_rows), outside, tuple(routed)


def verify():
    common_rows, outside, routed = residual_workboard()
    live = tuple(row["name"] for row in common_rows if row["reason"] == "live")
    if live != ("442-0a", "442-1b", "433-0", "433-1a", "433-1b"):
        raise RuntimeError(f"live common rows {live}")
    reasons = {row["name"]: row["reason"] for row in common_rows}
    if reasons["442-1a"] != "common-defect-budget":
        raise RuntimeError("multiplicity-four common row not deleted")
    if sum(row["orbit_size"] for row in common_rows if row["reason"] == "live") != 7:
        raise RuntimeError("live labeled common count")
    if tuple(len(outside[count][0]) for count in (0, 1)) != (6, 18):
        raise RuntimeError("raw outside counts")
    if tuple(len(outside[count][1]) for count in (0, 1)) != (2, 4):
        raise RuntimeError("outside orbit counts")
    route_counts = {name: len(routes) for name, routes in routed}
    if route_counts != {
        "442-0a": 3,
        "442-1b": 2,
        "433-0": 5,
        "433-1a": 1,
        "433-1b": 2,
    }:
        raise RuntimeError(f"route counts {route_counts}")
    return common_rows, outside, routed


def main():
    common_rows, outside, routed = verify()
    live = [row for row in common_rows if row["reason"] == "live"]
    print(
        "RATE_HALF_KB_POSITIVE_RESIDUAL_LOOP_WORKBOARD_PASS "
        f"common_orbits={len(common_rows)} live_orbits={len(live)} "
        f"live_labeled={sum(row['orbit_size'] for row in live)} "
        f"outside_raw={len(outside[0][0])},{len(outside[1][0])} "
        f"outside_orbits={len(outside[0][1])},{len(outside[1][1])} "
        f"routed_records={sum(len(routes) for _, routes in routed)}"
    )


if __name__ == "__main__":
    main()
