#!/usr/bin/env python3
"""Independently audit all E30 quotient-relaxation packets."""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from itertools import combinations_with_replacement, product
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASE_SOURCE = (
    HERE.parent.parent
    / "e1_n256_s16_sparse_l1_variance_exclusion"
    / "notes"
    / "e34_nested_quotient_census.cpp"
)
SOURCE = HERE / "e30_eight_profile_quotient_census.cpp"
DRIVER = HERE / "e30_eight_profile_quotient_probe_modal.py"
RESULT = HERE / "e30_eight_profile_quotient_probe_result.json"
CAPACITIES = {
    128: (3, 8, 8, 8, 8, 8, 8, 8, 4),
    64: (1, 4, 4, 4, 4, 4, 4, 4, 2),
}
PROFILES = (
    (6, 6),
    (2, 7),
    (5, 4, 1),
    (1, 5, 1),
    (4, 2, 2),
    (0, 3, 2),
    (6, 2, 0, 1),
    (3, 0, 3),
)
EXPECTED = {
    (6, 6): {128: (8_089_426, 1712), 64: (3_316_117, 1694)},
    (2, 7): {128: (271_115, 1600), 64: (164_143, 1600)},
    (5, 4, 1): {128: (5_421_301, 1430), 64: (3_086_861, 1376)},
    (1, 5, 1): {128: (99_689, 1344), 64: (75_961, 1344)},
    (4, 2, 2): {128: (970_010, 1230), 64: (690_477, 1230)},
    (0, 3, 2): {128: (6_892, 936), 64: (6_084, 936)},
    (6, 2, 0, 1): {128: (1_154_703, 1058), 64: (724_659, 1048)},
    (3, 0, 3): {128: (25_884, 1002), 64: (21_368, 940)},
}


def residues(counts: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * 16
    answer[0] = 2 * counts[0]
    answer[8] = 2 * counts[8]
    for residue in range(1, 8):
        answer[residue] = answer[16 - residue] = counts[residue]
    return tuple(answer)


def directed(
    left: tuple[int, ...], right: tuple[int, ...], target: tuple[int, ...]
) -> int:
    answer = 0
    for target_residue in range(16):
        pairs = sum(
            left[source] * right[(-target_residue - source) % 16]
            for source in range(16)
        )
        if target_residue == 0:
            pairs -= min(sum(left), sum(right))
        per_target = sum(
            min(left[source], right[(-target_residue - source) % 16])
            for source in range(16)
        )
        answer += min(pairs, target[target_residue] * per_target)
    return answer


def triple(
    first: tuple[int, ...], second: tuple[int, ...], third: tuple[int, ...]
) -> int:
    return min(
        directed(first, second, third),
        directed(first, third, second),
        directed(second, third, first),
    )


def objective(exact: tuple[tuple[int, ...], ...]) -> int:
    levels = len(exact)
    layers = [
        residues(
            tuple(
                sum(exact[level][category] for level in range(start, levels))
                for category in range(9)
            )
        )
        for start in range(levels)
    ]
    answer = 0
    for first, second, third in combinations_with_replacement(range(levels), 3):
        totals = tuple(sum(layers[index]) for index in (first, second, third))
        contribution = (
            0
            if totals == (2, 2, 2)
            else triple(layers[first], layers[second], layers[third])
        )
        multiplicity = 1 if first == third else 3 if first == second or second == third else 6
        answer += multiplicity * contribution
    return answer


def allocation_count(profile: tuple[int, ...], capacities: tuple[int, ...]) -> int:
    levels = len(profile)
    states = {(tuple(0 for _ in profile), False): 1}
    for category, capacity in enumerate(capacities):
        additions = [
            values
            for values in product(*(range(count + 1) for count in profile))
            if sum(values) <= capacity
        ]
        updated: defaultdict[tuple[tuple[int, ...], bool], int] = defaultdict(int)
        for (used, has_odd), count in states.items():
            for addition in additions:
                new = tuple(used[level] + addition[level] for level in range(levels))
                if any(new[level] > profile[level] for level in range(levels)):
                    continue
                updated[
                    (
                        new,
                        has_odd or (category in (1, 3, 5, 7) and sum(addition) > 0),
                    )
                ] += count
        states = updated
    return states[(profile, True)]


def main() -> None:
    packet = json.loads(RESULT.read_text())
    assert packet["schema"] == "e1-e30-eight-profile-quotient-probe-v1"
    assert packet["complete"] is True
    assert packet["completed_tasks"] == packet["expected_tasks"] == 128
    assert packet["shards"] == 8
    assert packet["source_sha256"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    assert packet["base_source_sha256"] == hashlib.sha256(BASE_SOURCE.read_bytes()).hexdigest()
    assert len(packet["rows"]) == 128

    for index, profile in enumerate(PROFILES):
        assert packet["profiles"][index] == ",".join(map(str, profile))
        for order, capacities in CAPACITIES.items():
            selected = [
                row for row in packet["rows"]
                if int(row["profile"]) == index and int(row["order"]) == order
            ]
            assert {int(row["shard"]) for row in selected} == set(range(8))
            assert all(int(row["shards"]) == 8 and row["complete"] is True for row in selected)
            tested, maximum = EXPECTED[profile][order]
            assert sum(int(row["tested"]) for row in selected) == tested
            assert allocation_count(profile, capacities) == tested
            assert max(int(row["best"]) for row in selected) == maximum
            summary = packet["summary"][",".join(map(str, profile))][str(order)]
            assert summary == {
                "completed_shards": 8,
                "tested": tested,
                "maximum": maximum,
            }
            for row in selected:
                assert tuple(map(int, row["profile_counts"])) == profile
                exact = tuple(tuple(map(int, values)) for values in row["exact"])
                assert tuple(sum(values) for values in exact) == profile
                outer = tuple(
                    sum(exact[level][category] for level in range(len(profile)))
                    for category in range(9)
                )
                assert all(value <= cap for value, cap in zip(outer, capacities))
                assert any(outer[category] for category in (1, 3, 5, 7))
                assert objective(exact) == int(row["best"])

    closed = {
        profile for profile in PROFILES
        if max(EXPECTED[profile][order][1] for order in CAPACITIES) <= 1087
    }
    assert closed == {(0, 3, 2), (6, 2, 0, 1), (3, 0, 3)}
    assert DRIVER.read_text().count("write_checkpoint(False)") >= 2

    print(
        "E30_EIGHT_PROFILE_QUOTIENT_PROBE_CHECK_PASS "
        "tasks=128 profiles=8 orders=2 closed=3 threshold=1087"
    )


if __name__ == "__main__":
    main()
