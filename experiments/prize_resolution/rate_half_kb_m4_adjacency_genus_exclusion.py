#!/usr/bin/env python3
"""Exclude every m4 passport by its outer adjacency-curve genus."""

from __future__ import annotations

import argparse
import copy
import hashlib
from itertools import combinations, permutations
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = (
    ROOT
    / "experiments/prize_resolution/rate_half_kb_m4_adjacency_genus_exclusion_result.json"
)
PAIRS = list(combinations(range(6), 2))
ADJACENT = [
    (left, right)
    for left in PAIRS
    for right in PAIRS
    if left != right and len(set(left) & set(right)) == 1
]
PASSPORTS = (
    ("S6_652", "S6", ((6,), (5, 1), (2, 1, 1, 1, 1))),
    ("S6_562", "S6", ((5, 1), (3, 2, 1), (2, 2, 2))),
    ("A6_542", "A6", ((5, 1), (4, 2), (2, 2, 1, 1))),
    (
        "S6_four_point",
        "S6",
        ((5, 1), (2, 1, 1, 1, 1), (2, 2, 1, 1), (2, 2, 2)),
    ),
)


def canonical_hash(data: dict[str, object]) -> str:
    payload = copy.deepcopy(data)
    payload.pop("payload_sha256", None)
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def cycle_permutation(cycle_lengths):
    result = list(range(6))
    start = 0
    for length in cycle_lengths:
        cycle = list(range(start, start + length))
        for index, value in enumerate(cycle):
            result[value] = cycle[(index + 1) % length]
        start += length
    assert start == 6
    return tuple(result)


def sign(permutation):
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(6)
        for right in range(left + 1, 6)
    )
    return -1 if inversions % 2 else 1


def act_pair(permutation, pair):
    return tuple(sorted(permutation[value] for value in pair))


def orbit(seed, group, action):
    return {action(permutation, seed) for permutation in group}


def adjacency_cycle_data(cycle_lengths):
    letter_permutation = cycle_permutation(cycle_lengths)
    index = {value: position for position, value in enumerate(ADJACENT)}
    action = [
        index[
            (
                act_pair(letter_permutation, left),
                act_pair(letter_permutation, right),
            )
        ]
        for left, right in ADJACENT
    ]
    seen = set()
    cycle_count = 0
    cycle_lengths_on_adjacency = []
    for start in range(len(action)):
        if start in seen:
            continue
        cycle_count += 1
        length = 0
        value = start
        while value not in seen:
            seen.add(value)
            length += 1
            value = action[value]
        cycle_lengths_on_adjacency.append(length)
    return {
        "letter_cycle_type": list(cycle_lengths),
        "cycle_count": cycle_count,
        "index": len(action) - cycle_count,
        "adjacency_cycle_type": sorted(cycle_lengths_on_adjacency, reverse=True),
    }


def build() -> dict[str, object]:
    assert len(PAIRS) == 15
    assert len(ADJACENT) == 120
    symmetric_group = tuple(permutations(range(6)))
    alternating_group = tuple(value for value in symmetric_group if sign(value) == 1)
    assert len(symmetric_group) == 720
    assert len(alternating_group) == 360

    base_pair = PAIRS[0]
    base_adjacent = ADJACENT[0]
    group_data = {}
    for name, group in (("S6", symmetric_group), ("A6", alternating_group)):
        stabilizer = tuple(
            permutation
            for permutation in group
            if act_pair(permutation, base_pair) == base_pair
        )
        remaining = set(PAIRS)
        subdegrees = []
        while remaining:
            seed = next(iter(remaining))
            current_orbit = orbit(seed, stabilizer, act_pair)
            subdegrees.append(len(current_orbit))
            remaining -= current_orbit
        adjacency_orbit = orbit(
            base_adjacent,
            group,
            lambda permutation, state: (
                act_pair(permutation, state[0]),
                act_pair(permutation, state[1]),
            ),
        )
        assert sorted(subdegrees) == [1, 6, 8]
        assert len(adjacency_orbit) == 120
        group_data[name] = {
            "order": len(group),
            "pair_stabilizer_order": len(stabilizer),
            "pair_subdegrees": sorted(subdegrees),
            "ordered_adjacency_orbit": len(adjacency_orbit),
        }

    passport_rows = []
    expected = {
        "S6_652": (244, 3, 5),
        "S6_562": (250, 6, 11),
        "A6_542": (246, 4, 7),
        "S6_four_point": (264, 13, 25),
    }
    for label, group_name, cycle_types in PASSPORTS:
        branch_rows = [adjacency_cycle_data(row) for row in cycle_types]
        total_index = sum(row["index"] for row in branch_rows)
        genus_numerator = -2 * len(ADJACENT) + total_index
        assert genus_numerator % 2 == 0
        adjacency_genus = 1 + genus_numerator // 2
        minimum_source_genus = 2 * adjacency_genus - 1
        assert (total_index, adjacency_genus, minimum_source_genus) == expected[label]
        assert minimum_source_genus > 3
        passport_rows.append(
            {
                "label": label,
                "group": group_name,
                "letter_cycle_types": [list(row) for row in cycle_types],
                "adjacency_branch_rows": branch_rows,
                "adjacency_cover_degree": len(ADJACENT),
                "total_branch_index": total_index,
                "adjacency_genus": adjacency_genus,
                "minimum_genus_of_degree_two_source": minimum_source_genus,
                "actual_source_genus_upper_bound": 3,
                "excluded": True,
            }
        )

    data: dict[str, object] = {
        "schema": "rate_half_kb_m4_adjacency_genus_exclusion_v1",
        "payload_sha256": "",
        "producer": {
            "path": str(Path(__file__).resolve().relative_to(ROOT)),
            "sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "imported_geometry": {
            "actual_component_bidegree": [2, 4],
            "actual_component_arithmetic_genus": 3,
            "birational_self_correspondence_bidegree": [4, 4],
            "outer_image_bidegree": [8, 8],
            "component_to_outer_image_degree": 2,
            "characteristic": 2130706433,
        },
        "group_actions": group_data,
        "passports": passport_rows,
        "conclusion": {
            "terminal": "M4_A6S6_ALL_FOUR_PASSPORTS_EXCLUDED_BY_ADJACENCY_GENUS",
            "inner_degree_four_row_empty": True,
            "remaining_independent_inner_degrees": [2, 3],
            "ledger_movement": 0,
        },
        "scope_fence": [
            "no inner-degree-two or inner-degree-three deletion",
            "no owner, carrier, data, or slope projection",
            "no u2, K3, endpoint, or KoalaBear row closure",
        ],
    }
    data["payload_sha256"] = canonical_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    arguments = parser.parse_args()
    data = build()
    if arguments.write:
        OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
