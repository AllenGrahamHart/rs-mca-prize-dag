#!/usr/bin/env python3
"""Independent structural audit of the E30 profile-(6,6) packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NOTES = Path(__file__).resolve().parent / "notes"
MAXIMUM_NORM = 384340001363476246612319029755636117549080229904040014178244445877664108548


def strip_runtime(row: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in row.items() if key != "worker_seconds"}


def main() -> None:
    relaxation = json.loads((NOTES / "e30_profile66_odd_difference_scan_result.json").read_text())
    relaxation_audit = json.loads((NOTES / "e30_profile66_odd_difference_scan_audit_result.json").read_text())
    first = sorted(relaxation["rows"], key=lambda row: int(row["index"]))
    second = sorted(relaxation_audit["rows"], key=lambda row: int(row["index"]))
    assert len(first) == len(second) == 1_234
    assert [strip_runtime(row) for row in first] == [strip_runtime(row) for row in second]
    assert sum(int(row["assignments"]) for row in first) == 44_779_702_968
    assert sum(int(row["above_threshold"]) for row in first) == 33_737

    actual = json.loads((NOTES / "e30_profile66_exceptional_actual_result.json").read_text())
    actual_audit = json.loads((NOTES / "e30_profile66_exceptional_actual_audit_result.json").read_text())
    actual_first = sorted(actual["rows"], key=lambda row: int(row["template"]))
    actual_second = sorted(actual_audit["rows"], key=lambda row: int(row["template"]))
    assert len(actual_first) == len(actual_second) == 1_191
    assert [strip_runtime(row) for row in actual_first] == [strip_runtime(row) for row in actual_second]
    assert sum(int(row["vectors"]) for row in actual_first) == 23_638_891_776
    assert sum(int(row["above_cutoff"]) for row in actual_first) == 6_244
    assert sum(int(row["full_above_cutoff"]) for row in actual_first) == 1_232

    norms = json.loads((NOTES / "e30_profile66_exceptional_norm_result.json").read_text())
    assert norms["flint_norms"] == norms["pari_norms"]
    assert len(norms["flint_norms"]) == 1_232
    assert max(int(value) for value in norms["flint_norms"]) == MAXIMUM_NORM
    assert 4 * MAXIMUM_NORM < 2**250

    relaxation_source = (NOTES / "e30_profile66_odd_difference_scan.cpp").read_text()
    relaxation_audit_source = (NOTES / "e30_profile66_odd_difference_scan_audit.cpp").read_text()
    actual_source = (NOTES / "e30_profile66_exceptional_actual_census.cpp").read_text()
    actual_audit_source = (NOTES / "e30_profile66_exceptional_actual_audit.cpp").read_text()
    norm_driver = (NOTES / "e30_profile66_exceptional_norm_modal.py").read_text()
    assert "make_kernel" in relaxation_source and "adjusted_pair" not in relaxation_source
    assert "unit_unit_unit" in relaxation_audit_source and "adjusted_pair" in relaxation_audit_source
    assert "folded_class" in actual_source and "reverse_exponent" not in actual_source
    assert "reverse_exponent" in actual_audit_source and "folded_class" not in actual_audit_source
    assert "python-flint" in norm_driver and "polresultant" in norm_driver

    print(
        "E1_N256_S16_E30_PROFILE_66_EXCLUSION_AUDIT_PASS "
        "assignments=44779702968 exceptions=33737 templates=1191 "
        "vectors=23638891776 actual=6244 full=1232 max_bits=248 engines=6"
    )


if __name__ == "__main__":
    main()
