#!/usr/bin/env python3
"""Independent Burnside audit of forced invariance cells."""

import itertools


def transform(cell, sign_multiplier=None, sign_permutation=None,
              record_map=None):
    signs, forced = cell
    if sign_permutation is not None:
        signs = tuple(signs[index] for index in sign_permutation)
    if sign_multiplier is not None:
        signs = tuple(left*right for left, right in zip(
            signs, sign_multiplier
        ))
    return signs, (record_map or {}).get(forced, forced)


def burnside(records, sign_dimension, generators):
    universe = tuple(
        (signs, forced)
        for signs in itertools.product((-1, 1), repeat=sign_dimension)
        for forced in records
    )
    indices = {cell: index for index, cell in enumerate(universe)}

    generator_permutations = []
    for generator in generators:
        generator_permutations.append(tuple(
            indices[transform(cell, **generator)] for cell in universe
        ))

    identity = tuple(range(len(universe)))
    group = {identity}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for generator in generator_permutations:
            composite = tuple(generator[current[index]]
                              for index in range(len(universe)))
            if composite not in group:
                group.add(composite)
                frontier.append(composite)

    fixed_sum = sum(
        sum(image == index for index, image in enumerate(permutation))
        for permutation in group
    )
    if fixed_sum % len(group):
        raise RuntimeError("nonintegral Burnside quotient")
    return len(universe), len(group), fixed_sum // len(group)


def main():
    s0 = burnside(
        ("CE", "CF", "DE+", "DE-", "DF+", "DF-", "EF"),
        3,
        (
            {"record_map": {"DE+": "DE-", "DE-": "DE+",
                            "DF+": "DF-", "DF-": "DF+"}},
            {"sign_multiplier": (-1, 1, -1),
             "record_map": {"DE+": "DE-", "DE-": "DE+"}},
            {"sign_multiplier": (1, -1, -1),
             "record_map": {"DF+": "DF-", "DF-": "DF+"}},
            {"sign_permutation": (1, 0, 2),
             "record_map": {"CE": "CF", "CF": "CE",
                            "DE+": "DF+", "DF+": "DE+",
                            "DE-": "DF-", "DF-": "DE-"}},
        ),
    )
    s1 = burnside(
        ("CE", "CF", "DD", "DE", "DF", "EF+", "EF-"),
        4,
        (
            {"sign_multiplier": (1, 1, -1, -1)},
            {"sign_multiplier": (-1, 1, -1, 1),
             "record_map": {"EF+": "EF-", "EF-": "EF+"}},
            {"sign_multiplier": (1, -1, 1, -1),
             "record_map": {"EF+": "EF-", "EF-": "EF+"}},
            {"sign_permutation": (1, 0, 3, 2),
             "record_map": {"CE": "CF", "CF": "CE",
                            "DE": "DF", "DF": "DE"}},
        ),
    )
    s2 = burnside(
        ("CD+", "CD-", "EE", "DF+", "DF-", "EF+", "EF-"),
        0,
        (
            {"record_map": {"CD+": "CD-", "CD-": "CD+",
                            "DF+": "DF-", "DF-": "DF+"}},
            {"record_map": {"EF+": "EF-", "EF-": "EF+"}},
            {"record_map": {"DF+": "DF-", "DF-": "DF+",
                            "EF+": "EF-", "EF-": "EF+"}},
        ),
    )
    if (s0, s1, s2) != ((56, 16, 6), (112, 16, 10), (7, 8, 4)):
        raise RuntimeError(f"forced-cell Burnside census: {s0}, {s1}, {s2}")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_BINARY_AUDIT_PASS "
        "groups=16,16,8 raw_forced=175 canonical=20 four_rows=80"
    )


if __name__ == "__main__":
    main()
