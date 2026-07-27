#!/usr/bin/env python3
"""Independent structural audit of the E30 profile-(5,4,1) packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / "background/nodes/e1_n256_s16_e30_profile_parity_light_reduction/notes"
MAXIMUM_NORM = 147314768947604483837877250659211387932426327951806688176613401078756416516


def main() -> None:
    production = json.loads((NOTES / "e30_profile541_odd_difference_relaxation_result.json").read_text())
    audit = json.loads((NOTES / "e30_profile541_odd_difference_relaxation_audit_result.json").read_text())
    first = sorted(production["rows"], key=lambda row: int(row["shard"]))
    second = sorted(audit["rows"], key=lambda row: int(row["shard"]))
    assert len(first) == len(second) == 64
    for left, right in zip(first, second):
        for key in (
            "shard", "tested_masks", "assignments", "above_threshold",
            "above_histogram", "maximum_m3", "witness", "exceptional",
        ):
            assert left[key] == right[key]
    assert sum(int(row["assignments"]) for row in first) == 2_924_654_040
    assert sum(int(row["above_threshold"]) for row in first) == 1_456

    actual = json.loads((NOTES / "e30_profile541_exceptional_actual_result.json").read_text())
    actual_audit = json.loads((NOTES / "e30_profile541_exceptional_actual_audit_result.json").read_text())
    actual_first = sorted(actual["rows"], key=lambda row: int(row["template"]))
    actual_second = sorted(actual_audit["rows"], key=lambda row: int(row["template"]))
    assert len(actual_first) == len(actual_second) == 321
    for left, right in zip(actual_first, actual_second):
        for key in (
            "template", "light", "supports", "vectors", "profile_count",
            "above_cutoff", "full_above_cutoff", "maximum_m3",
            "maximum_full_m3", "matches",
        ):
            assert left[key] == right[key]
    assert sum(int(row["vectors"]) for row in actual_first) == 6_371_187_456
    assert sum(int(row["above_cutoff"]) for row in actual_first) == 440
    assert sum(int(row["full_above_cutoff"]) for row in actual_first) == 86

    norms = json.loads((NOTES / "e30_profile541_exceptional_norm_result.json").read_text())
    assert norms["flint_norms"] == norms["pari_norms"]
    assert len(norms["flint_norms"]) == 86
    assert max(int(value) for value in norms["flint_norms"]) == MAXIMUM_NORM
    assert 12 * MAXIMUM_NORM < 2**250

    relaxation_source = (NOTES / "e30_profile541_odd_difference_relaxation.cpp").read_text()
    relaxation_audit_source = (NOTES / "e30_profile541_odd_difference_relaxation_audit.cpp").read_text()
    actual_source = (NOTES / "e30_profile541_exceptional_actual_census.cpp").read_text()
    actual_audit_source = (NOTES / "e30_profile541_exceptional_actual_audit.cpp").read_text()
    norm_driver = (NOTES / "e30_profile541_exceptional_norm_modal.py").read_text()
    assert "for (int first = 1; first < 128" in relaxation_source
    assert "first_gap" in relaxation_audit_source and "pair_sums" in relaxation_audit_source
    assert "folded_class" in actual_source and "reverse_exponent" not in actual_source
    assert "reverse_exponent" in actual_audit_source and "folded_class" not in actual_audit_source
    assert "python-flint" in norm_driver and "polresultant" in norm_driver

    print(
        "E1_N256_S16_E30_PROFILE_541_EXCLUSION_AUDIT_PASS "
        "assignments=2924654040 exceptions=1456 templates=321 "
        "vectors=6371187456 actual=440 full=86 max_bits=247 engines=6"
    )


if __name__ == "__main__":
    main()
