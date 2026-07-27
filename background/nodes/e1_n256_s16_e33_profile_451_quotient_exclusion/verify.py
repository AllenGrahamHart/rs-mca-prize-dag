#!/usr/bin/env python3
"""Verify the E=33 profile-(4,5,1) quotient exclusion."""

from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
from collections import defaultdict
from itertools import combinations_with_replacement
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e33_profile_451_quotient_exclusion"
PROFILE = "e1_n256_s16_e33_profile_parity_diameter_reduction"
CONDUCTOR = "e1_n256_proper_conductor_collision_exclusion"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
PROFILE_COUNTS = (4, 5, 1)
CAPACITIES = {
    128: (3, 8, 8, 8, 8, 8, 8, 8, 4),
    64: (1, 4, 4, 4, 4, 4, 4, 4, 2),
}
EXPECTED_PIN = {
    "base_census_file": "background/nodes/e1_n256_s16_sparse_l1_variance_exclusion/notes/e34_nested_quotient_census.cpp",
    "base_census_file_sha256": "ccdcefeb71d7805183c763aca062fe4da6a86ff6ff542ab8a0200267021f69f4",
    "collision_norm_file": "critical/nodes/collision_norm_criterion/statement.md",
    "collision_norm_file_sha256": "862ec8444336d720abe4f4d64edb2f28a1edf8e6b0d10fe3611923378e951566",
    "launcher_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/notes/e33_profile451_quotient_probe_modal.py",
    "launcher_file_sha256": "b5a910d792103fe3b431078fe0e2e4523b5f5d4c146a337c235df76e73432acf",
    "profile_reduction_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/statement.md",
    "profile_reduction_file_sha256": "5828b3f3a1c340075993b37eb218ad13bf0cb445a2807619c37e0b6a2965959b",
    "proper_conductor_file": "background/nodes/e1_n256_proper_conductor_collision_exclusion/statement.md",
    "proper_conductor_file_sha256": "4319261b9d388351f2980fd4f849d7fae4876a6e5db167c74467ea957a055d73",
    "wrapper_census_file": "background/nodes/e1_n256_s16_e33_profile_parity_diameter_reduction/notes/e33_profile451_quotient_census.cpp",
    "wrapper_census_file_sha256": "ee63f3ea73ddd9acc1a086a542f9cb5b2604edcd2983672f5dc0d910c267136b",
}


def residues(counts: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * 16
    answer[0] = 2 * counts[0]
    answer[8] = 2 * counts[8]
    for residue in range(1, 8):
        answer[residue] = answer[16 - residue] = counts[residue]
    return tuple(answer)


def directed(
    left: tuple[int, ...], right: tuple[int, ...], target: tuple[int, ...]
) -> int:
    answer = 0
    for target_residue in range(16):
        pairs = sum(
            left[source] * right[(-target_residue - source) % 16]
            for source in range(16)
        )
        if target_residue == 0:
            pairs -= min(sum(left), sum(right))
        per_target = sum(
            min(left[source], right[(-target_residue - source) % 16])
            for source in range(16)
        )
        answer += min(pairs, target[target_residue] * per_target)
    return answer


def triple(
    first: tuple[int, ...], second: tuple[int, ...], third: tuple[int, ...]
) -> int:
    return min(
        directed(first, second, third),
        directed(first, third, second),
        directed(second, third, first),
    )


def objective(exact: tuple[tuple[int, ...], ...]) -> int:
    layers = [
        residues(
            tuple(
                sum(exact[level][category] for level in range(start, 3))
                for category in range(9)
            )
        )
        for start in range(3)
    ]
    answer = 0
    for first, second, third in combinations_with_replacement(range(3), 3):
        totals = tuple(sum(layers[index]) for index in (first, second, third))
        contribution = (
            0
            if totals == (2, 2, 2)
            else triple(layers[first], layers[second], layers[third])
        )
        multiplicity = (
            1
            if first == third
            else 3
            if first == second or second == third
            else 6
        )
        answer += multiplicity * contribution
    return answer


def allocation_count(capacities: tuple[int, ...]) -> int:
    states = {((0, 0, 0), False): 1}
    for category, capacity in enumerate(capacities):
        additions = []
        for first in range(capacity + 1):
            for second in range(capacity - first + 1):
                for third in range(capacity - first - second + 1):
                    additions.append((first, second, third))
        updated: defaultdict[tuple[tuple[int, ...], bool], int] = defaultdict(int)
        for (used, has_odd), count in states.items():
            for addition in additions:
                new = tuple(
                    used[index] + addition[index] for index in range(3)
                )
                if any(
                    new[index] > PROFILE_COUNTS[index] for index in range(3)
                ):
                    continue
                updated[
                    (
                        new,
                        has_odd
                        or (category in (1, 3, 5, 7) and sum(addition) > 0),
                    )
                ] += count
        states = updated
    return states[(PROFILE_COUNTS, True)]


def compile_binary(directory: Path, pin: dict[str, str]) -> Path:
    binary = directory / "e33_profile451_quotient"
    base = ROOT / pin["base_census_file"]
    wrapper = ROOT / pin["wrapper_census_file"]
    subprocess.run(
        [
            "g++",
            "-O3",
            "-std=c++17",
            "-I",
            str(base.parent),
            str(wrapper),
            "-o",
            str(binary),
        ],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    return binary


def run_census(binary: Path, shards: int) -> list[dict[str, object]]:
    rows = []
    for order in (128, 64):
        for shard in range(shards):
            completed = subprocess.run(
                [str(binary), str(order), str(shard), str(shards)],
                check=True,
                capture_output=True,
                text=True,
                timeout=30,
            )
            rows.append(json.loads(completed.stdout))
    return rows


def check_rows(rows: list[dict[str, object]], shards: int) -> None:
    for order, capacities in CAPACITIES.items():
        selected = [row for row in rows if int(row["order"]) == order]
        assert {int(row["shard"]) for row in selected} == set(range(shards))
        assert sum(int(row["tested"]) for row in selected) == allocation_count(
            capacities
        )
        for row in selected:
            assert row["complete"] is True
            assert tuple(row["profile_counts"]) == PROFILE_COUNTS
            exact = tuple(tuple(map(int, values)) for values in row["exact"])
            assert tuple(sum(values) for values in exact) == PROFILE_COUNTS
            outer = tuple(
                sum(exact[level][category] for level in range(3))
                for category in range(9)
            )
            assert all(
                outer[index] <= capacities[index] for index in range(9)
            )
            assert any(outer[index] for index in (1, 3, 5, 7))
            assert objective(exact) == int(row["best"])
    assert {
        order: max(
            int(row["best"]) for row in rows if int(row["order"]) == order
        )
        for order in CAPACITIES
    } == {128: 1732, 64: 1670}


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[
                key + "_sha256"
            ]
    with tempfile.TemporaryDirectory() as temporary:
        rows = run_census(compile_binary(Path(temporary), pin), 16)
    check_rows(rows, 16)
    assert allocation_count(CAPACITIES[128]) == 5_421_301
    assert allocation_count(CAPACITIES[64]) == 3_086_861
    assert 50**32 < 2**250

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in (PROFILE, CONDUCTOR, NORM):
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "M_3<=1732" in nodes[NODE]["statement"]
    print(
        "E1_N256_S16_E33_PROFILE_451_QUOTIENT_EXCLUSION_PASS "
        "order128=5421301/1732 order64=3086861/1670 shards=16"
    )


if __name__ == "__main__":
    main()
