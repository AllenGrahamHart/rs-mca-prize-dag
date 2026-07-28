#!/usr/bin/env python3
"""Independent checker for the cutoff-free E21 profile/parity router."""

from __future__ import annotations

import hashlib
import json
from itertools import product
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = HERE / "e21_profile_parity_probe_modal.py"
RESULT = HERE / "e21_profile_parity_probe_result.json"
ATLAS = (
    ROOT
    / "background/nodes/e1_n256_s16_e27_profile_parity_light_reduction/notes"
    / "e27_profile_parity_probe_result.json"
)


def recursive_profiles(l1_bound: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    def visit(magnitude: int, energy: int, l1_norm: int, counts: list[int]) -> None:
        if magnitude == 6:
            if energy == 21:
                sizes = [2 * sum(counts[level:]) for level in range(5) if sum(counts[level:])]
                cap = sum(
                    min(a * b - min(a, b), a * c - min(a, c), b * c - min(b, c))
                    for a, b, c in product(sizes, repeat=3)
                )
                rows.append(
                    {
                        "cap": cap,
                        "profile": counts,
                        "l1": l1_norm,
                        "odd_classes": sum(counts[0::2]),
                    }
                )
            return
        for count in range((21 - energy) // (magnitude * magnitude) + 1):
            next_l1 = l1_norm + magnitude * count
            if next_l1 > l1_bound:
                break
            visit(
                magnitude + 1,
                energy + magnitude * magnitude * count,
                next_l1,
                counts + [count],
            )

    visit(1, 0, 0, [])
    return sorted(rows, key=lambda row: (int(row["cap"]), row["profile"]), reverse=True)


def independent_minima(maximum_slack: int) -> list[int | None]:
    classes = set()
    for count4 in range(4):
        for count2 in range(13):
            for count1 in range(7):
                if count4 + count2 + count1 == 0:
                    continue
                totals = {
                    abs(
                        4 * (count4 - 2 * neg4)
                        + 2 * (count2 - 2 * neg2)
                        + count1
                        - 2 * neg1
                    )
                    for neg4 in range(count4 + 1)
                    for neg2 in range(count2 + 1)
                    for neg1 in range(count1 + 1)
                }
                for total in totals:
                    slack = (total - 2) ** 2 + 4 * count2 + 3 * count1 - 4
                    if 0 < slack <= maximum_slack:
                        classes.add((slack, count2, count1, total * total))
    answer: list[int | None] = []
    for target in range(maximum_slack + 1):
        best = None
        for diam2 in range(4):
            for diam1 in range(3):
                if diam2 + 2 * diam1 > 4 or diam1 + diam2 > 3:
                    continue
                start = 4 * diam2 + 3 * diam1
                if start > target:
                    continue
                states = {(start, 0, 0): 0}
                changed = True
                while changed:
                    changed = False
                    for (slack, used2, used1), energy in tuple(states.items()):
                        for extra, count2, count1, square in classes:
                            key = (slack + extra, used2 + count2, used1 + count1)
                            if key[0] > target or key[1] > 12 - diam2 or key[2] > 6 - diam1:
                                continue
                            candidate = energy + square
                            if candidate < states.get(key, candidate + 1):
                                states[key] = candidate
                                changed = True
                for (slack, used2, used1), energy in states.items():
                    if slack != target:
                        continue
                    total = energy + 4 * (12 - diam2 - used2) + (6 - diam1 - used1)
                    best = total if best is None else min(best, total)
        answer.append(best)
    return answer


def independent_diameter_ledgers() -> list[list[int]]:
    weights = (2, 2, 2, 1, 1, 1, 1)
    masses: set[int] = set()

    def recurse(remaining: tuple[int, ...], mass: int, light_count: int) -> None:
        if not remaining:
            if light_count == 1:
                masses.add(mass)
            return
        first = remaining[0]
        recurse(remaining[1:], mass, light_count)
        for index in range(1, len(remaining)):
            second = remaining[index]
            recurse(
                remaining[1:index] + remaining[index + 1 :],
                mass + (weights[first] * weights[second]) ** 2,
                light_count + int(weights[first] == weights[second] == 1),
            )

    recurse(tuple(range(7)), 0, 0)
    return [[mass, (mass - 81) // 2] for mass in sorted(masses)]


def main() -> None:
    packet = json.loads(RESULT.read_text())
    atlas = json.loads(ATLAS.read_text())
    assert packet["schema"] == "e1-e21-profile-parity-route-probe-v1"
    assert packet["complete"] is True and packet["variance"] == 42 and packet["energy"] == 21
    assert packet["majorant_filter"] is None
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == packet["source_sha256"]
    assert hashlib.sha256(ATLAS.read_bytes()).hexdigest() == packet["atlas_source_sha256"]
    minima = independent_minima(48)
    trace = [[l1, 87 - 4 * l1, minima[87 - 4 * l1]] for l1 in range(21, 9, -1)]
    assert packet["slack_trace"] == trace
    qualifying = [row for row in trace if row[2] is not None and int(row[2]) <= 21]
    assert qualifying and packet["l1_bound"] == qualifying[0][0]
    profiles = recursive_profiles(int(packet["l1_bound"]))
    survivors = [row for row in profiles if int(row["odd_classes"]) <= 5]
    assert packet["profiles"] == profiles and packet["profile_count"] == len(profiles)
    assert packet["parity_survivors"] == survivors
    assert packet["parity_rejected"] == [row for row in profiles if int(row["odd_classes"]) > 5]
    assert packet["survivors_by_odd_count"] == {
        str(odd): [row for row in survivors if int(row["odd_classes"]) == odd]
        for odd in (1, 3, 5)
    }
    assert packet["diameter_ledgers"] == independent_diameter_ledgers()
    geometry = atlas["light_geometry"]
    expected_atlas = {
        key: {
            "normalized_supports": int(geometry["support_counts"][key]),
            "affine_orbits": int(geometry["orbit_counts"][key]),
        }
        for key in ("1", "3", "5")
    }
    assert packet["atlas_inputs"] == expected_atlas
    used = sorted({str(int(row["odd_classes"])) for row in survivors}, key=int)
    assert packet["used_odd_counts"] == used
    templates = sum(expected_atlas[key]["affine_orbits"] for key in used)
    supports = sum(expected_atlas[key]["normalized_supports"] for key in used)
    assert packet["relevant_affine_templates"] == templates
    assert packet["relevant_normalized_supports"] == supports
    assert packet["direct_vector_floor"] == templates * comb(124, 3) * 64
    assert [row for row in profiles if int(row["odd_classes"]) <= 1] != survivors
    print(
        "E21_PROFILE_PARITY_PROBE_CHECK_PASS "
        f"l1={packet['l1_bound']} profiles={len(profiles)} survivors={len(survivors)} "
        f"templates={templates} floor={packet['direct_vector_floor']} mutations=1"
    )


if __name__ == "__main__":
    main()
