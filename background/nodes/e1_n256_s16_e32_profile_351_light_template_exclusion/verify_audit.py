#!/usr/bin/env python3
"""Independent packet audit for the E32 profile-(3,5,1) exclusion."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / "background/nodes/e1_n256_s16_e32_profile_parity_diameter_reduction/notes"


def ledger(row: dict[str, object], profile: str) -> tuple[int, int, int, int]:
    value = row[profile]
    return tuple(
        int(value[key])
        for key in ("count", "full_conductor", "maximum_m3", "maximum_full_conductor_m3")
    )


def main() -> None:
    production = json.loads((NOTES / "e32_four_odd_joint_census_result.json").read_text())
    audit = json.loads((NOTES / "e32_four_odd_joint_census_audit_result.json").read_text())
    first = sorted(production["rows"], key=lambda row: int(row["template"]))
    second = sorted(audit["rows"], key=lambda row: int(row["template"]))
    assert len(first) == len(second) == 148
    expected_vectors = math.comb(124, 3) * 64
    assert sum(int(row["vectors"]) for row in first) == 148 * expected_vectors
    assert sum(int(row["vectors"]) for row in second) == 148 * expected_vectors
    for left, right in zip(first, second):
        assert int(left["template"]) == int(right["template"])
        assert left["light"] == right["light"]
        assert ledger(left, "profile_351") == ledger(right, "profile_351")
        assert ledger(left, "profile_47") == ledger(right, "profile_47")
    profile_ledgers = [ledger(row, "profile_351") for row in first]
    assert sum(value[0] for value in profile_ledgers) == 29_238
    assert sum(value[1] for value in profile_ledgers) == 15_440
    assert max(value[2] for value in profile_ledgers) == 1_392
    assert max(value[3] for value in profile_ledgers) == 1_392
    assert 1_392 < 1_517

    production_source = (NOTES / "e32_four_odd_joint_census.cpp").read_text()
    audit_source = (NOTES / "e32_four_odd_joint_census_audit.cpp").read_text()
    assert "folded_class" in production_source and "reverse_exponent" not in production_source
    assert "reverse_exponent" in audit_source and "folded_class" not in audit_source
    assert "Profile `(4,7)` remains" in (
        ROOT / "background/nodes/e1_n256_s16_e32_profile_351_light_template_exclusion/dependency_subdag.md"
    ).read_text()

    print(
        "E1_N256_S16_E32_PROFILE_351_LIGHT_TEMPLATE_EXCLUSION_AUDIT_PASS "
        "engines=2 rows=148 retained=29238 full=15440 m3=1392"
    )


if __name__ == "__main__":
    main()
