#!/usr/bin/env python3
"""Independently check the E34 progression census packets."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e34_progression_census.cpp"
PACKET = HERE / "e34_progression_census_result.json"
AUDIT_SOURCE = HERE / "e34_progression_audit.cpp"
AUDIT_PACKET = HERE / "e34_progression_audit_result.json"
TASKS = [1, 2, 4, 8, 16]
MULTIPLICITIES = {1: 32, 2: 16, 4: 8, 8: 4, 16: 2}


def distance(left: int, right: int) -> int:
    delta = (right - left) % 128
    return min(delta, 128 - delta)


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
    profile = {
        magnitude: sum(abs(value) == magnitude for value in half[1:])
        for magnitude in range(1, 8)
    }
    weight = [0] * 128
    for difference in range(1, 64):
        weight[difference] = abs(half[difference])
        weight[128 - difference] = weight[difference]
    m3 = sum(
        weight[x] * weight[y] * weight[(-x - y) % 128]
        for x in range(128)
        for y in range(128)
    )
    return energy, l1, profile, m3, math.gcd(256, *positions)


def main() -> None:
    packet = json.loads(PACKET.read_text())
    audit_packet = json.loads(AUDIT_PACKET.read_text())
    assert packet["schema"] == "e1-e34-progression-census-v1"
    assert packet["complete"] is True and packet["expected_tasks"] == TASKS
    assert packet["errors"] == []
    assert packet["source_sha256"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    assert audit_packet["schema"] == "e1-e34-progression-audit-v1"
    assert audit_packet["complete"] is True and audit_packet["expected_tasks"] == TASKS
    assert audit_packet["errors"] == []
    assert audit_packet["source_sha256"] == hashlib.sha256(AUDIT_SOURCE.read_bytes()).hexdigest()

    results = packet["results"]
    audit_results = audit_packet["results"]
    assert [result["t"] for result in results] == TASKS
    assert [result["t"] for result in audit_results] == TASKS
    supports_per_t = 1195965
    for t, result, audit_result in zip(TASKS, results, audit_results):
        assert result["complete"] is True and audit_result["complete"] is True
        assert result["supports"] == supports_per_t
        assert result["vectors"] == 32 * supports_per_t
        assert result["energy_34"] >= result["profile_67"] >= result["full_conductor"]
        for key in (
            "supports",
            "vectors",
            "energy_34",
            "profile_67",
            "full_conductor",
            "maximum_m3",
        ):
            assert audit_result[key] == result[key]

    assert 1 <= len(packet["witnesses"]) <= 12
    for witness in packet["witnesses"]:
        t = witness["t"]
        positions = witness["positions"]
        coefficients = witness["coefficients"]
        assert positions[:3] == [0, t, 2 * t] and t in TASKS
        light = set(positions[3:])
        weld = {(-2 * t) % 128, (3 * t) % 128, (-t) % 128, (4 * t) % 128}
        assert light & weld
        assert coefficients[0] == 2 and coefficients[2] == -2
        energy, l1, profile, m3, conductor = ledger(positions, coefficients)
        assert (energy, l1, profile[1], profile[2]) == (34, 20, 6, 7)
        assert all(profile[magnitude] == 0 for magnitude in range(3, 8))
        assert m3 == witness["m3"] and conductor == 1
        outer = distance(positions[0], positions[2])
        assert any(distance(light_position, heavy) == outer for light_position in light for heavy in positions[:3])

    representative_totals = {
        key: sum(result[key] for result in results)
        for key in ("supports", "vectors", "energy_34", "profile_67", "full_conductor")
    }
    weighted_totals = {
        key: sum(MULTIPLICITIES[result["t"]] * result[key] for result in results)
        for key in ("supports", "vectors", "energy_34", "profile_67", "full_conductor")
    }
    assert representative_totals["supports"] == 5 * supports_per_t
    assert representative_totals["vectors"] == 191354400
    assert weighted_totals["supports"] == 62 * supports_per_t
    assert weighted_totals["vectors"] == 2372794560
    maximum_m3 = max(result["maximum_m3"] for result in results)
    assert maximum_m3 == 1722
    assert maximum_m3 < 1947
    print(
        "E1_E34_PROGRESSION_CENSUS_CHECK_PASS "
        f"representative_totals={representative_totals} "
        f"weighted_totals={weighted_totals} maximum_m3={maximum_m3}"
    )


if __name__ == "__main__":
    main()
