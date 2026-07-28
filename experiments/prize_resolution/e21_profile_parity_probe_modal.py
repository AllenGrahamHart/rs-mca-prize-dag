#!/usr/bin/env python3
"""Derive and price the cutoff-free E21 profile/parity/light router."""

from __future__ import annotations

import hashlib
import json
from itertools import product
from math import comb
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
RESULT = HERE / "e21_profile_parity_probe_result.json"

app = modal.App("e1-n256-e21-profile-parity-route-probe")


def attainable_absolute_sums(count_4: int, count_2: int, count_1: int) -> set[int]:
    sums = {0}
    for value, count in ((4, count_4), (2, count_2), (1, count_1)):
        for _ in range(count):
            sums = {current + sign * value for current in sums for sign in (-1, 1)}
    return {abs(current) for current in sums}


def relaxed_minimum_energy_by_slack(maximum_slack: int) -> list[int | None]:
    class_types = set()
    for count_4 in range(4):
        for count_2 in range(13):
            for count_1 in range(7):
                if count_4 + count_2 + count_1 == 0:
                    continue
                for class_sum in attainable_absolute_sums(count_4, count_2, count_1):
                    slack = (class_sum - 2) ** 2 + 4 * count_2 + 3 * count_1 - 4
                    if 0 < slack <= maximum_slack:
                        class_types.add((slack, count_2, count_1, class_sum))
    answers: list[int | None] = []
    for target in range(maximum_slack + 1):
        best = None
        for diameter_2 in range(4):
            for diameter_1 in range(3):
                if diameter_2 + 2 * diameter_1 > 4 or diameter_1 + diameter_2 > 3:
                    continue
                diameter_slack = 4 * diameter_2 + 3 * diameter_1
                if diameter_slack > target:
                    continue
                class_target = target - diameter_slack
                states = {(0, 0, 0): 0}
                for used_slack in range(class_target + 1):
                    active = [item for item in states.items() if item[0][0] == used_slack]
                    for (state_slack, used_2, used_1), energy in active:
                        for slack, count_2, count_1, class_sum in class_types:
                            key = (state_slack + slack, used_2 + count_2, used_1 + count_1)
                            if (
                                key[0] > class_target
                                or key[1] > 12 - diameter_2
                                or key[2] > 6 - diameter_1
                            ):
                                continue
                            candidate = energy + class_sum * class_sum
                            states[key] = min(states.get(key, candidate), candidate)
                for (state_slack, used_2, used_1), energy in states.items():
                    if state_slack != class_target:
                        continue
                    total = energy + 4 * (12 - diameter_2 - used_2) + (6 - diameter_1 - used_1)
                    best = total if best is None else min(best, total)
        answers.append(best)
    return answers


def layer_cap(counts: tuple[int, ...]) -> int:
    sizes = [2 * sum(counts[level:]) for level in range(len(counts)) if sum(counts[level:])]
    return sum(
        min(a * b - min(a, b), a * c - min(a, c), b * c - min(b, c))
        for a, b, c in product(sizes, repeat=3)
    )


def energy_profiles(l1_bound: int) -> list[dict[str, object]]:
    rows = []
    for counts in product(range(22), range(6), range(3), range(2), range(1)):
        if sum((index + 1) ** 2 * count for index, count in enumerate(counts)) != 21:
            continue
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        if l1_norm > l1_bound:
            continue
        rows.append(
            {
                "cap": layer_cap(counts),
                "profile": list(counts),
                "l1": l1_norm,
                "odd_classes": sum(counts[0::2]),
            }
        )
    return sorted(rows, key=lambda row: (int(row["cap"]), row["profile"]), reverse=True)


def diameter_ledgers() -> list[list[int]]:
    weights = (2, 2, 2, 1, 1, 1, 1)
    square_masses: set[int] = set()

    def visit(available: tuple[int, ...], edges: tuple[tuple[int, int], ...]) -> None:
        if not available:
            if sum(weights[a] == weights[b] == 1 for a, b in edges) == 1:
                square_masses.add(sum((weights[a] * weights[b]) ** 2 for a, b in edges))
            return
        first = available[0]
        visit(available[1:], edges)
        for offset, second in enumerate(available[1:]):
            remainder = available[1 : offset + 1] + available[offset + 2 :]
            visit(remainder, edges + ((first, second),))

    visit(tuple(range(7)), ())
    return [[value, (value - 81) // 2] for value in sorted(square_masses)]


@app.function(cpu=1.0, memory=256, timeout=60)
def compute() -> dict[str, object]:
    slack = relaxed_minimum_energy_by_slack(48)
    trace = []
    l1_bound = None
    for l1_norm in range(21, 9, -1):
        delta = 21 + 66 - 4 * l1_norm
        trace.append([l1_norm, delta, slack[delta]])
        if slack[delta] is not None and int(slack[delta]) <= 21 and l1_bound is None:
            l1_bound = l1_norm
    assert l1_bound is not None
    profiles = energy_profiles(l1_bound)
    survivors = [row for row in profiles if int(row["odd_classes"]) <= 5]
    return {
        "complete": True,
        "variance": 42,
        "energy": 21,
        "slack_trace": trace,
        "l1_bound": l1_bound,
        "profiles": profiles,
        "profile_count": len(profiles),
        "majorant_filter": None,
        "majorant_policy": "not invoked: the fixed cubic-Hermite majorant is dead below V=50",
        "parity_survivors": survivors,
        "parity_rejected": [row for row in profiles if int(row["odd_classes"]) > 5],
        "survivors_by_odd_count": {
            str(odd): [row for row in survivors if int(row["odd_classes"]) == odd]
            for odd in (1, 3, 5)
        },
        "diameter_ledgers": diameter_ledgers(),
    }


@app.local_entrypoint()
def main() -> None:
    root = HERE.parents[1]
    atlas_path = (
        root
        / "background/nodes/e1_n256_s16_e27_profile_parity_light_reduction/notes"
        / "e27_profile_parity_probe_result.json"
    )
    atlas_packet = json.loads(atlas_path.read_text())
    geometry = atlas_packet["light_geometry"]
    if not atlas_packet["complete"]:
        raise RuntimeError("the one-diameter light atlas is incomplete")
    packet = compute.remote()
    used = {str(int(row["odd_classes"])) for row in packet["parity_survivors"]}
    packet["atlas_inputs"] = {
        key: {
            "normalized_supports": int(geometry["support_counts"][key]),
            "affine_orbits": int(geometry["orbit_counts"][key]),
        }
        for key in ("1", "3", "5")
    }
    packet["atlas_source_sha256"] = hashlib.sha256(atlas_path.read_bytes()).hexdigest()
    packet["used_odd_counts"] = sorted(used, key=int)
    packet["relevant_normalized_supports"] = sum(
        int(geometry["support_counts"][key]) for key in used
    )
    packet["relevant_affine_templates"] = sum(
        int(geometry["orbit_counts"][key]) for key in used
    )
    packet["vectors_per_template"] = comb(124, 3) * 64
    packet["direct_vector_floor"] = (
        packet["relevant_affine_templates"] * packet["vectors_per_template"]
    )
    packet["schema"] = "e1-e21-profile-parity-route-probe-v1"
    packet["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print(
        "E21_PROFILE_PARITY_ROUTE_PROBE "
        + json.dumps(
            {
                "l1_bound": packet["l1_bound"],
                "profiles": packet["profile_count"],
                "survivors_by_odd_count": {
                    key: len(value) for key, value in packet["survivors_by_odd_count"].items()
                },
                "rejected": len(packet["parity_rejected"]),
                "relevant_normalized_supports": packet["relevant_normalized_supports"],
                "relevant_affine_templates": packet["relevant_affine_templates"],
                "direct_vector_floor": packet["direct_vector_floor"],
            },
            sort_keys=True,
        )
    )
    print(f"E21_PROFILE_PARITY_ROUTE_PROBE_RESULT {RESULT}")
