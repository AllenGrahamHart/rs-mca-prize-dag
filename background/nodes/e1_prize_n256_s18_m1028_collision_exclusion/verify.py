#!/usr/bin/env python3
"""Verify the prize N=256 profile-(4,2,0) cofactor-1028 exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_m1028_collision_exclusion"
PARENT = "e1_prize_n256_s18_variance_cofactor_windows"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
EXPECTED_TOTALS = {
    "combination_count": 10009125,
    "signed_vector_count": 320292000,
    "energy5_count": 0,
    "energy9_count": 16,
    "energy5_div257_count": 0,
    "energy9_div257_count": 0,
}


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


def has_primitive_root(positions: list[int], coefficients: list[int]) -> bool:
    for exponent in range(1, 256, 2):
        value = sum(
            coefficient * pow(3, exponent * position, 257)
            for position, coefficient in zip(positions, coefficients)
        )
        if value % 257 == 0:
            return True
    return False


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
    node_dir = Path(__file__).parent
    pins = json.loads((node_dir / "source_pin.json").read_text())
    for key, value in pins.items():
        if not key.endswith("_file"):
            continue
        hash_key = key[:-5] + "_sha256"
        assert digest(ROOT / value) == pins[hash_key]
        checks += 1

    primary = json.loads((ROOT / pins["primary_result_file"]).read_text())
    audit = json.loads((ROOT / pins["audit_result_file"]).read_text())
    assert primary["complete"] is True and not primary["errors"]
    assert audit["complete"] is True and not audit["errors"]
    assert primary["totals"] == EXPECTED_TOTALS
    assert audit["totals"] == EXPECTED_TOTALS
    assert math.comb(126, 4) == EXPECTED_TOTALS["combination_count"]
    assert 32 * math.comb(126, 4) == EXPECTED_TOTALS["signed_vector_count"]
    checks += 6

    expected_primary = primary_shard_counts()
    primary_rows = sorted(primary["results"], key=lambda row: int(row["shard"]))
    audit_rows = sorted(audit["results"], key=lambda row: int(row["shard"]))
    assert [row["shard"] for row in primary_rows] == list(range(32))
    assert [row["shard"] for row in audit_rows] == list(range(32))
    assert [row["combination_count"] for row in primary_rows] == expected_primary
    quotient, remainder = divmod(math.comb(126, 4), 32)
    assert [row["combination_count"] for row in audit_rows] == [
        quotient + (index < remainder) for index in range(32)
    ]
    assert all(row["global_combination_count"] == math.comb(126, 4) for row in audit_rows)
    checks += 5

    witnesses = primary["witnesses"]
    assert len(witnesses) == 16
    seen = set()
    for witness in witnesses:
        positions = witness["positions"]
        coefficients = witness["coefficients"]
        assert positions[:2] == [0, 2]
        assert positions[2:] == sorted(positions[2:])
        assert len(set(positions)) == 6
        assert coefficients[0] == 1 and abs(coefficients[1]) == 1
        assert all(abs(value) == 2 for value in coefficients[2:])
        assert witness["energy"] == 9 == energy(positions, coefficients)
        assert witness["root_exponent"] == -1
        assert not has_primitive_root(positions, coefficients)
        seen.add((tuple(positions), tuple(coefficients)))
        checks += 8
    assert len(seen) == 16
    assert pow(3, 128, 257) == 256
    assert pow(3, 64, 257) != 1
    checks += 3

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
        "E1_PRIZE_N256_S18_M1028_COLLISION_EXCLUSION_PASS "
        "normalized_vectors=320292000 energy5=0 energy9=16 div257=0 "
        f"checks={checks}"
    )


if __name__ == "__main__":
    main()
