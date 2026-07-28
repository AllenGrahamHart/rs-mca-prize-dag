#!/usr/bin/env python3
"""Verify the prize N=256 profile-(4,2,0) cofactor-256 exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_m256_collision_exclusion"
PARENT = "e1_prize_n256_s18_variance_cofactor_windows"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
ENERGIES = [5, 9, 13, 17, 21, 25, 29, 33, 37]
ENERGY_COUNTS = [0, 28, 52, 204, 212, 864, 956, 15364, 3076]
B_PRIZE = 317494674775468773183020924238786383963
MAX_BELOW = 79966870433624456578392518772995331447805526474703846245310288507286369992961
MIN_ABOVE = 127117908459354031873489386413391045324297956117263458825602208201263580806401


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def energy(positions: list[int], coefficients: list[int]) -> int:
    values = [0] * 64
    for left in range(6):
        for right in range(left + 1, 6):
            difference = abs(positions[right] - positions[left])
            product = coefficients[left] * coefficients[right]
            if difference == 64:
                continue
            if difference < 64:
                values[difference] += product
            else:
                values[128 - difference] -= product
    return sum(value * value for value in values[1:])


def primary_shard_counts() -> list[int]:
    jobs = []
    for first in range(126):
        for second in range(first + 1, 126):
            remaining = 125 - second
            combinations = remaining * (remaining - 1) // 2
            if combinations:
                jobs.append((32 * combinations, first, second))
    jobs.sort(reverse=True)
    loads = [0] * 32
    combinations = [0] * 32
    for weight, _, _ in jobs:
        shard = min(range(32), key=lambda index: (loads[index], index))
        loads[shard] += weight
        combinations[shard] += weight // 32
    return combinations


def main() -> None:
    checks = 0
    pins = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    for key, value in pins.items():
        if key.endswith("_file"):
            assert digest(ROOT / value) == pins[key[:-5] + "_sha256"]
            checks += 1

    primary = json.loads((ROOT / pins["primary_result_file"]).read_text())
    audit = json.loads((ROOT / pins["audit_result_file"]).read_text())
    flint = json.loads((ROOT / pins["flint_result_file"]).read_text())
    pari = json.loads((ROOT / pins["pari_result_file"]).read_text())
    expected_totals = {
        "combination_count": math.comb(126, 4),
        "signed_vector_count": 32 * math.comb(126, 4),
        "energy_counts": ENERGY_COUNTS,
    }
    assert primary["complete"] is True and not primary["errors"]
    assert audit["complete"] is True and not audit["errors"]
    assert primary["totals"] == expected_totals
    assert audit["totals"] == expected_totals
    checks += 4

    primary_rows = sorted(primary["results"], key=lambda row: int(row["shard"]))
    audit_rows = sorted(audit["results"], key=lambda row: int(row["shard"]))
    assert [row["combination_count"] for row in primary_rows] == primary_shard_counts()
    quotient, remainder = divmod(math.comb(126, 4), 32)
    assert [row["combination_count"] for row in audit_rows] == [
        quotient + (index < remainder) for index in range(32)
    ]
    assert all(row["global_combination_count"] == math.comb(126, 4) for row in audit_rows)
    checks += 3

    witnesses = primary["witnesses"]
    assert len(witnesses) == sum(ENERGY_COUNTS) == 20756
    assert Counter(witness["energy"] for witness in witnesses) == Counter({
        value: count for value, count in zip(ENERGIES, ENERGY_COUNTS) if count
    })
    assert len({
        (tuple(witness["positions"]), tuple(witness["coefficients"]))
        for witness in witnesses
    }) == 20756
    checks += 3
    for witness in witnesses:
        assert witness["positions"][:2] == [0, 8]
        assert energy(witness["positions"], witness["coefficients"]) == witness["energy"]
        checks += 2

    p_min = B_PRIZE * 2**128
    p_max = (B_PRIZE + 1) * 2**128 - 1
    assert flint["complete"] is True and not flint["errors"]
    assert flint["row_count"] == 20756
    assert flint["prize_interval"] == [p_min, p_max]
    assert not flint["interval_rows"]
    assert flint["maximum_below"]["candidate"] == MAX_BELOW < p_min
    assert flint["minimum_above"]["candidate"] == MIN_ABOVE > p_max
    for energy_value, expected in zip(ENERGIES, ENERGY_COUNTS):
        row = flint["counts"][str(energy_value)]
        assert row["inside"] == 0
        if energy_value == 9:
            assert row == {"below": 0, "inside": 0, "above": expected}
        else:
            assert row == {"below": expected, "inside": 0, "above": 0}
        checks += 2
    checks += 6

    assert pari["complete"] is True and not pari["errors"]
    assert pari["row_count"] == 20756
    assert pari["primary_match"] is True
    flint_shards = sorted(flint["shards"], key=lambda row: int(row["shard"]))
    pari_shards = sorted(pari["shards"], key=lambda row: int(row["shard"]))
    assert [row["shard"] for row in flint_shards] == list(range(32))
    assert [row["shard"] for row in pari_shards] == list(range(32))
    assert [row["commitment_sha256"] for row in flint_shards] == [
        row["commitment_sha256"] for row in pari_shards
    ]
    assert [row["processed"] for row in flint_shards] == [
        row["processed"] for row in pari_shards
    ]
    checks += 7

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {entry["id"]: entry for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARENT]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    checks += 3
    for target in TARGETS:
        assert nodes[target]["status"] == "TARGET"
        assert (NODE, target, "ev") in edges
        assert (NODE, target, "req") not in edges
        checks += 3

    print(
        "E1_PRIZE_N256_S18_M256_COLLISION_EXCLUSION_PASS "
        "normalized_vectors=320292000 residual=20756 interval=0 "
        f"checks={checks}"
    )


if __name__ == "__main__":
    main()
