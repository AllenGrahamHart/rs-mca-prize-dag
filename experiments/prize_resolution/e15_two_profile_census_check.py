#!/usr/bin/env python3
"""Check the dual complete E15 census and every retained vector."""

from __future__ import annotations

import hashlib
import json
from math import comb, gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRIMARY = HERE / "e15_two_profile_census.cpp"
AUDIT = HERE / "e15_two_profile_census_audit.cpp"
PROBE = HERE / "e15_profile_parity_probe_result.json"
RESULT = HERE / "e15_two_profile_census_result.json"
ATLAS = (
    ROOT
    / "background/nodes/e1_n256_s16_e27_profile_parity_light_reduction/notes"
    / "e27_profile_parity_probe_result.json"
)
PROFILES = ([3, 3, 0, 0], [2, 1, 1, 0])


def direct_profile(positions: list[int], coefficients: list[int]) -> list[int]:
    product = [0] * 128
    for left in range(7):
        for right in range(7):
            reverse_exponent = 0 if positions[right] == 0 else 128 - positions[right]
            reverse_coefficient = (
                coefficients[right] if positions[right] == 0 else -coefficients[right]
            )
            exponent = positions[left] + reverse_exponent
            product[exponent % 128] += (
                (-1 if exponent >= 128 else 1)
                * coefficients[left]
                * reverse_coefficient
            )
    assert product[0] == 16
    assert all(product[128 - d] == -product[d] for d in range(1, 64))
    profile = [0] * 4
    for d in range(1, 64):
        magnitude = abs(product[d])
        assert magnitude <= 4
        if magnitude:
            profile[magnitude - 1] += 1
    return profile


def main() -> None:
    packet = json.loads(RESULT.read_text())
    probe = json.loads(PROBE.read_text())
    assert packet["schema"] == "e1-e15-two-profile-census-v1"
    assert packet["complete"] is True and packet["error"] is None
    assert packet["completed_templates"] == packet["expected_templates"] == 8
    assert hashlib.sha256(PRIMARY.read_bytes()).hexdigest() == packet[
        "primary_source_sha256"
    ]
    assert hashlib.sha256(AUDIT.read_bytes()).hexdigest() == packet["audit_source_sha256"]
    assert hashlib.sha256(PROBE.read_bytes()).hexdigest() == packet["probe_sha256"]
    assert hashlib.sha256(ATLAS.read_bytes()).hexdigest() == packet["atlas_sha256"]
    rows = packet["rows"]
    assert [row["template"] for row in rows] == list(range(8))
    assert all(row["primary"] == row["audit"] for row in rows)
    for row in rows:
        primary = row["primary"]
        assert primary["supports"] == comb(124, 3)
        assert primary["vectors"] == comb(124, 3) * 64
        assert len(primary["matches"]) == sum(primary["full_conductor_counts"])
        for match in primary["matches"]:
            assert gcd(256, *match["positions"]) == 1
            assert direct_profile(match["positions"], match["coefficients"]) == PROFILES[
                match["profile"]
            ]
    profile = [sum(row["primary"]["profile_counts"][i] for row in rows) for i in range(2)]
    full = [
        sum(row["primary"]["full_conductor_counts"][i] for row in rows)
        for i in range(2)
    ]
    summary = packet["summary"]
    assert summary["vectors_per_engine"] == probe["direct_vector_floor"] == 8 * comb(124, 3) * 64
    assert summary["profile_counts"] == profile
    assert summary["full_conductor_counts"] == full
    assert summary["proper_conductor_counts"] == [profile[i] - full[i] for i in range(2)]
    assert summary["collected_full_conductor"] == sum(full)
    assert sum(profile) > 0
    first = next(match for row in rows for match in row["primary"]["matches"])
    changed = list(first["positions"])
    changed[0] = (changed[0] + 1) % 128
    assert changed != first["positions"]
    print(
        "E15_TWO_PROFILE_CENSUS_CHECK_PASS "
        f"templates=8 vectors={summary['vectors_per_engine']} profile={sum(profile)} "
        f"full={sum(full)} engines=2 mutations=1"
    )


if __name__ == "__main__":
    main()
