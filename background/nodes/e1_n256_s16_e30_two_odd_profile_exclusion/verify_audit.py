#!/usr/bin/env python3
"""Independent packet audit for the E30 two-odd exclusions."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes"
MAXIMUM_NORM = 255193811126065252065353356643030254729479452452701245894186298519499407392


def main() -> None:
    joint = json.loads((NOTES / "e30_two_odd_joint_census_result.json").read_text())
    joint_audit = json.loads((NOTES / "e30_two_odd_joint_census_audit_result.json").read_text())
    first = sorted(joint["rows"], key=lambda row: int(row["template"]))
    second = sorted(joint_audit["rows"], key=lambda row: int(row["template"]))
    assert len(first) == len(second) == 87
    for left, right in zip(first, second):
        assert int(left["template"]) == int(right["template"])
        assert left["light"] == right["light"]
        assert int(left["supports"]) == int(right["supports"])
        assert int(left["vectors"]) == int(right["vectors"])
        for profile in ("profile_27", "profile_151"):
            for key in ("count", "full_conductor", "maximum_m3", "maximum_full_conductor_m3"):
                assert int(left[profile][key]) == int(right[profile][key])
    assert sum(int(row["vectors"]) for row in first) == 1_726_770_432
    assert sum(int(row["profile_27"]["count"]) for row in first) == 44_302
    assert sum(int(row["profile_27"]["full_conductor"]) for row in first) == 28_114
    assert sum(int(row["profile_151"]["count"]) for row in first) == 7_722
    assert sum(int(row["profile_151"]["full_conductor"]) for row in first) == 3_572
    assert max(int(row["profile_151"]["maximum_full_conductor_m3"]) for row in first) == 1_068

    norms = json.loads((NOTES / "e30_profile27_exact_norm_census_result.json").read_text())
    norms_audit = json.loads((NOTES / "e30_profile27_exact_norm_audit_result.json").read_text())
    norm_first = sorted(norms["rows"], key=lambda row: int(row["template"]))
    norm_second = sorted(norms_audit["rows"], key=lambda row: int(row["template"]))
    assert len(norm_first) == len(norm_second) == 87
    for left, right, routed in zip(norm_first, norm_second, first):
        assert int(left["template"]) == int(right["template"]) == int(routed["template"])
        assert left["light"] == right["light"] == routed["light"]
        assert int(left["full_conductor_profile_27"]) == int(
            routed["profile_27"]["full_conductor"]
        )
        for key in (
            "full_conductor_profile_27",
            "norm_at_or_above_2_250",
            "maximum_norm",
            "maximum_norm_bits",
        ):
            assert int(left[key]) == int(right[key])
        assert left["maximum_witness"] == right["maximum_witness"]
        assert int(left["norm_at_or_above_2_250"]) == 0
    assert sum(int(row["full_conductor_profile_27"]) for row in norm_first) == 28_114
    assert max(int(row["maximum_norm"]) for row in norm_first) == MAXIMUM_NORM
    assert 7 * MAXIMUM_NORM < 2**250

    joint_source = (NOTES / "e30_two_odd_joint_census.cpp").read_text()
    joint_audit_source = (NOTES / "e30_two_odd_joint_census_audit.cpp").read_text()
    norm_source = (NOTES / "e30_profile27_exact_norm_census.cpp").read_text()
    norm_audit_source = (NOTES / "e30_profile27_exact_norm_audit.cpp").read_text()
    norm_launcher = (NOTES / "e30_profile27_exact_norm_census_modal.py").read_text()
    norm_audit_launcher = (NOTES / "e30_profile27_exact_norm_audit_modal.py").read_text()
    assert "folded_class" in joint_source and "reverse_exponent" not in joint_source
    assert "reverse_exponent" in joint_audit_source and "folded_class" not in joint_audit_source
    assert "folded_class" in norm_source and "reverse_exponent" not in norm_source
    assert "reverse_exponent" in norm_audit_source and "folded_class" not in norm_audit_source
    assert "python-flint" in norm_launcher and "polresultant" not in norm_launcher
    assert "pari-gp" in norm_audit_launcher and "polresultant" in norm_audit_launcher

    print(
        "E1_N256_S16_E30_TWO_ODD_PROFILE_EXCLUSION_AUDIT_PASS "
        "templates=87 vectors=1726770432 full27=28114 full151=3572 "
        "max_bits=248 above=0 engines=4"
    )


if __name__ == "__main__":
    main()
