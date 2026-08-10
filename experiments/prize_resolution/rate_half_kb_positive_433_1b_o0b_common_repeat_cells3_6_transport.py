#!/usr/bin/env python3
"""Exact cell-3/cell-6 transport for repeated-BC 433-1b -> O0b."""

import itertools


COMMON_ROLE_SWAP = (0, 2, 1, 3, 4)
OUTSIDE_RECORD_SWAP = (1, 0, 4, 5, 2, 3, 6)
TARGET_VERTEX_SWAP = {"A": "A", "B": "C", "C": "B",
                      "D": "D", "E": "F", "F": "E"}
OUTSIDE_RECORDS = (
    (1, ("B", "E")),
    (1, ("C", "F")),
    (1, ("D", "E")),
    (-1, ("D", "E")),
    (1, ("D", "F")),
    (-1, ("D", "F")),
    (None, ("E", "F")),
)


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


COMMON_CELLS = tuple(
    (singleton, matching)
    for singleton in range(5)
    for matching in pairings(index for index in range(5) if index != singleton)
)
OUTSIDE_MATCHINGS = tuple(pairings(range(6)))
OUTSIDE_MATCHING_INDEX = {
    tuple(sorted(tuple(sorted(edge)) for edge in matching)): index
    for index, matching in enumerate(OUTSIDE_MATCHINGS)
}


def canonical_matching(matching):
    return tuple(sorted(tuple(sorted(pair)) for pair in matching))


def common_cell_image(cell_index):
    singleton, matching = COMMON_CELLS[cell_index]
    image = (
        COMMON_ROLE_SWAP[singleton],
        canonical_matching(tuple(
            (COMMON_ROLE_SWAP[left], COMMON_ROLE_SWAP[right])
            for left, right in matching
        )),
    )
    indexed = {
        (singleton, canonical_matching(matching)): index
        for index, (singleton, matching) in enumerate(COMMON_CELLS)
    }
    return indexed[image]


def outside_label_image(label):
    xi_index, pairing_index = label
    old_residual = tuple(index for index in range(7) if index != xi_index)
    new_xi = OUTSIDE_RECORD_SWAP[xi_index]
    new_residual = tuple(index for index in range(7) if index != new_xi)
    compact = {value: index for index, value in enumerate(new_residual)}
    image_matching = canonical_matching(tuple(
        (
            compact[OUTSIDE_RECORD_SWAP[old_residual[left]]],
            compact[OUTSIDE_RECORD_SWAP[old_residual[right]]],
        )
        for left, right in OUTSIDE_MATCHINGS[pairing_index]
    ))
    return new_xi, OUTSIDE_MATCHING_INDEX[image_matching]


def record_image(record, outside_cycle_sign):
    sign, endpoints = record
    if sign is None:
        sign = outside_cycle_sign
    endpoints = tuple(sorted(TARGET_VERTEX_SWAP[value] for value in endpoints))
    return sign, endpoints


def normalized_records(outside_cycle_sign):
    return tuple(
        (outside_cycle_sign if sign is None else sign, tuple(sorted(endpoints)))
        for sign, endpoints in OUTSIDE_RECORDS
    )


def validate():
    if common_cell_image(3) != 6 or common_cell_image(6) != 3:
        raise RuntimeError("common cell transport")
    labels = tuple(itertools.product(range(7), range(15)))
    if len(labels) != 105:
        raise RuntimeError("outside label census")
    label_images = {label: outside_label_image(label) for label in labels}
    if set(label_images.values()) != set(labels):
        raise RuntimeError("outside label bijection")
    if any(outside_label_image(image) != label
           for label, image in label_images.items()):
        raise RuntimeError("outside label involution")
    for outside_cycle_sign in (-1, 1):
        records = normalized_records(outside_cycle_sign)
        images = tuple(record_image(record, outside_cycle_sign)
                       for record in OUTSIDE_RECORDS)
        if any(images[index] != records[OUTSIDE_RECORD_SWAP[index]]
               for index in range(7)):
            raise RuntimeError("outside target-record transport")

    systems = set(itertools.product(
        (-1, 1), (-1, 1), (-1, 1), (-1, 1), range(7), range(15),
    ))
    images = {
        (epsilon_1, epsilon_2, bc_sign, outside_sign,
         *outside_label_image((xi_index, pairing_index)))
        for epsilon_1, epsilon_2, bc_sign, outside_sign,
        xi_index, pairing_index in systems
    }
    if len(systems) != 1680 or images != systems:
        raise RuntimeError("formal-system bijection")
    return labels, systems


def main():
    labels, systems = validate()
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELLS3_6_TRANSPORT_PASS "
        f"cell=3<->6 labels={len(labels)} systems={len(systems)} "
        "target=B<->C,E<->F records=7"
    )


if __name__ == "__main__":
    main()
