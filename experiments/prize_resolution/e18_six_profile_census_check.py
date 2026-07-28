#!/usr/bin/env python3
"""Check the dual complete E18 census and every retained vector."""

from __future__ import annotations

import hashlib
import json
from math import comb, gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRIMARY = HERE / "e18_six_profile_census.cpp"
AUDIT = HERE / "e18_six_profile_census_audit.cpp"
PROBE = HERE / "e18_profile_parity_probe_result.json"
RESULT = HERE / "e18_six_profile_census_result.json"
TWO_ATLAS = (
    ROOT
    / "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes"
    / "e30_two_six_odd_light_orbit_result.json"
)
SIX_ATLAS = (
    ROOT
    / "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes"
    / "e30_six_odd_mask_orbits_result.json"
)
PROFILES = (
    (6, 3, 0, 0),
    (2, 4, 0, 0),
    (5, 1, 1, 0),
    (1, 2, 1, 0),
    (0, 0, 2, 0),
    (2, 0, 0, 1),
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def direct_profile(match: dict[str, object]) -> tuple[int, ...]:
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
    assert all(product[128 - d] == -product[d] for d in range(1, 64))
    profile = [0, 0, 0, 0]
    for value in product[1:64]:
        magnitude = abs(value)
        assert magnitude <= 4
        if magnitude:
            profile[magnitude - 1] += 1
    return tuple(profile)


def main() -> None:
    packet = json.loads(RESULT.read_text())
    probe = json.loads(PROBE.read_text())
    assert packet["schema"] == "e1-e18-six-profile-census-v1"
    assert packet["complete"] is True and packet["error"] is None
    assert packet["completed_templates"] == packet["expected_templates"] == 1321
    assert packet["primary_source_sha256"] == digest(PRIMARY)
    assert packet["audit_source_sha256"] == digest(AUDIT)
    assert packet["probe_sha256"] == digest(PROBE)
    assert packet["two_atlas_sha256"] == digest(TWO_ATLAS)
    assert packet["six_atlas_sha256"] == digest(SIX_ATLAS)
    rows = packet["rows"]
    assert [int(row["template"]) for row in rows] == list(range(1321))
    assert all(row["primary"] == row["audit"] for row in rows)
    summary = packet["summary"]
    assert summary["vectors_per_engine"] == probe["direct_vector_floor"]
    assert summary["vectors_per_engine"] == 1321 * comb(124, 3) * 64
    profile = [sum(int(row["primary"]["profile_counts"][i]) for row in rows) for i in range(6)]
    full = [sum(int(row["primary"]["full_conductor_counts"][i]) for row in rows) for i in range(6)]
    assert summary["profile_counts"] == profile
    assert summary["full_conductor_counts"] == full
    assert summary["proper_conductor_counts"] == [profile[i] - full[i] for i in range(6)]
    seen = [0] * 6
    matches = []
    for row in rows:
        primary = row["primary"]
        assert primary["supports"] == comb(124, 3)
        assert primary["vectors"] == comb(124, 3) * 64
        assert len(primary["matches"]) == sum(primary["full_conductor_counts"])
        for match in primary["matches"]:
            index = int(match["profile"])
            positions = [int(value) for value in match["positions"]]
            assert 0 <= index < 6 and gcd(256, *positions) == 1
            assert direct_profile(match) == PROFILES[index]
            seen[index] += 1
            matches.append(match)
    assert seen == full
    assert len(matches) == summary["collected_full_conductor"] == sum(full)
    assert all(profile)
    changed = list(matches[0]["positions"])
    changed[0] = (changed[0] + 1) % 128
    assert changed != matches[0]["positions"]
    print(
        "E18_SIX_PROFILE_CENSUS_CHECK_PASS "
        f"templates=1321 vectors={summary['vectors_per_engine']} "
        f"profile={sum(profile)} full={sum(full)} engines=2 mutations=1"
    )


if __name__ == "__main__":
    main()
