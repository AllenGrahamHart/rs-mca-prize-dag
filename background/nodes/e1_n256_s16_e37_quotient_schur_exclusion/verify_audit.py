#!/usr/bin/env python3
"""Independent audit for the E=37 quotient-Schur proof."""

from __future__ import annotations

import copy
import json
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = (
    ROOT
    / "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes"
    / "e37_mod16_quotient_census_result.json"
)


def schur(left: set[int], right: set[int], target: set[int], order: int) -> int:
    return sum(
        (-left_value - right_value) % order in target
        for left_value in left
        for right_value in right
    )


def fibers(values: set[int]) -> list[int]:
    return [sum(value % 4 == residue for value in values) for residue in range(4)]


def oriented(left: set[int], right: set[int], target: set[int]) -> int:
    left_counts, right_counts, target_counts = map(fibers, (left, right, target))
    answer = 0
    for target_residue in range(4):
        pairs = sum(
            left_counts[index] * right_counts[(-target_residue - index) % 4]
            for index in range(4)
        )
        if target_residue == 0:
            pairs -= min(len(left), len(right))
        capacity = sum(
            min(left_counts[index], right_counts[(-target_residue - index) % 4])
            for index in range(4)
        )
        answer += min(pairs, target_counts[target_residue] * capacity)
    return answer


def bound(left: set[int], right: set[int], target: set[int]) -> int:
    return min(
        oriented(left, right, target),
        oriented(left, target, right),
        oriented(right, target, left),
    )


def packet_shape(packet: dict[str, object]) -> bool:
    rows = packet.get("results")
    return (
        packet.get("complete") is True
        and isinstance(rows, list)
        and len(rows) == 48
        and all(row.get("complete") is True for row in rows)
    )


def main() -> None:
    checked = 0
    for levels in product(range(4), repeat=7):
        layers = [set(), set(), set()]
        for representative, level in zip(range(1, 8), levels):
            pair = {representative, (-representative) % 16}
            for layer in range(min(level, 3)):
                layers[layer].update(pair)
        for indices in product(range(3), repeat=3):
            selected = tuple(layers[index] for index in indices)
            if not all(selected):
                continue
            assert schur(*selected, 16) <= bound(*selected)
            checked += 1

    bbb_maximum = 0
    for representatives in combinations(range(1, 16), 8):
        layer = set(representatives) | {(-value) % 32 for value in representatives}
        bbb_maximum = max(bbb_maximum, schur(layer, layer, layer, 32))
    assert bbb_maximum == 174

    packet = json.loads(RESULT.read_text())
    assert packet_shape(packet)
    missing = copy.deepcopy(packet)
    missing["results"].pop()
    assert not packet_shape(missing)
    incomplete = copy.deepcopy(packet)
    incomplete["results"][0]["complete"] = False
    assert not packet_shape(incomplete)
    assert packet["summaries"]["profile0_order128"]["best_not4"]["best_not4"] == 2576
    assert packet["summaries"]["profile0_order128"]["best_inner4_refined"][
        "best_inner4_refined"
    ] == 2560

    print(
        "E1_N256_S16_E37_QUOTIENT_SCHUR_EXCLUSION_AUDIT_PASS "
        f"small_group_cases={checked} bbb_sets=6435 hostile_mutations=2"
    )


if __name__ == "__main__":
    main()
