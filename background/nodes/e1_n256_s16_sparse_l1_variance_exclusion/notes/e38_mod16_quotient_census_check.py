#!/usr/bin/env python3
"""Check the complete E=38 mod-16 quotient census packet."""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e38_mod16_quotient_census.cpp"
RESULT = HERE / "e38_mod16_quotient_census_result.json"
PROFILES = {
    0: (6, 8),
    1: (2, 9),
    2: (15, 0),
}
CAPACITIES = {
    128: (3, 8, 8, 8, 8, 8, 8, 8, 4),
    64: (1, 4, 4, 4, 4, 4, 4, 4, 2),
}
EXPECTED = {
    (0, 128): (32, 32_509_144, 2782),
    (0, 64): (16, 8_835_832, 2760),
    (1, 128): (8, 978_431, 2580),
    (1, 64): (8, 430_458, 2422),
    (2, 128): (8, 352_184, 840),
    (2, 64): (8, 47_034, 840),
}


def allocation_count(capacities: tuple[int, ...], ones: int, twos: int) -> int:
    states = {(0, 0, False): 1}
    for index, capacity in enumerate(capacities):
        updated: defaultdict[tuple[int, int, bool], int] = defaultdict(int)
        for (used_one, used_two, has_odd), count in states.items():
            for one in range(min(capacity, ones - used_one) + 1):
                for two in range(
                    min(capacity - one, twos - used_two) + 1
                ):
                    updated[
                        (
                            used_one + one,
                            used_two + two,
                            has_odd or (index in (1, 3, 5, 7) and one + two > 0),
                        )
                    ] += count
        states = updated
    return states.get((ones, twos, True), 0)


def residue_counts(category_counts: list[int]) -> list[int]:
    result = [0] * 16
    result[0] = 2 * category_counts[0]
    result[8] = 2 * category_counts[8]
    for residue in range(1, 8):
        result[residue] = category_counts[residue]
        result[16 - residue] = category_counts[residue]
    return result


def pair_bound(
    left: list[int],
    right: list[int],
    target: list[int],
    left_total: int,
    right_total: int,
) -> int:
    answer = 0
    for target_residue in range(16):
        pairs = sum(
            left[left_residue] * right[(-target_residue - left_residue) % 16]
            for left_residue in range(16)
        )
        if target_residue == 0:
            pairs -= min(left_total, right_total)
        per_target = sum(
            min(left[left_residue], right[(-target_residue - left_residue) % 16])
            for left_residue in range(16)
        )
        answer += min(pairs, target[target_residue] * per_target)
    return answer


def evaluate(ones: list[int], twos: list[int]) -> tuple[int, list[int]]:
    outer = residue_counts([one + two for one, two in zip(ones, twos)])
    inner = residue_counts(twos)
    outer_total = sum(outer)
    inner_total = sum(inner)
    aaa = pair_bound(outer, outer, outer, outer_total, outer_total)
    if inner_total == 0:
        return aaa, [aaa, 0, 0, 0]
    aab = min(
        pair_bound(outer, outer, inner, outer_total, outer_total),
        pair_bound(outer, inner, outer, outer_total, inner_total),
    )
    abb = min(
        pair_bound(outer, inner, inner, outer_total, inner_total),
        pair_bound(inner, inner, outer, inner_total, inner_total),
    )
    bbb = pair_bound(inner, inner, inner, inner_total, inner_total)
    return aaa + 3 * aab + 3 * abb + bbb, [aaa, aab, abb, bbb]


def main() -> None:
    packet = json.loads(RESULT.read_text())
    assert packet["schema"] == "e1-e38-mod16-quotient-census-v1"
    assert packet["complete"] is True
    assert packet["source_sha256"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    results = packet["results"]
    assert len(results) == sum(shards for shards, _, _ in EXPECTED.values()) == 80

    grouped: defaultdict[tuple[int, int], list[dict[str, object]]] = defaultdict(list)
    for result in results:
        assert result["complete"] is True
        profile = int(result["profile"])
        order = int(result["order"])
        ones = [int(value) for value in result["ones"]]
        twos = [int(value) for value in result["twos"]]
        one_target, two_target = PROFILES[profile]
        capacities = CAPACITIES[order]
        assert len(ones) == len(twos) == len(capacities) == 9
        assert sum(ones) == one_target
        assert sum(twos) == two_target
        assert all(one + two <= cap for one, two, cap in zip(ones, twos, capacities))
        assert any(ones[index] + twos[index] for index in (1, 3, 5, 7))
        objective, components = evaluate(ones, twos)
        assert objective == result["best"]
        assert components == result["components"]
        grouped[profile, order].append(result)

    for key, (shard_count, tested, maximum) in EXPECTED.items():
        rows = grouped[key]
        assert len(rows) == shard_count
        assert {int(row["shard"]) for row in rows} == set(range(shard_count))
        assert {int(row["shards"]) for row in rows} == {shard_count}
        assert sum(int(row["tested"]) for row in rows) == tested
        assert allocation_count(CAPACITIES[key[1]], *PROFILES[key[0]]) == tested
        assert max(int(row["best"]) for row in rows) == maximum
        summary = packet["summaries"][f"profile{key[0]}_order{key[1]}"]
        assert summary["complete"] is True
        assert summary["shards"] == shard_count
        assert summary["tested"] == tested
        assert summary["best"] in rows
        assert summary["best"]["best"] == maximum

    print(
        "E1_E38_MOD16_QUOTIENT_CENSUS_CHECK_PASS "
        "allocations=43153083 maxima=2782,2760,2580,2422,840,840"
    )


if __name__ == "__main__":
    main()
