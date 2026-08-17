#!/usr/bin/env python3
"""Compose the exact B/C--E/F and D-sign actions on split lane S0."""

from collections import Counter
import importlib.util
import itertools
from pathlib import Path


HERE = Path(__file__).resolve().parent
BC_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_split_bc_ef_involution.py"
D_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_outside_label_router.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BC = load("split_bc_ef", BC_PATH)
D_SIGN = load("outside_d_sign", D_PATH)
D_PERMUTATION = D_SIGN.D_SIGN_FLIP


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def compose(left, right):
    return tuple(left[right[index]] for index in range(len(left)))


def verify_target_action(d_permutation=D_PERMUTATION):
    d_full_permutation = tuple(range(5)) + tuple(value + 5 for value in d_permutation)
    require(compose(d_permutation, d_permutation) == tuple(range(7)),
            "D-sign target involution")
    require(compose(d_permutation, BC.OUTSIDE_PERMUTATION) ==
            compose(BC.OUTSIDE_PERMUTATION, d_permutation),
            "target actions commute")
    values = tuple(BC.variable(index) for index in range(BC.VARIABLE_COUNT))
    d_flipped = values[:3] + (BC.pscale(values[3], -1),) + values[4:]
    require(BC.target_guards(values) == BC.target_guards(d_flipped),
            "D-sign target guards")
    for sigma_o in (-1, 1):
        old = BC.target_records("S0", sigma_o, values)
        new = BC.target_records("S0", sigma_o, d_flipped)
        for old_index, new_index in enumerate(d_full_permutation):
            require(new[old_index] == old[new_index], "D-sign complete record action")
    return 2


def bc_action(row, matching_rows):
    state = row[:5]
    xi, matching = BC.case_transport(
        row[5], row[6], matching_rows, BC.OUTSIDE_PERMUTATION
    )
    return (*BC.state_action(state), xi, matching)


def d_action(row, permutation=D_PERMUTATION):
    return (*row[:5], *D_SIGN.act(row[5:], permutation))


def verify_quotient(d_permutation=D_PERMUTATION):
    matching_rows = tuple(BC.pairings(range(6)))
    states = tuple(
        ("S0", sigma_o, cell, epsilon_1, epsilon_2)
        for sigma_o, cell, epsilon_1, epsilon_2 in itertools.product(
            (-1, 1), range(15), (-1, 1), (-1, 1)
        )
    )
    rows = {
        (*state, xi, matching)
        for state in states
        for xi, matching in itertools.product(range(7), range(15))
    }
    require(len(states) == 120 and len(rows) == 12600, "raw S0 census")
    require({bc_action(row, matching_rows) for row in rows} == rows,
            "B/C--E/F S0 closure")
    require({d_action(row, d_permutation) for row in rows} == rows, "D-sign S0 closure")
    require(all(bc_action(bc_action(row, matching_rows), matching_rows) == row
                for row in rows), "B/C--E/F row involution")
    require(all(d_action(d_action(row, d_permutation), d_permutation) == row
                for row in rows),
            "D-sign row involution")
    require(all(bc_action(d_action(row, d_permutation), matching_rows) ==
                d_action(bc_action(row, matching_rows), d_permutation) for row in rows),
            "row actions commute")

    unseen = set(rows)
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = {
            seed,
            d_action(seed, d_permutation),
            bc_action(seed, matching_rows),
            d_action(bc_action(seed, matching_rows), d_permutation),
        }
        require(orbit <= rows, "orbit closure")
        unseen -= orbit
        orbits.append(tuple(sorted(orbit)))
    profile = Counter(map(len, orbits))
    require(profile == Counter({4: 2880, 2: 540}), "S0 V4 orbit profile")
    require(sum(size * count for size, count in profile.items()) == 12600,
            "S0 orbit cover")
    return len(states), len(rows), len(orbits), dict(sorted(profile.items()))


def verify(d_permutation=D_PERMUTATION):
    lanes = verify_target_action(d_permutation)
    states, raw_rows, s0_orbits, profile = verify_quotient(d_permutation)
    split_orbits = s0_orbits + 12600
    require(split_orbits == 16020, "complete split representative census")
    return {
        "s0_lanes": lanes,
        "s0_states": states,
        "s0_raw_rows": raw_rows,
        "s0_orbits": s0_orbits,
        "s0_profile": profile,
        "split_orbits": split_orbits,
    }


def main():
    result = verify()
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_S0_V4_LABEL_QUOTIENT_PASS "
        f"states={result['s0_states']} raw={result['s0_raw_rows']} "
        f"orbits={result['s0_orbits']} profile={result['s0_profile']} "
        f"split_orbits={result['split_orbits']}"
    )


if __name__ == "__main__":
    main()
