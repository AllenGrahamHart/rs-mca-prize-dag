#!/usr/bin/env python3
"""Validate the complete dual E21 count packet and its pins."""

from __future__ import annotations

import hashlib
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRIMARY = HERE / "e21_seven_profile_count.cpp"
AUDIT = HERE / "e21_seven_profile_count_audit.cpp"
PROBE = HERE / "e21_profile_parity_probe_result.json"
ATLAS = (
    ROOT
    / "background/nodes/e1_n256_s16_e27_profile_parity_light_reduction/notes"
    / "e27_profile_parity_probe_result.json"
)
RESULT = HERE / "e21_seven_profile_count_result.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    packet = json.loads(RESULT.read_text())
    probe = json.loads(PROBE.read_text())
    assert packet["schema"] == "e1-e21-seven-profile-count-v1"
    assert packet["complete"] is True and packet["error"] is None
    assert packet["completed_templates"] == packet["expected_templates"] == 111
    assert packet["primary_source_sha256"] == digest(PRIMARY)
    assert packet["audit_source_sha256"] == digest(AUDIT)
    assert packet["probe_sha256"] == digest(PROBE)
    assert packet["atlas_sha256"] == digest(ATLAS)
    rows = packet["rows"]
    assert [int(row["template"]) for row in rows] == list(range(111))
    assert all(row["primary"] == row["audit"] for row in rows)
    assert all(row["primary"]["complete"] is True for row in rows)
    assert all(int(row["primary"]["vectors"]) == comb(124, 3) * 64 for row in rows)

    def total(key: str) -> list[int]:
        return [sum(int(row["primary"][key][i]) for row in rows) for i in range(7)]

    summary = packet["summary"]
    assert summary["vectors_per_engine"] == probe["direct_vector_floor"]
    assert summary["profile_counts"] == total("profile_counts")
    assert summary["full_conductor_counts"] == total("full_conductor_counts")
    assert summary["hash_sums"] == total("hash_sums")
    assert summary["hash_xors"] == total("hash_xors")
    assert summary["proper_conductor_counts"] == [
        int(summary["profile_counts"][i]) - int(summary["full_conductor_counts"][i])
        for i in range(7)
    ]
    assert all(int(value) >= 0 for value in summary["proper_conductor_counts"])
    print(
        "E21_SEVEN_PROFILE_COUNT_CHECK_PASS "
        f"templates=111 vectors={summary['vectors_per_engine']} "
        f"profiles={sum(summary['profile_counts'])} full={sum(summary['full_conductor_counts'])}"
    )


if __name__ == "__main__":
    main()
