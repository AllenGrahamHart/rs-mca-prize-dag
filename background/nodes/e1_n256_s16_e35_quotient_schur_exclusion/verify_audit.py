#!/usr/bin/env python3
"""Independent audit for the E=35 quotient-Schur proof."""

from __future__ import annotations

import copy
import hashlib
import json
from collections.abc import Iterator
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = (
    ROOT
    / "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes"
)
SOURCE = NOTES / "e35_mod16_quotient_census.cpp"
RESULT = NOTES / "e35_mod16_quotient_census_result.json"
CAPACITIES = {
    128: (3, 8, 8, 8, 8, 8, 8, 8, 4),
    64: (1, 4, 4, 4, 4, 4, 4, 4, 2),
}


def packet_shape(packet: dict[str, object]) -> bool:
    rows = packet.get("results")
    summaries = packet.get("summaries")
    if not (
        packet.get("schema") == "e1-e35-mod16-quotient-census-v1"
        and packet.get("complete") is True
        and packet.get("errors") == []
        and packet.get("source_sha256")
        == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
        and isinstance(rows, list)
        and len(rows) == 32
        and isinstance(summaries, dict)
        and len(summaries) == 4
    ):
        return False
    for profile in range(2):
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


def compositions(
    capacities: tuple[int, ...], total: int, index: int = 0
) -> Iterator[tuple[int, ...]]:
    if index == len(capacities):
        if total == 0:
            yield ()
        return
    for value in range(min(capacities[index], total) + 1):
        for suffix in compositions(capacities, total - value, index + 1):
            yield (value,) + suffix


def category_points(counts: tuple[int, ...]) -> tuple[int, ...]:
    points = [0] * 16
    points[0] = 2 * counts[0]
    points[8] = 2 * counts[8]
    for residue in range(1, 8):
        points[residue] = points[16 - residue] = counts[residue]
    return tuple(points)


def quotient_oriented(
    left: tuple[int, ...],
    right: tuple[int, ...],
    target: tuple[int, ...],
) -> int:
    result = 0
    for target_residue, target_count in enumerate(target):
        pairs = 0
        capacity = 0
        for left_residue, left_count in enumerate(left):
            right_count = right[(-target_residue - left_residue) % 16]
            pairs += left_count * right_count
            capacity += min(left_count, right_count)
        if target_residue == 0:
            pairs -= min(sum(left), sum(right))
        result += min(pairs, target_count * capacity)
    return result


def quotient_bound(
    first: tuple[int, ...],
    second: tuple[int, ...],
    third: tuple[int, ...],
) -> int:
    return min(
        quotient_oriented(first, second, third),
        quotient_oriented(first, third, second),
        quotient_oriented(second, third, first),
    )


def full_score(
    outer: tuple[int, ...],
    middle: tuple[int, ...],
    top: tuple[int, ...],
) -> int:
    layers = tuple(map(category_points, (outer, middle, top)))
    score = 0
    for first, second, third in product(range(3), repeat=3):
        if first == second == third == 2:
            continue
        score += quotient_bound(layers[first], layers[second], layers[third])
    return score


def main() -> None:
    packet = json.loads(RESULT.read_text())
    assert packet_shape(packet)
    missing = copy.deepcopy(packet)
    missing["results"].pop()
    assert not packet_shape(missing)
    incomplete = copy.deepcopy(packet)
    incomplete["results"][0]["complete"] = False
    assert not packet_shape(incomplete)
    altered = copy.deepcopy(packet)
    altered["summaries"]["profile0_order128"]["best"]["best"] += 2
    assert not packet_shape(altered)

    high = []
    outer_counts = {}
    for order, capacities in CAPACITIES.items():
        tested = 0
        high_here = []
        for outer in compositions(capacities, 12):
            if not any(outer[index] for index in (1, 3, 5, 7)):
                continue
            tested += 1
            points = category_points(outer)
            aaa = quotient_bound(points, points, points)
            if aaa > 458:
                high_here.append((aaa, outer))
        outer_counts[order] = tested
        if order == 128:
            high = high_here
        else:
            assert high_here == []
    assert outer_counts == {128: 104_750, 64: 32_346}
    assert len(high) == 4 and {value for value, _ in high} == {460}

    nested = 0
    maximum = -1
    for _, outer in high:
        for middle in compositions(outer, 6):
            for index, count in enumerate(middle):
                if count:
                    top = tuple(int(position == index) for position in range(9))
                    nested += 1
                    maximum = max(maximum, full_score(outer, middle, top))
    assert nested == 276 and maximum == 2054

    print(
        "E1_N256_S16_E35_QUOTIENT_SCHUR_EXCLUSION_AUDIT_PASS "
        "outer=104750/32346 high=4 "
        "nested=276 hostile_mutations=3"
    )


if __name__ == "__main__":
    main()
