#!/usr/bin/env python3
"""Independent Burnside audit and hostile outside-action control."""

import importlib.util
import itertools
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SCRIPT = (ROOT / "experiments/prize_resolution" /
          "rate_half_kb_positive_433_1b_o0b_cells1_2_v4_quotient.py")
D_PERMUTATION = (0, 1, 3, 2, 5, 4, 6)


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


def act(label):
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


def independent_burnside():
    labels = tuple(itertools.product(range(7), range(15)))
    fixed_labels = sum(act(label) == label for label in labels)
    require(fixed_labels == 9, "D-sign fixed-label census")
    identity_fixed = 16*105
    d_fixed = 16*fixed_labels
    orbits = (identity_fixed + d_fixed) // 4
    require(orbits == 456, "cells1/2 Burnside quotient")
    require(d_fixed // 2 == 72, "doubleton profile")
    require((identity_fixed - d_fixed) // 4 == 384, "four-orbit profile")
    return fixed_labels, orbits


def hostile_control():
    spec = importlib.util.spec_from_file_location("cells1_2_v4", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    try:
        module.verify(tuple(range(7)))
    except RuntimeError:
        return
    raise RuntimeError("identity D-sign mutation survived")


def main():
    fixed_labels, orbits = independent_burnside()
    hostile_control()
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_CELLS1_2_V4_AUDIT_PASS "
        f"fixed_labels={fixed_labels} orbits={orbits} mutations=1/1"
    )


if __name__ == "__main__":
    main()
