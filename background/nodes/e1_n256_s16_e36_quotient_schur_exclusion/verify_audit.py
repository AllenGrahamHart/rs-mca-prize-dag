#!/usr/bin/env python3
"""Independent audit for the E=36 quotient-Schur proof."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = (
    ROOT
    / "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes"
)
QUOTIENT_SOURCE = NOTES / "e36_mod16_quotient_census.cpp"
QUOTIENT_RESULT = NOTES / "e36_mod16_quotient_census_result.json"
BBB_SOURCE = NOTES / "e36_bbb64_census.cpp"
BBB_RESULT = NOTES / "e36_bbb64_census_result.json"


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


def quotient_shape(packet: dict[str, object]) -> bool:
    rows = packet.get("results")
    summaries = packet.get("summaries")
    if not (
        packet.get("schema") == "e1-e36-mod16-quotient-census-v1"
        and packet.get("complete") is True
        and packet.get("errors") == []
        and packet.get("source_sha256")
        == hashlib.sha256(QUOTIENT_SOURCE.read_bytes()).hexdigest()
        and isinstance(rows, list)
        and len(rows) == 48
        and isinstance(summaries, dict)
        and len(summaries) == 6
    ):
        return False
    for profile in range(3):
        for order in (128, 64):
            selected = [
                row
                for row in rows
                if row.get("profile") == profile and row.get("order") == order
            ]
            summary = summaries.get(f"profile{profile}_order{order}")
            if not (
                len(selected) == 8
                and {row.get("shard") for row in selected} == set(range(8))
                and all(row.get("complete") is True for row in selected)
                and isinstance(summary, dict)
                and summary.get("complete") is True
                and summary.get("best") in selected
                and summary["best"].get("best")
                == max(row.get("best") for row in selected)
            ):
                return False
    return True


def bbb_shape(packet: dict[str, object]) -> bool:
    rows = packet.get("results")
    if not (
        packet.get("schema") == "e1-e36-bbb64-census-v1"
        and packet.get("complete") is True
        and packet.get("errors") == []
        and packet.get("source_sha256")
        == hashlib.sha256(BBB_SOURCE.read_bytes()).hexdigest()
        and isinstance(rows, list)
        and len(rows) == 16
        and {row.get("shard") for row in rows} == set(range(16))
        and all(row.get("complete") is True for row in rows)
        and packet.get("processed") == math.comb(31, 8)
        and packet.get("best") in rows
        and packet["best"].get("best") == max(row.get("best") for row in rows)
    ):
        return False
    representatives = packet["best"].get("representatives")
    return (
        isinstance(representatives, list)
        and len(representatives) == 8
        and schur(
            set(representatives) | {(-value) % 64 for value in representatives},
            set(representatives) | {(-value) % 64 for value in representatives},
            set(representatives) | {(-value) % 64 for value in representatives},
            64,
        )
        == packet["best"].get("best")
        == 174
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

    quotient = json.loads(QUOTIENT_RESULT.read_text())
    assert quotient_shape(quotient)
    missing = copy.deepcopy(quotient)
    missing["results"].pop()
    assert not quotient_shape(missing)
    incomplete = copy.deepcopy(quotient)
    incomplete["results"][0]["complete"] = False
    assert not quotient_shape(incomplete)
    altered = copy.deepcopy(quotient)
    altered["summaries"]["profile0_order128"]["best"]["best"] += 2
    assert not quotient_shape(altered)

    bbb = json.loads(BBB_RESULT.read_text())
    assert bbb_shape(bbb)
    missing_bbb = copy.deepcopy(bbb)
    missing_bbb["results"].pop()
    assert not bbb_shape(missing_bbb)
    altered_bbb = copy.deepcopy(bbb)
    altered_bbb["best"]["best"] += 2
    assert not bbb_shape(altered_bbb)

    print(
        "E1_N256_S16_E36_QUOTIENT_SCHUR_EXCLUSION_AUDIT_PASS "
        f"small_group_cases={checked} quotient_shards=48 "
        "bbb64_sets=7888725 hostile_mutations=5"
    )


if __name__ == "__main__":
    main()
