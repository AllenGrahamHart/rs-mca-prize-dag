#!/usr/bin/env python3
"""Independent structural audit of the E26 two-odd exclusion."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = Path(__file__).resolve().parent / "notes"
MAXIMUM_NORM = 902560312161452055740126650872074695232473707768299835426377069738129096704


def strip_runtime(row: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in row.items() if key != "worker_seconds"}


def main() -> None:
    production = json.loads((NOTES / "e26_six_two_odd_profile_census_result.json").read_text())
    audit = json.loads((NOTES / "e26_six_two_odd_profile_census_audit_result.json").read_text())
    first = sorted(production["rows"], key=lambda row: int(row["template"]))
    second = sorted(audit["rows"], key=lambda row: int(row["template"]))
    assert len(first) == len(second) == 87
    assert [strip_runtime(row) for row in first] == [strip_runtime(row) for row in second]
    assert sum(int(row["vectors"]) for row in first) == 1_726_770_432
    assert sum(sum(int(value) for value in row["profile_counts"]) for row in first) == 27_380
    assert sum(sum(int(value) for value in row["above_cutoff"]) for row in first) == 17_624
    assert sum(sum(int(value) for value in row["full_above_cutoff"]) for row in first) == 8_060
    norms = json.loads((NOTES / "e26_six_two_odd_profile_exceptional_norm_result.json").read_text())
    assert norms["flint_norms"] == norms["pari_norms"] and len(norms["flint_norms"]) == 8_060
    assert max(int(value) for value in norms["flint_norms"]) == MAXIMUM_NORM
    assert 2 * MAXIMUM_NORM < 2**250 < 3 * MAXIMUM_NORM
    production_source = (NOTES / "e26_six_two_odd_profile_census.cpp").read_text()
    audit_source = (NOTES / "e26_six_two_odd_profile_census_audit.cpp").read_text()
    assert "folded_class" in production_source and "reverse_exponent" not in production_source
    assert "reverse_exponent" in audit_source and "folded_class" not in audit_source
    print("E1_N256_S16_E26_SIX_TWO_ODD_PROFILE_EXCLUSION_AUDIT_PASS templates=87 vectors=1726770432 exceptions=17624 full=8060 max_bits=249 engines=4")


if __name__ == "__main__":
    main()
