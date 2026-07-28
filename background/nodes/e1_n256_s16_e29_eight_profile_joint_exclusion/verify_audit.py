#!/usr/bin/env python3
"""Independent structural audit of the E29 joint exclusion packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = ROOT / "background/nodes/e1_n256_s16_e29_profile_parity_light_reduction/notes"
MAXIMUM_NORM = 186828941137106397532470537651505306486275228904728704307636700572095315972


def strip_runtime(row: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in row.items() if key != "worker_seconds"}


def main() -> None:
    production = json.loads((NOTES / "e29_eight_profile_joint_census_result.json").read_text())
    audit = json.loads((NOTES / "e29_eight_profile_joint_census_audit_result.json").read_text())
    first = sorted(production["rows"], key=lambda row: int(row["template"]))
    second = sorted(audit["rows"], key=lambda row: int(row["template"]))
    assert len(first) == len(second) == 111
    assert [strip_runtime(row) for row in first] == [strip_runtime(row) for row in second]
    assert sum(int(row["vectors"]) for row in first) == 2_203_120_896
    assert sum(sum(int(value) for value in row["profile_counts"]) for row in first) == 61_408
    assert sum(sum(int(value) for value in row["above_cutoff"]) for row in first) == 4_812
    assert sum(sum(int(value) for value in row["full_above_cutoff"]) for row in first) == 820

    norms = json.loads((NOTES / "e29_eight_profile_exceptional_norm_result.json").read_text())
    assert norms["flint_norms"] == norms["pari_norms"]
    assert len(norms["flint_norms"]) == 820
    assert max(int(value) for value in norms["flint_norms"]) == MAXIMUM_NORM
    assert 9 * MAXIMUM_NORM < 2**250

    production_source = (NOTES / "e29_eight_profile_joint_census.cpp").read_text()
    audit_source = (NOTES / "e29_eight_profile_joint_census_audit.cpp").read_text()
    norm_driver = (NOTES / "e29_eight_profile_exceptional_norm_modal.py").read_text()
    assert "folded_class" in production_source and "reverse_exponent" not in production_source
    assert "reverse_exponent" in audit_source and "folded_class" not in audit_source
    assert "python-flint" in norm_driver and "polresultant" in norm_driver

    print("E1_N256_S16_E29_EIGHT_PROFILE_JOINT_EXCLUSION_AUDIT_PASS templates=111 vectors=2203120896 exceptions=4812 full=820 max_bits=247 engines=4")


if __name__ == "__main__":
    main()
