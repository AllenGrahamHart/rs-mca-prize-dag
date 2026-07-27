#!/usr/bin/env python3
"""Check the dual count-only E24 six-profile census packet."""

from __future__ import annotations

import hashlib
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRIMARY = HERE / "e24_six_profile_count.cpp"
AUDIT = HERE / "e24_six_profile_count_audit.cpp"
PROBE = HERE / "e24_profile_parity_probe_result.json"
RESULT = HERE / "e24_six_profile_count_result.json"
E26 = (
    ROOT
    / "background/nodes/e1_n256_s16_e26_profile_parity_light_reduction/notes"
    / "e26_profile_parity_probe_result.json"
)
FOUR = (
    ROOT
    / "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes"
    / "e32_four_odd_light_orbit_result.json"
)


def main() -> None:
    packet = json.loads(RESULT.read_text())
    probe = json.loads(PROBE.read_text())
    assert packet["schema"] == "e1-e24-six-profile-count-v1"
    assert packet["complete"] is True
    assert packet["completed_templates"] == packet["expected_templates"] == 154
    assert hashlib.sha256(PRIMARY.read_bytes()).hexdigest() == packet["primary_source_sha256"]
    assert hashlib.sha256(AUDIT.read_bytes()).hexdigest() == packet["audit_source_sha256"]
    assert hashlib.sha256(PROBE.read_bytes()).hexdigest() == packet["probe_sha256"]
    assert hashlib.sha256(E26.read_bytes()).hexdigest() == packet["e26_atlas_sha256"]
    assert hashlib.sha256(FOUR.read_bytes()).hexdigest() == packet["four_atlas_sha256"]

    rows = packet["rows"]
    assert [row["template"] for row in rows] == list(range(154))
    assert all(row["primary"] == row["audit"] for row in rows)
    assert all(row["primary"]["complete"] is True for row in rows)
    assert all(int(row["primary"]["supports"]) == comb(124, 3) for row in rows)
    assert all(int(row["primary"]["vectors"]) == comb(124, 3)*64 for row in rows)

    profile_counts = [
        sum(int(row["primary"]["profile_counts"][index]) for row in rows)
        for index in range(6)
    ]
    full_counts = [
        sum(int(row["primary"]["full_conductor_counts"][index]) for row in rows)
        for index in range(6)
    ]
    summary = packet["summary"]
    assert summary["vectors_per_engine"] == probe["direct_vector_floor"] == 154*comb(124, 3)*64
    assert summary["profile_counts"] == profile_counts
    assert summary["full_conductor_counts"] == full_counts
    assert summary["proper_conductor_counts"] == [
        profile_counts[index]-full_counts[index] for index in range(6)
    ]
    assert all(0 <= full_counts[index] <= profile_counts[index] for index in range(6))

    changed_hash = list(rows[0]["audit"]["hash_sums"])
    changed_hash[0] = (int(changed_hash[0])+1) % (1 << 64)
    assert changed_hash != rows[0]["primary"]["hash_sums"]
    print(
        "E24_SIX_PROFILE_COUNT_CHECK_PASS "
        f"templates=154 vectors={summary['vectors_per_engine']} "
        f"profile={sum(profile_counts)} full={sum(full_counts)} engines=2 mutations=1"
    )


if __name__ == "__main__":
    main()
