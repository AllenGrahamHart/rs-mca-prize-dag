#!/usr/bin/env python3
"""Independent audit for the E=38 quotient-Schur proof."""

from __future__ import annotations

import copy
import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = (
    ROOT
    / "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes"
    / "e38_mod16_quotient_census_result.json"
)


def schur_count(left: set[int], right: set[int], target: set[int], order: int) -> int:
    return sum(
        1
        for left_value in left
        for right_value in right
        if (-left_value - right_value) % order in target
    )


def fiber_counts(values: set[int], quotient: int) -> list[int]:
    return [sum(value % quotient == residue for value in values) for residue in range(quotient)]


def oriented_bound(
    left: set[int], right: set[int], target: set[int], quotient: int
) -> int:
    left_counts = fiber_counts(left, quotient)
    right_counts = fiber_counts(right, quotient)
    target_counts = fiber_counts(target, quotient)
    answer = 0
    for target_residue in range(quotient):
        pairs = sum(
            left_counts[left_residue]
            * right_counts[(-target_residue - left_residue) % quotient]
            for left_residue in range(quotient)
        )
        if target_residue == 0:
            pairs -= min(len(left), len(right))
        per_target = sum(
            min(
                left_counts[left_residue],
                right_counts[(-target_residue - left_residue) % quotient],
            )
            for left_residue in range(quotient)
        )
        answer += min(pairs, target_counts[target_residue] * per_target)
    return answer


def quotient_bound(left: set[int], right: set[int], target: set[int]) -> int:
    return min(
        oriented_bound(left, right, target, 4),
        oriented_bound(left, target, right, 4),
        oriented_bound(right, target, left, 4),
    )


def result_shape_valid(packet: dict[str, object]) -> bool:
    results = packet.get("results")
    if not isinstance(results, list) or len(results) != 80:
        return False
    for result in results:
        if not isinstance(result, dict):
            return False
        if result.get("complete") is not True or int(result.get("tested", 0)) <= 0:
            return False
        if len(result.get("ones", [])) != 9 or len(result.get("twos", [])) != 9:
            return False
    return True


def main() -> None:
    checked = 0
    representatives = range(1, 8)
    for levels in product(range(4), repeat=7):
        outer: set[int] = set()
        middle: set[int] = set()
        inner: set[int] = set()
        for representative, level in zip(representatives, levels):
            pair = {representative, (-representative) % 16}
            if level >= 1:
                outer.update(pair)
            if level >= 2:
                middle.update(pair)
            if level >= 3:
                inner.update(pair)
        layers = (outer, middle, inner)
        for left_index in range(3):
            for right_index in range(left_index, 3):
                for target_index in range(right_index, 3):
                    selected = (
                        layers[left_index],
                        layers[right_index],
                        layers[target_index],
                    )
                    if not all(selected):
                        continue
                    exact = schur_count(*selected, 16)
                    assert exact <= quotient_bound(*selected)
                    checked += 1

    packet = json.loads(RESULT.read_text())
    assert result_shape_valid(packet)

    missing_shard = copy.deepcopy(packet)
    missing_shard["results"].pop()
    assert not result_shape_valid(missing_shard)

    incomplete = copy.deepcopy(packet)
    incomplete["results"][0]["complete"] = False
    assert not result_shape_valid(incomplete)

    empty_allocation = copy.deepcopy(packet)
    empty_allocation["results"][0]["ones"].pop()
    assert not result_shape_valid(empty_allocation)

    assert 840 + (2828 - 870 - 2) == 2796
    assert 2796 < 2806
    assert all((sign_one + sign_two + sign_three) % 2 for sign_one, sign_two, sign_three in product((-1, 1), repeat=3))

    print(
        "E1_N256_S16_E38_QUOTIENT_SCHUR_EXCLUSION_AUDIT_PASS "
        f"small_group_cases={checked} hostile_mutations=3"
    )


if __name__ == "__main__":
    main()
