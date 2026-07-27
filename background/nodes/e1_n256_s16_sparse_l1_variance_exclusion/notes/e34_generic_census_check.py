#!/usr/bin/env python3
"""Independently check the E34 generic census packets."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e34_generic_census.cpp"
PACKET = HERE / "e34_generic_census_result.json"
AUDIT_SOURCE = HERE / "e34_generic_audit.cpp"
AUDIT_PACKET = HERE / "e34_generic_audit_result.json"
ORBIT_PACKET = HERE / "e34_generic_orbit_result.json"


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
    orbit_packet = json.loads(ORBIT_PACKET.read_text())
    rows = orbit_packet["results"]["primary"]["rows"]
    assert len(rows) == 57
    assert packet["schema"] == "e1-e34-generic-census-v1"
    assert packet["complete"] is True and packet["expected_tasks"] == 57
    assert packet["errors"] == []
    assert packet["source_sha256"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    assert packet["orbit_packet_sha256"] == hashlib.sha256(ORBIT_PACKET.read_bytes()).hexdigest()
    assert audit_packet["schema"] == "e1-e34-generic-audit-v1"
    assert audit_packet["complete"] is True and audit_packet["expected_tasks"] == 57
    assert audit_packet["errors"] == []
    assert audit_packet["source_sha256"] == hashlib.sha256(AUDIT_SOURCE.read_bytes()).hexdigest()
    assert audit_packet["orbit_packet_sha256"] == hashlib.sha256(ORBIT_PACKET.read_bytes()).hexdigest()

    results = packet["results"]
    audit_results = audit_packet["results"]
    assert [result["orbit"] for result in results] == list(range(57))
    assert [result["orbit"] for result in audit_results] == list(range(57))
    for orbit, result, audit_result, row in zip(range(57), results, audit_results, rows):
        assert result["heavy"] == audit_result["heavy"] == row["heavy"]
        assert result["supports"] == row["supports"]
        assert result["vectors"] == row["census_vectors"]
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
        positions = witness["positions"]
        coefficients = witness["coefficients"]
        orbit = witness["orbit"]
        assert positions[:3] == rows[orbit]["heavy"]
        assert coefficients[0] == 2 and all(abs(value) == 2 for value in coefficients[:3])
        energy, l1, profile, m3, conductor = ledger(positions, coefficients)
        assert (energy, l1, profile[1], profile[2]) == (34, 20, 6, 7)
        assert all(profile[magnitude] == 0 for magnitude in range(3, 8))
        assert m3 == witness["m3"] and conductor == 1

    totals = {
        key: sum(result[key] for result in results)
        for key in ("supports", "vectors", "energy_34", "profile_67", "full_conductor")
    }
    assert totals["vectors"] == 243285056
    maximum_m3 = max(result["maximum_m3"] for result in results)
    assert maximum_m3 == 1770
    assert maximum_m3 < 1947
    print(
        "E1_E34_GENERIC_CENSUS_CHECK_PASS "
        f"totals={totals} maximum_m3={maximum_m3}"
    )


if __name__ == "__main__":
    main()
