#!/usr/bin/env python3
"""Compose lane exchange with duplicate-copy swaps in SDE/SDF."""

from collections import Counter
import importlib.util
import itertools
from pathlib import Path


HERE = Path(__file__).resolve().parent
BC_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_split_bc_ef_involution.py"
ROUTER_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_outside_label_router.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BC = load("split_bc_ef", BC_PATH)
ROUTER = load("outside_label_router", ROUTER_PATH)
DUPLICATE_PERMUTATIONS = {
    "SDE": (0, 1, 3, 2, 4, 5, 6),
    "SDF": (0, 1, 2, 3, 5, 4, 6),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def compose(left, right):
    return tuple(left[right[index]] for index in range(len(left)))


def verify_target_action(permutations=DUPLICATE_PERMUTATIONS):
    for lane in ("SDE", "SDF"):
        permutation = permutations[lane]
        require(compose(permutation, permutation) == tuple(range(7)),
                "duplicate target involution")
        values = tuple(BC.variable(index) for index in range(BC.VARIABLE_COUNT))
        for sigma_o in (-1, 1):
            records = BC.target_records(lane, sigma_o, values)[5:]
            require(all(records[index] == records[permutation[index]]
                        for index in range(7)), "duplicate record identity")
    require(compose(BC.OUTSIDE_PERMUTATION, permutations["SDE"]) ==
            compose(permutations["SDF"], BC.OUTSIDE_PERMUTATION),
            "duplicate/lane-exchange equivariance")
    return 4


def bc_action(row, matching_rows):
    state = row[:5]
    xi, matching = BC.case_transport(
        row[5], row[6], matching_rows, BC.OUTSIDE_PERMUTATION
    )
    return (*BC.state_action(state), xi, matching)


def duplicate_action(row, permutations=DUPLICATE_PERMUTATIONS):
    permutation = permutations[row[0]]
    return (*row[:5], *ROUTER.act(row[5:], permutation))


def verify_quotient(permutations=DUPLICATE_PERMUTATIONS):
    matching_rows = tuple(BC.pairings(range(6)))
    states = tuple(
        (lane, sigma_o, cell, epsilon_1, epsilon_2)
        for lane, sigma_o, cell, epsilon_1, epsilon_2 in itertools.product(
            ("SDE", "SDF"), (-1, 1), range(15), (-1, 1), (-1, 1)
        )
    )
    rows = {
        (*state, xi, matching)
        for state in states
        for xi, matching in itertools.product(range(7), range(15))
    }
    require(len(states) == 240 and len(rows) == 25200, "raw repeated-lane census")
    require({bc_action(row, matching_rows) for row in rows} == rows,
            "lane-exchange closure")
    require({duplicate_action(row, permutations) for row in rows} == rows,
            "duplicate-swap closure")
    require(all(bc_action(bc_action(row, matching_rows), matching_rows) == row
                for row in rows), "lane-exchange row involution")
    require(all(duplicate_action(duplicate_action(row, permutations), permutations) == row
                for row in rows), "duplicate row involution")
    require(all(bc_action(duplicate_action(row, permutations), matching_rows) ==
                duplicate_action(bc_action(row, matching_rows), permutations)
                for row in rows), "row actions commute")

    unseen = set(rows)
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = {
            seed,
            duplicate_action(seed, permutations),
            bc_action(seed, matching_rows),
            duplicate_action(bc_action(seed, matching_rows), permutations),
        }
        require(orbit <= rows, "orbit closure")
        unseen -= orbit
        orbits.append(tuple(sorted(orbit)))
    profile = Counter(map(len, orbits))
    require(profile == Counter({4: 5400, 2: 1800}), "repeated-lane V4 profile")
    require(sum(size * count for size, count in profile.items()) == 25200,
            "repeated-lane orbit cover")
    return len(states), len(rows), len(orbits), dict(sorted(profile.items()))


def verify(permutations=DUPLICATE_PERMUTATIONS):
    lanes = verify_target_action(permutations)
    states, raw_rows, repeated_orbits, profile = verify_quotient(permutations)
    split_orbits = 3420 + repeated_orbits
    require(split_orbits == 10620, "full split representative census")
    return {
        "repeated_lanes": lanes,
        "repeated_states": states,
        "repeated_raw_rows": raw_rows,
        "repeated_orbits": repeated_orbits,
        "repeated_profile": profile,
        "split_orbits": split_orbits,
    }


def main():
    result = verify()
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEATED_OUTSIDE_V4_QUOTIENT_PASS "
        f"states={result['repeated_states']} raw={result['repeated_raw_rows']} "
        f"orbits={result['repeated_orbits']} profile={result['repeated_profile']} "
        f"split_orbits={result['split_orbits']}"
    )


if __name__ == "__main__":
    main()
