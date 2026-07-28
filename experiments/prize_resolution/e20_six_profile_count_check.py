#!/usr/bin/env python3
"""Validate the complete dual E20 count packet and its pins."""

from __future__ import annotations

import hashlib
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRIMARY = HERE / "e20_six_profile_count.cpp"
AUDIT = HERE / "e20_six_profile_count_audit.cpp"
PROBE = HERE / "e20_profile_parity_probe_result.json"
E26_ATLAS = (
    ROOT
    / "background/nodes/e1_n256_s16_e26_profile_parity_light_reduction/notes"
    / "e26_profile_parity_probe_result.json"
)
FOUR_ATLAS = (
    ROOT
    / "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes"
    / "e32_four_odd_light_orbit_result.json"
)
RESULT = HERE / "e20_six_profile_count_result.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    packet = json.loads(RESULT.read_text())
    probe = json.loads(PROBE.read_text())
    assert packet["schema"] == "e1-e20-six-profile-count-v1"
    assert packet["complete"] is True and packet["error"] is None
    assert packet["completed_templates"] == packet["expected_templates"] == 154
    assert packet["primary_source_sha256"] == digest(PRIMARY)
    assert packet["audit_source_sha256"] == digest(AUDIT)
    assert packet["probe_sha256"] == digest(PROBE)
    assert packet["e26_atlas_sha256"] == digest(E26_ATLAS)
    assert packet["four_atlas_sha256"] == digest(FOUR_ATLAS)
    rows = packet["rows"]
    assert [int(row["template"]) for row in rows] == list(range(154))
    assert all(row["primary"] == row["audit"] for row in rows)
    assert all(row["primary"]["complete"] is True for row in rows)
    assert all(int(row["primary"]["vectors"]) == comb(124, 3) * 64 for row in rows)

    def total(key: str) -> list[int]:
        return [sum(int(row["primary"][key][i]) for row in rows) for i in range(6)]

    summary = packet["summary"]
    assert summary["vectors_per_engine"] == probe["direct_vector_floor"]
    for key in ("profile_counts", "full_conductor_counts", "hash_sums", "hash_xors"):
        assert summary[key] == total(key)
    assert summary["proper_conductor_counts"] == [
        int(summary["profile_counts"][i]) - int(summary["full_conductor_counts"][i])
        for i in range(6)
    ]
    assert all(int(value) >= 0 for value in summary["proper_conductor_counts"])
    print(
        "E20_SIX_PROFILE_COUNT_CHECK_PASS "
        f"templates=154 vectors={summary['vectors_per_engine']} "
        f"profiles={sum(summary['profile_counts'])} full={sum(summary['full_conductor_counts'])}"
    )


if __name__ == "__main__":
    main()
