#!/usr/bin/env python3
"""Independently check an E=35 quotient-census packet."""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e35_mod16_quotient_census.cpp"
RESULT = HERE / "e35_mod16_quotient_census_result.json"
PROFILES = {0: (3, 8), 1: (12, 0)}
CAPACITIES = {
    128: (3, 8, 8, 8, 8, 8, 8, 8, 4),
    64: (1, 4, 4, 4, 4, 4, 4, 4, 2),
}


def allocation_count(capacities: tuple[int, ...], ones: int, twos: int) -> int:
    states = {(0, 0, False): 1}
    for index, capacity in enumerate(capacities):
        updated: defaultdict[tuple[int, int, bool], int] = defaultdict(int)
        for (used_one, used_two, has_odd), count in states.items():
            for one in range(min(capacity, ones - used_one) + 1):
                for two in range(min(capacity - one, twos - used_two) + 1):
                    key = (
                        used_one + one,
                        used_two + two,
                        has_odd or (index in (1, 3, 5, 7) and one + two > 0),
                    )
                    updated[key] += count
        states = updated
    return states.get((ones, twos, True), 0)


def residues(counts: list[int]) -> list[int]:
    result = [0] * 16
    result[0] = 2 * counts[0]
    result[8] = 2 * counts[8]
    for residue in range(1, 8):
        result[residue] = result[16 - residue] = counts[residue]
    return result


def pair_bound(left: list[int], right: list[int], target: list[int]) -> int:
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


def evaluate(ones: list[int], twos: list[int]) -> tuple[int, list[int]]:
    outer = residues([one + two for one, two in zip(ones, twos)])
    inner = residues(twos)
    aaa = pair_bound(outer, outer, outer)
    if not any(inner):
        return aaa, [aaa, 0, 0, 0]
    aab = min(pair_bound(outer, outer, inner), pair_bound(outer, inner, outer))
    abb = min(pair_bound(outer, inner, inner), pair_bound(inner, inner, outer))
    bbb = pair_bound(inner, inner, inner)
    return aaa + 3 * aab + 3 * abb + bbb, [aaa, aab, abb, bbb]


def main() -> None:
    packet = json.loads(RESULT.read_text())
    assert packet["schema"] == "e1-e35-mod16-quotient-census-v1"
    assert packet["complete"] is True and packet["errors"] == []
    assert packet["source_sha256"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    results = packet["results"]
    assert len(results) == 32
    grouped: defaultdict[tuple[int, int], list[dict[str, object]]] = defaultdict(list)
    for result in results:
        assert result["complete"] is True
        profile = int(result["profile"])
        order = int(result["order"])
        ones = [int(value) for value in result["ones"]]
        twos = [int(value) for value in result["twos"]]
        assert sum(ones) == PROFILES[profile][0]
        assert sum(twos) == PROFILES[profile][1]
        assert all(
            one + two <= capacity
            for one, two, capacity in zip(ones, twos, CAPACITIES[order])
        )
        objective, components = evaluate(ones, twos)
        assert objective == result["best"]
        assert components == result["components"]
        if int(result["best_outside_inner2"]) >= 0:
            outside_ones = [int(value) for value in result["outside_inner2_ones"]]
            outside_twos = [int(value) for value in result["outside_inner2_twos"]]
            if any(outside_twos):
                assert order == 128
                assert any(outside_twos[index] for index in (1, 3, 5, 7))
            else:
                assert profile == 1
            outside_objective, outside_components = evaluate(outside_ones, outside_twos)
            assert outside_objective == result["best_outside_inner2"]
            assert outside_components == result["outside_inner2_components"]
        if int(result["best_inner2_refined"]) >= 0:
            inner_ones = [int(value) for value in result["inner2_ones"]]
            inner_twos = [int(value) for value in result["inner2_twos"]]
            if order == 128:
                assert not any(inner_twos[index] for index in (1, 3, 5, 7))
            inner_objective, inner_components = evaluate(inner_ones, inner_twos)
            refined = inner_objective - inner_components[3] + min(
                inner_components[3], 174
            )
            assert refined == result["best_inner2_refined"]
            assert inner_components == result["inner2_components"]
        grouped[profile, order].append(result)

    maxima = {}
    refinements = {}
    total = 0
    for profile in PROFILES:
        for order in CAPACITIES:
            rows = grouped[profile, order]
            assert len(rows) == 8
            assert {int(row["shard"]) for row in rows} == set(range(8))
            tested = sum(int(row["tested"]) for row in rows)
            assert tested == allocation_count(CAPACITIES[order], *PROFILES[profile])
            total += tested
            maximum = max(int(row["best"]) for row in rows)
            maxima[f"profile{profile}_order{order}"] = maximum
            summary = packet["summaries"][f"profile{profile}_order{order}"]
            assert summary["complete"] is True
            assert summary["tested"] == tested
            assert summary["best"] in rows
            assert summary["best"]["best"] == maximum
            outside_rows = [
                row for row in rows if int(row["best_outside_inner2"]) >= 0
            ]
            if outside_rows:
                assert summary["best_outside_inner2"] in outside_rows
                assert summary["best_outside_inner2"]["best_outside_inner2"] == max(
                    int(row["best_outside_inner2"]) for row in outside_rows
                )
            inner_rows = [
                row for row in rows if int(row["best_inner2_refined"]) >= 0
            ]
            if inner_rows:
                assert summary["best_inner2_refined"] in inner_rows
                assert summary["best_inner2_refined"]["best_inner2_refined"] == max(
                    int(row["best_inner2_refined"]) for row in inner_rows
                )
                refinements[f"profile{profile}_order{order}_inner2"] = summary[
                    "best_inner2_refined"
                ]["best_inner2_refined"]
            if outside_rows:
                refinements[f"profile{profile}_order{order}_outside_inner2"] = summary[
                    "best_outside_inner2"
                ]["best_outside_inner2"]

    print(
        "E1_E35_MOD16_QUOTIENT_CENSUS_CHECK_PASS "
        f"allocations={total} "
        f"maxima={json.dumps(maxima, sort_keys=True)} "
        f"refinements={json.dumps(refinements, sort_keys=True)}"
    )


if __name__ == "__main__":
    main()
