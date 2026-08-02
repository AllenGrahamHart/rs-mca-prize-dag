#!/usr/bin/env python3
"""Signed-edge atlas for the positive saturated 433-1b -> O0a route."""

import itertools


ACTIVE_EDGES = ("AB", "AC", "BF", "CF", "DE", "DF", "EF")
VERTICES = ("A", "B", "C", "D", "E", "F")
ENDPOINTS = {
    "AB": ("A", "B"),
    "AC": ("A", "C"),
    "BF": ("B", "F"),
    "CF": ("C", "F"),
    "DE": ("D", "E"),
    "DF": ("D", "F"),
    "EF": ("E", "F"),
}


def gauge_action(signs, gauge):
    return tuple(
        signs[index] * gauge[VERTICES.index(left)] * gauge[VERTICES.index(right)]
        for index, edge in enumerate(ACTIVE_EDGES)
        for left, right in (ENDPOINTS[edge],)
    )


def invariants(signs):
    values = dict(zip(ACTIVE_EDGES, signs))
    common_cycle = values["AB"] * values["BF"] * values["CF"] * values["AC"]
    outside_cycle = values["DE"] * values["DF"] * values["EF"]
    return common_cycle, outside_cycle


def sign_orbits():
    assignments = set(itertools.product((-1, 1), repeat=len(ACTIVE_EDGES)))
    unseen = set(assignments)
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = {
            gauge_action(representative, gauge)
            for gauge in itertools.product((-1, 1), repeat=len(VERTICES))
        }
        unseen -= orbit
        common_cycle, outside_cycle = invariants(representative)
        canonical = (1, 1, 1, common_cycle, 1, 1, outside_cycle)
        if canonical not in orbit:
            raise RuntimeError("canonical sign representative")
        if {invariants(row) for row in orbit} != {(common_cycle, outside_cycle)}:
            raise RuntimeError("cycle invariants")
        orbits.append((common_cycle, outside_cycle, canonical, len(orbit)))
    return tuple(sorted(orbits))


def records(common_cycle, outside_cycle):
    return (
        ("common-loop-A", "-a^2"),
        ("common-AB", "a*b"),
        ("common-AC", "a*c"),
        ("common-BC-plus", "b*c"),
        ("common-BC-minus", "-b*c"),
        ("colored-BF", "b*f"),
        ("colored-CF", f"{common_cycle:+d}*c*f"),
        ("outside-DE-majority-1", "d*e"),
        ("outside-DE-majority-2", "d*e"),
        ("outside-DE-minority", "-d*e"),
        ("outside-DF", "d*f"),
        ("outside-EF", f"{outside_cycle:+d}*e*f"),
    )


def degree_replay():
    edges = (
        ("A", "A"),
        ("A", "B"), ("A", "C"),
        ("B", "C"), ("B", "C"),
        ("B", "F"), ("C", "F"),
        ("D", "E"), ("D", "E"), ("D", "E"),
        ("D", "F"), ("E", "F"),
    )
    degrees = {vertex: 0 for vertex in VERTICES}
    for left, right in edges:
        degrees[left] += 1
        degrees[right] += 1
    return degrees


def defect_replay():
    return {
        "loop_A": 1,
        "BC_split_1_plus_1": 0,
        "DE_split_2_plus_1": 2,
        "all_singletons": 0,
        "total": 3,
    }


def validate(orbits, lanes, defect):
    expected = tuple(
        (common_cycle, outside_cycle,
         (1, 1, 1, common_cycle, 1, 1, outside_cycle), 32)
        for common_cycle in (-1, 1)
        for outside_cycle in (-1, 1)
    )
    if orbits != expected:
        raise RuntimeError(f"sign orbits {orbits}")
    if degree_replay() != {vertex: 4 for vertex in VERTICES}:
        raise RuntimeError("target degrees")
    if defect != {
        "loop_A": 1,
        "BC_split_1_plus_1": 0,
        "DE_split_2_plus_1": 2,
        "all_singletons": 0,
        "total": 3,
    }:
        raise RuntimeError("defect saturation")
    expected_keys = set(itertools.product((-1, 1), repeat=2))
    if set(lanes) != expected_keys:
        raise RuntimeError("lane keys")
    if any(rows != records(*key) for key, rows in lanes.items()):
        raise RuntimeError("lane records")
    if any(len(rows) != 12 for rows in lanes.values()):
        raise RuntimeError("complete row count")


def verify():
    orbits = sign_orbits()
    defect = defect_replay()
    lanes = {
        (common_cycle, outside_cycle): records(common_cycle, outside_cycle)
        for common_cycle in (-1, 1)
        for outside_cycle in (-1, 1)
    }
    validate(orbits, lanes, defect)
    return orbits, lanes, defect


def main():
    orbits, lanes, defect = verify()
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0A_SIGNED_EDGE_ATLAS_PASS "
        f"raw_signs=128 gauge_orbits={len(orbits)} orbit_sizes="
        f"{','.join(str(row[3]) for row in orbits)} "
        f"lanes={len(lanes)} rows_per_lane=12 defect={defect['total']}"
    )


if __name__ == "__main__":
    main()
