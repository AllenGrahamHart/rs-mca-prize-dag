#!/usr/bin/env python3
"""Exact Klein-four quotient of O0b split-principal cells 3 and 6."""

import argparse
from collections import Counter
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
BC_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_split_bc_ef_involution.py"
S0_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_s0_v4_label_quotient.py"
REPEATED_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_repeated_outside_v4_quotient.py"
MANIFEST_PATH = (
    HERE / "rate_half_kb_positive_433_1b_o0b_split_cells3_6_representatives.json"
)
LANES = tuple(itertools.product(("S0", "SDE", "SDF"), (-1, 1)))
CELLS = (3, 6)
SOURCE_SIGNS = tuple(itertools.product((-1, 1), repeat=2))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BC = load("o0b_bc_ef", BC_PATH)
S0 = load("o0b_s0_v4", S0_PATH)
REPEATED = load("o0b_repeated_v4", REPEATED_PATH)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def bc_action(row, matching_rows, outside_permutation=BC.OUTSIDE_PERMUTATION):
    cell, lane, sigma_o, epsilon_1, epsilon_2, xi, matching = row
    state = BC.state_action((lane, sigma_o, cell, epsilon_1, epsilon_2))
    require(state[2] == 9 - cell, "cells 3/6 destination")
    require(state[3:] == (epsilon_1, -epsilon_2), "cells 3/6 sign action")
    new_xi, new_matching = BC.case_transport(
        xi, matching, matching_rows, outside_permutation
    )
    return state[2], state[0], state[1], state[3], state[4], new_xi, new_matching


def secondary_action(
    row,
    s0_d_permutation=S0.D_PERMUTATION,
    duplicate_permutations=REPEATED.DUPLICATE_PERMUTATIONS,
):
    cell, lane, sigma_o, epsilon_1, epsilon_2, xi, matching = row
    if lane == "S0":
        new_xi, new_matching = S0.D_SIGN.act(
            (xi, matching), s0_d_permutation
        )
    else:
        new_xi, new_matching = REPEATED.ROUTER.act(
            (xi, matching), duplicate_permutations[lane]
        )
    return (
        cell,
        lane,
        sigma_o,
        epsilon_1,
        epsilon_2,
        new_xi,
        new_matching,
    )


def orbit_profile(rows, first_action, second_action):
    rows = set(rows)
    require({first_action(row) for row in rows} == rows, "first action closure")
    require({second_action(row) for row in rows} == rows, "second action closure")
    require(
        all(first_action(first_action(row)) == row for row in rows),
        "first action involution",
    )
    require(
        all(second_action(second_action(row)) == row for row in rows),
        "second action involution",
    )
    require(
        all(
            first_action(second_action(row)) == second_action(first_action(row))
            for row in rows
        ),
        "commuting actions",
    )
    unseen = set(rows)
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = {
            seed,
            first_action(seed),
            second_action(seed),
            first_action(second_action(seed)),
        }
        require(orbit <= rows, "orbit closure")
        unseen -= orbit
        orbits.append(tuple(sorted(orbit)))
    orbits = tuple(sorted(orbits))
    return (
        dict(sorted(Counter(map(len, orbits)).items())),
        tuple(orbit[0] for orbit in orbits),
        orbits,
    )


def representative_manifest(
    outside_permutation=BC.OUTSIDE_PERMUTATION,
    s0_d_permutation=S0.D_PERMUTATION,
    duplicate_permutations=REPEATED.DUPLICATE_PERMUTATIONS,
):
    matching_rows = tuple(BC.pairings(range(6)))
    rows = {
        (cell, lane, sigma_o, epsilon_1, epsilon_2, xi, matching)
        for cell, (lane, sigma_o), (epsilon_1, epsilon_2), xi, matching
        in itertools.product(CELLS, LANES, SOURCE_SIGNS, range(7), range(15))
    }
    require(len(rows) == 5040, "cells 3/6 raw-case census")
    first = lambda row: bc_action(row, matching_rows, outside_permutation)
    second = lambda row: secondary_action(
        row, s0_d_permutation, duplicate_permutations
    )
    s0_rows = {row for row in rows if row[1] == "S0"}
    repeated_rows = rows - s0_rows
    s0_profile, s0_representatives, s0_orbits = orbit_profile(
        s0_rows, first, second
    )
    repeated_profile, repeated_representatives, repeated_orbits = orbit_profile(
        repeated_rows, first, second
    )
    require(s0_profile == {2: 72, 4: 384}, "S0 cells 3/6 quotient")
    require(
        repeated_profile == {2: 240, 4: 720},
        "repeated-lane cells 3/6 quotient",
    )
    representatives = tuple(sorted(s0_representatives + repeated_representatives))
    require(len(representatives) == 1416, "cells 3/6 representative census")
    encoded = json.dumps(representatives, separators=(",", ":"))

    pilot_owners = {}
    for orbit in tuple(sorted(s0_orbits + repeated_orbits)):
        representative = orbit[0]
        for row in orbit:
            _, lane, sigma_o, epsilon_1, _, xi, _ = row
            lane_orbit = "S0" if lane == "S0" else "SDE/SDF"
            pilot_owners.setdefault(
                (lane_orbit, sigma_o, epsilon_1, xi), representative
            )
    require(len(pilot_owners) == 56, "pilot stratum cover")
    pilot_representatives = tuple(sorted(set(pilot_owners.values())))
    pilot_encoded = json.dumps(pilot_representatives, separators=(",", ":"))
    return {
        "raw_cases": len(rows),
        "s0_profile": s0_profile,
        "repeated_profile": repeated_profile,
        "representative_count": len(representatives),
        "representatives_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
        "pilot_stratum_count": len(pilot_owners),
        "pilot_representative_count": len(pilot_representatives),
        "pilot_representatives_sha256": hashlib.sha256(
            pilot_encoded.encode()
        ).hexdigest(),
        "representatives": representatives,
        "pilot_representatives": pilot_representatives,
    }


def verify(
    outside_permutation=BC.OUTSIDE_PERMUTATION,
    s0_d_permutation=S0.D_PERMUTATION,
    duplicate_permutations=REPEATED.DUPLICATE_PERMUTATIONS,
):
    result = representative_manifest(
        outside_permutation, s0_d_permutation, duplicate_permutations
    )
    return {
        key: value
        for key, value in result.items()
        if key not in {"representatives", "pilot_representatives"}
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-manifest", action="store_true")
    args = parser.parse_args()
    manifest = representative_manifest()
    result = {
        key: value
        for key, value in manifest.items()
        if key not in {"representatives", "pilot_representatives"}
    }
    if args.write_manifest:
        payload = {
            "schema": "rate-half-kb-positive-433-1b-o0b-split-cells3-6-representatives-v1",
            **result,
            "representatives": manifest["representatives"],
            "pilot_representatives": manifest["pilot_representatives"],
        }
        MANIFEST_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_CELLS3_6_QUOTIENT_PASS "
        f"raw={result['raw_cases']} reps={result['representative_count']} "
        f"sha256={result['representatives_sha256']} "
        f"pilot={result['pilot_representative_count']}/"
        f"{result['pilot_stratum_count']} "
        f"manifest={'written' if args.write_manifest else 'not-written'}"
    )


if __name__ == "__main__":
    main()
