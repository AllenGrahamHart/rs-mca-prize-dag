#!/usr/bin/env python3
"""Independently check the E34 normalized-quarter census packet."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e34_quarter_template_census.cpp"
PACKET = HERE / "e34_quarter_template_census_result.json"
AUDIT_SOURCE = HERE / "e34_quarter_template_audit.cpp"
AUDIT_PACKET = HERE / "e34_quarter_template_audit_result.json"
TASKS = 121


def ledger(positions: list[int], coefficients: list[int]):
    half = [0] * 64
    for left_index in range(7):
        for right_index in range(left_index + 1, 7):
            left, right = sorted((positions[left_index], positions[right_index]))
            difference = right - left
            product = coefficients[left_index] * coefficients[right_index]
            if difference == 64:
                continue
            if difference < 64:
                half[difference] += product
            else:
                half[128 - difference] -= product
    energy = sum(value * value for value in half)
    l1 = sum(abs(value) for value in half)
    profile = {magnitude: sum(abs(value) == magnitude for value in half[1:]) for magnitude in range(1, 8)}
    weight = [0] * 128
    for difference in range(1, 64):
        weight[difference] = abs(half[difference])
        weight[128 - difference] = weight[difference]
    m3 = sum(
        weight[x] * weight[y] * weight[(-x - y) % 128]
        for x in range(128)
        for y in range(128)
    )
    conductor = math.gcd(256, *positions)
    return energy, l1, profile, m3, conductor


def main() -> None:
    packet = json.loads(PACKET.read_text())
    audit_packet = json.loads(AUDIT_PACKET.read_text())
    assert packet["schema"] == "e1-e34-quarter-template-census-v1"
    assert packet["complete"] is True
    assert packet["expected_tasks"] == TASKS
    assert packet["errors"] == []
    assert packet["source_sha256"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    assert audit_packet["schema"] == "e1-e34-quarter-template-audit-v1"
    assert audit_packet["complete"] is True
    assert audit_packet["expected_tasks"] == TASKS
    assert audit_packet["errors"] == []
    assert audit_packet["source_sha256"] == hashlib.sha256(AUDIT_SOURCE.read_bytes()).hexdigest()

    results = packet["results"]
    audit_results = audit_packet["results"]
    assert [result["shard"] for result in results] == list(range(TASKS))
    assert [result["shard"] for result in audit_results] == list(range(TASKS))
    for shard, result in enumerate(results):
        assert result["complete"] is True
        expected_supports = math.comb(123 - shard, 3)
        assert result["supports"] == expected_supports
        assert result["vectors"] == 32 * expected_supports
        assert result["energy_34"] >= result["profile_67"] >= result["full_conductor"]
        audit_result = audit_results[shard]
        for key in (
            "supports",
            "vectors",
            "energy_34",
            "profile_67",
            "full_conductor",
            "maximum_m3",
        ):
            assert audit_result[key] == result[key]

    assert len(packet["witnesses"]) == 8
    for witness in packet["witnesses"]:
        positions = witness["positions"]
        coefficients = witness["coefficients"]
        assert positions[:3] == [0, 32, 64]
        assert coefficients[0] == 2 and coefficients[2] == -2
        assert 96 not in positions
        energy, l1, profile, m3, conductor = ledger(positions, coefficients)
        assert (energy, l1, profile[1], profile[2]) == (34, 20, 6, 7)
        assert all(profile[magnitude] == 0 for magnitude in range(3, 8))
        assert m3 == witness["m3"]
        assert conductor == 1

    supports = sum(result["supports"] for result in results)
    vectors = sum(result["vectors"] for result in results)
    assert supports == math.comb(124, 4)
    assert vectors == 32 * supports
    totals = {
        key: sum(result[key] for result in results)
        for key in ("energy_34", "profile_67", "full_conductor")
    }
    maximum_m3 = max(result["maximum_m3"] for result in results)
    print(
        "E1_E34_QUARTER_TEMPLATE_CENSUS_CHECK_PASS "
        f"supports={supports} vectors={vectors} totals={totals} maximum_m3={maximum_m3}"
    )


if __name__ == "__main__":
    main()
