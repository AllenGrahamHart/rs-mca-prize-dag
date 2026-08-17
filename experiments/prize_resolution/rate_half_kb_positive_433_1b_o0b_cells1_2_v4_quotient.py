#!/usr/bin/env python3
"""Exact duplicate-common/outside-sign quotient of repeated-BC cells 1/2."""

from collections import Counter
import importlib.util
import itertools
from pathlib import Path


HERE = Path(__file__).resolve().parent
COMPILER_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_common_repeat_vieta_compiler.py"
ROUTER_PATH = HERE / "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_outside_label_router.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


COMPILER = load("repeat_compiler", COMPILER_PATH)
ROUTER = load("outside_router", ROUTER_PATH)
COMMON_ROLE_PERMUTATION = (0, 1, 2, 4, 3)
D_PERMUTATION = ROUTER.D_SIGN_FLIP


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def canonical_cell(cell):
    singleton, matching = cell
    return singleton, tuple(sorted(tuple(sorted(pair)) for pair in matching))


def permute_cell(cell, permutation=COMMON_ROLE_PERMUTATION):
    singleton, matching = cell
    return canonical_cell((
        permutation[singleton],
        tuple((permutation[left], permutation[right]) for left, right in matching),
    ))


def source_roots(cell, epsilon_1, epsilon_2):
    singleton, matching = COMPILER.cells()[cell]
    roots = [None] * 5
    roots[matching[0][0]] = ("1", 1)
    roots[matching[0][1]] = ("i", epsilon_1)
    roots[matching[1][0]] = ("r", 1)
    roots[matching[1][1]] = ("ir", epsilon_2)
    roots[singleton] = ("t", 1)
    return tuple(roots)


def verify_common_action():
    cells = COMPILER.cells()
    lookup = {canonical_cell(cell): index for index, cell in enumerate(cells)}
    require(lookup[permute_cell(cells[1])] == 2 and
            lookup[permute_cell(cells[2])] == 1, "duplicate-role cell action")
    require((1, 2) in COMPILER.cell_orbits(), "compiler cell orbit")
    for cell, epsilon_1, epsilon_2 in itertools.product(
            (1, 2), (-1, 1), (-1, 1)):
        old = source_roots(cell, epsilon_1, epsilon_2)
        new_cell = 3 - cell
        new = source_roots(new_cell, epsilon_1, epsilon_2)
        require(all(new[COMMON_ROLE_PERMUTATION[index]] == old[index]
                    for index in range(5)), "source-root row permutation")
    for bc_sign in (-1, 1):
        products = (-1, "b", "c", f"{bc_sign}bc", f"{bc_sign}bc")
        sums = (0, "1+b", "1+c", f"b+{bc_sign}c", f"b+{bc_sign}c")
        require(products[3] == products[4] and sums[3] == sums[4],
                "duplicate common records")
    return 8


def common_action(row):
    cell, epsilon_1, epsilon_2, bc_sign, sigma_o, xi, matching = row
    return 3 - cell, epsilon_1, epsilon_2, bc_sign, sigma_o, xi, matching


def d_action(row, permutation=D_PERMUTATION):
    return (*row[:5], *ROUTER.act(row[5:], permutation))


def verify_quotient(d_permutation=D_PERMUTATION):
    states = tuple(
        (cell, epsilon_1, epsilon_2, bc_sign, sigma_o)
        for cell, (epsilon_1, epsilon_2), bc_sign, sigma_o in itertools.product(
            (1, 2), ((-1, 1), (1, -1)), (-1, 1), (-1, 1)
        )
    )
    rows = {
        (*state, xi, matching)
        for state in states
        for xi, matching in itertools.product(range(7), range(15))
    }
    require(len(states) == 16 and len(rows) == 1680, "cells1/2 survivor census")
    require({common_action(row) for row in rows} == rows, "common-swap closure")
    require({d_action(row, d_permutation) for row in rows} == rows,
            "D-sign closure")
    require(all(common_action(common_action(row)) == row for row in rows),
            "common-swap involution")
    require(all(d_action(d_action(row, d_permutation), d_permutation) == row
                for row in rows), "D-sign involution")
    require(all(common_action(d_action(row, d_permutation)) ==
                d_action(common_action(row), d_permutation) for row in rows),
            "actions commute")

    unseen = set(rows)
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = {
            seed,
            common_action(seed),
            d_action(seed, d_permutation),
            common_action(d_action(seed, d_permutation)),
        }
        require(orbit <= rows, "orbit closure")
        unseen -= orbit
        orbits.append(tuple(sorted(orbit)))
    profile = Counter(map(len, orbits))
    require(profile == Counter({4: 384, 2: 72}), "cells1/2 V4 profile")
    require(sum(size * count for size, count in profile.items()) == 1680,
            "cells1/2 orbit cover")
    return len(states), len(rows), len(orbits), dict(sorted(profile.items()))


def verify(d_permutation=D_PERMUTATION):
    common_rows = verify_common_action()
    states, raw_rows, orbits, profile = verify_quotient(d_permutation)
    owner_orbits = 10620 + orbits
    require(owner_orbits == 11076, "complete owner representative census")
    return {
        "common_rows": common_rows,
        "states": states,
        "raw_rows": raw_rows,
        "orbits": orbits,
        "profile": profile,
        "owner_orbits": owner_orbits,
    }


def main():
    result = verify()
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_CELLS1_2_V4_QUOTIENT_PASS "
        f"states={result['states']} raw={result['raw_rows']} "
        f"orbits={result['orbits']} profile={result['profile']} "
        f"owner_orbits={result['owner_orbits']}"
    )


if __name__ == "__main__":
    main()
