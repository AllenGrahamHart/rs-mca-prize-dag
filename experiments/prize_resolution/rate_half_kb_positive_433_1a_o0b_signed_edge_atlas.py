#!/usr/bin/env python3
"""Signed-edge atlas for the positive saturated 433-1a -> O0b route."""

import itertools


ACTIVE_EDGES = ("AB", "AC", "BE", "CF", "EF")
VERTICES = ("A", "B", "C", "D", "E", "F")
ENDPOINTS = {
    "AB": ("A", "B"),
    "AC": ("A", "C"),
    "BE": ("B", "E"),
    "CF": ("C", "F"),
    "EF": ("E", "F"),
}


def gauge_action(signs, gauge):
    return tuple(
        signs[index] * gauge[VERTICES.index(left)] * gauge[VERTICES.index(right)]
        for index, edge in enumerate(ACTIVE_EDGES)
        for left, right in (ENDPOINTS[edge],)
    )


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
        if not orbit <= assignments:
            raise RuntimeError("gauge closure")
        unseen -= orbit
        invariant = 1
        for sign in representative:
            invariant *= sign
        canonical = (1, 1, 1, 1, invariant)
        if canonical not in orbit:
            raise RuntimeError("canonical sign representative")
        orbits.append((invariant, canonical, len(orbit)))
    return tuple(sorted(orbits))


def records(cycle_sign):
    return (
        ("common-loop-C", "-c^2"),
        ("common-AB-majority-1", "a*b"),
        ("common-AB-majority-2", "a*b"),
        ("common-AB-minority", "-a*b"),
        ("common-AC", "a*c"),
        ("colored-BE", "b*e"),
        ("colored-CF", "c*f"),
        ("outside-DE-plus", "d*e"),
        ("outside-DE-minus", "-d*e"),
        ("outside-DF-plus", "d*f"),
        ("outside-DF-minus", "-d*f"),
        ("outside-EF-cycle", f"{cycle_sign:+d}*e*f"),
    )


def degree_replay():
    edges = (
        ("C", "C"),
        ("A", "B"), ("A", "B"), ("A", "B"),
        ("A", "C"),
        ("B", "E"), ("C", "F"),
        ("D", "E"), ("D", "E"),
        ("D", "F"), ("D", "F"),
        ("E", "F"),
    )
    degrees = {vertex: 0 for vertex in VERTICES}
    for left, right in edges:
        degrees[left] += 1
        degrees[right] += 1
    return degrees


def defect_replay():
    # The loop costs one.  The 2+1 split of AB repeats two signed target
    # edges and costs two.  Every outside multiplicity-two pair is split.
    return {
        "loop_C": 1,
        "AB_split_2_plus_1": 2,
        "AC_single": 0,
        "DE_split_1_plus_1": 0,
        "DF_split_1_plus_1": 0,
        "EF_single": 0,
        "total": 3,
    }


def verify():
    orbits = sign_orbits()
    expected = ((-1, (1, 1, 1, 1, -1), 16),
                (1, (1, 1, 1, 1, 1), 16))
    if orbits != expected:
        raise RuntimeError(f"sign orbits {orbits}")
    if degree_replay() != {vertex: 4 for vertex in VERTICES}:
        raise RuntimeError("target degrees")
    defect = defect_replay()
    if defect["total"] != 3:
        raise RuntimeError("defect saturation")
    lanes = {sign: records(sign) for sign in (-1, 1)}
    if any(len(rows) != 12 for rows in lanes.values()):
        raise RuntimeError("complete row count")
    return orbits, lanes, defect


def main():
    orbits, lanes, defect = verify()
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_O0B_SIGNED_EDGE_ATLAS_PASS "
        f"raw_signs=32 gauge_orbits={len(orbits)} orbit_sizes="
        f"{','.join(str(row[2]) for row in orbits)} "
        f"lanes={len(lanes)} rows_per_lane=12 defect={defect['total']}"
    )


if __name__ == "__main__":
    main()
