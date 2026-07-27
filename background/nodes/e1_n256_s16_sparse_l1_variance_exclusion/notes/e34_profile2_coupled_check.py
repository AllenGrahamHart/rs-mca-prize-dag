#!/usr/bin/env python3
"""Independently check the E=34 profile-(2,8) coupled census."""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
QUOTIENT_SOURCE = HERE / "e34_profile2_refined_quotient_census.cpp"
SUPPORT_SOURCE = HERE / "e34_profile2_inner4_support_census.cpp"
RESULT = HERE / "e34_profile2_coupled_result.json"
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


def quotient_values(
    ones: tuple[int, ...], twos: tuple[int, ...], order: int
) -> tuple[tuple[int, int, int, int], int, int, bool, bool]:
    outer = residues(tuple(one + two for one, two in zip(ones, twos)))
    inner = residues(twos)
    aaa = triple_bound(outer, outer, outer)
    aab = triple_bound(outer, outer, inner)
    abb = triple_bound(outer, inner, inner)
    bbb = triple_bound(inner, inner, inner)
    objective = aaa + 3 * aab + 3 * abb + bbb
    inner_even = not any(twos[index] for index in (1, 3, 5, 7))
    inner_four = not any(twos[index] for index in (1, 2, 3, 5, 6, 7))
    refined = objective - bbb + (min(bbb, 174) if order == 64 or inner_even else bbb)
    return (aaa, aab, abb, bbb), objective, refined, inner_even, inner_four


def check_candidate(candidate: dict[str, object], order: int, kind: str) -> None:
    value = int(candidate["value"])
    if value < 0:
        return
    ones = tuple(map(int, candidate["ones"]))
    twos = tuple(map(int, candidate["twos"]))
    assert len(ones) == len(twos) == 9
    assert sum(ones) == 2 and sum(twos) == 8
    assert all(ones[index] + twos[index] <= CAPACITIES[order][index] for index in range(9))
    assert any(ones[index] + twos[index] for index in (1, 3, 5, 7))
    components, objective, refined, _, inner_four = quotient_values(ones, twos, order)
    assert tuple(map(int, candidate["components"])) == components
    expected = objective if kind == "best" else refined
    if kind == "best_inside_four":
        assert inner_four
    if kind == "best_outside_four":
        assert not inner_four
    assert value == expected


def quotient_allocation_count(capacities: tuple[int, ...]) -> int:
    states = {(0, 0, False): 1}
    for category, capacity in enumerate(capacities):
        updated: defaultdict[tuple[int, int, bool], int] = defaultdict(int)
        for (used_one, used_two, has_odd), count in states.items():
            for one in range(min(2 - used_one, capacity) + 1):
                for two in range(min(8 - used_two, capacity - one) + 1):
                    updated[
                        (
                            used_one + one,
                            used_two + two,
                            has_odd or (category in (1, 3, 5, 7) and one + two > 0),
                        )
                    ] += count
        states = updated
    return states.get((2, 8, True), 0)


def support_objective(b: tuple[int, ...], u: tuple[int, ...]) -> int:
    weights = [0] * 128
    for value in b:
        weights[value] = weights[128 - value] = 2
    for value in u:
        weights[value] = weights[128 - value] = 1
    return sum(
        weights[left] * weights[right] * weights[(-left - right) % 128]
        for left in range(128)
        if weights[left]
        for right in range(128)
        if weights[right]
    )


def main() -> None:
    packet = json.loads(RESULT.read_text())
    assert packet["schema"] == "e1-e34-profile2-coupled-v1"
    assert packet["complete"] is True and packet["errors"] == []
    assert packet["quotient_source_sha256"] == hashlib.sha256(QUOTIENT_SOURCE.read_bytes()).hexdigest()
    assert packet["support_source_sha256"] == hashlib.sha256(SUPPORT_SOURCE.read_bytes()).hexdigest()

    quotient_results = packet["quotient_results"]
    assert len(quotient_results) == 32
    quotient_maxima = {}
    for order, capacities in CAPACITIES.items():
        selected = [row for row in quotient_results if int(row["order"]) == order]
        assert {int(row["shard"]) for row in selected} == set(range(16))
        assert all(int(row["shards"]) == 16 for row in selected)
        assert sum(int(row["tested"]) for row in selected) == quotient_allocation_count(capacities)
        for row in selected:
            for kind in ("best", "best_refined", "best_inside_four", "best_outside_four"):
                check_candidate(row[kind], order, kind)
        for kind in ("best", "best_refined", "best_inside_four", "best_outside_four"):
            quotient_maxima[f"order{order}_{kind}"] = max(int(row[kind]["value"]) for row in selected)

    support_results = packet["support_results"]
    assert len(support_results) == 32
    assert {int(row["shard"]) for row in support_results} == set(range(32))
    assert all(int(row["shards"]) == 32 for row in support_results)
    assert sum(int(row["tested"]) for row in support_results) == 7_927_920
    for row in support_results:
        b = tuple(map(int, row["b"]))
        u = tuple(map(int, row["u"]))
        assert len(b) == 8 and tuple(sorted(b)) == b
        assert all(value % 4 == 0 and 1 <= value < 64 for value in b)
        assert len(u) == 2 and tuple(sorted(u)) == u
        assert not set(b) & set(u) and any(value % 2 for value in u)
        assert support_objective(b, u) == int(row["best"])
    support_maximum = max(int(row["best"]) for row in support_results)

    print(
        "E1_E34_PROFILE2_COUPLED_CHECK_PASS "
        f"quotient={json.dumps(quotient_maxima, sort_keys=True)} "
        f"support_tested=7927920 support_max={support_maximum}"
    )


if __name__ == "__main__":
    main()
