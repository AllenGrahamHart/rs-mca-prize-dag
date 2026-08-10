#!/usr/bin/env python3
"""Exact signed-edge atlas for the positive 433-1b -> O0b route."""

import itertools


VERTICES = ("A", "B", "C", "D", "E", "F")
SINGLE_EDGES = ("AB", "AC", "BE", "CF", "EF")
REPEATED_PAIRS = ("BC", "DE", "DF")
STRATA = ("S0", "SBC", "SDE", "SDF")
REPEATED_EDGE = {"S0": None, "SBC": "BC", "SDE": "DE", "SDF": "DF"}
ENDPOINTS = {
    "AB": ("A", "B"),
    "AC": ("A", "C"),
    "BC": ("B", "C"),
    "BE": ("B", "E"),
    "CF": ("C", "F"),
    "DE": ("D", "E"),
    "DF": ("D", "F"),
    "EF": ("E", "F"),
}


def active_edges(stratum):
    repeated = REPEATED_EDGE[stratum]
    return SINGLE_EDGES + (() if repeated is None else (repeated,))


def gauge_action(edges, signs, gauge):
    vertex_sign = dict(zip(VERTICES, gauge))
    return tuple(
        sign * vertex_sign[left] * vertex_sign[right]
        for edge, sign in zip(edges, signs)
        for left, right in (ENDPOINTS[edge],)
    )


def invariants(stratum, edges, signs):
    values = dict(zip(edges, signs))
    base_cycle = (
        values["AB"] * values["BE"] * values["EF"]
        * values["CF"] * values["AC"]
    )
    if stratum == "SBC":
        common_triangle = values["AB"] * values["BC"] * values["AC"]
        return base_cycle, common_triangle
    return (base_cycle,)


def canonical(stratum, invariant):
    base_cycle = invariant[0]
    row = [1, 1, 1, 1, base_cycle]
    if stratum == "SBC":
        row.append(invariant[1])
    elif stratum in {"SDE", "SDF"}:
        row.append(1)
    return tuple(row)


def sign_orbits(stratum):
    edges = active_edges(stratum)
    assignments = set(itertools.product((-1, 1), repeat=len(edges)))
    unseen = set(assignments)
    orbits = []
    while unseen:
        representative = min(unseen)
        orbit = {
            gauge_action(edges, representative, gauge)
            for gauge in itertools.product((-1, 1), repeat=len(VERTICES))
        }
        if not orbit <= assignments:
            raise RuntimeError("gauge closure")
        unseen -= orbit
        invariant = invariants(stratum, edges, representative)
        if {invariants(stratum, edges, row) for row in orbit} != {invariant}:
            raise RuntimeError("cycle invariant")
        normal = canonical(stratum, invariant)
        if normal not in orbit:
            raise RuntimeError("canonical representative")
        orbits.append((invariant, normal, len(orbit)))
    return tuple(sorted(orbits))


def signed_product(sign, monomial):
    return monomial if sign == 1 else f"-{monomial}"


def pair_records(edge, stratum, repeated_sign):
    monomial = {"BC": "b*c", "DE": "d*e", "DF": "d*f"}[edge]
    if REPEATED_EDGE[stratum] == edge:
        value = signed_product(repeated_sign, monomial)
        return ((f"{edge}-repeat-1", value), (f"{edge}-repeat-2", value))
    return ((f"{edge}-plus", monomial), (f"{edge}-minus", f"-{monomial}"))


def records(stratum, invariant):
    base_cycle = invariant[0]
    common_triangle = invariant[1] if stratum == "SBC" else 1
    repeated_signs = {"BC": common_triangle, "DE": 1, "DF": 1}
    return (
        ("common-loop-A", "-a^2"),
        ("common-AB", "a*b"),
        ("common-AC", "a*c"),
        *pair_records("BC", stratum, repeated_signs["BC"]),
        ("colored-BE", "b*e"),
        ("colored-CF", "c*f"),
        *pair_records("DE", stratum, repeated_signs["DE"]),
        *pair_records("DF", stratum, repeated_signs["DF"]),
        ("outside-EF-cycle", signed_product(base_cycle, "e*f")),
    )


def degree_replay():
    edges = (
        ("A", "A"),
        ("A", "B"), ("A", "C"),
        ("B", "C"), ("B", "C"),
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


def defect_replay(stratum):
    repeated = REPEATED_EDGE[stratum]
    return {
        "loop_A": 1,
        "BC": 2 if repeated == "BC" else 0,
        "DE": 2 if repeated == "DE" else 0,
        "DF": 2 if repeated == "DF" else 0,
        "total": 1 + (2 if repeated is not None else 0),
    }


def validate(atlases, lanes, defects):
    expected = {
        "S0": tuple(((sign,), (1, 1, 1, 1, sign), 16)
                    for sign in (-1, 1)),
        "SBC": tuple(((base, triangle),
                       (1, 1, 1, 1, base, triangle), 16)
                      for base in (-1, 1) for triangle in (-1, 1)),
        "SDE": tuple(((sign,), (1, 1, 1, 1, sign, 1), 32)
                     for sign in (-1, 1)),
        "SDF": tuple(((sign,), (1, 1, 1, 1, sign, 1), 32)
                     for sign in (-1, 1)),
    }
    if atlases != expected:
        raise RuntimeError(f"orbit census {atlases}")
    if degree_replay() != {vertex: 4 for vertex in VERTICES}:
        raise RuntimeError("target degrees")
    if {stratum: row["total"] for stratum, row in defects.items()} != {
        "S0": 1, "SBC": 3, "SDE": 3, "SDF": 3,
    }:
        raise RuntimeError("defect ledger")
    if len(lanes) != 10 or any(len(rows) != 12 for rows in lanes.values()):
        raise RuntimeError("lane census")
    expected_keys = {
        (stratum, *invariant)
        for stratum, orbits in atlases.items()
        for invariant, _, _ in orbits
    }
    if set(lanes) != expected_keys:
        raise RuntimeError("lane keys")
    if any(rows != records(key[0], key[1:]) for key, rows in lanes.items()):
        raise RuntimeError("lane records")
    raw_signs = sum(sum(row[2] for row in orbits) for orbits in atlases.values())
    if raw_signs != 224:
        raise RuntimeError("raw sign census")


def verify():
    atlases = {stratum: sign_orbits(stratum) for stratum in STRATA}
    defects = {stratum: defect_replay(stratum) for stratum in STRATA}
    lanes = {
        (stratum, *invariant): records(stratum, invariant)
        for stratum, orbits in atlases.items()
        for invariant, _, _ in orbits
    }
    validate(atlases, lanes, defects)
    return atlases, lanes, defects


def main():
    atlases, lanes, defects = verify()
    counts = ",".join(f"{key}:{len(atlases[key])}" for key in STRATA)
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_SIGNED_EDGE_ATLAS_PASS "
        f"raw_signs=224 gauge_orbits=10 strata={counts} "
        f"lanes={len(lanes)} rows_per_lane=12 defects="
        f"{','.join(str(defects[key]['total']) for key in STRATA)}"
    )


if __name__ == "__main__":
    main()
