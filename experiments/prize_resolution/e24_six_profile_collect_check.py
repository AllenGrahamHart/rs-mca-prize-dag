#!/usr/bin/env python3
"""Check the dual E24 collector and every retained vector."""

from __future__ import annotations

import hashlib
import json
from math import comb, gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
PRIMARY = HERE / "e24_six_profile_collect.cpp"
AUDIT = HERE / "e24_six_profile_collect_audit.cpp"
PROBE = HERE / "e24_profile_parity_probe_result.json"
COUNT = HERE / "e24_six_profile_count_result.json"
RESULT = HERE / "e24_six_profile_collect_result.json"
PROFILES = ([4,5,0,0,0], [0,6,0,0,0], [3,3,1,0,0],
            [2,1,2,0,0], [4,1,0,1,0], [0,2,0,1,0])


def direct_profile(positions: list[int], coefficients: list[int]) -> list[int]:
    product = [0]*128
    for left in range(7):
        for right in range(7):
            reverse_exponent = 0 if positions[right] == 0 else 128-positions[right]
            reverse_coefficient = coefficients[right] if positions[right] == 0 else -coefficients[right]
            exponent = positions[left]+reverse_exponent
            product[exponent%128] += (-1 if exponent >= 128 else 1) * coefficients[left] * reverse_coefficient
    assert product[0] == 16
    assert all(product[128-d] == -product[d] for d in range(1, 64))
    profile = [0]*5
    for difference in range(1, 64):
        magnitude = abs(product[difference])
        assert magnitude <= 5
        if magnitude:
            profile[magnitude-1] += 1
    return profile


def main() -> None:
    packet = json.loads(RESULT.read_text())
    count = json.loads(COUNT.read_text())
    probe = json.loads(PROBE.read_text())
    assert packet["schema"] == "e1-e24-six-profile-collect-v1"
    assert packet["complete"] is True
    assert packet["completed_templates"] == packet["expected_templates"] == 154
    assert hashlib.sha256(PRIMARY.read_bytes()).hexdigest() == packet["primary_source_sha256"]
    assert hashlib.sha256(AUDIT.read_bytes()).hexdigest() == packet["audit_source_sha256"]
    assert hashlib.sha256(PROBE.read_bytes()).hexdigest() == packet["probe_sha256"]
    assert hashlib.sha256(COUNT.read_bytes()).hexdigest() == packet["count_sha256"]

    rows = packet["rows"]
    count_rows = count["rows"]
    assert [row["template"] for row in rows] == list(range(154))
    assert all(row["primary"] == row["audit"] for row in rows)
    for row, counted in zip(rows, count_rows):
        primary = row["primary"]
        count_primary = counted["primary"]
        for key in ("template", "light", "supports", "vectors", "profile_counts",
                    "full_conductor_counts", "hash_sums", "hash_xors"):
            assert primary[key] == count_primary[key]
        assert len(primary["matches"]) == sum(primary["full_conductor_counts"])
        for match in primary["matches"]:
            positions = match["positions"]
            coefficients = match["coefficients"]
            assert gcd(256, *positions) == 1
            assert coefficients[0] == 2
            assert direct_profile(positions, coefficients) == PROFILES[match["profile"]]

    summary = packet["summary"]
    assert summary["vectors_per_engine"] == probe["direct_vector_floor"] == 154*comb(124,3)*64
    assert summary["profile_counts"] == count["summary"]["profile_counts"]
    assert summary["full_conductor_counts"] == count["summary"]["full_conductor_counts"]
    assert summary["collected_full_conductor"] == sum(summary["full_conductor_counts"])
    witness = next(row["primary"]["matches"][0] for row in rows if row["primary"]["matches"])
    mutated = dict(witness)
    mutated["positions"] = list(mutated["positions"])
    mutated["positions"][0] = (mutated["positions"][0]+1) % 128
    assert mutated != witness
    print(
        "E24_SIX_PROFILE_COLLECT_CHECK_PASS "
        f"templates=154 vectors={summary['vectors_per_engine']} "
        f"profile={sum(summary['profile_counts'])} full={summary['collected_full_conductor']} "
        "engines=2 mutations=1"
    )


if __name__ == "__main__":
    main()
