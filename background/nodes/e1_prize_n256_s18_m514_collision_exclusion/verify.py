#!/usr/bin/env python3
"""Verify the prize N=256 profile-(4,2,0) cofactor-514 exclusion."""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_prize_n256_s18_m514_collision_exclusion"
PARENT = "e1_prize_n256_s18_variance_cofactor_windows"
TARGETS = {
    "e1_official_low_square_mass_pair_budget",
    "e1_official_prime_exception_control",
    "unsafe_crossing_family_instantiation",
}
ENERGIES = [5, 9, 13, 17, 21, 25]
EXPECTED_TOTALS = {
    "combination_count": 10009125,
    "signed_vector_count": 320292000,
    "energy_counts": [0, 16, 8, 88, 88, 232],
    "div257_counts": [0, 4, 4, 48, 40, 88],
}
B_PRIZE = 317494674775468773183020924238786383963
MAX_CANDIDATE = 66082262884856162162140234757894655654959953149381163882659090799481192796929


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


def dividing_roots(positions: list[int], coefficients: list[int]) -> list[int]:
    return [
        exponent
        for exponent in range(1, 256, 2)
        if sum(
            coefficient * pow(3, exponent * position, 257)
            for position, coefficient in zip(positions, coefficients)
        ) % 257 == 0
    ]


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
    assert primary["complete"] is True and not primary["errors"]
    assert audit["complete"] is True and not audit["errors"]
    assert primary["totals"] == EXPECTED_TOTALS
    assert audit["totals"] == EXPECTED_TOTALS
    assert math.comb(126, 4) == EXPECTED_TOTALS["combination_count"]
    checks += 5

    primary_rows = sorted(primary["results"], key=lambda row: int(row["shard"]))
    audit_rows = sorted(audit["results"], key=lambda row: int(row["shard"]))
    assert [row["combination_count"] for row in primary_rows] == primary_shard_counts()
    quotient, remainder = divmod(math.comb(126, 4), 32)
    assert [row["combination_count"] for row in audit_rows] == [
        quotient + (index < remainder) for index in range(32)
    ]
    assert all(row["global_combination_count"] == math.comb(126, 4) for row in audit_rows)
    checks += 3

    divisor_witnesses = [
        witness for witness in primary["witnesses"]
        if int(witness["root_exponent"]) >= 0
    ]
    assert len(divisor_witnesses) == sum(EXPECTED_TOTALS["div257_counts"]) == 184
    assert len({
        (tuple(witness["positions"]), tuple(witness["coefficients"]))
        for witness in divisor_witnesses
    }) == 184
    assert Counter(witness["energy"] for witness in divisor_witnesses) == Counter({
        energy_value: count
        for energy_value, count in zip(ENERGIES, EXPECTED_TOTALS["div257_counts"])
        if count
    })
    checks += 3
    for witness in divisor_witnesses:
        positions = witness["positions"]
        coefficients = witness["coefficients"]
        assert positions[:2] == [0, 1]
        assert energy(positions, coefficients) == witness["energy"]
        roots = dividing_roots(positions, coefficients)
        assert witness["root_exponent"] in roots
        checks += 3

    p_min = B_PRIZE * 2**128
    p_max = (B_PRIZE + 1) * 2**128 - 1
    assert flint["complete"] is True
    assert flint["row_count"] == 184
    assert flint["distinct_norm_count"] == 46
    assert flint["interval_row_count"] == 0
    assert flint["prize_interval"] == [p_min, p_max]
    assert len(flint["rows"]) == len(divisor_witnesses)
    candidates = []
    for witness, row in zip(divisor_witnesses, flint["rows"]):
        assert row["positions"] == witness["positions"]
        assert row["coefficients"] == witness["coefficients"]
        assert row["norm"] % 514 == 0
        assert row["candidate"] == row["norm"] // 514
        assert row["candidate"] < p_min
        candidates.append(row["candidate"])
        checks += 5
    assert max(candidates) == MAX_CANDIDATE < p_min
    checks += 7

    assert pari["complete"] is True
    assert pari["primary_match"] is True
    assert pari["row_count"] == 184
    assert pari["distinct_norm_count"] == 46
    assert pari["interval_row_count"] == 0
    assert pari["maximum_candidate"] == MAX_CANDIDATE
    checks += 6

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
        "E1_PRIZE_N256_S18_M514_COLLISION_EXCLUSION_PASS "
        "normalized_vectors=320292000 div257=184 distinct_norms=46 interval=0 "
        f"checks={checks}"
    )


if __name__ == "__main__":
    main()
