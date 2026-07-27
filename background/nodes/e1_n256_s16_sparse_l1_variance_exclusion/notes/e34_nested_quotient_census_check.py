#!/usr/bin/env python3
"""Independently check an E=34 nested quotient-census packet."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from itertools import combinations_with_replacement
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e34_nested_quotient_census.cpp"
PILOT = HERE / "e34_nested_quotient_pilot_result.json"
FULL = HERE / "e34_nested_quotient_census_result.json"
PROFILES = ((6, 7), (9, 4, 1), (2, 8), (12, 1, 2), (5, 5, 1), (14, 1, 0, 1))
CAPACITIES = {
    128: (3, 8, 8, 8, 8, 8, 8, 8, 4),
    64: (1, 4, 4, 4, 4, 4, 4, 4, 2),
}


def residues(counts: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * 16
    result[0] = 2 * counts[0]
    result[8] = 2 * counts[8]
    for residue in range(1, 8):
        result[residue] = result[16 - residue] = counts[residue]
    return tuple(result)


def directed_bound(
    left: tuple[int, ...], right: tuple[int, ...], target: tuple[int, ...]
) -> int:
    answer = 0
    for target_residue in range(16):
        pairs = sum(
            left[left_residue] * right[(-target_residue - left_residue) % 16]
            for left_residue in range(16)
        )
        if target_residue == 0:
            pairs -= min(sum(left), sum(right))
        per_target = sum(
            min(left[left_residue], right[(-target_residue - left_residue) % 16])
            for left_residue in range(16)
        )
        answer += min(pairs, target[target_residue] * per_target)
    return answer


def triple_bound(
    first: tuple[int, ...], second: tuple[int, ...], third: tuple[int, ...]
) -> int:
    return min(
        directed_bound(first, second, third),
        directed_bound(first, third, second),
        directed_bound(second, third, first),
    )


def objective(exact: tuple[tuple[int, ...], ...]) -> int:
    layers = []
    for level in range(len(exact)):
        layers.append(
            residues(
                tuple(
                    sum(exact[exact_level][category] for exact_level in range(level, len(exact)))
                    for category in range(9)
                )
            )
        )
    answer = 0
    for first, second, third in combinations_with_replacement(range(len(layers)), 3):
        totals = tuple(map(sum, (layers[first], layers[second], layers[third])))
        contribution = 0 if totals == (2, 2, 2) else triple_bound(
            layers[first], layers[second], layers[third]
        )
        multiplicity = 1 if first == third else 3 if first == second or second == third else 6
        answer += multiplicity * contribution
    return answer


def allocation_count(capacities: tuple[int, ...], profile: tuple[int, ...]) -> int:
    start = (tuple(0 for _ in profile), False)
    states = {start: 1}
    for category, capacity in enumerate(capacities):
        updated: defaultdict[tuple[tuple[int, ...], bool], int] = defaultdict(int)
        additions = []

        def build(level: int, left: int, values: list[int]) -> None:
            if level == len(profile):
                if left == 0:
                    additions.append(tuple(values))
                return
            for value in range(left + 1):
                values.append(value)
                build(level + 1, left - value, values)
                values.pop()

        for used_capacity in range(capacity + 1):
            build(0, used_capacity, [])
        for (used, has_odd), count in states.items():
            for addition in additions:
                new = tuple(used[index] + addition[index] for index in range(len(profile)))
                if any(new[index] > profile[index] for index in range(len(profile))):
                    continue
                updated[(new, has_odd or (category in (1, 3, 5, 7) and sum(addition) > 0))] += count
        states = updated
    return states.get((profile, True), 0)


def check_result(result: dict[str, object]) -> None:
    assert result["complete"] is True
    profile_index = int(result["profile"])
    order = int(result["order"])
    profile = PROFILES[profile_index]
    assert tuple(map(int, result["profile_counts"])) == profile
    exact = tuple(tuple(map(int, row)) for row in result["exact"])
    assert len(exact) == len(profile)
    assert all(len(row) == 9 for row in exact)
    assert tuple(sum(row) for row in exact) == profile
    outer = tuple(sum(row[category] for row in exact) for category in range(9))
    assert all(outer[index] <= CAPACITIES[order][index] for index in range(9))
    assert any(outer[index] for index in (1, 3, 5, 7))
    assert objective(exact) == int(result["best"])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true")
    args = parser.parse_args()
    path = FULL if args.full else PILOT
    packet = json.loads(path.read_text())
    assert packet["schema"] == "e1-e34-nested-quotient-census-v1"
    assert packet["source_sha256"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    results = packet["results"]
    for result in results:
        check_result(result)
    keys = [(int(result["profile"]), int(result["order"]), int(result["shard"])) for result in results]
    assert len(keys) == len(set(keys))

    if args.full:
        assert packet["mode"] == "full" and packet["complete"] is True
        assert packet["errors"] == []
        shards = int(packet["shards_per_case"])
        assert len(results) == len(PROFILES) * len(CAPACITIES) * shards
        maxima = {}
        tested = 0
        for profile_index, profile in enumerate(PROFILES):
            for order, capacities in CAPACITIES.items():
                selected = [
                    result
                    for result in results
                    if int(result["profile"]) == profile_index and int(result["order"]) == order
                ]
                assert {int(result["shard"]) for result in selected} == set(range(shards))
                expected = allocation_count(capacities, profile)
                actual = sum(int(result["tested"]) for result in selected)
                assert actual == expected
                tested += actual
                maxima[f"profile{profile_index}_order{order}"] = max(
                    int(result["best"]) for result in selected
                )
        print(
            "E1_E34_NESTED_QUOTIENT_CENSUS_CHECK_PASS "
            f"tested={tested} maxima={json.dumps(maxima, sort_keys=True)}"
        )
    else:
        assert packet["mode"] == "pilot" and packet["complete"] is True
        assert int(packet["shards_per_case"]) == 128
        assert packet["errors"] == []
        assert len(results) == len(PROFILES) * len(CAPACITIES)
        assert {(profile, order) for profile, order, _ in keys} == {
            (profile, order)
            for profile in range(len(PROFILES))
            for order in CAPACITIES
        }
        assert {shard for _, _, shard in keys} == {0}
        maxima = {
            f"profile{int(result['profile'])}_order{int(result['order'])}": int(result["best"])
            for result in results
        }
        print(
            "E1_E34_NESTED_QUOTIENT_PILOT_CHECK_PASS "
            f"shards={len(results)} maxima={json.dumps(maxima, sort_keys=True)}"
        )


if __name__ == "__main__":
    main()
