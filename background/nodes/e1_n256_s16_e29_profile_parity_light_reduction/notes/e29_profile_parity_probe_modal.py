#!/usr/bin/env python3
"""Compute the exact E29 slack, profile, parity, and light-orbit frontier."""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
RESULT = HERE / "e29_profile_parity_probe_result.json"
UNITS = tuple(range(1, 128, 2))

app = modal.App("e1-n256-e29-profile-parity-probe")


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
    for target_slack in range(maximum_slack + 1):
        best = None
        for diameter_2 in range(4):
            for diameter_1 in range(3):
                if diameter_2 + 2 * diameter_1 > 4 or diameter_1 + diameter_2 > 3:
                    continue
                diameter_slack = 4 * diameter_2 + 3 * diameter_1
                if diameter_slack > target_slack:
                    continue
                class_target = target_slack - diameter_slack
                states = {(0, 0, 0): 0}
                for used_slack in range(class_target + 1):
                    current = [item for item in states.items() if item[0][0] == used_slack]
                    for (state_slack, used_2, used_1), energy in current:
                        for slack, count_2, count_1, class_sum in class_types:
                            key = (state_slack + slack, used_2 + count_2, used_1 + count_1)
                            if key[0] > class_target or key[1] > 12 - diameter_2 or key[2] > 6 - diameter_1:
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
        min(
            first * second - min(first, second),
            first * third - min(first, third),
            second * third - min(second, third),
        )
        for first, second, third in product(sizes, repeat=3)
    )


def energy_profiles(l1_bound: int) -> list[dict[str, object]]:
    rows = []
    for counts in product(range(30), range(8), range(4), range(2), range(2)):
        if sum((index + 1) ** 2 * count for index, count in enumerate(counts)) != 29:
            continue
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        if l1_norm > l1_bound:
            continue
        rows.append({
            "cap": layer_cap(counts),
            "profile": list(counts),
            "l1": l1_norm,
            "odd_classes": sum(counts[0::2]),
        })
    return sorted(rows, key=lambda row: (int(row["cap"]), row["profile"]), reverse=True)


def atanh_log_bounds(value: Fraction, terms: int = 8) -> tuple[Fraction, Fraction]:
    parameter = (value - 1) / (value + 1)
    lower = 2 * sum(parameter ** (2 * index + 1) / (2 * index + 1) for index in range(terms))
    degree = 2 * terms + 1
    return lower, lower + 2 * parameter**degree / (degree * (1 - parameter * parameter))


def add_forms(*forms: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(sum(form[index] for form in forms) for index in range(3))  # type: ignore[return-value]


def scale_form(scalar: Fraction, form: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(scalar * value for value in form)  # type: ignore[return-value]


def cubic_cutoff() -> tuple[int, list[dict[str, object]]]:
    hermite = (
        (Fraction(48735, 79507), Fraction(30772, 79507), Fraction(-3445, 1849)),
        (Fraction(4788, 79507), Fraction(-4788, 79507), Fraction(301253, 1475502)),
        (Fraction(-213, 79507), Fraction(213, 79507), Fraction(-4243, 737751)),
        (Fraction(2, 79507), Fraction(-2, 79507), Fraction(71, 1475502)),
    )
    l2, u2 = atanh_log_bounds(Fraction(2))
    l87, u87 = atanh_log_bounds(Fraction(8, 7))
    l6457, u6457 = atanh_log_bounds(Fraction(64, 57))
    signs = []
    for moment in range(0, 5000):
        form = add_forms(
            hermite[0],
            scale_form(Fraction(16), hermite[1]),
            scale_form(Fraction(314), hermite[2]),
            scale_form(Fraction(6880 + moment), hermite[3]),
        )
        coefficient_2 = Fraction(-(704825 - 128 * moment), 2544224)
        lower = coefficient_2 * u2 + form[0] * l87 + form[1] * l6457 - form[2]
        upper = coefficient_2 * l2 + form[0] * u87 + form[1] * u6457 - form[2]
        if lower > 0 or upper < 0:
            signs.append({
                "moment": moment,
                "form": [str(value) for value in form],
                "coefficient_log2": str(coefficient_2),
                "certified_sign": 1 if lower > 0 else -1,
            })
    cutoff = max(int(row["moment"]) for row in signs if int(row["certified_sign"]) == 1)
    boundary = [row for row in signs if int(row["moment"]) in (cutoff, cutoff + 1)]
    assert [row["certified_sign"] for row in boundary] == [1, -1]
    return cutoff, boundary


def distance(left: int, right: int) -> int:
    difference = (left - right) % 128
    return min(difference, 128 - difference)


def canonical(support: tuple[int, ...]) -> tuple[int, ...]:
    return min(
        tuple(sorted((unit * (value - anchor)) % 128 for value in support))
        for anchor in support
        for unit in UNITS
    )


def light_geometry() -> dict[str, object]:
    counts: Counter[int] = Counter()
    partitions: defaultdict[int, Counter[tuple[int, ...]]] = defaultdict(Counter)
    orbits: defaultdict[int, set[tuple[int, ...]]] = defaultdict(set)
    repeated_shared: Counter[int] = Counter()
    for rest in combinations(range(1, 128), 3):
        support = (0,) + rest
        chords = [(distance(left, right), left, right) for left, right in combinations(support, 2)]
        if sum(chord == 64 for chord, _, _ in chords) != 1:
            continue
        multiplicities = Counter(chord for chord, _, _ in chords if chord != 64)
        odd = sum(count % 2 for count in multiplicities.values())
        counts[odd] += 1
        partitions[odd][tuple(sorted(multiplicities.values(), reverse=True))] += 1
        orbits[odd].add(canonical(support))
        repeated = [chord for chord, count in multiplicities.items() if count > 1]
        if len(repeated) == 1 and multiplicities[repeated[0]] == 2:
            edges = [(left, right) for chord, left, right in chords if chord == repeated[0]]
            repeated_shared[odd] += bool(set(edges[0]) & set(edges[1]))
    return {
        "support_counts": {str(key): value for key, value in sorted(counts.items())},
        "orbit_counts": {str(key): len(value) for key, value in sorted(orbits.items())},
        "partition_histograms": {
            str(odd): {str(list(partition)): count for partition, count in sorted(histogram.items())}
            for odd, histogram in sorted(partitions.items())
        },
        "repeated_chord_shared_vertex": {
            str(key): value for key, value in sorted(repeated_shared.items())
        },
        "orbit_representatives": {
            str(key): [list(value) for value in sorted(values)]
            for key, values in sorted(orbits.items())
        },
    }


@app.function(cpu=1.0, memory=256, timeout=60)
def compute() -> dict[str, object]:
    slack = relaxed_minimum_energy_by_slack(40)
    trace = []
    l1_bound = None
    for l1_norm in range(23, 14, -1):
        delta = 29 + 66 - 4 * l1_norm
        trace.append([l1_norm, delta, slack[delta]])
        if slack[delta] is not None and int(slack[delta]) <= 29 and l1_bound is None:
            l1_bound = l1_norm
    assert l1_bound is not None
    profiles = energy_profiles(l1_bound)
    cutoff, boundary = cubic_cutoff()
    above = [row for row in profiles if int(row["cap"]) > cutoff]
    survivors = [row for row in above if int(row["odd_classes"]) <= 5]
    diameter_ledgers = []
    for heavy_heavy in range(2):
        for heavy_light in range(4):
            if heavy_light > min(3 - 2 * heavy_heavy, 2):
                continue
            square_mass = 1 + 4 * heavy_light + 16 * heavy_heavy
            diameter_ledgers.append([square_mass, (square_mass - 73) // 2])
    return {
        "complete": True,
        "variance": 58,
        "energy": 29,
        "slack_trace": trace,
        "l1_bound": l1_bound,
        "profiles": profiles,
        "profile_count": len(profiles),
        "cubic_cutoff": cutoff,
        "cubic_boundary": boundary,
        "above_cutoff": above,
        "parity_survivors": survivors,
        "diameter_ledgers": sorted(diameter_ledgers),
        "light_geometry": light_geometry(),
    }


@app.local_entrypoint()
def main() -> None:
    packet = compute.remote()
    packet["schema"] = "e1-e29-profile-parity-probe-v1"
    packet["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print("E29_PROFILE_PARITY_PROBE " + json.dumps({
        "l1_bound": packet["l1_bound"],
        "profiles": packet["profile_count"],
        "cubic_cutoff": packet["cubic_cutoff"],
        "above_cutoff": len(packet["above_cutoff"]),
        "survivors": packet["parity_survivors"],
        "support_counts": packet["light_geometry"]["support_counts"],
        "orbit_counts": packet["light_geometry"]["orbit_counts"],
    }, sort_keys=True))
    print(f"E29_PROFILE_PARITY_PROBE_RESULT {RESULT}")
