#!/usr/bin/env python3
"""Independently check an E=37 quotient-census packet."""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e37_mod16_quotient_census.cpp"
RESULT = HERE / "e37_mod16_quotient_census_result.json"
PROFILES = {0: (5, 8), 1: (1, 9), 2: (14, 0)}
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
    assert packet["schema"] == "e1-e37-mod16-quotient-census-v1"
    assert packet["complete"] is True and packet["errors"] == []
    assert packet["source_sha256"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    results = packet["results"]
    assert len(results) == 48
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
        if int(result["best_not4"]) >= 0:
            not4_ones = [int(value) for value in result["not4_ones"]]
            not4_twos = [int(value) for value in result["not4_twos"]]
            assert any(not4_twos[index] for index in (1, 2, 3, 5, 6, 7))
            not4_objective, not4_components = evaluate(not4_ones, not4_twos)
            assert not4_objective == result["best_not4"]
            assert not4_components == result["not4_components"]
        if int(result["best_inner4_refined"]) >= 0:
            inner4_ones = [int(value) for value in result["inner4_ones"]]
            inner4_twos = [int(value) for value in result["inner4_twos"]]
            assert not any(inner4_twos[index] for index in (1, 2, 3, 5, 6, 7))
            inner4_objective, inner4_components = evaluate(inner4_ones, inner4_twos)
            refined = inner4_objective - inner4_components[3] + min(
                inner4_components[3], 174
            )
            assert refined == result["best_inner4_refined"]
            assert inner4_components == result["inner4_components"]
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
            not4_rows = [row for row in rows if int(row["best_not4"]) >= 0]
            if not4_rows:
                assert summary["best_not4"] in not4_rows
                assert summary["best_not4"]["best_not4"] == max(
                    int(row["best_not4"]) for row in not4_rows
                )
            inner4_rows = [
                row for row in rows if int(row["best_inner4_refined"]) >= 0
            ]
            if inner4_rows:
                assert summary["best_inner4_refined"] in inner4_rows
                assert summary["best_inner4_refined"][
                    "best_inner4_refined"
                ] == max(int(row["best_inner4_refined"]) for row in inner4_rows)
                refinements[f"profile{profile}_order{order}_inner4"] = summary[
                    "best_inner4_refined"
                ]["best_inner4_refined"]
            if not4_rows:
                refinements[f"profile{profile}_order{order}_not4"] = summary[
                    "best_not4"
                ]["best_not4"]

    bbb_maximum = 0
    for representatives in combinations(range(1, 16), 8):
        layer = set(representatives) | {(-value) % 32 for value in representatives}
        bbb_maximum = max(
            bbb_maximum,
            sum((-left - right) % 32 in layer for left in layer for right in layer),
        )
    assert bbb_maximum == 174

    print(
        "E1_E37_MOD16_QUOTIENT_CENSUS_CHECK_PASS "
        f"allocations={total} bbb32={bbb_maximum} "
        f"maxima={json.dumps(maxima, sort_keys=True)} "
        f"refinements={json.dumps(refinements, sort_keys=True)}"
    )


if __name__ == "__main__":
    main()
