#!/usr/bin/env python3
"""Independently check the dual E21 full-conductor collection."""

from __future__ import annotations

import hashlib
import json
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
PRIMARY = HERE / "e21_seven_profile_collect.cpp"
AUDIT = HERE / "e21_seven_profile_collect_audit.cpp"
PROBE = HERE / "e21_profile_parity_probe_result.json"
COUNT = HERE / "e21_seven_profile_count_result.json"
RESULT = HERE / "e21_seven_profile_collect_result.json"
PROFILES = (
    (5, 4, 0, 0),
    (1, 5, 0, 0),
    (4, 2, 1, 0),
    (0, 3, 1, 0),
    (3, 0, 2, 0),
    (5, 0, 0, 1),
    (1, 1, 0, 1),
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def negacyclic_profile(match: dict[str, object]) -> tuple[int, ...]:
    positions = [int(value) for value in match["positions"]]
    coefficients = [int(value) for value in match["coefficients"]]
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
    assert all(
        product[128 - difference] == -product[difference]
        for difference in range(1, 64)
    )
    profile = [0, 0, 0, 0]
    for value in product[1:64]:
        magnitude = abs(value)
        assert magnitude <= 4
        if magnitude:
            profile[magnitude - 1] += 1
    return tuple(profile)


def main() -> None:
    packet = json.loads(RESULT.read_text())
    count = json.loads(COUNT.read_text())
    assert packet["schema"] == "e1-e21-seven-profile-collect-v1"
    assert packet["complete"] is True and packet["error"] is None
    assert packet["completed_templates"] == packet["expected_templates"] == 111
    assert packet["primary_source_sha256"] == digest(PRIMARY)
    assert packet["audit_source_sha256"] == digest(AUDIT)
    assert packet["probe_sha256"] == digest(PROBE)
    assert packet["count_sha256"] == digest(COUNT)
    rows = packet["rows"]
    assert [int(row["template"]) for row in rows] == list(range(111))
    assert all(row["primary"] == row["audit"] for row in rows)
    summary = packet["summary"]
    for key in (
        "vectors_per_engine",
        "profile_counts",
        "full_conductor_counts",
        "hash_sums",
        "hash_xors",
    ):
        assert summary[key] == count["summary"][key]

    per_profile = [0] * 7
    matches = []
    for row in rows:
        primary = row["primary"]
        assert len(primary["matches"]) == sum(
            int(value) for value in primary["full_conductor_counts"]
        )
        for match in primary["matches"]:
            profile = int(match["profile"])
            positions = [int(value) for value in match["positions"]]
            assert 0 <= profile < 7 and len(positions) == 7
            assert gcd(256, *positions) == 1
            assert negacyclic_profile(match) == PROFILES[profile]
            per_profile[profile] += 1
            matches.append(match)
    assert per_profile == summary["full_conductor_counts"]
    assert len(matches) == summary["collected_full_conductor"] == sum(per_profile)
    print(
        "E21_SEVEN_PROFILE_COLLECT_CHECK_PASS "
        f"templates=111 vectors={summary['vectors_per_engine']} "
        f"matches={len(matches)} profiles={per_profile} engines=2"
    )


if __name__ == "__main__":
    main()
