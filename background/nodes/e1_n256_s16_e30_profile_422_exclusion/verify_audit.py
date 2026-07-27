#!/usr/bin/env python3
"""Independent structural audit of the E30 profile-(4,2,2) packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes"
MAXIMUM_NORM = 4039047355553663302249733085042470588482730556495866201164489362016333826


def main() -> None:
    production = json.loads((NOTES / "e30_profile422_odd_difference_relaxation_result.json").read_text())
    audit = json.loads((NOTES / "e30_profile422_odd_difference_relaxation_audit_result.json").read_text())
    first = sorted(production["rows"], key=lambda row: int(row["shard"]))
    second = sorted(audit["rows"], key=lambda row: int(row["shard"]))
    assert len(first) == len(second) == 4
    for left, right in zip(first, second):
        for key in (
            "shard",
            "normalized_six_odd_supports",
            "distinct_odd_masks",
            "tested_masks",
            "assignments",
            "above_threshold",
            "above_histogram",
            "maximum_m3",
            "witness",
            "exceptional",
        ):
            assert left[key] == right[key]
    assert sum(int(row["assignments"]) for row in first) == 29_541_960
    assert sum(int(row["above_threshold"]) for row in first) == 3
    assert max(int(row["maximum_m3"]) for row in first) == 1146

    actual = json.loads((NOTES / "e30_profile422_exceptional_actual_result.json").read_text())
    actual_first = sorted(actual["production"], key=lambda row: int(row["template"]))
    actual_second = sorted(actual["audit"], key=lambda row: int(row["template"]))
    assert len(actual_first) == len(actual_second) == 3
    for left, right in zip(actual_first, actual_second):
        for key in ("template", "light", "supports", "vectors", "count", "full_conductor", "matches"):
            assert left[key] == right[key]
    assert [int(row["count"]) for row in actual_first] == [2, 2, 2]
    assert [int(row["full_conductor"]) for row in actual_first] == [2, 0, 0]
    for scale, row in zip((1, 2, 4), actual_first):
        for primitive, vector in zip(actual_first[0]["matches"], row["matches"]):
            assert vector["positions"] == [scale * value for value in primitive["positions"]]
            assert vector["coefficients"] == primitive["coefficients"]

    norms = json.loads((NOTES / "e30_profile422_exceptional_norm_result.json").read_text())
    assert norms["flint_norms"] == norms["pari_norms"] == [MAXIMUM_NORM, MAXIMUM_NORM]
    assert 447 * MAXIMUM_NORM < 2**250

    relaxation_source = (NOTES / "e30_profile422_odd_difference_relaxation.cpp").read_text()
    relaxation_audit_source = (NOTES / "e30_profile422_odd_difference_relaxation_audit.cpp").read_text()
    actual_source = (NOTES / "e30_profile422_exceptional_actual_census.cpp").read_text()
    actual_audit_source = (NOTES / "e30_profile422_exceptional_actual_audit.cpp").read_text()
    norm_driver = (NOTES / "e30_profile422_exceptional_norm_modal.py").read_text()
    assert "base_base_unit" in relaxation_source and "make_kernel" not in relaxation_source
    assert "make_kernel" in relaxation_audit_source and "first_gap" in relaxation_audit_source
    assert "folded_class" in actual_source and "reverse_exponent" not in actual_source
    assert "reverse_exponent" in actual_audit_source and "folded_class" not in actual_audit_source
    assert "python-flint" in norm_driver and "polresultant" in norm_driver

    print(
        "E1_N256_S16_E30_PROFILE_422_EXCLUSION_AUDIT_PASS "
        "masks=1234 assignments=29541960 exceptions=3 actual=6 full=2 "
        "max_bits=242 engines=6"
    )


if __name__ == "__main__":
    main()
