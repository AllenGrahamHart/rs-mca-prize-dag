#!/usr/bin/env python3
"""Independent Burnside audit and hostile D-sign control."""

from collections import Counter
import importlib.util
import itertools
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (ROOT / "experiments/prize_resolution" /
          "rate_half_kb_positive_433_1b_o0b_s0_v4_label_quotient.py")
D_PERMUTATION = (0, 1, 3, 2, 5, 4, 6)
CELL_ACTION = (0, 2, 1, 6, 7, 8, 3, 4, 5, 10, 9, 11, 13, 12, 14)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return

    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, second),) + tail


MATCHINGS = tuple(pairings(range(6)))
MATCHING_INDEX = {
    tuple(sorted(tuple(sorted(pair)) for pair in matching)): index
    for index, matching in enumerate(MATCHINGS)
}


def label_action(label):
    xi, matching_index = label
    old_residual = tuple(index for index in range(7) if index != xi)
    new_xi = D_PERMUTATION[xi]
    new_residual = tuple(index for index in range(7) if index != new_xi)
    compact = {value: index for index, value in enumerate(new_residual)}
    image = tuple(sorted(tuple(sorted((
        compact[D_PERMUTATION[old_residual[left]]],
        compact[D_PERMUTATION[old_residual[right]]],
    ))) for left, right in MATCHINGS[matching_index]))
    return new_xi, MATCHING_INDEX[image]


def sign_action(cell, epsilon_1, epsilon_2):
    if cell == 0:
        return -epsilon_1, -epsilon_2
    if cell == 1:
        return -epsilon_2, epsilon_1
    if cell == 2:
        return epsilon_2, -epsilon_1
    if cell in (3, 4, 6, 7, 9, 10):
        return epsilon_1, -epsilon_2
    if cell in (5, 8):
        return -epsilon_1, epsilon_2
    if cell == 11:
        return -epsilon_1, -epsilon_2
    if cell in (12, 13):
        return epsilon_1, epsilon_2
    if cell == 14:
        return epsilon_1, -epsilon_2
    raise RuntimeError("cell")


def independent_burnside():
    labels = tuple(itertools.product(range(7), range(15)))
    fixed_labels = sum(label_action(label) == label for label in labels)
    require(fixed_labels == 9, "independent fixed-label census")
    profile = Counter()
    unseen = set(labels)
    while unseen:
        seed = min(unseen)
        orbit = {seed, label_action(seed)}
        unseen -= orbit
        profile[len(orbit)] += 1
    require(profile == Counter({2: 48, 1: 9}), "independent label profile")

    fixed_states = 0
    for sigma_o, cell, epsilon_1, epsilon_2 in itertools.product(
            (-1, 1), range(15), (-1, 1), (-1, 1)):
        new_signs = sign_action(cell, epsilon_1, epsilon_2)
        fixed_states += CELL_ACTION[cell] == cell and new_signs == (epsilon_1, epsilon_2)
    require(fixed_states == 0, "independent B/C--E/F fixed states")
    identity_fixed = 120*105
    d_fixed = 120*fixed_labels
    orbit_count = (identity_fixed + d_fixed) // 4
    require(orbit_count == 3420, "Burnside quotient")
    return fixed_labels, orbit_count


def hostile_control():
    spec = importlib.util.spec_from_file_location("s0_v4", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    try:
        module.verify(tuple(range(7)))
    except RuntimeError:
        return
    raise RuntimeError("identity D-sign mutation survived")


def main():
    fixed_labels, orbit_count = independent_burnside()
    hostile_control()
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_S0_V4_QUOTIENT_AUDIT_PASS "
        f"fixed_labels={fixed_labels} orbits={orbit_count} mutations=1/1"
    )


if __name__ == "__main__":
    main()
